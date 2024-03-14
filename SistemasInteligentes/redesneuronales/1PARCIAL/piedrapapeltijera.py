options = ["piedra", "tijeras", "papel"] 

def search_winner(p1,p2):
    if p1 == p2: 
        result = 0 
    elif p1 == "piedra" and p2=="tijeras":
        result =1 
    elif p1 == "piedra" and p2 =="papel":
        result =2 
    elif p1 == "tijeras" and p2 == "piedra":
        result =2
    elif p1 == "tijeras" and p2 == "papel":
        result = 1
    elif p1 == "papel" and p2 == "piedra":
        result = 1 
    elif p1 == "papel" and p2 == "tijeras": 
        result = 2 
        
    return result 


#comprobacion
print(search_winner("piedra", "papel"))

test = [
    ["piedra", "piedra", 0],
    ["piedra", "tijeras", 1],
    ["piedra", "papel", 2]
]

for partida in test: 
    print("player 1: %s player 2: %s Winner: %s Validation: "
          "%s" % (
              partida[0], partida [1], search_winner(partida[0], partida[1]), partida[2])
          )
    
#eleccion del jugador 1 de forma aleatoria 

from random import choice
def get_choice():
    return choice(options)


for i in range(10):
    player1 = get_choice()
    player2 = get_choice()
    print("player 1: %s player 2: %s Winner: %s" % (
        player1, player2, search_winner(player1, player2)

    ))
    
#inicia la red neuronal 
def str_to_listo(option):
    if option == "piedra":
        res = [1,0,0]
    elif option == "tijeras":
        res = [0,1,0]
    else: 
        res = [0,0,1]
    return res 

data_X = list(map(str_to_listo,["piedra", "tijeras", "papel"]))
data_Y = list(map(str_to_listo,["papel", "piedra", "tijeras"]))

print(data_X)
print(data_Y)


#se inicia la red neuronal 

from sklearn.neural_network import MLPClassifier
#mlpclassifier ayuda a trabajar con la red
clf = MLPClassifier(verbose=False, warm_start=True)

model = clf.fit( [data_X[0]], [data_Y[0]])
print(model)
#funcion para que juegue y aprenda al mismo tiempo
def play_and_learn(iters=10, debug=False):
    score = {"win": 0, "loose": 0}
    
    data_x = []
    data_y = []
    
    for i in range(iters): 
        player1 = get_choice()
        
        predict = model.predict_proba([str_to_listo(player1)])[0]
        
        if predict[0] >= 0.95:
            player2 = options[0]
        elif predict[1] >= 0.95:
            player2 = options[1]
        elif predict[2] >= 0.95:
            player2 = options[2]
        
        else:
            player2 = get_choice()
            
        if debug==True: 
            print("player 1: %s player 2 (modelo): %s -->%s" % (player1, predict, player2))
        
        winner = search_winner(player1, player2)
        if debug==True:
            print("comprobamos: p1 vs p2: %s" % (winner))
        
        if winner == 2: 
            data_x.append(str_to_listo(player1))
            data_y.append(str_to_listo(player1))
            
            score["win"]+=1
        else:
            score["loose"]+=1
    return score, data_X, data_Y 
#score, dataxy van a hacer las variables q diran que juegue, el debug en true para mostrar como se va jugando
score, data_x,data_y = play_and_learn(1, debug=True)
print(data_x) #jugador 1
print(data_y) #jugador 2 
print("score: %s %s %%" % (score, (score["win"]*100/(score["win"] + score["loose"]))))
if len(data_x):
    model = model.partial_fit(data_x, data_y)
    
i = 0
historic_pct = []
while True:
    i+=1
    score, data_x, data_y = play_and_learn(1000, debug= False)
    pct = (score["win"] * 100 / (score["win"] + score["loose"]))
    historic_pct.append(pct)
    print("Item: %s -score: %s %s %%" % (i, score, pct))
    
    if len(data_x):
        model = model.partial_fit(data_x, data_y)
        
    if sum(historic_pct[-9:])==900:
        break;

import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

x= range(len(historic_pct))
y= historic_pct

fig, ax = plt.subplots()
ax.set_ylabel('%')
ax.set_xlabel('Iter')
ax.set_title('porcentaje de aprendizaje en cada iteración')
plt.plot( x, y)
plt.show()