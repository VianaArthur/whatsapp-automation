from os import listdir
from os.path import isfile, join
from pathlib import Path

import constants as const


def read_files():
    files = []

    for f in listdir(const.FILES_FOLDER):
        if isfile(join(const.FILES_FOLDER, f)):
            global_file = True

            if "__" in f:
                global_file = False

            dt = {"name": f, "isGlobal": global_file}
            files.append(dt)

    return files


def filter_files(contact, files):
    return [
        element
        for element in files
        if contact in element["name"] or element["isGlobal"]
    ]


def move_file(current_file_path, file):
    if not file["isGlobal"]:
        file_name = file["name"]
        Path(current_file_path).rename(f"{const.SENT_FILES_FOLDER}/{file_name}")
