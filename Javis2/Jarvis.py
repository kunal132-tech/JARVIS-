from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from Head.Ear import listen
from Head.Mouth import speak
import random
from Function.wish import wish
from Function.welcome import Welcome
from Automations.open import open
from Automations.close import close
from Time import get_current_time, get_current_date, get_current_day
from GoogleFunctions import GoogleAgent

app = Flask(__name__)

# API Key Configuration (Use environment variables in production!)
GOOGLE_API_KEY = 'AIzaSyDOjRiMdd2tQOkF2jGZFIJJ-CSgyPYOgMc'
genai.configure(api_key=GOOGLE_API_KEY)

# AI Model Setup
model_name = 'chat-bison-001'
generation_config = {"temperature": 0.7, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]
model = genai.GenerativeModel(model_name, generation_config=generation_config, safety_settings=safety_settings)
convo = model.start_chat()

# Agent-Based AI System
class Manager:
    def __init__(self):
        self.agents = {
            "listener": ListenerAgent(),
            "speaker": SpeakerAgent(),
            "opener": OpenAgent(),
            "closer": CloseAgent(),
            "time_agent": TimeAgent(),
            "ai_agent": AIAgent(),
            "google_agent": GoogleAgent()
        }

    def call_agent(self, agent_name, *args):
        if agent_name in self.agents:
            return self.agents[agent_name].run(*args)
        else:
            return "Agent not found."

# Define Agents
class ListenerAgent:
    def run(self):
        return listen().lower()

class SpeakerAgent:
    def run(self, message):
        speak(message)

class OpenAgent:
    def run(self, app_name):
        open(app_name)

class CloseAgent:
    def run(self, app_name):
        close(app_name)

class TimeAgent:
    def run(self, query):
        if "time" in query:
            return get_current_time()
        elif "date" in query:
            return get_current_date()
        elif "day" in query:
            return get_current_day()

class AIAgent:
    def run(self, query):
        convo.send_message(query)
        response = convo.last.text.strip().replace("*", "").replace("**", "")
        return response

class GoogleAgent:
    def run(self, platform, contact, message):
        permission = input(f"Do you allow sending a message to {contact} on {platform}? (yes/no): ")
        if permission.lower() == "yes":
            return f"Message sent to {contact} on {platform}."
        else:
            return "Permission denied. Message not sent."

# Main Execution
manager = Manager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    user_command = request.json.get('command')
    if user_command:
        if user_command in ["hey jarvis", "wake up"]:
            return jsonify({"response": "Welcome!"})
        elif user_command in ["bye", "goodbye", "exit"]:
            return jsonify({"response": random.choice(["Goodbye!", "See you later!", "Exiting now."])})
        elif user_command.startswith("open"):
            app_name = user_command.replace("open", "").strip()
            manager.call_agent("opener", app_name)
            return jsonify({"response": f"Opening {app_name}."})
        elif user_command.startswith("close"):
            app_name = user_command.replace("close", "").strip()
            manager.call_agent("closer", app_name)
            return jsonify({"response": f"Closing {app_name}."})
        elif user_command.endswith("time") or user_command.endswith("date") or user_command.endswith("day"):
            return jsonify({"response": manager.call_agent("time_agent", user_command)})
        elif user_command.startswith("send message"):
            parts = user_command.split(" ")
            platform = parts[2]
            contact = parts[3]
            message = " ".join(parts[4:])
            return jsonify({"response": manager.call_agent("google_agent", platform, contact, message)})
        else:
            return jsonify({"response": manager.call_agent("ai_agent", user_command)})
    return jsonify({"response": "No command received."})

if __name__ == '__main__':
    app.run(debug=True)