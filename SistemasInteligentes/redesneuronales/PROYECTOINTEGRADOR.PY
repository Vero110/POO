import re 
import pandas as pd
from deep_translator import GoogleTranslator
import nltk
#libreria para el PASO 4
from textblob import TextBlob
#libreria para la intensidad del sentimiento
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#
from nltk.corpus import sentiwordnet as swn 
import matplotlib.pyplot as plt 

#nltk.download()

#CARGAR EL SSL certificado de seguridad
""" import ssl 
try:
    __create_unverified_https_context = ssl._create_unverified_context

except AttributeError:
    pass
else: 
    ssl._create_default_https_context = __create_unverified_https_context

 """
"""  descargar directamente el corpues especificamente la libreria que se quiere 
  nltk.download('stopwords) """

from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

#Paso 1 Limpiar y Traducir el texto

#Cargamos el archivo con los comentarios
data = pd.read_csv("SistemasInteligentes\\redesneuronales\\respuestas1.csv", delimiter = ",", encoding='latin1')
data.head()

#Eliminamos la columna Unnamed:1
mydata = data.drop('Unnamed: 1', axis=1)
mydata.head()
print("---- | Español | ----\n", mydata)

#Traducimos los comentarios a inglés
translator = GoogleTranslator(source='es', target='en')
mydata.review = mydata.review.apply(translator.translate)
print("\n\n\n---- | Inglés | ----\n", mydata)

#Función para limpiar el texto
def clean(text):
    #Removemos los caractceres y números
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text

#Limpiamos el texto en la columna "comentario"
mydata['Cleaned_Reviews'] = mydata['review'].apply(clean)
mydata.head()
print("\n\n\n--------------------------------------------- | Limpieza | ---------------------------------------------\n", mydata)

#Paso 2:
#2.1 Tokenización = Es el proceso de dividir el texto en palabras o frases
#2.2 Etiquetado POS (Etiquedado Gramatical): Es un proceso de conversión de cada token en una tupla que tiene la forma (palabra,etiqueta)
#2.3 Elimimación de palabras irrelevantes (Stopwords)

#Genereamos el diccionario de etiquetado gramatical
# J = Adjetivo, V = Verbo, N = Sustantivo, R = Adverbio

pos_dict = {'J': wordnet.ADJ, 'V': wordnet.VERB, 'N': wordnet.NOUN, 'R': wordnet.ADV}

def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist

mydata['POS_tagged'] = mydata['Cleaned_Reviews'].apply(token_stop_pos)
mydata.head()
print("\n\n\n--------------------------------------------- | Tokenización | ---------------------------------------------\n", mydata)

#Paso 3: Obtener la palabra raíz
#Una palabra raíz es parte de una palabra responsable de su significado léxico
wordnet_lemmatizer = WordNetLemmatizer()

def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew

mydata['Lemma'] = mydata['POS_tagged'].apply(lemmatize)
mydata.head()

#Aqui se muestra la oración inicial contra la oración procesada
#Mostrando las palabras importantes que se procesaran
print("\n\n\n--------------------------------------------- | Oración Raíz | ---------------------------------------------\n" ,mydata[['review', 'Lemma']])

# Segunda Libería VADER
# Algoritmo de Sentimientos con VADER(VALANCE AWARE DICTIONARY AND SENTIMENT REASONER)
# Este algoritmo aparte de conocer si es positivo, negativo o neutro, también nos
# obtiene la intensidad de la emoción
# La suma de las intensidades de positivo, negativo y neutro nos dará 1.
# El compuesto varía de -1 a 1, y es la métrica utilizada para dibujar el sentimiento
# #Regla es positivo si compuesto >= 0.5, nuestro si esta en -0.5 < compuesto < 0.5
# negativo si -0.5 >= compuesto
#Función para calcular la subjetividad
def getSubjectivity(comentarios):
    return TextBlob(comentarios).sentiment.subjectivity

#Función para calcular la polaridad
def getPolarity(comentarios):
    return TextBlob(comentarios).sentiment.polarity

#Función para analizar los resultados
def analysis(score):
    if score < 0 :
        return 'Negativo'
    elif score == 0:
        return 'Neutro'
    else: 
        return 'Positivo'
    
fin_data = pd.DataFrame(mydata[['review', 'Lemma']])
fin_data['Sujectividad'] = fin_data['Lemma'].apply(getSubjectivity)
fin_data['Polaridad'] = fin_data['Lemma'].apply(getPolarity)
fin_data['Resultado'] = fin_data['Polaridad'].apply(analysis)
fin_data.head()
print(fin_data)

tb_counts = fin_data.Resultado.value_counts()
print(tb_counts)
analyzer = SentimentIntensityAnalyzer()

def vadersentimentanalysis(comentario):
    vs = analyzer.polarity_scores(comentario)
    return vs['compound']

fin_data['Vader_Sentiment'] = fin_data['Lemma'].apply(vadersentimentanalysis)

def vader_analysis(compound):
    if compound >= 0.5:
        return 'Positivo'
    elif compound <= -0.5:
        return 'Negativo'
    else:
        return 'Neutro'
    
fin_data['Vader_Sentiment'] = fin_data['Vader_Sentiment'].apply(vader_analysis)
fin_data.head()
print(fin_data)


vader_counts = fin_data['Vader_Sentiment'].value_counts()
print(vader_counts)

plt.title("Resultado de VADER")
plt.figure(figsize=(10,7))
plt.pie(vader_counts.values, labels=tb_counts.index, explode=(0.1,0,0), autopct='%1.1f%%', shadow=False)
plt.show()