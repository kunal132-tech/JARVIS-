from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random

def Welcome():
    welcome_message = random.choice(welcome_dlg)
    speak(welcome_message)

