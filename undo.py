import os
import shutil

FOLDERS = [
    "Images",
    "Documents",
    "Music",
    "Videos",
    "Archives",
    "TextFiles",
    "Others"
]

folder_path = input("Enter the organized folder path: ")

for folder in FOLDERS:
    folder_location = os.path.join(folder_path, folder)

    if os.path.exists(folder_location):
        for file in os.listdir(folder_location):
            source = os.path.join(folder_location, file)
            destination = os.path.join(folder_path, file)

            shutil.move(source, destination)

        os.rmdir(folder_location)

print(" Folder restored successfully!")