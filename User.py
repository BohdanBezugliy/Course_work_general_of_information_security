class User:

    def __init__(self, name):
        self.__name = name

    def get_user_lvl(self):
        with open("nameuser.txt", "r") as file:
            for line in file.readlines():
                if line.split(" ")[0] == self.__name:
                    return line.split(" ")[2]
            return None
    def get_name(self):
        return  self.__name

class UserAdmin(User):
    def __init__(self):
        super().__init__("admin")