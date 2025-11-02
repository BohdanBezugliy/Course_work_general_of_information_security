from User import User, UserAdmin

def identify():
    name = input("Введіть своє імʼя: ")
    password = input("Введіть пароль: ")
    with open("nameuser.txt", "r") as file:
        content = file.read()
        content = content.split("\n")
        for item in content:
            if item.split(" ")[0] == name and item.split(" ")[1] == password:
                print("Авторизація пройшла успішно")
                if name == "admin":
                    return UserAdmin()
                else:
                    return User(name)
        return None