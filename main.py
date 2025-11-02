from Identify import identify
from DirectoryManager import DirectoryManager
from User import User, UserAdmin
from UserManager import UserManager

while True:

    user = identify()

    if user is None:
        print("Не правильний пароль або імʼя користувача. Спробуйте ще раз.")
        continue
    else:
        print(f"\nВітаємо, {user.get_name()}!")
        while True:
            if isinstance(user, UserAdmin):

                actions = {"USERS", "DIR", "LOGOUT"}
                choice_action = input("\n[Admin] Чим бажаєте керувати (USERS, DIR, LOGOUT): ").upper()

                if choice_action not in actions:
                    print("Виберіть існуючу дію!")
                    continue

                if choice_action == "USERS":
                    usManager = UserManager()
                    print(f"--- Поточні користувачі(max 15, наразі {len(usManager.get_users())}) ---")
                    print(usManager.get_users())
                    print("------------------------------------------------------------------------")

                    user_actions = {"ADD", "DEL", "BACK"}
                    sub_choice = input("Оберіть дію (ADD - додати, DEL - видалити, BACK - назад): ").upper()

                    if sub_choice == "ADD":
                        usManager.create_user()
                    elif sub_choice == "DEL":
                        name_user = input("Оберіть користувача якого треба видалити: ")
                        if name_user in usManager.get_users():
                            usManager.remove_user(User(name_user))
                            continue
                        else:
                            print("Такого користувача не існує!")
                    elif sub_choice == "BACK":
                        continue
                    else:
                        print("Невідома під-дія.")

                elif choice_action == "DIR":
                    disks = {"A", "B", "C", "D", "E"}
                    disk = input("Який каталог бажаєте обрати (A,B,C,D,E): ").upper()

                    if disk in disks:
                        dir_manager = DirectoryManager(disk, user) #TODO FIX COUNTER OF AUTHENTIFICATION

                        file_actions = {"READ", "WRITE", "DELETE", "BACK"}
                        print(f"Обрано диск {disk}.")

                        file_choice = input("Оберіть дію (READ, WRITE, DELETE, EXECUTE, BACK - назад): ").upper()

                        if file_choice == "READ":
                            filename = input("Введіть ім'я файлу для читання: ")
                            dir_manager.read_file(filename)
                        elif file_choice == "WRITE":
                            filename = input("Введіть ім'я файлу для запису: ")
                            content = input("Введіть вміст: ")
                            dir_manager.create_file(filename, content)
                        elif file_choice == "DELETE":
                            filename = input("Введіть ім'я файлу для видалення: ")
                            dir_manager.remove_file(filename)
                        elif file_choice == "EXECUTE":
                            filename = input("Введіть ім'я файлу для запуску: ")
                            dir_manager.execution_file(filename)
                        elif file_choice == "BACK":
                            continue
                        else:
                            print("Невідома дія з файлом.")
                    else:
                        print("Виберіть існуючий диск!")

                elif choice_action == "LOGOUT":
                    print("Вихід з сесії...")
                    break

            else:
                actions = {"DIR", "LOGOUT"}
                choice_action = input("\n[User] Оберіть дію (DIR - директорії, LOGOUT - вихід): ").upper()

                if choice_action not in actions:
                    print("Виберіть існуючу дію!")
                    continue

                if choice_action == "DIR":
                    disks = {"A", "B", "C", "D", "E"}
                    print(f"Рівні доступа для кожного каталога(1-максимальний, 2-тільки читання та запуск файлів):\n {user.get_user_lvl()}")
                    disk = input("Який каталог бажаєте обрати (A,B,C,D,E): ").upper()

                    if disk in disks:
                        dir_manager = DirectoryManager(disk, user)

                        file_actions = {"READ", "WRITE", "DELETE", "BACK"}
                        privileges = user.get_user_lvl().split(",")
                        disk_privilege = 0
                        for privilege in privileges:
                            if disk in privilege:
                                disk_privilege = int(privilege[1])

                        if disk_privilege == 1:
                            print(f"Обрано диск {disk} [Рівень 1: Повний доступ]")
                            dir_manager = DirectoryManager(disk, user) #TODO FIX COUNTER OF AUTHENTIFICATION

                            file_actions = {"READ", "WRITE", "DELETE", "EXECUTE", "BACK"}
                            file_choice = input("Оберіть дію (READ, WRITE, DELETE, EXECUTE, BACK): ").upper()

                            if file_choice == "READ":
                                dir_manager.read_file(input("Ім'я файлу: "))
                            elif file_choice == "WRITE":
                                dir_manager.create_file(input("Ім'я файлу: "), input("Вміст: "))
                            elif file_choice == "DELETE":
                                dir_manager.remove_file(input("Ім'я файлу: "))
                            elif file_choice == "EXECUTE":
                                dir_manager.execution_file(input("Ім'я файлу: "))
                            elif file_choice == "BACK":
                                continue

                        elif disk_privilege == 2:
                            print(f"Обрано диск {disk} [Рівень 2: Читання та Запуск]")
                            dir_manager = DirectoryManager(disk, user) #TODO FIX COUNTER OF AUTHENTIFICATION

                            file_actions = {"READ", "EXECUTE", "BACK"}
                            file_choice = input("Оберіть дію (READ, EXECUTE, BACK): ").upper()

                            if file_choice == "READ":
                                dir_manager.read_file(input("Ім'я файлу: "))
                            elif file_choice == "EXECUTE":
                                dir_manager.execution_file(input("Ім'я файлу: "))
                            elif file_choice == "BACK":
                                continue
                            else:
                                print("ПОМИЛКА: Ця дія недоступна для вашого рівня доступу.")

                        else:
                            print(f"ДОСТУП ЗАБОРОНЕНО: У вас немає прав на диск {disk}.")
                    else:
                        print("Виберіть існуючий диск!")

                elif choice_action == "LOGOUT":
                    print("Вихід з сесії...")
                    break