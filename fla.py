import os
import shutil
from zipfile import ZipFile
import subprocess

class Library():
    contents = []

    def __init__(self, library_folder):
        if not os.path.exists(library_folder):
            print("Library does not exist")
            return

        for file in os.listdir(library_folder):
            if os.path.isfile(os.path.join(library_folder, file)):
                self.contents.append(file)

    def get_contents(self):
        return self.contents

class FLADocument():
    extracted_path = ""

    LIBRARY:Library

    def __init__(self, path:str):
        self.unpack(path)

        self.LIBRARY = Library(f"{self.extracted_path}/LIBRARY")

    def unpack(self, path:str):
        if not os.path.exists(path):
            return

        fla_dir = f"./output/{os.path.basename(path)}_unpacked"

        if os.path.exists(fla_dir) and os.path.isdir(fla_dir):
            shutil.rmtree(fla_dir)

        os.mkdir(fla_dir)

        basename_split = os.path.basename(path).split(".")
        temp_file_path = f"{basename_split[0]}_TMP.{basename_split[1]}"

        shutil.copy(path, temp_file_path)

        #magicnum = bytearray(b"\xd0\xcd\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        #with open(temp_file_path, "ab") as f:
        #    f.write(magicnum)
        #with ZipFile(temp_file_path, "r") as z:
        #    z.extractall(fla_dir)

        #subprocess.Popen()
        subprocess.call(f"./bin/unzip.exe \"{path}\" -d \"{fla_dir}\"", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        self.extracted_path = fla_dir