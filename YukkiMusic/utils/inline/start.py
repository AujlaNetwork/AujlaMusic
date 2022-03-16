#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [

                    InlineKeyboardButton(

                        "❰➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕❱",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url=f"https://telegra.ph/Commands-01-10-2")],

                







                [

                    InlineKeyboardButton(

                        "❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/World_friends_chatting_group"

                    ),

                    InlineKeyboardButton(

                        "❰𝗢𝘄𝗻𝗲𝗿❱", url=f"https://t.me/ARMY0071"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "❰➕ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ➕❱",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", url=f"https://telegra.ph/Commands-01-10-2")],

                







                [

                    InlineKeyboardButton(

                        "❰𝗚𝗿𝗼𝘂𝗽❱", url=f"https://t.me/World_friends_chatting_group"

                    ),

                    InlineKeyboardButton(

                        "❰𝗢𝘄𝗻𝗲𝗿❱", url=f"https://t.me/ARMY0071"

                    ),

                ],
    ]
  
    return buttons
