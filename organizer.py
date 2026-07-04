import os
import shutil

from config import FILE_TYPES
from utils import create_folder, get_extension, is_file
from logger import log_move


def organize_files(folder_path):
    """
    Organizes files in the given folder based on their extensions.
    """

    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    files = os.listdir(folder_path)

    moved_files = 0

    for file in files:

        file_path = os.path.join(folder_path, file)

        if not is_file(file_path):
            continue

        extension = get_extension(file)

        destination_folder = FILE_TYPES.get(extension, "Others")
        destination_path = os.path.join(folder_path, destination_folder)

        create_folder(destination_path)

        filename = os.path.splitext(file)[0]

        new_filename = file
        counter = 1

        while os.path.exists(os.path.join(destination_path, new_filename)):
            new_filename = f"{filename}({counter}){extension}"
            counter += 1

        new_file_path = os.path.join(destination_path, new_filename)

        try:
            shutil.move(file_path, new_file_path)

            print(f"{file}  →  {destination_folder}/{new_filename}")

            log_move(file, new_filename)

            moved_files += 1

        except Exception as e:
            print(f" Error moving {file}: {e}")

    print("\n==============================")
    print(f" Organization Complete!")
    print(f" Files moved : {moved_files}")
    print("==============================")


def main():
    print("=" * 40)
    print("      SMART FILE ORGANIZER")
    print("=" * 40)

    folder_path = input("Enter folder path: ").strip()

    organize_files(folder_path)


if __name__ == "__main__":
    main()

