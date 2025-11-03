from datetime import datetime
from Authentification import auth
from User import User
class StepLog:
    def __init__(self):
        self.__log_file = "us_book.txt"
        self.__T = 3
        self.__t = 0
    def log(self, user, message):
        self.__t+=1
        if self.__t > self.__T:
            if not auth():
                with open(self.__log_file, "a") as file:
                    file.write(f"{datetime.now().strftime("%d.%m.%y,%H:%M:%S")} " + user.get_name() + " " + "невдала автентифікація" + "\n")
                return False
            else:
                with open(self.__log_file, "a") as file:
                    file.write(f"{datetime.now().strftime("%d.%m.%y,%H:%M:%S")} " + user.get_name() + " " + "успішна автентифікація" + "\n")
                    file.write(f"{datetime.now().strftime("%d.%m.%y,%H:%M:%S")} " + user.get_name() + " " + message + "\n")
                self.__t = 0
                return True
        else:
            with open(self.__log_file, "a") as file:
                file.write(f"{datetime.now().strftime("%d.%m.%y,%H:%M:%S")} "+ user.get_name() + " " + message + "\n")
            return True
