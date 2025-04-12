import os
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init
import pygame

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I Am Listening Sir......", end="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)
        print("", end="", flush=True)

def translate_hindi_to_english(txt):
    english_txt = translate(txt, "en-IN")
    return english_txt

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False  # hum jo bhi bol rahe hai usski intensity yeh aapne hisab se change nahi karega
    recognizer.energy_threshold = 3500  # yeh initial audio set kiya hai agar incoming audio iss value se kam hai toh usse yeh ignore karega
    recognizer.dynamic_energy_adjustment_damping = 0.005  # jitna low value hoga utna high power hoga listen karne ka thik hai
    recognizer.dynamic_energy_ratio = 1.0  # yeh jitna zyada hoga microphone ki sensitivity utni he zyada hogi
    recognizer.pause_threshold = 0.5  # user ki speaking speed pe depend karta hai agar fast bolta hai toh value kam rakhna agar slow bolta hai toh value ko increase kardena
    recognizer.operation_timeout = None  # iska matlab hai ki koi specific time limit nahi hai recognizer ke liye, woh jitna time chahiye lega
    recognizer.pause_threshold = 0.2  # user ki speaking speed pe depend karta hai agar fast bolta hai toh value kam rakhna agar slow bolta hai toh value ko increase kardena
    recognizer.non_speaking_duration = 0.1  # Yeh decide karta hai ki jab user chup hai, tab kitna time tak recognizer active rahega, taki agle bolne se pehle thoda time ka buffer ho

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            # Use raw string for the audio file path
            file_path = r'C:\Users\VICTUS\Downloads\kusai\J.A.R.V.I.S 4\J.A.R.V.I.S 4\Initialise.mp3'
            play_sound(file_path)
            print(Fore.LIGHTGREEN_EX + "I Am Listening......", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTYELLOW_EX + "Analyzing the command......", end="", flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()

                if recognized_txt:
                    translated_txt = translate_hindi_to_english(recognized_txt)
                    print("\r" + Fore.BLUE + "Mr Ansh : " + translated_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r", end="",  flush=True)
