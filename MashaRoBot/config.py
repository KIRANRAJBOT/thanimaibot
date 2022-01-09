import json
import os


def get_user_list(config, key):
    with open('{}/MashaRoBot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = 8962397  # integer value, dont use ""
    API_HASH = "0336e890a385149db77821a136a7fce3"
    TOKEN = "5092817961:AAG1yNtue_fZk1EkRZBXaMsntv35AWxTrNE"
    OWNER_ID = 1928904042  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "TheTelegrampro"
    SUPPORT_CHAT = 'thanimaisupport'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001739802989  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001739802989  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = 'postgres://kkzncyijeufsar:f5d15b472e033a224781aa8638ea1b5052543234f0b63bbed4b9941278769a01@ec2-3-222-34-244.compute-1.amazonaws.com:5432/ddob55b7lf7vif'
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "2052309535"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
   
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
