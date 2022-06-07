import requests
import json 
from gtts import gTTS
from pygame import mixer
import time
from pynput.keyboard import Key, Listener

print("press 'o' key to generate a new discussion")
print("press 'p' to stop")

def article():
    url = 'https://en.wikipedia.org/api/rest_v1/page/random/summary'
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers)
    json_response = json.loads(response.text)

    mytext = json_response["title"] + ". " + json_response["extract"]

    print(mytext)
    print("\n")
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    myobj.save("discussion.mp3")

    mixer.init()
    mixer.music.load('discussion.mp3')
    mixer.music.play()
def on_press(key):
    if hasattr(key, 'char'):
        if key.char == "o":
            article()
        if key.char == "p":
            mixer.music.stop()
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()