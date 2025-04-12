from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from Head.Ear import listen
from Head.Mouth import speak
from Function.wish import wish
from Function.welcome import Welcome
from Automations.open import open
from Automations.close import close
from Time import get_current_time, get_current_date, get_current_day

# Initialize Flask
app = Flask(__name__)

# Google AI API Key (Replace with your actual key)
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("chat-bison-001")

# Flask Route: Serve HTML Page
@app.route('/')
def home():
    return render_template('index.html')

# Flask Route: Handle AI Requests
@app.route('/jarvis', methods=['POST'])
def jarvis():
    data = request.get_json()
    user_text = data.get('message', '')

    if user_text.lower() in ["hey jarvis", "wake up"]:
        response = "Welcome! How can I assist you?"
    elif user_text.lower() in ["bye", "goodbye", "exit"]:
        response = "Goodbye! See you later."
    elif "time" in user_text:
        response = get_current_time()
    elif "date" in user_text:
        response = get_current_date()
    elif "day" in user_text:
        response = get_current_day()
    else:
        convo = model.start_chat()
        convo.send_message(user_text)
        response = convo.last.text.strip()

    return jsonify({"response": response})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
   
