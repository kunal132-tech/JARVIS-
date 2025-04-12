from Head.Mouth import speak

class GoogleAgent:
    def run(self, platform, contact, message):
        permission = input(f"Do you allow sending a message to {contact} on {platform}? (yes/no): ")
        if permission.lower() == "yes":
            print(f"Sending '{message}' to {contact} on {platform}...")
            speak(f"Message sent to {contact} on {platform}.")
        else:
            speak("Permission denied. Message not sent.")
