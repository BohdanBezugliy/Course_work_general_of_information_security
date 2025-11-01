from User import User, UserAdmin

def auth():
    name = input("Введіть своє імʼя: ")
    password = input("Введіть пароль: ")
    if name == "admin" and password == "admin":
        return UserAdmin(name)
    with open("nameuser.txt", "r") as file:
        content = file.read()
        content = content.split("\n")
        for item in content:
            if item.split(" ")[0] == name and item.split(" ")[1] == password:
                print("Авторизація пройшла успішно")
                return User(name,content.index(item))
        return None

User = auth()
if User is None:
    print("Неправильний логін або пароль!")