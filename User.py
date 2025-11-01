class User:
    def __init__(self, name,i):
        self.__name = name
        self.__i = i
        with open("nameuser.txt", "r") as f:
            line = f.read().split("\n")[i].split(" ")[2].split(":")
            self.__access = {
                item.split('(')[0]: item.split('(')[1].strip(')')
                for item in line
            }
        print(f"Вітаю {User.getName()}! Дозволи:{User.getAccess()}")
    def getAccess(self):
        return self.__access
    def getName(self):
        return  self.__name

class UserAdmin(User):
    def __init__(self, name):
        self.__name = name
        self.__access = {
            "Access": "Full"
        }
        print(f"Вітаю {self.getName()}! Дозволи:{self.getAccess()}")
        if input("Бажаєте взаємодіяти з користувачами чи з директоріями(введіть usr(з користувачами) або dir(з директоріями): ") == "usr":
            with open("nameuser.txt", "r") as f:
                print("Повний список користувачів(максимум 15):\n" + f.read())
            if input("Бажаєте видалити користувача чи додати(введіть add(для додавання) або del(для видалення): ") == "add":
                with open('nameuser.txt', 'a') as f:
                    f.write("\n")
                    f.write(f"{input('Введіть імʼя нового користувача: ')} {input('Введіть пароль нового користувача: ')}")
    def getAccess(self):
        return self.__access
    def getName(self):
        return self.__name