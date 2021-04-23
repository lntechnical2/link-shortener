# copyrights (mr_python_noob)
import pyshorteners
import os
from pyrogram import Client, filters
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


TOKEN = os.environ.get("BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = API_HASH = os.environ.get("API_HASH", "")
app = Client("short_link", bot_token =TOKEN , api_id = API_ID, api_hash = API_HASH )

@app.on_message(filters.command(['start']))
def start(client, message):
 message.reply_text(text =f"Hello **{message.from_user.first_name } **\n I am simple Short link generator \ n Send me long link I can convert to short \n \n**This bot created by @lntechnical** ",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],
                 [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]
           ]
        ) )

@app.on_message(filters.text & filters.private) 
def echo(client, message):
	msg = message.reply_text("🧐 **checking link is valid or not **",reply_to_message_id = message.message_id , parse_mode="markdown")
	link = message.text
	try:
		short = pyshorteners.Shortener()
		short_link =short.tinyurl.short(link)
		validate = URLValidator()
		validate(link)
	except ValidationError as exception:
		msg.edit("😒 **send me valid URL ......**",parse_mode="markdown")
		return
		msg.delete()
	message.reply_text(f" **Here your short link**\n {short_link}", disable_web_page_preview = False )	
		
app.run()

