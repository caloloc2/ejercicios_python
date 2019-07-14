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

def procesar(target, palabra, repeticiones, ind_size):
    #ind_size = len(target)
    n_ind = 1

    letter_pool = np.array(list(range(32,127)), dtype='int8')  # Genetic pool

    # First generation
    individuals_num = np.random.choice(letter_pool, (n_ind,ind_size))
    population = ind_2_string(individuals_num)
    best_individual = population[0]
    best_fit = np.array([similarity(target, i) for i in population])[0]

    best_individual, best_fit

    for i in range(repeticiones):
        print(best_individual, best_fit)
        best_individual = mutate(best_individual, target, letter_pool)
        best_fit = similarity(target, best_individual)
        
## lee los parametros ingresados desde consola
## python ejercicio3.py archivo_txt start_word sentence_length n_rep
## 'texto a procesar'
## start_word
## sentence_length
## n_rep

archivo_txt = sys.argv[1]
start_word = sys.argv[2]
sentence_length = int(sys.argv[3])
n_rep = int(sys.argv[3])

file = open(archivo_txt, 'rt')
text = file.read()
file.close()

procesar(text, start_word, n_rep, sentence_length)