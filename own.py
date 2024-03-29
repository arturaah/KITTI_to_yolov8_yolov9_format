import os
import shutil

# Replace these with your actual directory paths
source_labels_folder = ""
source_images_folder = ""

# Define the paths for the target folders
target_labels_folder = "labels"
target_images_folder = "images"

# Function to create target folders if they don't exist
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Create the target folders
create_folder(target_labels_folder)
create_folder(target_images_folder)

# Function to process the files and populate the target folders
def process_files():
    # Loop through each label file
    for file_num in range(21):  # Assuming inclusive of 0020
        file_name = f"{file_num:04}.txt"
        label_file_path = os.path.join(source_labels_folder, file_name)

        # Read the label file and store the lines based on the first argument
        label_lines = {}
        with open(label_file_path, 'r') as label_file:
            for line in label_file:
                image_num = int(line.split()[0])
                if image_num not in label_lines:
                    label_lines[image_num] = []
                label_lines[image_num].append(line)

        # Process corresponding images in the images folder
        images_folder_path = os.path.join(source_images_folder, f"{file_num:04}")
        for image_name in os.listdir(images_folder_path):
            # Construct the new image name
            new_image_name = f"{file_num:04}{image_name}"
            new_image_path = os.path.join(target_images_folder, new_image_name)

            # Copy the image to the new location with new name
            shutil.copy2(os.path.join(images_folder_path, image_name), new_image_path)

            # Create corresponding label file in the new labels folder
            image_num = int(image_name.split('.')[0])  # Assuming the format is 000000.png or similar
            new_label_name = f"{new_image_name}.txt"
            new_label_path = os.path.join(target_labels_folder, new_label_name)
            print(label_lines)
            with open(new_label_path, 'w') as new_label_file:
                if image_num in label_lines:
                    for line in label_lines[image_num]:
                        new_label_file.write(line)

                # Debug: Print a message if no lines were found for this image_num
                else:
                    print(f"No label lines found for image {new_image_name}")


# Call the function to process files
process_files()
