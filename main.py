import os

from pyrogram import Client, filters,enums
from instagram import Pdf
from dotenv import load_dotenv
import requests
import re
load_dotenv()
processed_messages = set()

async def get_json():
    data = requests.get('http://127.0.0.1:8000/word')
    return data.json()

async def admin_get_json():
    data = requests.get('http://127.0.0.1:8000/admins/')
    return data.json()

async def user_add_json(tg_id,xabar,soz,f_name,kanal):
    data = requests.get(f'http://127.0.0.1:8000/users/{tg_id}/\"{xabar}\"/{soz}/{f_name}/{kanal}/')

    return data.text
app = Client(api_id='9781625',api_hash='837e8e634a13a5df9856fcc8a93df48e',name='internet2209')
# app = Client(api_id=os.getenv("api_id"),api_hash=os.getenv('api_hash'),name=os.getenv('name'))





app.set_parse_mode(enums.ParseMode.HTML)

@app.on_message(filters.channel)
async def hello(client, message):
    if message.id in processed_messages:
        return

    processed_messages.add(message.id)
    print(f"Processing message ID: {message.id}, Chat ID: {message.chat.id}")
    if message.text is None and message.caption is None:
         return 0
    if message.text is None:
        msg = message.caption
    else:
        msg = message.text
    words = await get_json()
    res = False
    word = []
    for i in words:
        req = re.findall(f'{i["word"]}', msg, flags=re.IGNORECASE)
        if req != []:
            res = True
            word.append(i['word'])
    if res:

        for admin in await admin_get_json():
            if message.chat.username is None:
                await app.send_message(admin['telegram_id'], f'ID: {message.chat.id}\n'
                                                   f'SO`Z: {word}\n'
                                                   f'SANA: {message.date}\n'
                                                   f'Kanal: {message.chat.title}\n'
                                                   f'<a href=\"https://telegram.me/c/{str(message.chat.id)[4:]}/{message.id}\">XABAR:{msg}</a>\n',
                                       parse_mode=enums.ParseMode.HTML)
            else:
                await app.send_message(admin[ 'telegram_id' ], f'ID: {message.chat.id}\n'
                                                               f'SO`Z: {word}\n'
                                                               f'SANA: {message.date}\n'
                                                               f'Kanal: {message.chat.title}\n'
                                                               f'<a href=\"https://telegram.me/{message.chat.username}/{message.id}\">XABAR:{msg}</a>\n\n',
                                       parse_mode=enums.ParseMode.HTML)
        if message.chat.first_name is None:
            await user_add_json(tg_id=message.chat.id,xabar=msg,soz=word,f_name=message.chat.id,kanal=message.chat.title)
        else:
            await user_add_json(tg_id=message.chat.id,xabar=msg,soz=word,f_name=message.chat.first_name,kanal=message.chat.title)

@app.on_message(filters.incoming)
async def hello(client, message):
    if message.id in processed_messages:
        return

    processed_messages.add(message.id)
    print(f"Processing message ID: {message.id}, Chat ID: {message.chat.id}")
    words = await get_json()
    if message.text is None and message.caption is None:
         return 0
    if message.text is None:
        msg = message.caption
    else:
        msg = message.text
    res = []
    word = []
    for i in words:
        req = re.findall(f'{i["word"]}', msg, flags=re.IGNORECASE)
        if req:
            res = True
            word.append(i['word'])
    if message.chat.title is None:
        title = f'@{message.chat.username}'
    else:
        title = message.chat.title


    if res:
        for admin in await admin_get_json():
            await app.send_message(admin['telegram_id'],f'ID: {message.chat.id}\n'
                                               f'SO`Z: {word}\n'
                                               f'SANA: {message.date}\n' 
                                               f'Kanal: {title}\n'
                                               f'<a href=\"t.me/{message.chat.username}/{message.id}\">XABAR: {msg}\n\n</a>',
                                   parse_mode=enums.ParseMode.HTML)

        if message.chat.first_name is None:
            await user_add_json(tg_id=message.chat.id, xabar=msg, soz=word, f_name=message.chat.id,
                                kanal=message.chat.title)
        else:
            await user_add_json(tg_id=message.chat.id, xabar=msg, soz=word, f_name=message.chat.first_name,
                                kanal=message.chat.title)

        await Pdf(id=1,kanal=message.chat.title,user=message.from_user.first_name,xabar=msg,link=f"t.me/{message.chat.username}/{message.id}",vaqt=message.date)




app.run()
