import datetime
from datetime import datetime,timedelta


class User:

    def __init__(self, name):
        self.__name = name
        safe_period_passw = timedelta(days=90)
        with open("nameuser.txt", "r") as file:
            for line in file.readlines():
                if line.split(" ")[0] == self.__name:
                    if datetime.strptime(line.split(" ")[3].replace("\n",""), '%d.%m.%y,%H:%M:%S')+safe_period_passw < datetime.now():
                        print("Час змінити пароль!")
                    else:
                        print("Пароль досі актуальний!")

    def get_user_lvl(self):
        with open("nameuser.txt", "r") as file:
            for line in file.readlines():
                if line.split(" ")[0] == self.__name:
                    return line.split(" ")[2]

    def get_name(self):
        return  self.__name

class UserAdmin(User):
    def __init__(self):
        super().__init__("admin")