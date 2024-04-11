import re 
import pandas as pd
from deep_translator import GoogleTranslator
from textblob import TextBlob
import matplotlib.pyplot as plt 

from nltk.tokenize import word_tokenize 
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Paso 1: Limpiar y Traducir el texto
# Leer el primer archivo CSV
data_calif = pd.read_csv("SistemasInteligentes\\redesneuronales\\3PARCIAL\\ANALISIS DE SENTIMIENTOS-AUV (CALIF).csv", delimiter = ",")
data_calif = data_calif.drop('Unnamed: 1', axis=1)
print("---- | Español (Calif) | ----\n", data_calif)

# Leer el segundo archivo CSV
data_respuestas = pd.read_csv("SistemasInteligentes\\redesneuronales\\3PARCIAL\\ANALISIS DE SENTIMIENTOS-AUV (respuestas).csv", delimiter = ",")
data_respuestas = data_respuestas.drop('Unnamed: 1', axis=1)
print("\n---- | Español (Respuestas) | ----\n", data_respuestas)

# Traducir los comentarios a inglés en ambos conjuntos de datos
translator = GoogleTranslator(source='es', target='en')
data_calif['review'] = data_calif['review'].apply(translator.translate)
data_respuestas['review'] = data_respuestas['review'].apply(translator.translate)
print("\n\n\n---- | Inglés (Calif) | ----\n", data_calif)
print("\n---- | Inglés (Respuestas) | ----\n", data_respuestas)

# Función para limpiar el texto
def clean(text):
    # Removemos los caracteres y números
    text = re.sub('[^A-Za-z]+', ' ', text)
    return text

# Limpiamos el texto en ambos conjuntos de datos
data_calif['Cleaned_Reviews'] = data_calif['review'].apply(clean)
data_respuestas['Cleaned_Reviews'] = data_respuestas['review'].apply(clean)

# Paso 2: Tokenización y etiquetado POS
pos_dict = {'J': wordnet.ADJ, 'V': wordnet.VERB, 'N': wordnet.NOUN, 'R': wordnet.ADV}

def token_stop_pos(text):
    tags = pos_tag(word_tokenize(text))
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist

data_calif['POS_tagged'] = data_calif['Cleaned_Reviews'].apply(token_stop_pos)
data_respuestas['POS_tagged'] = data_respuestas['Cleaned_Reviews'].apply(token_stop_pos)

# Paso 3: Obtener la palabra raíz
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

data_calif['Lemma'] = data_calif['POS_tagged'].apply(lemmatize)
data_respuestas['Lemma'] = data_respuestas['POS_tagged'].apply(lemmatize)

# Análisis de sentimientos con TextBlob para ambos conjuntos de datos

# Función para calcular la subjetividad
def getSubjectivity(comentarios):
    return TextBlob(comentarios).sentiment.subjectivity

# Función para calcular la polaridad
def getPolarity(comentarios):
    return TextBlob(comentarios).sentiment.polarity

# Función para analizar los resultados
def analysis(score):
    if score < 0 :
        return 'Negativo'
    elif score == 0:
        return 'Neutro'
    else: 
        return 'Positivo'

# Aplicar el análisis de sentimientos a ambos conjuntos de datos
def analyze_sentiments(data):
    fin_data = pd.DataFrame(data[['review', 'Lemma']])
    fin_data['Sujectividad'] = fin_data['Lemma'].apply(getSubjectivity)
    fin_data['Polaridad'] = fin_data['Lemma'].apply(getPolarity)
    fin_data['Resultado'] = fin_data['Polaridad'].apply(analysis)
    return fin_data

# Resultados de análisis de sentimientos para ambos conjuntos de datos
result_calif = analyze_sentiments(data_calif)
result_respuestas = analyze_sentiments(data_respuestas)

# Imprimir los resultados
print("\n\n\n---- | Resultados (Calif) | ----\n", result_calif)
print("\n---- | Resultados (Respuestas) | ----\n", result_respuestas)

# Gráficas para ambos conjuntos de datos
plt.figure(figsize=(10, 7))
plt.subplot(1, 2, 1)
tb_counts_calif = result_calif['Resultado'].value_counts()
plt.title("Resultado de TextBlob (Calif)")
plt.pie(tb_counts_calif.values, labels=tb_counts_calif.index, explode=(0.1, 0, 0), autopct='%1.1f%%', shadow=False)

plt.subplot(1, 2, 2)
tb_counts_respuestas = result_respuestas['Resultado'].value_counts()
plt.title("Resultado de TextBlob (Respuestas)")
plt.pie(tb_counts_respuestas.values, labels=tb_counts_respuestas.index, explode=(0.1, 0, 0), autopct='%1.1f%%', shadow=False)

plt.show()
