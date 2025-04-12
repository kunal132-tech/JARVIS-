import random
import pyautogui as ui
import time
from Head.Mouth import speak
from Data.dlg_data.dlg import *
import webbrowser
import difflib

# Define or import open_dld, success_open, websites, open_maybe, and sorry_open here
def search_on_web(text):
    text = text.strip().lower()  # Convert to lowercase for case-insensitive comparison
    if "youtube" in text:
        # Remove unnecessary words from the search query
        text = text.replace("youtube", "").replace("play", "").replace("on", "").replace("search", "").strip()
        search_url_youtube = "https://www.youtube.com/results?search_query=" + text
        speak("Searching for " + text + " on YouTube")
        webbrowser.open(search_url_youtube)
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)
        time.sleep(0.5)
        ui.leftClick(762, 369)
    elif "amazon" in text:
        # Remove unnecessary words from the search query
        text = text.replace("amazon", "").replace("on", "").replace("search", "").strip()
        search_url_amazon = "https://www.amazon.com/s?k=" + text
        speak("Searching for " + text + " on Amazon")
        webbrowser.open(search_url_amazon)
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)
    elif "google" in text:
        # Remove unnecessary words from the search query
        text = text.replace("google", "").replace("on", "").replace("search", "").strip()
        search_url_google = "https://www.google.com/search?q=" + text
        speak("Searching for " + text + " on Google Search Engine")
        webbrowser.open(search_url_google)
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)


def app_open(text):
    text = text.replace("open","")
    text = text.strip()
    random_dlg = random.choice(open_dld)
    speak(random_dlg + text)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    randonsuccess = random.choice(success_open)
    speak(randonsuccess)

def open_web(text):

    # Convert the input to lowercase for case-insensitive matching
    website_name_lower = text.lower()

    # Check if the exact website name exists in the dictionary
    if website_name_lower in websites:
        random_dlg = random.choice(open_dld)
        speak(random_dlg + text)
        url = websites[website_name_lower]
        webbrowser.open(url)
        randonsuccess = random.choice(success_open)
        speak(randonsuccess)
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            random_dlg = random.choice(open_dld)
            randonopen2 = random.choice(open_maybe)
            closest_match = matches[0]
            speak(randonopen2 + random_dlg + text)
            url = websites[closest_match]
            webbrowser.open(url)
            randonsuccess = random.choice(success_open)
            speak(randonsuccess)
        else:
            randonsorry = random.choice(sorry_open)
            speak(randonsorry +" named " + text)

def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open","")
        text = text.replace("website","")
        text = text.replace("site","")
        text = text.strip()
        open_web(text)
    elif "app" in text or "application" in text:
        text = text.replace("app", "")
        text = text.replace("application", "")
        text = text.replace("open", "")
        text = text.strip()
        app_open(text)
    else:
        text = text.replace("open", "")
        text = text.strip()
        app_open(text)
