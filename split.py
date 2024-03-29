import os
import shutil
import random

# Set the path to your images and labels
images_dir = ""
labels_dir = ""
dest_dir = ""

# Create train, valid, test directories along with their images and labels subdirectories
for folder in ['train', 'valid', 'test']:
    os.makedirs(os.path.join(dest_dir, folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, folder, 'labels'), exist_ok=True)

# Get all file names (without extensions) from the images and labels directories
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith('.png')]
label_files = [os.path.splitext(f)[0] for f in os.listdir(labels_dir) if f.endswith('.txt')]

# Shuffle the files together to maintain correspondence between images and labels
files = list(set(image_files) & set(label_files))  # Ensure only files with both image and label are included
random.shuffle(files)

# Calculate split indices
total_files = len(files)
train_end = int(total_files * 0.7)
valid_end = int(total_files * 0.9)

# Function to copy files
def copy_files(files, data_type):
    for f in files:
        # Copy image
        shutil.copyfile(
            os.path.join(images_dir, f + '.png'),
            os.path.join(dest_dir, data_type, 'images', f + '.png')
        )
        # Copy label
        shutil.copyfile(
            os.path.join(labels_dir, f + '.txt'),
            os.path.join(dest_dir, data_type, 'labels', f + '.txt')
        )

# Copy files into their respective directories
copy_files(files[:train_end], 'train')  # 70% to train
copy_files(files[train_end:valid_end], 'valid')  # 20% to valid
copy_files(files[valid_end:], 'test')  # 10% to test

print("Dataset successfully split into train, valid, and test sets.")
