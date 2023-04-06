#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "19413864"))
API_HASH = getenv("API_HASH", "9e33b9fdf4b840a508be5706104737eb")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5562514845:AAEyeafD0gcAgInwQj8v2WtUk-QtqNTDpv8")

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hunter:hunterop@cluster0.yffzly7.mongodb.net/?retryWrites=true&w=majority")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "180000000000000000000000")
)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180000000000000000000000")
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001821175020"))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝗧𝗕𝗛 ✦ 𝗠𝗨𝗦𝗜𝗖 ")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5388906652").split())
)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Jatindalal875/musicc",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/THE_BROTHERHOOD_COUNCIL"
)  # Example:- https://t.me/TheYukki
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/EAGLE_MAFIA_CLUB"
)  # Example:- https://t.me/YukkiSupport

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", True)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "180")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "120")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://te.legra.ph/file/a0a72d2971424c77000e3.jpg")

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "c15a0fbfb2234180b452281e8afc26cd")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "997b0914cf444a3b994efd7cc0ca443d")

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "20"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot 
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



████████╗██████╗░██╗░░██╗  ███╗░░░███╗██╗░░░██╗░██████╗██╗░█████╗░
╚══██╔══╝██╔══██╗██║░░██║  ████╗░████║██║░░░██║██╔════╝██║██╔══██╗
░░░██║░░░██████╦╝███████║  ██╔████╔██║██║░░░██║╚█████╗░██║██║░░╚═╝
░░░██║░░░██╔══██╗██╔══██║  ██║╚██╔╝██║██║░░░██║░╚═══██╗██║██║░░██╗
░░░██║░░░██████╦╝██║░░██║  ██║░╚═╝░██║╚██████╔╝██████╔╝██║╚█████╔╝
░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/ef0cce2646b2a30f128cc.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/a4ca47f0b3937c44642b3.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/ad1f7fb314b8b893a25d6.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://te.legra.ph/file/1f6e25d1302a1bd28eb35.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://te.legra.ph/file/3c09a6ae3dc4e271aaf28.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/3c09a6ae3dc4e271aaf28.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/62708c6c5d6a2890ec63c.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://te.legra.ph/file/b7347f15ad229b5745bee.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://te.legra.ph/file/b70b6423922bd16323858.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://te.legra.ph/file/89aad4451af049426a553.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/89aad4451af049426a553.jpg                              ",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

