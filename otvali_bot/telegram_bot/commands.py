from .mytelebot import myTeleBot
from models.chat import sync_chat
from models.client import save_new_client, get_client_by_tg_id, get_admins
from .answers import *



def setup_default_commands(bot: myTeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.logger.info(f'{message.from_user.username} sent {message.text}')
        if message.chat.type == 'private':
            client = get_client_by_tg_id(message.from_user.id)
            if client is None:
                save_new_client(message.from_user.id, message.from_user.username)
                bot.send_message(message.chat.id, request_waitlist_text)
                send_notification_to_admins(message.from_user.username)
            else:
                if client.is_declined:
                    bot.send_message(message.chat.id, request_declined_text)
                else:
                    if client.is_approved:
                        bot.send_message(message.chat.id, already_approved_text)
                    else:
                        bot.send_message(message.chat.id, already_requested_text)


    @bot.message_handler(commands=['help'])
    def send_help(message):
        sync_chat(message)
        bot.logger.info(f'{message.from_user.username} sent {message.text}')
        bot.send_message(message.chat.id, help_text, parse_mode='Markdown', disable_web_page_preview=True)


    @bot.message_handler(func=lambda m: True)
    def error(message):
        sync_chat(message)
        bot.logger.info(f'{message.from_user.username} sent {message.text}')
        bot.reply_to(message, "Error!")

    def send_notification_to_admins(new_user_name):
        admins = get_admins()
        for admin in admins:
            bot.send_message(admin.tg_id, f'New user on the waitlist - @{new_user_name}')

