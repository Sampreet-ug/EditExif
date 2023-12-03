import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ExifTags

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.image_label = tk.Label(root)
        self.image_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.exif_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
        self.exif_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

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
        image.thumbnail((self.root.winfo_width() // 2, self.root.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def display_exif_data(self, file_path):
        exif_data = self.get_exif_data(file_path)

        self.exif_text.config(state=tk.NORMAL)
        self.exif_text.delete(1.0, tk.END)

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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    app = ImageViewer(root)

    root.mainloop()
