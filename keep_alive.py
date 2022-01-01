#  ██▀███  ▓█████▄▄▄█████▓ ██▀███   ▒█████
# ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
# ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
# ▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
# ░██▓ ▒██▒░▒████▒ ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
# ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░
#   ░▒ ░ ▒░ ░ ░  ░   ░      ░▒ ░ ▒░  ░ ▒ ▒░
#   ░░   ░    ░    ░        ░░   ░ ░ ░ ░ ▒
#    ░        ░  ░           ░         ░ ░

""""This file is for if you want to run your bot in the internet make it's site and all"""

# Libraries
from flask import Flask
from threading import Thread

    print("  ██▀███  ▓█████▄▄▄█████▓ ██▀███   ▒█████ ")
    print(" ▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ")
    print(" ▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ")
    print(" ▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ")
    print(" ░██▓ ▒██▒░▒████▒ ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ")
    print(" ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ")
    print(" ░▒ ░ ▒░ ░ ░  ░   ░      ░▒ ░ ▒░  ░ ▒ ▒░  ")
    print(" ░░   ░    ░    ░        ░░   ░ ░ ░ ░ ▒  ")
    print("  ░        ░  ░           ░         ░ ░   ")

app = Flask('')

@app.route('/')
def home():
    return "The site and the bot is online!!"

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
