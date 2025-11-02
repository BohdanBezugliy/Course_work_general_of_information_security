from pathlib import Path
from Crypto import Crypto
from StepLog import StepLog


class DirectoryManager:
    def __init__(self,dir,user):
        self.__dir = dir
        self.__log = StepLog()
        self.__user = user
        self.__file_names = [file.name for file in Path(dir).iterdir() if file.is_file()]

    def get_files(self):
        return self.__file_names

    def create_file(self,filename,content):
        dir_path = Path(self.__dir)
        file_path = dir_path / filename
        encrypted_content = Crypto.rsa_encrypt(content)
        file_path.write_text(encrypted_content)
        self.__log.log(self.__user,f"був створений файл {filename}")

    def read_file(self,filename):
        if filename in self.__file_names:
            with open(f"{self.__dir}/{filename}","r") as f:
                self.__log.log(self.__user, f"було зчитано інформацію з файла {filename}")
                return Crypto.rsa_decrypt(f.read())
        else:
            print("Такого файла не існує!")

    def remove_file(self,filename):
        if filename in self.__file_names:
            dir_path = Path(self.__dir)
            file_path = dir_path / filename
            file_path.unlink()
            self.__log.log(self.__user, f"було видалено файл {filename}")
        else:
            print("Такого файла не існує!")

    def execution_file(self,filename):
        if filename in self.__file_names:
            print(f"Виконання: {filename}")
            self.__log.log(self.__user, f"було запущено файл {filename}")
        else:
            print("Такого файла не існує!")

