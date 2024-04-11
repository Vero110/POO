import nltk, json, random, pickle
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import numpy as np 
from tensorflow import keras 
import tkinter as tk 
from tkinter import * 

#trabajar con los archivos necearios que son las librerias, para nuestro chatboot 
model = keras.models.load_model('chatbot_model.h5')
intents = json.load(open("SistemasInteligentes\\redesneuronales\\3PARCIAL\\intents.json", encoding='utf-8'))
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

#funcion para tokenizar (Separar) el txt definido por el usuario 
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

#se crea la bolsa de palabras. una funcion para la bolsa de palabras que se van a estar analizando 
def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

#funcion para calcular la prediccion. calculo de la prediccion 
def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25 
    results = [[i,r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]
    # probabilidad y calculado para regresar la lista que es la funcion de prediccion 
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list  

#funcion para obtener la respuesta 
def getResponse(inst, intents_json):
    tag = inst[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']==tag):
            result = random.choice(i['responses'])
            break
    return result

#funcion para iniciar el chatbot 
def begin(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res 

# se creara, la funcion para enviar el mensaje, donde se va a tener toda la interfaz del usuario 
def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END) 
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: "+msg+ '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        res = begin (msg)
        ChatLog.insert(END, "Bot: "+res+'\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
base = Tk()
base.title("Hola")  # <-- Corrección aquí (title, no tittle)
base.geometry("400x500")
base.resizable(False, False)

ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial") 
ChatLog.config(state=DISABLED)

scroll = Scrollbar(base, command=ChatLog.yview, cursor="heart") 
ChatLog['yscrollcommand'] = scroll.set          
    
sendbutton = Button(base, font=("Verdana",12,'bold'), text="Send",width="12", height=5, bd=0, bg="#32de97", fg='#ffffff', command=send)

EntryBox = Text(base, bd=0, bg="white", width="29", height="5",font="Arial")
scroll.place(x=376, y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
sendbutton.place(x=6, y=401, height=90)
base.mainloop()
