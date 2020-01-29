import configparser
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.vendor.ptb_urllib3 import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log")


def get_param(section, name):
    """
    Возращает значение параметра "name" из секции "section"

    Args:
        section: имя секции
        name: имя параметра

    Returns:
        значение параметра.
    """
    # TODO: Переместить функцию в глобальный файл (utils|tools).py
    path = os.path.expanduser("~/.mpython_conf")
    if not os.path.exists(path):
        print("{} not found".format(path))
        return

    config = configparser.ConfigParser()

    config.read(path)
    value = config.get(section, name)
    return value


def start(update, context):
    """
    Обработчик команды /start
    Args:
        update:  Контекст бота
        context: Внешний контекст

    Returns:
        None
    """
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    """
    Обработчик входящего сообщения
    Args:
        update:  Контекст бота
        context: Внешний контекст

    Returns:
        None
    """
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    # Получаем данные из конфига
    token = get_param("telegram_setting", "learn_atseplyaev_bot_token")
    proxy_url = get_param("telegram_setting", "proxy_url")
    proxy_username = get_param("telegram_setting", "proxy_username")
    proxy_password = get_param("telegram_setting", "proxy_password")

    PROXY = {
        'proxy_url': proxy_url,
        'urllib3_proxy_kwargs': {
            'username': proxy_username,
            'password': proxy_password,
        }
    }
    print(PROXY)

    bot = Updater(token, use_context=True, request_kwargs=PROXY)

    dp = bot.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
