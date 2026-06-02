import os
import shutil

files = os.listdir()

for file in files:

    if file == "file_organizer.py":
        continue

    if os.path.isdir(file):
        continue

    name, extension = os.path.splitext(file)

    if extension in [".pdf", ".docx", ".txt"]:
        folder_name = "Documents"

    elif extension in [".csv", ".xlsx"]:
        folder_name = "Spreadsheets"

    elif extension in [".jpg", ".jpeg", ".png"]:
        folder_name = "Images"

    elif extension in [".mp4"]:
        folder_name = "Videos"

    elif extension in [".mp3"]:
        folder_name = "Audio"

    else:
        continue

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    destination = os.path.join(folder_name, file)

    shutil.move(file, destination)

    print(f"Moved {file} to {folder_name}")
