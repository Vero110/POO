import re 
import pandas as pd
from deep_translator import GoogleTranslator
import nltk

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

#cargar archivo con los comentarios, los datos que tenemos
data = pd.read_csv("SistemasInteligentes\\redesneuronales\\2PARCIAL\\Comentarios.csv", delimiter = ",")
data.head()

#eliminamos la columna numero1
mydata = data.drop('Unnamed: 1', axis=1)
mydata.head()
print(mydata)

#traducir el texto de español a ingles
translator = GoogleTranslator(source="es", target="en")
mydatareview = mydata.review.apply(translator.translate)
print (mydata) 

#funcion para limpiar el texto del archivo 
def clean(text):
    #remover los caracteres y numeros que se ocupen 
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text

#limpiar el txt en la columna comentario
mydata['Cleaned_Reviews'] = mydata['review'].apply(clean)
mydata.head()
print(mydata)

#PASO 2
#2.1 Tokenizacion = proceso para dividir el txt en diferentes partes llamadas tokens
#2.2 Etiquetado POS (gramatical) = proceso de conversion de cada token en una tupla que tiene la forma (palabra, etiqueta)
#2.3 Eliminacion de palabras irrelevantes

#generacion del diccionario de etiquetado gramatical 
# J = adjetivo, V = Verbo, N = Sustantivo, R = Adverbio