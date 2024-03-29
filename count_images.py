import os

def count_images_in_directories(base_dir, image_extensions={'png', 'jpg', 'jpeg'}):
    """
    Count the number of image files in each main directory (and subdirectories) within the base directory.

    :param base_dir: The base directory containing the dataset and its reduced versions.
    :param image_extensions: A set of image file extensions to look for.
    """
    for root, dirs, files in os.walk(base_dir):
        # Filter directories to count images in 'images' subdirectories specifically
        if os.path.basename(root) == 'images':
            image_count = sum(1 for file in files if file.split('.')[-1].lower() in image_extensions)
            print(f"Total images in {os.path.relpath(root, base_dir)}: {image_count}")

# Example usage
base_directory = r""  # Update this to your base directory
count_images_in_directories(base_directory)
