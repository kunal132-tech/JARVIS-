from datetime import date
import datetime
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random

today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.datetime.now()


def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(good_morning_dlg)
        speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoon_dlg)
        speak(ga_dlg)
    elif 17 <= current_hour < 21:
        ge_dlg = random.choice(good_evening_dlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_night_dlg)
        speak(gn_dlg)