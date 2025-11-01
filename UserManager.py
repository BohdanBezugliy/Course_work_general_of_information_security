import re

class UserManager:

    def __init__(self):
        users = []
        self.__names=[]
        with open("nameuser.txt", "r") as f:
            users = f.read().split("\n")
        self.__N = 15
        self.__n = self.__N - len(users)
        for user in users:
            self.__names.append(user.split(" ")[0])


    def GetUsers(self):
        return self.__users

    def GetN(self):
        return self.__N


    def addUser(self):
        if self.__n <= 0:
            print("Неможливо додати нового користувача!")
            return
        with open("nameuser.txt", "a") as f:
            reg_pattern_name = re.compile(r"^.{3,50}$")
            while True:
                username = input("Введіть імʼя нового користувача: ")
                if re.search(reg_pattern_name, username):
                    if username in self.__names:
                        print(
                            "Імʼя користувача вже зайняте, оберіть інше!\nЯкщо бажаєте відмінити операцію введіть cenc, "
                            "щоб продвжити натисніть Enter")
                        if input() == "cenc":
                            return
                    else:
                        break
                else:
                    print("Імʼя користувача не може бути коротшим\nза 3 та довшим за 50 символів, оберіть інше! "
                          "Якщо бажаєте відмінити операцію введіть cenc, "
                            "щоб продвжити натисніть Enter")
                    if input() == "cenc":
                        return
            reg_pattern_passw = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,32}$")
            while True:
                passw = input("Введіть пароль для нового користувача:")
                if re.search(reg_pattern_passw, passw):
                    disks = ["A", "B", "C", "D", "E"]
                    access = ""
                    for disk in disks:
                        while True:
                            rule = input(f"Оберіть для каталогу {disk}\nнаступні дозволи(Введіть символи через кому)"
                                f"\n(Е-виконання, R-читання, W-запис, "
                                f"А-доповнення, мінімальні R або Е, середні R, Е, або R, Е, А):")
                            reg_pattern_access =re.compile(
                                r"^(?!.*E.*,E.*)"
                                r"(?!.*R.*,R.*)"
                                r"(?!.*W.*,W.*)" 
                                r"(?!.*A.*,A.*)"
                                r"(N|([ERWA](?:,[ERWA]){0,3}))$"
                            )
                            if re.search(reg_pattern_access, rule):
                                if disk =="E":
                                    access+=disk+"("+rule+")"
                                else:
                                    access+=disk+"("+rule+"):"
                                break
                            else:
                                print("Введіть дозволи в правильному форматі!")
                    f.write(f"\n{username} {passw} {access}")
                    print(len(self.__names))
                    from User import User
                    return User(username, len(self.__names)-1)
                else:
                    print("Пароль має містити в собі\nхоча б одну велику та малу літери\nта цифру і довжиною має бути"
                        "не менше 8 та не більше 32 символів, оберіть інший!\n"
                        "Якщо бажаєте відмінити операцію введіть cenc, щоб продвжити натисніть Enter")
                    if input().lower()=="cenc":
                        return

    def DeleteUser(self,User):
        with open("nameuser.txt", "r") as f:
            file_content = f.readlines()
        new_file =[]
        for line in file_content:
            if line.split(" ")[0] != User.getName():
                new_file.append(line)
        with open("nameuser.txt", "w") as f:
            f.writelines(new_file)
