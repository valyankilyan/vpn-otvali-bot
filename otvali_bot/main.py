from telegram_bot.mytelebot import myTeleBot
from telegram_bot.bot import init_bot, init_message_handlers, init_webhook
from logger.logger import getLogger
from telegram_bot.utils import init_util_bot
from outline_service.outline_getter import OutlineGetter
from flask import Flask
from config.bot import *

app = Flask(__name__)

if __name__ == "__main__":
    logger = getLogger(logging_config_path)

    logger.debug("reading config")

    OutlineGetter.get_instance(outline_service_url)

    logger.debug(f"token = {token}")
    logger.debug(bool(use_webhook))
    bot = myTeleBot(token, logger)
    init_bot(bot)

    init_util_bot(bot)

    init_message_handlers(bot)

    if use_webhook == "True":
        init_webhook(bot, app, webhook_host, webhook_url_path, webhook_listen, int(webhook_port))
    else:
        bot.polling(none_stop=True)