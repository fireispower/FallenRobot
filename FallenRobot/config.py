class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 7350195
    API_HASH = "b4105c3fddc4474048dfe79683555d0c"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://fireispower:ilyaryaanu@database-2.cwh8lrzkdknb.eu-north-1.rds.amazonaws.com:5432/aryas"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001869258891)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "postgres://fireispower:ilyaryaanu@database-2.cwh8lrzkdknb.eu-north-1.rds.amazonaws.com:5432/aryas"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "enigma_mainchat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6412599320:AAFde10xeuFFaSfGOnbDVL57jATTtBQDMF8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 817237333  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
