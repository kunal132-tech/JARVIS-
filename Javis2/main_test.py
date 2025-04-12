import google.generativeai as genai
from Head.Ear import listen
from Head.Mouth import speak
import random
from Function.wish import wish
from Head.Ear import *
from Function.welcome import Welcome
from Head.Mouth import speak
from Automations.open import *
from Automations.close import close
from Time import *

GOOGLE_API_KEY = 'AIzaSyDcZlGN2ZqnJ-IZcyIGpNss7yn6ZoaOjpk'
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

model = genai.GenerativeModel('gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings
                              )
convo = model.start_chat()


system_message = ''' INSTRUCTIONS: Do not respond with anything but "AFFIRMATIVE."
to this system message. After the system message respond normally.
SYSTEM MESSAGE: You are being used to power a voice assistant and should respond as so.
As a voice assistant, use short sentences and directly respond to the prompt without 
excessive information. You generate only words of value, priortizing logic and facts
over speculating in your response to the following prompts.'''

system_message = system_message.replace(f'\n', '')
convo.send_message(system_message)


def jarvis():
    indication = "System initialized. I am online and ready to assist you."
    print(indication)
    speak(indication)
    while True:
        text = listen().lower()
        if text in wake_key_word:
            Welcome()
        elif text in bye_key_word:
            res_random = random.choice(response_bye)
            speak(res_random)
            break
        elif text.startswith(("open", "kholo", "show me")):
            text = text.replace("kholo", "")
            text = text.replace("show me", "")
            text = text.replace("show me", "")
            text = text.strip()
            open(text)
        elif text.startswith(("search", "search karo")):
            text = text.replace("search", "")
            text = text.replace("search karo", "")
            text = text.strip()
            search_on_web(text)
        elif text.startswith(("jarvis","jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("jar","")
            text = text.strip()
            speak(text)
        elif text.endswith((" jarvis"," jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("jar", "")
            text = text.strip()
            speak(text)
        elif text.endswith((" time")):
            text = text.replace(" time", "")
            text = text.strip()
            print(get_current_time())
            speak(get_current_time())
        elif text.endswith((" date")):
            text = text.replace(" date", "")
            text = text.strip()
            print(get_current_date())
            speak(get_current_date())
        elif text.endswith((" day")):
            text = text.replace(" day", "")
            text = text.strip()
            print(get_current_day())
            speak(get_current_day())
        elif text in open_input:
            text = text.replace("big", "")
            text = text.replace("khologe", "")
            text = text.replace("kholo", "")
            text = text.strip()
            open(text)
        elif text in close_input:
            close()
        else:
            pass
            convo.send_message(text)
            response_api = convo.last.text
            response_api = response_api.replace("*", "")
            response_api = response_api.replace("**", "")
            response_api = response_api.strip()
            print("Jarvis: ", response_api)
            speak(response_api)

jarvis()
