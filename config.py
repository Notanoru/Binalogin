from os import environ 

class Config:
    API_ID = environ.get("API_ID", "DEAFULT")
    API_HASH = environ.get("API_HASH", "DEFAULT")
    BOT_TOKEN = environ.get("BOT_TOKEN", "DEFAULT") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", 'DEFAULT').split()]

