import pyttsx3

# इंजन शुरू करें
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# अपना नाम यहाँ लिखें
if __name__ == "__main__":
    speak("Hello Prasenjit Yogi, how may I help you today?")