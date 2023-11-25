import cv2
import os
import numpy as np

# Function to load images from a folder and convert them to 2D arrays using cv2
def load_images_cv2(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            try:
                image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                image_array = np.array(image)
                image_list.append(image_array)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    return image_list

folder_path = r"E:\.DESK\DATA SCIENCE\IMAGES\Output\LAMBO"
image_list = load_images_cv2(folder_path)
print(image_list[0])
