import os
import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from numpy import zeros_like
def remove_background(input_folder, output_folder):
    # Get a list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        messagebox.showinfo("Error", "No image format file at that folder.")
        return
    
    # Process each image and remove background
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)
        
        # Convert the image to grayscale for background subtraction
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply background subtraction
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours and create a mask for the foreground object
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = zeros_like(img)
        cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
        
        # Bitwise AND operation to extract the foreground object
        result = cv2.bitwise_and(img, mask)
        
        # Convert the image to grayscale
        gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        
        # Resize the image to 28x28
        resized_result = cv2.resize(gray_result, (32,32), interpolation=cv2.INTER_AREA)
        
        # Flatten the 2D array into a 1D array (784 pixels)
        flattened_array = resized_result.flatten()

        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, flattened_array.reshape((32,32)))

    messagebox.showinfo("Done", "Processing done!")

def browse_input_folder():
    folder_selected = filedialog.askdirectory()
    entry1.delete(0, tk.END)  # Clear the entry field
    entry1.insert(0, folder_selected)

def browse_output_folder():
    folder_selected = filedialog.askdirectory()
    entry2.delete(0, tk.END)  # Clear the entry field
    entry2.insert(0, folder_selected)

# Create the main window
root = tk.Tk()
root.title("Image Processing")

# Create input fields and labels
label1 = tk.Label(root, text="Input Folder Path:")
label1.pack()
entry1 = tk.Entry(root, width=50)
entry1.pack()

browse_button1 = tk.Button(root, text="Browse", command=browse_input_folder)
browse_button1.pack()

label2 = tk.Label(root, text="Output Folder Path:")
label2.pack()
entry2 = tk.Entry(root, width=50)
entry2.pack()

browse_button2 = tk.Button(root, text="Browse", command=browse_output_folder)
browse_button2.pack()

# Create a button to perform tasks
process_button = tk.Button(root, text="Perform Tasks", command=lambda: remove_background(entry1.get(), entry2.get()))
process_button.pack()

# Start the tkinter main loop
root.mainloop()



# E:\.DESK\DATA SCIENCE\IMAGES\removebg\BUGGATI
# E:\.DESK\DATA SCIENCE\IMAGES\Output\50BUGGATI

# E:\.DESK\DATA SCIENCE\IMAGES\removebg\LAMBO
# E:\.DESK\DATA SCIENCE\IMAGES\Output\50LAMBO

#
#

# import os

# # Directory path
# directory = r"E:\.DESK\DATA SCIENCE\IMAGES\removebg\BUGGATI"
# name = r"buggati"
# try:
#     # Get a list of all files in the directory
#     files = os.listdir(directory)

#     # Iterate through the files and rename them
#     for i, file in enumerate(files, start=1):
#         # Get the file extension
#         file_name, file_extension = os.path.splitext(file)
        
#         # Create the new file name with the pattern "name{index}"
#         new_file_name = f"{name}{i}{file_extension}"
        
#         # Create the full path for the old and new file names
#         old_path = os.path.join(directory, file)
#         new_path = os.path.join(directory, new_file_name)

#         # Check if the new file name already exists, and iterate until a unique name is found
#         while os.path.exists(new_path):
#             i += 1
#             new_file_name = f"{name}{i}{file_extension}"
#             new_path = os.path.join(directory, new_file_name)
        
#         # Rename the file
#         os.rename(old_path, new_path)

#     print("All files have been renamed successfully.")

# except Exception as e:
#     print(f"An error occurred: {e}")

