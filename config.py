from os import environ

API_ID = int(environ.get("API_ID", "23685822"))
API_HASH = environ.get("API_HASH", "ff0572e13ff2f63a50f6dc707e0c4c9f")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002927765158"))
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://kmjc4lad8c_db_user:jEXRvn3Dt1E5fOvz@cluster0.bbypg1m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
ADMINS = set(str(x) for x in environ.get("ADMINS", "6725874739 1018033649").split())
AUTO_DELETE = environ.get("AUTO_DELETE", "1") == "1"
AUTO_DELETE_SECOND = int(environ.get("AUTO_DELETE_SECOND", "300"))
