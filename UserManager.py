import re

class UserManager:

    def __init__(self):
        self.__names=[]
        with open("nameuser.txt", "r") as f:
            for line in f.readlines():
                self.__names.append(line.split(" ")[0])

        self.__N = 15
        self.__n = self.__N - len(self.__names)

    def get_users(self):
        return self.__names

    def create_user(self):
        if self.__n <= 0:
            print("Неможливо додати нового користувача!")
            return None
        with open("nameuser.txt", "a") as f:
            reg_pattern_name = re.compile(r"^.{3,50}$")
            while True:
                username = input("Введіть імʼя нового користувача: ").replace(" ", "")
                if re.search(reg_pattern_name, username):
                    if username in self.__names:
                        print(
                            "Імʼя користувача вже зайняте, оберіть інше!\nЯкщо бажаєте відмінити операцію введіть cenc, "
                            "щоб продвжити натисніть Enter")
                        if input() == "cenc":
                            return None
                    else:
                        break
                else:
                    print("Імʼя користувача не може бути коротшим\nза 3 та довшим за 50 символів, оберіть інше! "
                          "Якщо бажаєте відмінити операцію введіть cenc, "
                            "щоб продвжити натисніть Enter")
                    if input() == "cenc":
                        return None
            reg_pattern_passw = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,32}$")

            while True:
                passw = input("Введіть пароль для нового користувача:").replace(" ", "")
                if re.search(reg_pattern_passw, passw):
                    break
                else:
                    print("Пароль має містити в собі\nхоча б одну велику та малу літери\nта цифру і довжиною має бути"
                        "не менше 8 та не більше 32 символів, оберіть інший!\n"
                        "Якщо бажаєте відмінити операцію введіть cenc, щоб продвжити натисніть Enter")
                    if input().lower()=="cenc":
                        return None

            disks = ["A", "B", "C", "D", "E"]
            access = ""
            for disk in disks:
                while True:
                    lvl_access = input(f"Оберіть для каталогу {disk} рівень доступу(1-повний,2-тільки перегляд та виконання): ")
                    if lvl_access == "1" or lvl_access == "2":
                        if disk == "E":
                            access += f"{disk}" + f"{lvl_access}"
                        else:
                            access += f"{disk}" + f"{lvl_access}" + ","
                        break
                    else:
                        print("Введіть рівень доступу в правильному форматі!")
            f.write(f"\n{username} {passw} {access}")
            from User import User
            return User(username)

    def remove_user(self,user):
        new_file = []
        with open("nameuser.txt", "r") as f:
            file_content = f.readlines()
            for line in file_content:
                if line.split(" ")[0] != user.get_name():
                    new_file.append(line)
        with open("nameuser.txt", "w") as f:
            f.writelines(new_file)
