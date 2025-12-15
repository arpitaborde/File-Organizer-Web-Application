import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files(directory):
    if not os.path.exists(directory):
        return "Directory does not exist"

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(directory, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, filename))

    return "Files organized successfully"
