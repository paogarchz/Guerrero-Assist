from tkinter import ttk
from tkinter import *
import cv2
import pyttsx3
from PIL import ImageTk, Image
from pyttsx3.engine import Engine
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia

class Guerrero:
    
    def __init__(self, window): 
        self.wind = window
        self.wind.title('Guerrero Assist')
        self.wind.geometry("800x600")

        # Fondo de pantalla
        self.bg_image = ImageTk.PhotoImage(Image.open("logopagina.png"))
        self.background = Label(self.wind, image=self.bg_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # Estilos
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14), background="#0066cc", foreground="white", padx=20, pady=10)

        # Etiqueta y botón para iniciar detector de objetos
        frame = LabelFrame(self.wind, text="Detector de Objetos", font=("Helvetica", 18))
        frame.grid(row=0, column=0, padx=50, pady=50)
        Button(frame, text="Iniciar detector", command=self.detector).grid(row=0, column=0, padx=20, pady=10)


        # Etiqueta y botón para acerca de
        frame1 = LabelFrame(self.wind, text="Acerca de", font=("Helvetica", 18))
        frame1.grid(row=1, column=0, padx=50, pady=50)
        Button(frame, text="Riesgos", command=self.detector).grid(row=1, column=0, padx=20, pady=10)

        # Etiqueta y botón para iniciar asistente de voz
        frame2 = LabelFrame(self.wind, text="Asistente de Voz", font=("Helvetica", 18))
        frame2.grid(row=2, column=0, padx=50, pady=50)
        Button(frame, text="Iniciar Asistente", command=self.detector).grid(row=2, column=0, padx=20, pady=10)

    def detector(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ResistolClassif = cv2.CascadeClassifier('resistol.xml')
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            Resistol = ResistolClassif.detectMultiScale(gray,
                                                        scaleFactor=4,
                                                        minNeighbors=91,
                                                        minSize=(50,80))
            for (x, y, w, h) in Resistol:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Resistol', (x, y-10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:
                break

    def acercade(self):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        text = "La exposición en dosis altas a esas sustancias puede causar confusión y delirio. Además, puede causar mareos, somnolencia, dificultad para hablar, letargo, falta de reflejos, debilidad muscular general y estupor"
        engine.say(text)
        engine.runAndWait()

    def asisst(self):
        name = 'guerrero'
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

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
            while True:
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

        run()


if __name__ == '__main__':
    window = Tk()
    application = Guerrero(window)
    window.geometry("500x250")
    window.mainloop()
