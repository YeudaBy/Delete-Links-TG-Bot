from bot.helper import json_load, json_dump
from pyrogram.types import InlineKeyboardMarkup as kmark, InlineKeyboardButton as kbut

path_users = 'bot/json_bot/users.json'
path_msg_text = 'bot/json_bot/MSG.json'
def private_start(c, m):
    m.reply(json_load(path_msg_text)['start_message'].format(
        f'[{m.from_user.first_name}](tg://user?id={m.from_user.id})',
    'DeleteTGLinkesHEbot'),
        disable_web_page_preview=True,
        reply_markup=kmark([[kbut("עדכוני רובוטים 👽", url= "t.me/m100achuzBots")]]))
    users = json_load(path_users)
    if m.from_user.id not in users:
        users.append(m.from_user.id)
        json_dump(users, path_users)

def private_help(c, m):
    m.reply(json_load(path_msg_text)['help_message'],disable_web_page_preview=True)

def peivate_exce(c, m):
    m.reply(json_load(path_msg_text)['add_exce_private'])
