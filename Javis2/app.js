const btn = document.querySelector('.talk');
const content = document.querySelector('.content');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.continuous = true;  // Keep listening continuously
recognition.interimResults = false; // Avoid duplicate execution by disabling interim results
recognition.lang = "en-US";  // Set language to English
recognition.maxAlternatives = 1; // Reduce alternatives to prevent duplicate processing

let isRecognitionActive = false;
let lastCommand = "";

function speak(text) {
    const text_speak = new SpeechSynthesisUtterance(text);
    text_speak.rate = 1;
    text_speak.volume = 1;
    text_speak.pitch = 1;

    window.speechSynthesis.speak(text_speak);
    console.log("Speaking:", text);
}

function wishMe() {
    var hour = new Date().getHours();

    if (hour < 12) {
        speak("Good Morning Boss...");
    } else if (hour < 17) {
        speak("Good Afternoon Boss...");
    } else {
        speak("Good Evening Boss...");
    }
}

function openWebsite(command) {
    let sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://www.facebook.com",
        "whatsapp": "https://web.whatsapp.com",
        "telegram": "https://web.telegram.org"
    };

    if (command === lastCommand) return; // Prevent duplicate execution
    lastCommand = command;

    for (let key in sites) {
        if (command.includes(key)) {
            speak("Opening " + key);
            window.open(sites[key], "_blank");
            setTimeout(() => {
                recognition.stop(); // Stop recognition to refresh
                setTimeout(() => recognition.start(), 60); // Restart after 60ms delay for accuracy
            }, 2000); // Allow time for action before restarting
            return;
        }
    }
    speak("Sorry, I don't know that website.");
}

function sendWhatsAppMessage(contact, message) {
    let url = `https://web.whatsapp.com/send?phone=${contact}&text=${encodeURIComponent(message)}`;
    speak("Sending message to " + contact);
    window.open(url, "_blank");
}

function sendTelegramMessage(user, message) {
    let url = `https://web.telegram.org/k/#@${encodeURIComponent(user)}`;
    speak("Sending message to " + user);
    window.open(url, "_blank");
}

function searchQuery(query) {
    if (!query) {
        speak("What do you want to search?");
        return;
    }
    let searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    speak("Searching for " + query);
    window.open(searchUrl, "_blank");
}

// Handle speech recognition results
recognition.onresult = function (event) {
    const spokenText = event.results[event.results.length - 1][0].transcript.toLowerCase().trim();
    console.log("Recognized Speech:", spokenText);

    if (spokenText.includes("open")) {
        openWebsite(spokenText);
    } else if (spokenText.includes("send whatsapp message to")) {
        let parts = spokenText.replace("send whatsapp message to", "").trim().split(" ");
        let contact = parts[0];
        let message = parts.slice(1).join(" ");
        sendWhatsAppMessage(contact, message);
    } else if (spokenText.includes("send telegram message to")) {
        let parts = spokenText.replace("send telegram message to", "").trim().split(" ");
        let user = parts[0];
        let message = parts.slice(1).join(" ");
        sendTelegramMessage(user, message);
    } else if (spokenText.includes("search for")) {
        let query = spokenText.replace("search for", "").trim();
        searchQuery(query);
    } else {
        speak("I don't know, but I can search it on Google for you.");
        searchQuery(spokenText);
    }
};

recognition.onstart = function () {
    isRecognitionActive = true;
    console.log("Voice recognition started...");
};

recognition.onend = function () {
    isRecognitionActive = false;
    console.log("Voice recognition stopped. Restarting...");
    setTimeout(() => recognition.start(), 60); // Restart after 60ms delay
};

recognition.onerror = function (event) {
    console.error("Speech recognition error:", event.error);
    if (event.error === "network" || event.error === "not-allowed") {
        speak("Please check your microphone and internet connection.");
    }
};

// Start recognition only if it's not already running
btn.addEventListener("click", () => {
    if (!isRecognitionActive) {
        recognition.start();
        console.log("Started voice recognition via button.");
    } else {
        console.warn("Speech recognition is already running.");
    }
});

window.addEventListener("DOMContentLoaded", () => {
    wishMe();
    setTimeout(() => recognition.start(), 60); // Start quickly after page loads with 60ms accuracy
});
