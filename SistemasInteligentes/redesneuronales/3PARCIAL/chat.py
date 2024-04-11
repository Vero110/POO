import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json 
import pickle
import numpy as np 
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

#importamos y cargamos el archivo json 
#palabras que va a ignorar para poder trabajar
randomwords=[]
words=[]
classes=[]
documents=[]
ignore_words=['¿','?','!']

#ecoding es para que nos lea los acentos
data_file = open("SistemasInteligentes\\redesneuronales\\3PARCIAL\\intents.json", encoding='utf-8').read()
intents = json.loads(data_file)
#informacion del documento de manera correcta
#print(intents)

#prepocesamos los datos
#se creal los tokens
#iteraremos a traves de los patrones y tokenizacion
#agregamos cada palabra en las listas de palabras de nuestras etiquetas 

#la variable se va a estar ejecutando siempre y cuando este ahí 
for intent in intents['intents']:
    for pattern in intent['patterns']:
        #tokenizacion en cada palabra. Parte donde se separa cada palabra 
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #agregamos el documento a corpus 
        documents.append((w, intent['tag']))
        
        #validar si la etiqueta no esta, se va a empezar a agregar al arreglo donde esta definido como clases 
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
#vamos a obtener solo las palabras que se necesitan, y generar las palabras que no estuvieran dentro de nuestro diccionario 
#lematizar cada palabra y eliminaremos palabras duplicadas en la lista 
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
print(words)

#generar los documentos, de las clases y palabras que se estan ocupando 
pickle.dump(classes,open('classes.pkl', 'wb'))
pickle.dump(words, open('words.pkl', 'wb'))

#arreglo para guardar los datos del entrenamiento
#crear datos de entramiento y prueba

training = []
output_empty = [0] * len(classes)

#documents solo es el .json
for doc in documents:
    #espacio para palabras 
    bag = []
    #lista de tokens
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    #se crea la matriz de palabras con 1 
    
    for w in words: 
        bag.append(1) if w in pattern_words else bag.append(0)
        
    output_row = list(output_empty)
    #a traves del doc de arreglo de clases, obtener el indice todos los q estan como indice y generar el valor igualado a 1
    output_row[classes.index(doc[1])] = 1
    
    #bag = palabras correspondientes 
    #obtener las palabras correspondientes y en que fila van 
    training.append([bag, output_row])
    print(training) 
    
#radom, agarrar valores aleatorios del arreglo que tenemos como training 
random.shuffle(training)
#todos los valores que esten dentro de training, guardalos en 
train_x = [t[0] for t in training]
train_y = [t[1] for t in training]

#MODEL
#trabajaremos el modelo. Va a aprender de manera en que si una palabra ya se metio, ya no le va a dar tiempo para procesarla 
#puesto que solo va a tomar las palabras que no se han tomado, y que no se han procesado
#va a trabajar con modelo secuencial, no va a variar, es modelo lineal 
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),),activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
#esta activacion va a sumar los valores que sean igual a 1, y los 0 los va a descartar 
model.add(Dense(len(train_y[0]), activation='softmax'))

#va a empezar a decir el rango de aprendizaje de 0.01, y el decay va a validar cada uno de los aprendizajes para despues elevarlos, y en nesterov va a activar la neurona correspondiente
sgd = SGD(learning_rate = 0.01, decay = 1e-6, momentum = 0.9, nesterov=True)
#para los valores de perdida va a traer todo lo q no se estuvo trabajando 
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=300, batch_size=5,verbose=1)
model.save('chatbot_model.h5', hist)

