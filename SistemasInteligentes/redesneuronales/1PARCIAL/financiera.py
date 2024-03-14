#importar librerias
from keras.models import Sequential
from keras.layers import Dense
import numpy 

#fijar las semillas y trabajarmos con 7 valores especificos 
numpy.random.seed(7)

from random import choice, randint
#generación de los datos, registros
#estado civil, genero y edad y los ingresos
def generate_data(num_records=100):
    data = []
    for _ in range(num_records):
        estado_civil = choice(["soltero", "casado", "divorciado"])
        genero = choice(["hombre", "mujer"])
        edad = randint(18, 70)
        ingresos = randint(10000, 999999999)
        data.append([estado_civil, genero, edad, ingresos])
    return data

#función para evaluar la fiabilidad basada en reglas de asociasion 
#que es 1 el cliente fiable y el 0 no es cliente NO fiable 
def evaluate_reliability(client):
    if client[2] >= 25 and client[3] >= 29000:
        return 1 
    else:
        return 0  

#aplicacion las reglas de asociación
clientes_data = generate_data()
clientes_labels = [evaluate_reliability(client) for client in clientes_data]

clientes_data_encoded = []
for client in clientes_data:
    encoded_client = []
    encoded_client.extend([1 if client[0] == estado else 0 for estado in ["Soltero", "Casado", "Divorciado"]])
    encoded_client.extend([1 if client[1] == genero else 0 for genero in ["Hombre", "Mujer"]])
    encoded_client.extend([client[2], client[3]])
    encoded_client.extend([0] * (8 - len(encoded_client)))
    clientes_data_encoded.append(encoded_client)

#conversion de los registros de array 
X = numpy.array(clientes_data_encoded)
Y = numpy.array(clientes_labels)

#inicia la red neuronal 
#crea el modelo de la red densificar cada una de las capas que ayuda a decidir en que direccion va 
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# entrena el modelo conforme a los valores dados
model.fit(X, Y, epochs=150, batch_size=10, verbose=1)

#evaluacion del modelo con la variable del scores 
test_data = generate_data(5)
test_data_encoded = []
for client in test_data:
    encoded_client = []
    encoded_client.extend([1 if client[0] == estado else 0 for estado in ["Soltero", "Casado", "Divorciado"]])
    encoded_client.extend([1 if client[1] == genero else 0 for genero in ["Hombre", "Mujer"]])
    encoded_client.extend([client[2], client[3]])
    test_data_encoded.append(encoded_client)

X_test = numpy.array(test_data_encoded)
predictions = model.predict(X_test)

#redondeo de las predicciones
rounded_predictions = [round(x[0]) for x in predictions]


# imprension de resultados
for i in range(5):
    print(f"Cliente {i+1}: Datos={test_data[i]}, Fiabilidad Predicha={rounded_predictions[i]}")
