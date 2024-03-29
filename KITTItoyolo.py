import os

# Directory paths (change these to your own paths)
source_labels_dir = ""  # Directory of KITTI label files
target_labels_dir = "labels_converted"  # Directory for converted label files

# Class mapping from KITTI object type to YOLOv8 class index

class_mapping = {'Pedestrian': 0, 'Person_sitting': 0, 'Cyclist': 1, 'Car': 2,
                 'Van': 7, 'Truck': 7, 'Tram': 6}

# Ensure the target directory exists
os.makedirs(target_labels_dir, exist_ok=True)

# Function to convert one line of KITTI format to YOLOv8 format
def kitti_to_yolo(line, img_width, img_height):
    parts = line.strip().split(' ')
    object_type = parts[2]
    if object_type not in class_mapping:
        return None  # Ignore unrecognized classes

    # Extract coordinates and dimensions
    x1, y1, x2, y2 = map(float, parts[6:10])
    bbox_width = x2 - x1
    bbox_height = y2 - y1
    x_center = x1 + bbox_width / 2
    y_center = y1 + bbox_height / 2

    # Normalize coordinates and dimensions
    x_center /= img_width
    y_center /= img_height
    bbox_width /= img_width
    bbox_height /= img_height

    return f"{class_mapping[object_type]} {x_center} {y_center} {bbox_width} {bbox_height}"

# Process each file in the source directory
for filename in os.listdir(source_labels_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(source_labels_dir, filename), 'r') as file:
            lines = file.readlines()

        # Prepare the converted content
        converted_lines = []
        for line in lines:
            # You need to know the dimensions of the image to normalize coordinates
            img_width, img_height = 1242, 375  # Replace with actual dimensions
            converted_line = kitti_to_yolo(line, img_width, img_height)
            if converted_line:
                converted_lines.append(converted_line)

        # Write the converted lines to a new file in the target directory
        with open(os.path.join(target_labels_dir, filename), 'w') as file:
            file.write('\n'.join(converted_lines))

print("Conversion completed.")