import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Capture audio from the microphone and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the recognition service.")
        except Exception as e:
            speak("An error occurred. Please try again.")
        return ""

def tell_date():
    """Respond with the current date."""
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}.")

def tell_time():
    """Respond with the current time."""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}.")

def search_web(query):
    """Search the web using the given query."""
    speak(f"Searching for {query} on the web.")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_wikipedia(query):
    """Search Wikipedia for the given query and provide a summary."""
    speak(f"Searching Wikipedia for {query}.")
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia: {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results on Wikipedia for that query.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")

def handle_command(command):
    """Handle the voice command and trigger appropriate actions."""
    command = command.lower()

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "date" in command:
        tell_date()
    elif "time" in command:
        tell_time()
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            search_web(query)
        else:
            speak("What should I search for?")
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        if query:
            search_wikipedia(query)
        else:
            speak("What should I search for on Wikipedia?")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I'm sorry, I can't perform that task right now.")

if __name__ == "__main__":
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = get_audio()
        if command:
            handle_command(command)
