import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

#fijar las semillas y se trabajara con valores especificos 
np.random.seed(42)

#acciones
options = ["escapar", "andar", "atacar", "esconderse"]

def str_to_list(option):
    res = [0] * len(options)
    res[options.index(option)] = 1
    return res

# generar los datos de variables de entrada y salida
data_X = []
data_Y = []

from sklearn.model_selection import train_test_split
from random import choice

#funcion del número de registros de entrenamiento es de 150
for _ in range(150):
    health = choice(["Debil", "Medio", "Fuerte"])
    has_knife = choice(["Si", "No"])
    has_gun = choice(["Si", "No"])
    enemies = np.random.randint(0, 10)
    action = choice(options)

    input_data = [health, has_knife, has_gun, enemies]
    output_data = str_to_list(action)

    data_X.append(input_data)
    data_Y.append(output_data)

# datos de conjunto
X_train, X_test, y_train, y_test = train_test_split(data_X, data_Y, test_size=0.2, random_state=42)

# Crea el modelo de red neuronal
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('encoder', ColumnTransformer(
        transformers=[
            ('onehot', OneHotEncoder(drop='first', sparse_output=False), [0, 1, 2])  # Aplicar one-hot solo a las primeras 3 columnas
        ],
        remainder='passthrough'
    )),
    ('scaler', StandardScaler()),
    ('classifier', MLPClassifier(random_state=42, verbose=False, warm_start=True))
])

model = pipeline.fit(X_train, y_train)

# evaluacion del modelo con datos de prueba
accuracy = model.score(X_test, y_test)
print("Accuracy on test set: {:.2f}%".format(accuracy * 100))

# resultados de predicción en datos de prueba
print("\nResults on test data:")
for i, data in enumerate(X_test):
    prediction = model.predict([data])
    predicted_action = options[np.argmax(prediction)]
    print("Input: {}, Predicted Action: {}".format(data, predicted_action))
