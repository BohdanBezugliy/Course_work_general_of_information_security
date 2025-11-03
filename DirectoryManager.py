from pathlib import Path
from Crypto import Crypto
from StepLog import StepLog


class DirectoryManager:
    def __init__(self,dir,user,log):
        self.__dir = dir
        self.__log = log
        self.__user = user
        self.__file_names = [file.name for file in Path(dir).iterdir() if file.is_file()]

    def get_files(self):
        return self.__file_names

    def create_file(self,filename,content):
        dir_path = Path(self.__dir)
        file_path = dir_path / filename
        encrypted_content = Crypto.rsa_encrypt(content)
        file_path.write_text(encrypted_content)
        checkauth = self.__log.log(self.__user,f"був створений файл {filename}")
        if checkauth:
            return True
        else:
            return False

    def read_file(self,filename):
        if filename in self.__file_names:
            with open(f"{self.__dir}/{filename}","r") as f:
                checkauth = self.__log.log(self.__user, f"було зчитано інформацію з файла {filename}")
                if checkauth:
                    return True, Crypto.rsa_decrypt(f.read())
                else:
                    return False, None
        else:
            print("Такого файла не існує!")
            return False, None

    def remove_file(self,filename):
        if filename in self.__file_names:
            dir_path = Path(self.__dir)
            file_path = dir_path / filename
            file_path.unlink()
            checkauth = self.__log.log(self.__user, f"було видалено файл {filename}")
            if checkauth:
                return True
            else:
                return False
        else:
            print("Такого файла не існує!")
            return True

    def execution_file(self,filename):
        if filename in self.__file_names:
            print(f"Виконання: {filename}")
            checkauth = self.__log.log(self.__user, f"було запущено файл {filename}")
            if checkauth:
                return True
            else:
                return False
        else:
            print("Такого файла не існує!")
            return True

