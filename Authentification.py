from random import randint

def auth():
    with open("ask.txt", "r") as file:
        X = file.readlines()
        x = float(X[randint(0, len(X) - 1)])
        try:
            y = float(input(
                f"Введіть секретне значення Y(максимум 4 знаки після коми, якщо число дробове) при X = {x}, для продовження операції: "))
            if y == round(4 * x ** 1.5, 4):
                print("Аутентифікація пройшла успішно!")
                return True
            else:
                return False
        except ValueError:
            return False