from PIL import Image
import os

# Set your directory here
directory = ""

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".png"):  # Check if the file is a PNG image
        img_path = os.path.join(directory, filename)
        with Image.open(img_path) as img:
            # Resize the image
            img = img.resize((640, 640), Image.Resampling.LANCZOS)
            img.save(img_path)  # Save the resized image back to the directory

print("All PNG images have been resized to 640x640 pixels.")
