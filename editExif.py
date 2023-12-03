import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ExifTags

class EditExif:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.image_label = tk.Label(root)
        self.image_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.exif_frame = tk.Frame(root)
        self.exif_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.exif_text = tk.Text(self.exif_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.exif_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.exif_entry = tk.Entry(self.exif_frame)
        self.exif_entry.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        self.update_button = tk.Button(self.exif_frame, text="Update EXIF", command=self.save_exif)
        self.update_button.pack(side=tk.BOTTOM, pady=5)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            self.display_image(file_path)
            self.display_exif_data(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        self.original_image = image
        image.thumbnail((self.root.winfo_width() // 2, self.root.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def display_exif_data(self, file_path):
        exif_data = self.get_exif_data(file_path)

        self.exif_text.config(state=tk.NORMAL)
        self.exif_text.delete(1.0, tk.END)
        print(exif_data)

        for tag, value in exif_data.items():
            self.exif_text.insert(tk.END, f"{tag}: {value}\n")

        self.exif_text.config(state=tk.DISABLED)

    def get_exif_data(self, file_path):
        exif_data = {}
        image = Image.open(file_path)

        try:
            for tag, value in image._getexif().items():
                if tag in ExifTags.TAGS:
                    exif_data[ExifTags.TAGS[tag]] = value
        except (AttributeError, KeyError, IndexError):
            pass

        return exif_data

    def save_exif(self):
        if self.original_image and self.exif_entry.get():
            new_exif_data = self.parse_input_exif_data(self.exif_entry.get())
            for tag, value in new_exif_data.items():
                print("New Exif: " + ExifTags.TAGS[tag])
                self.original_image.info[ExifTags.TAGS[tag]] = value
            # Save the image with updated EXIF data
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                       filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
            if save_path:
                self.original_image.save(save_path)
                print("Image saved with updated EXIF data.")

    def parse_input_exif_data(self, input_text):
        # For simplicity, assuming input in the format "Tag1: Value1\nTag2: Value2\n..."
        lines = input_text.split("\n")
        exif_data = {}
        for line in lines:
            parts = line.split(":")
            if len(parts) == 2:
                tag = parts[0].strip()
                value = parts[1].strip()
                # Find the tag ID based on its name
                tag_id = [k for k, v in ExifTags.TAGS.items() if v == tag]
                if tag_id:
                    exif_data[tag_id[0]] = value
                else:
                    print(f"Tag '{tag}' not found in EXIF tags.")
        return exif_data

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    app = EditExif(root)

    root.mainloop()
