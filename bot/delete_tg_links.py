from pyrogram.filters import regex, group, private, text, command, me
from pyrogram.handlers import MessageHandler

from .config_bot.app import app

from bot.group import delete_TG_links, re_tg_libks, add_exception
from bot.private import private_start, private_help, peivate_exce

app.add_handler(MessageHandler(private_start, private & command('start')))
app.add_handler(MessageHandler(private_help, private & command('help')))
app.add_handler(MessageHandler(peivate_exce, private & command('add_exce')))

app.add_handler(MessageHandler(delete_TG_links,
                ~command('add_exce') & ~me & text & group & regex(re_tg_libks)))

app.add_handler(MessageHandler(add_exception, command('add_exce') & group))
