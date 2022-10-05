from pyrogram import Client, filters,enums
import pyrogram
from instagram import Pdf
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import requests
import re



async def get_json():
    data = requests.get('http://127.0.0.1:8000/word')
    return data.json()

async def admin_get_json():
    data = requests.get('http://127.0.0.1:8000/admins/')
    return data.json()

async def user_add_json(tg_id,xabar,soz,f_name,kanal):
    data = requests.get(f'http://127.0.0.1:8000/users/{tg_id}/\"{xabar}\"/{soz}/{f_name}/{kanal}/')

    return data.text
app = Client(api_id='Your Id',api_hash='Your Hash',name='Name',)





tugma = InlineKeyboardMarkup([[
        InlineKeyboardButton("New button", callback_data="new_data")]])

app.set_parse_mode(enums.ParseMode.HTML)

@app.on_message(filters.channel)
async def hello(client, message):
    if message.text == None:
        msg = message.caption
    else:
        msg = message.text
    words = await get_json()
    req = []
    res = False
    word = []
    for i in words:
        req = re.findall(f'{i["word"]}', m, flags=re.IGNORECASE)
        if req != []:
            res = True
            word.append(i['word'])
    if res:
        for admin in await admin_get_json():
            await app.send_message(admin['telegram_id'], f'ID: {message.chat.id}\n'
                                               f'SO`Z: {word}\n'
                                               f'SANA: {message.date}\n'
                                               f'Kanal: {message.chat.title}\n'
                                               f'<a href=\"https://telegram.me/{message.chat.username}/{message.id}\">XABAR:{msg}</a>\n\n',
                                   parse_mode=enums.ParseMode.HTML)
            add = await user_add_json(tg_id=message.chat.id,xabar=msg,soz=word,f_name=message.from_user.first_name,kanal=message.chat.title)
@app.on_message(filters.incoming)
async def hello(client, message):
    words = await get_json()
    if message.text == None:
        msg = message.caption
    else:
        msg = message.text
    res = []
    word = []
    for i in words:
        req = re.findall(f'{i["word"]}', msg, flags=re.IGNORECASE)
        if req != []:
            res = True
            word.append(i['word'])
    if message.chat.title == None:
        title = f'@{message.chat.username}'
    else:
        title = message.chat.title


    if res == True:
        print(message.from_user)
        for admin in await admin_get_json():
            await app.send_message(admin['telegram_id'],f'ID: {message.chat.id}\n'
                                               f'SO`Z: {word}\n'
                                               f'SANA: {message.date}\n' 
                                               f'Kanal: {message.chat.title}\n'
                                               f'<a href=\"t.me/{message.chat.username}/{message.id}\">XABAR: {msg}\n\n</a>',
                                   parse_mode=enums.ParseMode.HTML)

            add = await user_add_json(tg_id=message.chat.id, xabar=msg, soz=word, f_name=message.from_user.first_name,
                                      kanal=message.chat.title)

        await Pdf(id=1,kanal=message.chat.title,user=message.from_user.first_name,xabar=msg,link=f"t.me/{message.chat.username}/{message.id}",vaqt=message.date)




app.run()
