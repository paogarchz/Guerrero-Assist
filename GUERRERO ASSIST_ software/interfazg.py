from tkinter import ttk
from tkinter import *
import cv2
import pyttsx3
from PIL import ImageTk, Image
from os import name
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

class Guerrero:
	
    def __init__(self, window): 
        self.wind = window
        self.wind.title('Guerrero Assist')
        

        frame = LabelFrame ()
        frame.grid(row = 5, column = 0, columnspan = 3, pady = 50, padx = 50)
        Button(frame, text = "Iniciar detector de objetos",command = detector).grid(row = 5, column = 2, padx = 10, pady = 50)

        frame1 = LabelFrame ()
        frame1.grid(row = 5, column = 0, columnspan = 3, pady = 30, padx = 50)
        Button(frame, text = "Indicaciones",command = acercade).grid(row = 5, column = 10, padx = 10)
        
        
        frame2 = LabelFrame ()
        frame2.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 0)
        Button(frame, text = "Iniciar asistente",command = asisst).grid(row = 5, column = 3, padx = 10)




def detector():
     cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
     ResistolClassif = cv2.CascadeClassifier('resistol.xml')
     while True:
         ret,frame = cap.read()
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         Resistol = ResistolClassif.detectMultiScale(gray,
                                                     scaleFactor=4,
                                                     minNeighbors=91,
                                                     minSize=(50,80))
         for (x,y,w,h) in Resistol:
             cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
             cv2.putText(frame,'Resistol',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

             cv2.imshow('frame',frame)
             if cv2.waitKey(1) == 27:
                 break



def acercade():

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    text = "Preciona el boton de Iniciar detector de objetos para identificar los objetos peligrosos, y para el asistente puedes ocupar las siguientes palabras para interectuar, guerrero dime la fecha, guerrero ¿que hora es?, guerrero Reproduce, guerrero busca"
    engine.say(text)
    engine.runAndWait()


def asisst ():
    name = 'guerrero'
    listener = sr.Recognizer()

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

        def listen():
            try:
                with sr.Microphone() as source:
                    print("Escuchando...")
                    voice = listener.listen(source)
                    rec = listener.recognize_google(voice)
                    rec = rec.lower()
                    if name in rec:
                        rec = rec.replace(name, '')
                        print(rec)
            except:
                pass
            return rec
        def run():
            rec = listen()
            if 'reproduce' in rec:
                music = rec.replace('reproduce', '')
                talk('Reproduciendo'+ music)
                pywhatkit.playonyt(music)
            elif 'hora' in rec:
                hora = datetime.datetime.now().strftime('%I:%M %p')
                talk("Son las " + hora)
            elif 'fecha' in rec:
                fecha =datetime.datetime.now().strftime('%d:%m %Y')
                talk("Hoy es" + fecha)
            elif 'busca' in rec:
                order = rec.replace('busca', '')
                info = wikipedia.summary(order, 1)
                talk(info)
            else:
                talk("Vuelve a intentarlo")
        while True:
           run()

if __name__ == '__main__':
    window = Tk()
    application = Guerrero(window)
    window.geometry("500x250")
    window.mainloop()