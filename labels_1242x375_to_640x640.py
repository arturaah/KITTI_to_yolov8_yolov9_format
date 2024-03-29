
import os
import glob

def convert_annotation(original_size, target_size, bbox):
    """
    Convert bounding box annotations to the target image size.
    """
    ox, oy = original_size
    tx, ty = target_size

    # Unpack the original bounding box
    x, y, w, h = bbox

    # Convert normalized coordinates to absolute coordinates (relative to original size)
    x_abs = x * ox
    y_abs = y * oy
    w_abs = w * ox
    h_abs = h * oy

    # Convert absolute coordinates to new scale (relative to target size)
    x_new = x_abs * (tx / ox)
    y_new = y_abs * (ty / oy)
    w_new = w_abs * (tx / ox)
    h_new = h_abs * (ty / oy)

    # Convert back to normalized coordinates
    x_new /= tx
    y_new /= ty
    w_new /= tx
    h_new /= ty

    return [x_new, y_new, w_new, h_new]

def process_annotations(input_dir, output_dir, original_size, target_size):
    """
    Process all annotation files in the input directory and save them to the output directory.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of annotation files
    files = glob.glob(os.path.join(input_dir, "*.txt"))

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            class_id, bbox = parts[0], list(map(float, parts[1:]))
            new_bbox = convert_annotation(original_size, target_size, bbox)
            new_line = f"{class_id} {' '.join(map(str, new_bbox))}\n"
            new_lines.append(new_line)

        # Write updated annotations to new file in output directory
        with open(os.path.join(output_dir, os.path.basename(file)), 'w') as f:
            f.writelines(new_lines)

# Define original and target image sizes (width, height)
original_size = (1245, 375)
target_size = (640, 640)

# Define input and output directories
input_dir = ''#Rename with your path name
output_dir = ''#Rename with your path name

# Process the annotations
process_annotations(input_dir, output_dir, original_size, target_size)

