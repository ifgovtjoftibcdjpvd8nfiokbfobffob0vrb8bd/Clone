import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "24621592"))
API_HASH = getenv("API_HASH", "f8316a8865477f009ab53b7126eb52c3")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7251014091:AAEyZqTsES7OzF1RzwrQbWd0oVQuNsidwaQ")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","legend_mickey")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "SHEHZADIXMUSICBOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "Sheh")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "alishaxd")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mainhoonnadil:DilSagar@dilsagar.utaqo.mongodb.net/?retryWrites=true&w=majority&appName=DilSagar")
API_KEY = getenv("API_KEY")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002010769961))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 8130531095))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# config.py
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/Clone",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YASH_ABOUT_XD_lll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAM_BADNAM_BOTS")
SOURCE = getenv("SOURCE", "https://t.me/Sonali_music_bot")
CHAT = getenv("CHAT", "https://t.me/TEAM_BADNAM_BOTS")
# ------------------------------------------------------------------------------
# --------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQF3shgAwWP_ZRVQ9LvmKGSqc2F6txg6KwQPvz1YE1e8JHO12j6z2m7krA6TmmJgmvpnbqisdlS4yII8J7NcIU23RWoJM1CcWM_If2qiJqWBhB7nijSo7jirOB0QcXzxybVmLCcJOy6AmSI-3z7bF81yBJmOnph539PPK-W2vtlP3QoO1hoI5E0uGANIJWWNaPdjniJ9gIUY4nBnZwuBwtpSIVqreFmeetv7JIkiKuKM3YA6DDy8IDKchoY93qoY4ERHXkGnAhukt8-KqaBb20Cm5F9e4q2ugqDwzxF6djDfiyGakv3m8dapM5x9cuB4Ks2J5zS9P_NdrZVS6HLKP28aczC3TwAAAAHRuNNDAA")
STRING2 = getenv("STRING_SESSION2", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/cm1e7m.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/6ew59e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/66b7bb1cf206376dd5ceb-03d047178a9c3418c9.jpg"
STATS_IMG_URL = "https://graph.org/file/7db127c0ab5acc37bdfa5-30891a03d37366afbe.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
STREAM_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/20864fc056612017d4238-2d1f9b66d2fa9939f0.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

CLONE_LOGGER = int(getenv("CLONE_LOGGER", -1002046320443))
