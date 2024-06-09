from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25120174")
    API_HASH = environ.get("API_HASH", "89a10ea368b634194752731a7c405e30")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7177898659:AAHvM5KKzCAdWsjdG5ApKxU5q4qBXPy9rbg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5477824201').split()]

