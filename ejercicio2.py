import math, sys
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


def mutate(individuals, prob, letters):
    for i, ind in enumerate(individuals):
        for ci in range(len(ind)):
            if np.random.random() < prob:
                mutation = np.random.choice(letters).tostring().decode("ascii")
                ind = ind[0:ci] + mutation + ind[ci+1:]
        individuals[i] = ind


def procesar(ind_size, n_ind, n_gen, p_mut):
    target = "To be or, not to be: that is the question."
    letter_pool = np.array(list(range(32,127)), dtype='int8')  # Genetic pool

    # First generation
    individuals_num = np.random.choice(letter_pool, (n_ind,ind_size))
    population = ind_2_string(individuals_num)
    print(population)

    # Evolve for n_gen generations
    sim_pop = []
    for gi in range(n_gen):
        sim_vector = np.array([similarity(target, i) for i in population])
        sim_pop += [np.mean(sim_vector)]
        fitness = sim_vector / np.sum(sim_vector)
        offspring = []
        for i in range(n_ind//2):
            parents = np.random.choice(n_ind, 2, p=fitness)
            cross_point = np.random.randint(ind_size)
            offspring += [population[parents[0]][:cross_point] + population[parents[1]][cross_point:]]
            offspring += [population[parents[1]][:cross_point] + population[parents[0]][cross_point:]]
        population = offspring
        if gi < n_gen:
            mutate(population, p_mut, letter_pool)

    sim_vector = np.array([similarity(target, i) for i in population])

    hits = np.where(sim_vector == np.max(sim_vector))

    print("Best sequence:", population[hits[0][0]], "\nFrequency:", len(hits), "\nSimilarity:", np.max(sim_vector))

## lee los parametros ingresados desde consola
## python ejercicio2.py ind_size n_ind n_gen p_mut
## ind_size ==> tamano de individuales
## n_ind ==> numero de individuales
## n_gen ==> numero de generaciones
## p_mut ==> probabilidad de mutacion

if (sys.argv[1].isnumeric()):
    if (sys.argv[2].isnumeric()):
        if (sys.argv[3].isnumeric()):
            
            ind_size = int(sys.argv[1])
            n_ind = int(sys.argv[2])
            n_gen = int(sys.argv[3])
            p_mut = float(sys.argv[3])

            # crea los valores para la funcion dada
            x = np.arange(0, ind_size, 0.01)
            f = []
            for i in range(ind_size):    
                aux = (-1*(0.1 + pow((1-x[i]), 2) - (0.1*(math.cos((6*math.pi)*(1-x[i])))))) + 2    
                f.append(aux)

            procesar(ind_size, n_ind, n_gen, p_mut)

            plt.plot(f)
            plt.show()

        else:
            print("El tercer parametro debe ser un valor numerico entero")
    else:
        print("El segundo parametro debe ser un valor numerico entero")
else:
    print("El primer parametro debe ser un valor numerico entero")