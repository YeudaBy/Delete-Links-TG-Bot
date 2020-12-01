from bot.helper import json_load, json_dump

re_tg_libks = "(?i)telegram.me|t\\.me"
path_exception_file = 'bot/json_bot/exceptions.json'
path_text_msg = 'bot/json_bot/MSG.json'
path_groups_id = "bot/json_bot/groups.json"

def check_not_admin(message):
    return message.chat.get_member(message.from_user.id).status not in ['creator', 'administrator']

def delete_TG_links(c, m):
    if check_not_admin(m):
        m.delete()
    if m.chat.id not in json_load(path_groups_id):
        groups = json_load(path_groups_id)
        groups.append(m.chat.id)
        json_dump(groups, path_groups_id)

def add_exception(c, m):
   if not check_not_admin(m):
        exceptions = json_load(path_exception_file)
        if len(m.command) != 2:
            m.reply(json_load(path_text_msg)['error_formating'])
        else:
            try:
                exceptions[str(m.chat.id)] = m.command[1]
                json_dump(exceptions, path_exception_file)
                m.reply(json_load(path_text_msg)['successful_addition'].format(
                    json_load(path_exception_file)[str(m.chat.id)]
                ))
            except Exception as e:
                m.reply(f'`{str(e)}`')

