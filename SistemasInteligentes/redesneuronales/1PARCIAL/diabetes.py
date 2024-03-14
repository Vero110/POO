#importar librerias
from keras.models import Sequential
from keras.layers import Dense
import numpy 

#fijar las semillas y trabajarmos con 7 valores especificos 
numpy.random.seed(7)

#cargar datos. tipo una matriz de inf 
dataset = numpy.loadtxt("SistemasInteligentes\\ejercicio\\pima-indians-diabetes.csv", delimiter=",")
# dividido en variables de entrada x y salida y 
X = dataset[:,0:8]
Y = dataset[:,8]

#crea el modelo . densificar cada una de las capas que ayuda a decidir en que direccion va 
#va a saber que tiene 8 variables y solo una salida. Todos los nums arriba de 1 los convierte en 0 y 0 es  0
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#compilar el modelo. El adam compara fila 1 con 2, 2 con 3 y etc. Generación de solo el modelo 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit: entrena el modelo conforme a los valores, y se guardan en Y. Ejecuta cada valor 150 veces. Valor del archivo 10
model.fit(X, Y, epochs=150, batch_size=10)

#evaluacion del modelo con la variable del scores 
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#calcular predicciones
predictions = model.predict(X)
print(predictions)
#redondear las predicciones
rounded = [round(x[0]) for x in predictions]
print(rounded)