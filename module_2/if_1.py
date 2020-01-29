try:
    age = int(input("Введите возраст: "))
except ValueError:
    print("Было введено не целочисленное значение")
    print("Перезапустите программу и попробуйте снова")
    exit()

def action_time(age:int):
    """
    Определяет по возросту чем должен заниматься пользователь

    Args:
        age (int): Возраст пользователя.
    """
    action = ""
    if age < 7:
        action = "Вам надо учиться в детском саду"
    elif age < 18:
        action = "Вам надо учиться в школе"
    elif age < 22:
        action = "Вам надо учиться в ВУЗе"
    else:
        action = "Вам надо уже идти работать"
    return action


action = action_time(age)
print(action)
