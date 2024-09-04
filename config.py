import os

API_ID = API_ID = 23865844

API_HASH = os.environ.get("API_HASH", "644ca71d8f3a8bf718cc317c53114d9d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7447109300:AAGxmGEdHBVpr_RjSvzOJK9nL2-W1DhItIs")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7535195022")

LOG = -1002159628443

try:
    ADMINS=[7535195022]
    for x in (os.environ.get("ADMINS", "7535195022").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
