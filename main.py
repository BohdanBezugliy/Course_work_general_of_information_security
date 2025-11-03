from Identify import identify
from DirectoryManager import DirectoryManager
from StepLog import StepLog
from User import User, UserAdmin
from UserManager import UserManager


def get_disk_privilege(user, disk):
    if isinstance(user, UserAdmin):
        return 1

    privileges = user.get_user_lvl().split(",")
    for privilege in privileges:
        if disk in privilege:
            try:
                return int(privilege[1])
            except (ValueError, IndexError):
                return 0
    return 0


def manage_users():
    usManager = UserManager()
    print(f"--- Поточні користувачі(max 15, наразі {len(usManager.get_users())}) ---")
    print(usManager.get_users())
    print("------------------------------------------")

    user_actions = {"ADD", "DEL", "BACK"}
    sub_choice = input("Оберіть дію (ADD - додати, DEL - видалити, BACK - назад): ").upper()

    if sub_choice == "ADD":
        usManager.create_user()
    elif sub_choice == "DEL":
        name_user = input("Оберіть користувача якого треба видалити: ")
        if name_user in usManager.get_users():
            usManager.remove_user(User(name_user))
        else:
            print("Такого користувача не існує!")
    elif sub_choice == "BACK":
        return
    else:
        print("Невідома під-дія.")


def manage_directories(user, log):
    disks = {"A", "B", "C", "D", "E"}
    if not isinstance(user, UserAdmin):
        print(
            f"Рівні доступа для кожного каталога(1-максимальний, 2-тільки читання та запуск файлів):\n {user.get_user_lvl()}")

    disk = input("Який каталог бажаєте обрати (A,B,C,D,E): ").upper()
    if disk not in disks:
        print("Виберіть існуючий диск!")
        return True

    privilege = get_disk_privilege(user, disk)
    if privilege == 0:
        print(f"ДОСТУП ЗАБОРОНЕНО: У вас немає прав на диск {disk}.")
        return True

    dir_manager = DirectoryManager(disk, user, log)
    print(f"Обрано диск {disk} [Рівень {privilege}]")
    print(f"---Список файлів({len(dir_manager.get_files())} штук) ---")
    print(dir_manager.get_files())
    print("-----------------------------")

    if privilege == 1:
        file_choice = input("Оберіть дію (READ, WRITE, DELETE, EXECUTE, BACK): ").upper()

        if file_choice == "READ":
            auth_ok, content = dir_manager.read_file(input("Ім'я файлу: "))
            if not auth_ok:
                return False
            if content is not None:
                print(content)

        elif file_choice == "WRITE":
            filename = input("Введіть ім'я файлу для запису: ")
            content = input("Введіть вміст: ")
            if not dir_manager.create_file(filename, content):
                return False

        elif file_choice == "DELETE":
            filename = input("Введіть ім'я файлу для видалення: ")
            if not dir_manager.remove_file(filename):
                return False

        elif file_choice == "EXECUTE":
            filename = input("Введіть ім'я файлу для запуску: ")
            if not dir_manager.execution_file(filename):
                return False

        elif file_choice == "BACK":
            return True

        else:
            print("Невідома дія з файлом.")

    elif privilege == 2:
        file_choice = input("Оберіть дію (READ, EXECUTE, BACK): ").upper()

        if file_choice == "READ":
            auth_ok, content = dir_manager.read_file(input("Ім'я файлу: "))
            if not auth_ok:
                return False
            if content is not None:
                print(content)

        elif file_choice == "EXECUTE":
            filename = input("Введіть ім'я файлу для запуску: ")
            if not dir_manager.execution_file(filename):
                return False

        elif file_choice == "BACK":
            return True

        else:
            print("ПОМИЛКА: Ця дія недоступна для вашого рівня доступу.")

    return True


def handle_user_session(user):
    log = StepLog()
    print(f"Вітаємо, {user.get_name()}!")

    while True:
        if isinstance(user, UserAdmin):
            actions = {"USERS", "DIR", "LOGOUT"}
            choice_action = input("[Admin] Чим бажаєте керувати (USERS, DIR, LOGOUT): ").upper()
        else:
            actions = {"DIR", "LOGOUT"}
            choice_action = input("[User] Оберіть дію (DIR - директорії, LOGOUT - вихід): ").upper()

        if choice_action not in actions:
            print("Виберіть існуючу дію!")
            continue

        stay_logged_in = True
        if choice_action == "USERS":
            manage_users()

        elif choice_action == "DIR":
            stay_logged_in = manage_directories(user, log)

        elif choice_action == "LOGOUT":
            stay_logged_in = False

        if not stay_logged_in:
            print("Вихід з сесії...")
            break


if __name__ == "__main__":
    while True:
        user = identify()
        if user is None:
            print("Не правильний пароль або імʼя користувача. Спробуйте ще раз.")
            continue
        else:
            handle_user_session(user)