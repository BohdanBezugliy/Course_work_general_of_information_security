from pathlib import Path
from Crypto import Crypto

class DirectoryManager:
    def __init__(self,dir):
        self.__dir = dir

    def create_file(self,filename,content):
        dir_path = Path(self.__dir)
        file_path = dir_path / filename
        encrypted_content = Crypto.rsa_encrypt(content)
        file_path.write_text(encrypted_content)

    def read_file(self,filename):
        with open(f"{self.__dir}/{filename}","r") as f:
            return Crypto.rsa_decrypt(f.read())

    def remove_file(self,filename):
        dir_path = Path(self.__dir)
        file_path = dir_path / filename
        file_path.unlink()

    def execution_file(self,filename):
        print(f"Виконання: {filename}")

