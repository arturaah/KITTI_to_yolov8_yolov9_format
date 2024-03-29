import os

# Define the directory in which files are located
directory_path = ''

# Iterate trough all files in the specified directory
for filename in os.listdir(directory_path):
    # Verificy if it is a text file
    if filename.endswith('.txt'):
        # Build the entire path of the directory
        full_file_path = os.path.join(directory_path, filename)

        # Build a new name for the errased .png
        new_filename = filename.replace('.png', '')
        new_full_file_path = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(full_file_path, new_full_file_path)

print("Renaming compelted.")