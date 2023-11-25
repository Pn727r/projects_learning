
import os

# Directory path
directory = r"E:\.DESK\DATA SCIENCE\IMAGES\removebg\BUGGATI"
name = r"buggati"
try:
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Iterate through the files and rename them
    for i, file in enumerate(files, start=1):
        # Get the file extension
        file_name, file_extension = os.path.splitext(file)
        
        # Create the new file name with the pattern "name{index}"
        new_file_name = f"{name}{i}{file_extension}"
        
        # Create the full path for the old and new file names
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)

    print("All files have been renamed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

