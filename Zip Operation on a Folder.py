Aim:
To write a Python program that backs up a given folder in the current working directory by creating a ZIP file of the folder using relevant Python modules.

Algorithm:
Start the program.
Import the shutil and os modules.
Input the folder name from the user.
Check if the folder exists in the current working directory.
Use shutil.make_archive() to create a ZIP file of the folder.
Display a message that the folder has been successfully backed up.
End the program.
Program (Python Code):
# Program: Zip Operation on a Folder
import shutil
import os
# Input folder name
folder_name = input("Enter the folder name to backup: ")
# Check if folder exists
if os.path.exists(folder_name) and os.path.isdir(folder_name):
    # Create ZIP file (folder_name.zip)
    shutil.make_archive(folder_name, 'zip', folder_name)
    print(f"The folder '{folder_name}' has been successfully backed up as '{folder_name}.zip'.")
else:
    print(f"Error: Folder '{folder_name}' does not exist in the current directory.")

Result:
The program successfully backs up a folder in the current working directory into a ZIP file with the same folder name.
Uses the shutil.make_archive() method for efficient archiving.

Checks if the folder exists before creating the ZIP file to prevent errors.
