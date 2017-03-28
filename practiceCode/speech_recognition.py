#2.7 version supportable
import pyttsx
engine = pyttsx.init()
bool = 0
while bool == 0:
    message = raw_input("Type Keyword: ")
    if(message == "quit" or message =="exit"):
        bool = 1
    else:
        engine.say(message)
        engine.runAndWait()
