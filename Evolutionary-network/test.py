import pandas as pd
from api import numpy_functions
from api.layers.layers import layer
from api.evolutionary_algoritm import evolutionary_network,best_neural_networks

from projeto_series_financeiras.api.database import dataset

def create_initial_population(size):
    population=[]

    for cont in range(size):
        network = evolutionary_network()
        network.add_layer(layer(24, number_neurons=100, activation_function="tanh"))
        network.add_layer(layer(100, number_neurons=100, activation_function="relu"))
        network.add_layer(layer(100,1,"linear"))

        population.append(network)

    return population

def evolutionary_perceptron_network():
    best_network=None

    dataset = pd.read_csv("datasets//cancer classificacao.csv")

    dataX = dataset.iloc[:, 2:26].values
    dataY = numpy_functions.categorical_text_to_number(dataset.iloc[:, 1], {"M": 1, "B": 0})

    trainX, testX = numpy_functions.create_train_test(dataX)
    trainY, testY = numpy_functions.create_train_test(dataY)

    networks=create_initial_population(15)
    melhor_rede_encontrada=False

    while(not melhor_rede_encontrada):
        score_total=0
        for network in networks:
            network.evaluate_fitness(trainX,trainY,len(trainX))
            score_total=score_total+network.fitness

            if(network.fitness>=1.0):
                best_network=network
                melhor_rede_encontrada=True

            print(network.fitness)

        score_medio=score_total/len(networks)
        print("score medio:"+str(score_medio))

        if(score_medio>=1):
            break

        new_networks=[]
        best_networks,worse_networks=best_neural_networks(networks,4)
        [new_networks.append(network) for network in best_networks]

        for cont in range(0,len(best_networks)):
            for cont_2 in range(cont,len(best_networks)):
                crossover_network=best_networks[cont].crossover(best_networks[cont_2])
                new_networks.append(crossover_network)

        [new_networks.append(network) for network in numpy_functions.np.random.choice(worse_networks,5)]

        networks=new_networks

    print(best_network.predict(trainX))





if __name__=="__main__":
    evolutionary_perceptron_network()
