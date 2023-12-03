# EditExif - Image EXIF Editor

EditExif is a simple Python application that allows you to view and edit the EXIF data of an image. The application is built using the Tkinter library for the graphical user interface and the Pillow library for image processing.

## Features

- **Open Image:** Select an image file (supported formats: PNG, JPG, JPEG, GIF, BMP) to view and edit its EXIF data.
- **Display Image:** The selected image is displayed on the left side of the application window.
- **Display EXIF Data:** The EXIF data of the image is displayed on the top right side of the application window. Tags and their corresponding values are shown.
- **Edit EXIF Data:** Enter new EXIF data in the provided text entry field. The data should be in the format "Tag1: Value1\nTag2: Value2\n...".
- **Update EXIF:** Click the "Update EXIF" button to apply the entered EXIF data to the image.
- **Save Image:** After updating the EXIF data, you can save the modified image with the new information.

## Usage

1. Run the EditExif application by executing the following command in your terminal:

    ```bash
    python edit_exif.py
    ```

2. Open an image using the "File" menu and selecting "Open".
3. View and edit the EXIF data on the right side of the application.
4. Enter new EXIF data in the provided text entry field.
5. Click the "Update EXIF" button to apply the changes.
6. Save the modified image using the "File" menu and selecting "Save".

## Requirements

- Python 3.x
- Pillow library (PIL)
- Tkinter library

## Installation

1. Install the required libraries:

   ```bash
   pip install Pillow

## Notes

- The application assumes a basic format for entering new EXIF data. Ensure that the entered data follows the pattern "Tag: Value" for each line.
- Some EXIF tags may not be editable, and modifying certain tags may lead to unexpected behavior.

## Feedback

Feel free to use and modify this code according to your needs. If you encounter any issues or have suggestions for improvement, please let me know.

Enjoy editing your image's EXIF data with EditExif!