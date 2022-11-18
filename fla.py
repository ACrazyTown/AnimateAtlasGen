import os
import shutil
from zipfile import ZipFile
import subprocess

class Library():
    def __init__(self, library_folder:str):
        self.contents = {}

        if not os.path.exists(library_folder):
            print("Library does not exist")
            return

        for file in os.listdir(library_folder):
            path = os.path.join(library_folder, file)
            if os.path.isfile(path):
                self.contents[path] = self.get_file_type(path)

    def get_contents(self):
        return self.contents

    def get_symbols(self):
        symbols = []

        for key in self.contents.keys():
            v = self.contents.get(key)
            if v == "symbol":
                name = os.path.splitext(os.path.basename(key))[0]
                symbols.append(name)

        return symbols


    def get_file_type(self, path:str):
        # TODO: improve this
        ext = os.path.splitext(path)[1].lower().replace(".", "")
        if ext == "png" or ext == "jpg" or ext == "jpeg":
            return "image"
        elif ext == "mp3" or ext == "wav" or ext == "ogg":
            return "sound"
        elif ext == "flv" or ext == "mp4":
            return "video"
        elif ext == "xml":
            return "symbol"

class FLADocument():
    def __init__(self, path:str):
        self.extracted_path = ""

        self.unpack(path)

        self.LIBRARY = Library(f"{self.extracted_path}/LIBRARY")

    def unpack(self, path:str):
        if not os.path.exists(path):
            return

        fla_dir = f"./temp/{os.path.basename(path)}_unpacked"

        if os.path.exists(fla_dir) and os.path.isdir(fla_dir):
            shutil.rmtree(fla_dir)

        os.mkdir(fla_dir)

        #basename_split = os.path.splitext(path)
        #temp_file_path = f"{basename_split[0]}_TMP.{basename_split[1]}"
        #shutil.copy(path, temp_file_path)
        #magicnum = bytearray(b"\xd0\xcd\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        #with open(temp_file_path, "ab") as f:
        #    f.write(magicnum)
        #with ZipFile(temp_file_path, "r") as z:
        #    z.extractall(fla_dir)

        #subprocess.Popen()
        subprocess.call(f"./bin/unzip.exe \"{path}\" -d \"{fla_dir}\"", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        self.extracted_path = fla_dir