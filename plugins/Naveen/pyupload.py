from info import tbot 
from plugins.events import register
import os
import asyncio
import os
import time

OWNER_ID = 2107036689

from datetime import datetime
from nandhabot import dev_user as DEV_USERS
from nandhabot import TEMP_DOWNLOAD_DIRECTORY as path
water = "./plugins/Naveen/IMG_20220625_144547_141.jpg"

client = tbot

@register(pattern=r"^/pyupload ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID or event.sender_id == DEV_USERS:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./plugins/Naveen/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("**No File Found!**")