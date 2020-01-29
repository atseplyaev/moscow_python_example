def ask_user():
    """
    Разговаривает с пользователем
    """
    answer_collect = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую"
    }
    while True:
        question = input("Пользователь: ")
        answer = answer_collect.get(question, "Я не понимаю")
        print(answer)


ask_user()
