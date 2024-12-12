from os import getenv

API_ID = getenv("28132883")
API_HASH = getenv("22eefd902a5b8edfceeeab1487ed60c8")
BOT_TOKEN = getenv("7259513984:AAHP3IVTymfLQScfh_rZGm4ESH-ehWLiykM")
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

DATABASE_URL = getenv("mongodb+srv://kala:kala@cluster0.qpadelh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))
