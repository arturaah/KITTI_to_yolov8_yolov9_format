import os
import shutil
import random

def reduce_dataset(source_dir, reduction_factor):
    base_dir = os.path.dirname(source_dir)
    original_dir_name = os.path.basename(source_dir)
    new_dir_name = f"{original_dir_name}_reduced_{reduction_factor}"
    new_dir_path = os.path.join(base_dir, new_dir_name)

    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)

    for subset in ["train", "valid", "test"]:
        images_path = os.path.join(source_dir, subset, "images")
        labels_path = os.path.join(source_dir, subset, "labels")
        new_images_path = os.path.join(new_dir_path, subset, "images")
        new_labels_path = os.path.join(new_dir_path, subset, "labels")

        # Ensure the new directories exist
        os.makedirs(new_images_path, exist_ok=True)
        os.makedirs(new_labels_path, exist_ok=True)

        # List all images
        image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
        # Randomly select a subset of image files based on the reduction factor
        selected_files = random.sample(image_files, int(len(image_files) * reduction_factor))

        for image_file in selected_files:
            # Construct the expected label file name based on the image file name
            label_file = os.path.splitext(image_file)[0] + ".txt"

            # Check if both the image and label files exist before copying
            if os.path.exists(os.path.join(images_path, image_file)) and os.path.exists(os.path.join(labels_path, label_file)):
                # Copy the image file
                shutil.copy2(os.path.join(images_path, image_file), os.path.join(new_images_path, image_file))
                # Copy the corresponding label file
                shutil.copy2(os.path.join(labels_path, label_file), os.path.join(new_labels_path, label_file))
            else:
                print(f"Skipping {image_file} as the corresponding image or label file is missing.")

if __name__ == "__main__":
    source_dir = r""  # Adjust this path
    reduction_factor = 0.5  # Adjust this factor as needed
    reduce_dataset(source_dir, reduction_factor)
