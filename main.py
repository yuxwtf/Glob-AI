import time
import requests
import modules.pyload as pyload
import json
import random
import pyttsx3
import speech_recognition as sr

class Actions:

    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(txt: str):
        Actions.engine.say(str(txt))
        Actions.engine.runAndWait()
            

    def runaction(a):
        if 'joke' in str(a).lower():
            Actions.speak(requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"}).json()['joke'])
            


class BaseMemory:

    idk = ["What? Sorry I Never Heard That. So, I Can't Reply.", "Uhh, i don't know how to reply to that question, sorry.", "Sorry I Can't Reply...", "I Don't Know.", 'I am not yet smart enough to answer that question.', 'I am not yet enough trained to answer that question.']
    ok = ["Mhh, Ok", 'Yea, Ok', 'Ok!', 'Okk', 'Yeah Ok!']
    yes = ["Yeah!", 'Yes Sure!', 'yes', 'Yes', 'Sure!', 'Mhh Yea!', "Ye", "YES", 'Of Course!', 'sure']
    no = ['Nah', 'No sorry', 'No', 'no.', 'no..', 'No...', 'Nahh!', 'No, Never!']

    def simplelearn():
        Glob.learn("hi", "hello!!")
        Glob.learn("whats your name", "glob.")
        Glob.learn("where you live", "in yux VPS.")
        Glob.learn("how are you", "i feel good.")
        Glob.learn("how old are you", random.choice(BaseMemory.idk).replace("'", ''))
        Glob.learn("are you gay", random.choice(BaseMemory.no).replace("'", ' '))
        Glob.learn("can you do a joke", random.choice(BaseMemory.ok).replace("'", ' '))


class AI:


    def __init__(self) -> None:
        self.trainpath = "./data/trained/train.json"
        self.memorydata = open(self.trainpath, "r")
        self.trained_data = {}
        self.memory = BaseMemory()

    def trainmode(self):
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                pyload.Utils.clear()
                print(pyload.Utils.Center("Waiting Your Question..."))
                r.pause_threshold = 1
                audio = r.listen(source)
            question = str(r.recognize_google(audio, language='en-en')).replace("'", '')
            with sr.Microphone() as source:
                pyload.Utils.clear()
                print(pyload.Utils.Center(f"Reply to : '{question}'"))
                r.pause_threshold = 1
                audio = r.listen(source)
            response = str(r.recognize_google(audio, language='en-en')).replace("'", '')
            pyload.Utils.clear()
            print(pyload.Utils.Center(f"You replied to '{question}' with '{response}'"))
            time.sleep(3)
            if question == "stop":
                break
            if response == "stop":
                break
            self.learn(q=question.lower(), a=response.lower())
    
    def learn(self, q, a):
        self.trained_data[f"{q}"] = a
        open(self.trainpath, 'w').write(str(self.trained_data).replace("'", '"'))

    def ask(self, q):
        dm = json.loads(str(self.memorydata.read()))
        try:
            Actions.runaction(q)
            return dm[q]
        except:
            print(f' [LOG] replying idk to {q}')
            return random.choice(BaseMemory.idk)

    def userinput(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyload.Utils.clear()
            print(pyload.Utils.Center("LISTENING"))
            r.pause_threshold = 1
            audio = r.listen(source)
        query = str(r.recognize_google(audio, language='en-en')).replace("'", '')
        pyload.Loading.bar(0.001, f'Thinking about "{query}"', background_color=pyload.COLORS.white, textcolor=pyload.COLORS.green)
        try:
            Actions.speak(self.ask(query.lower()))
        except:
            print(f' [LOG] replying idk to {query}')
            Actions.speak(random.choice(BaseMemory.idk))


if __name__ == "__main__":
    Actions.speak('Loading')
    pyload.Loading.simple(0.5, "Loading GLOB-AI", textcolor=pyload.COLORS.red,background_color=pyload.COLORS.white)
    Glob = AI()
    Actions.speak('Learning Basic Things')
    pyload.Loading.simple(2, "Learning Simple Datas", textcolor=pyload.COLORS.red,background_color=pyload.COLORS.white)
    BaseMemory.simplelearn()
    Actions.speak('Finished Learning Basic Datas')
    tm = input('Train Mode? (Yes/No)')
    if tm.lower().replace(' ', '') == "yes":
        Glob.trainmode()
    else:
        while True:
            try:
                Glob.userinput()
            except:
                print(f' [LOG] microphone translate failed, restarting proccess')
