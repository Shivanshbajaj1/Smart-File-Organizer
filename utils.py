import os

def get_extension(filename):
    """
    Returns the lowercase extension of a file.
    """
    return os.path.splitext(filename)[1].lower()


def create_folder(path):
    """
    Creates a folder if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def is_file(path):
    """
    Returns True if path is a file.
    """
    return os.path.isfile(path)