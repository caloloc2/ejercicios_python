import sys
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def string_difference(target, test):
    match_pattern = zip(target, test)  #give list of tuples (of letters at each index)
    difference = sum(1 for e in match_pattern if e[0] != e[1])  #count tuples with non matching elements
    difference = difference + abs(len(target) - len(test)) 
    return(difference)


def ind_2_string(unicode_ind):
    individuals_str = []
    for i in unicode_ind: 
        individuals_str += [i.tostring().decode("ascii")]
    return(individuals_str)


def similarity(target, ind):
    return(1 - string_difference(target, ind)/len(ind))


def mutate(individual, target, letters):
    match_pattern = zip(target, individual)
    for i, l in enumerate(match_pattern):
        lt, li = l[0], l[1]
        if lt != li:
            li = np.random.choice(letters).tostring().decode("ascii")
            individual = individual[0:i] + li + individual[i+1:]
    return(individual)

def procesar(target, repeticiones, tipo):
    ind_size = len(target)
    n_ind = 1

    letter_pool = np.array(list(range(32,127)), dtype='int8')  # Genetic pool

    # First generation
    individuals_num = np.random.choice(letter_pool, (n_ind,ind_size))
    population = ind_2_string(individuals_num)
    best_individual = population[0]
    best_fit = np.array([similarity(target, i) for i in population])[0]

    best_individual, best_fit

    for i in range(repeticiones):
        if (tipo==1):
            print(best_individual, best_fit)
        best_individual = mutate(best_individual, target, letter_pool)
        best_fit = similarity(target, best_individual)

    if (tipo==0):
        print(best_individual, best_fit)
        
## lee los parametros ingresados desde consola
## python ejercicio3.py 'texto a procesar' numero_de_repeticiones tipo_de_salida
## 'texto a procesar' ==> cualquier texto que se desee analizar
## numero_de_repeticiones ==> numero entero para el numero de repeticiones
## tipo_de_salida ===>  1: muestra todos los textos generados, 0:muestra solo el texto con el mayor valor

if (sys.argv[2].isnumeric()):
    if (sys.argv[3].isnumeric()):

        texto = sys.argv[1]
        num_rep = int(sys.argv[2])
        tipo = int(sys.argv[3])

        if ((tipo==0) or (tipo==1)):
            procesar(texto, num_rep, tipo)
        else:
            print("El tipo de salida de ser 1 o 0")
    else:
        print("El tipo de salida de ser un valor numerico")
else:
    print("El numero de repeticiones debe ser numero")