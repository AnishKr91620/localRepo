import speech_recognition as sr
import pyautogui
import time

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands (say 'scroll up' or 'scroll down')...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Error with the recognition service: {e}")
        return ""

def scroll(command):
    # Simulate scrolling in the active window (YouTube browser)
    if "scroll up" in command:
        pyautogui.scroll(300)  # Scroll up
        print("Scrolling up...")
    elif "scroll down" in command:
        pyautogui.scroll(-300)  # Scroll down
        print("Scrolling down...")
    else:
        print("No scroll command detected.")

if __name__ == "__main__":
    print("Open YouTube in your browser and position the mouse over the video feed.")
    time.sleep(5)  # Wait for the user to set up
    
    while True:
        command = recognize_voice()
        scroll(command)
