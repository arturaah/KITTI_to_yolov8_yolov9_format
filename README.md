# KITTI_to_yolov8_yolov9_format
A simple set of scripts to adapt the KITTI dataset to train and test the newest yolov8 and yolov9 algorithms

The different scripts are kept separated to allow skipping certain preprocessing steps for the target dataset.
All images from the dataset are assumed to be 1242x375 pixels originally(which constitutes the majority image size of the KITTI dataset) and are resized to 640x640 through stretching. Labels are adapted accordingly.

Remember to replace to fill in the original dataset path and target path for each script. Also ensure you install:

pip install PIL

Running order:
1 - KITTItoyolo.py - adapts label format from custom KITTI labelling to yolov8/9
2 - resize.py - stretches to 640x640
3 - labels_1242x375_to_640x640.py - adapts labels
4 - own.py - restructures the directory to have subdirectories "train", "valid", "test" and each of them "images" and "labels"
5 - split.py - set to 70%, 20%valid and 10% test
 

Additional scripts:
- count_images: goes trough all directories within a specified directory and counts the number of files having a 'png', 'jpg' or 'jpeg'extension.
- reduce_v1: reduces a given dataset found in the desired directory by a reduction factor that can be adjusted. The target directory must have sub directories "train", "valid", "test" and each of these subfolders "images" and "labels". Then it will create a new directory with a replicated structured but ith a reduced number of images, proportionally in each subfolder. Images are selected randomly, with no particular order.
- quitpng.py is added in case there is any incompatibility in naming between label and corresponding png image. 
