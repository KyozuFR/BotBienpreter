import requests

#BotBienpreter  Copyright (C) 2023  Linares Julien
#This program comes with ABSOLUTELY NO WARRANTY; for details look at readme.md and LICENSE files.
#This is free software, and you are welcome to redistribute it
#under certain conditions; for details look at readme.md and LICENSE files.


def notify(lien, prix):
    try:
        with open("module/NTFY/notify.txt", "r") as mdp:
            notif = mdp.readlines(0)[0]
    except:
        print("'notify.txt' is not created. Notification, not functional")
        return
    requests.post(f"https://ntfy.sh/{notif}",
    data=f"{lien}, successful {prix} purchase".encode('utf-8'),
    headers={
        "Title": "BotBienpreter",
        "Priority": "urgent",
        "Tags": "warning",
        "Click": f"{lien}"
    })