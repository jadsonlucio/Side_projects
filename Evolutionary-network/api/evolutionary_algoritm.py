from .networks.perceptron import perceptron_network
from .numpy_functions import probability,np



class evolutionary_network(perceptron_network):
    def __init__(self,**kwargs):
        perceptron_network.__init__(self,**kwargs)
        self.fitness=0

    def evaluate_fitness(self,dataX,dataY,max_points):
        absolute_erro=-0.01
        predict=self.predict(dataX)

        for real_value,predict_value in zip(dataY,predict):
            absolute_erro=absolute_erro+abs(real_value[0]-predict_value[0])

        self.fitness=(max_points-absolute_erro)/max_points

    def mutation(self):
        for layer in self.layers:
            for neuron in layer.neurons:
                neuron_weights=[]
                for weight in neuron.weights:
                    if(probability(self.fitness)):
                        new_weight=weight+np.random.random()*2-1
                        neuron_weights.append(new_weight)
                    else:
                        neuron_weights.append(weight)

                neuron.weights=neuron_weights


    def crossover(self,other):
        len_layers_net_1=len(self.layers)
        len_layers_net_2=len(other.layers)
        if(len_layers_net_1==len_layers_net_2):
            min_layer_size=len_layers_net_1
        elif(len_layers_net_1>len_layers_net_2):
            min_layer_size=len_layers_net_2
        else:
            min_layer_size=len_layers_net_1

        perceptron_crossover=self.__copy__()

        for layer_net_1,layer_net_2 in zip(perceptron_crossover.layers[:min_layer_size],other.layers[:min_layer_size]):
            len_neurons_layer_1=len(layer_net_1.neurons)
            len_neurons_layer_2=len(layer_net_2.neurons)
            if(len_neurons_layer_1==len_neurons_layer_2):
                min_neurons_size=len_neurons_layer_1
            elif(len_neurons_layer_1>len_neurons_layer_2):
                min_neurons_size=len_neurons_layer_2
            else:
                min_neurons_size=len_neurons_layer_1

            for neoron_net_1,neoron_net_2 in zip(layer_net_1.neurons[:min_neurons_size],layer_net_2.neurons[:min_neurons_size]):
                len_weights_neoron_1=len(neoron_net_1.weights)
                len_weights_neoron_2=len(neoron_net_2.weights)

                if(len_weights_neoron_1==len_weights_neoron_2):
                    min_weights_size=len_weights_neoron_1
                elif(len_weights_neoron_1>len_weights_neoron_2):
                    min_weights_size=len_weights_neoron_2
                else:
                    min_weights_size=len_weights_neoron_1

                perceptron_crossover_weights=[]
                for weights_1,weights_2 in zip(neoron_net_1.weights[:min_weights_size],neoron_net_2.weights[:min_weights_size]):
                    probability_weight_1=self.fitness/(self.fitness+other.fitness)
                    probability_weight_2=other.fitness/(self.fitness+other.fitness)

                    if(probability(probability_weight_1)):
                        perceptron_crossover_weights.append(weights_1)
                    else:
                        perceptron_crossover_weights.append(weights_2)

                neoron_net_1.weights=perceptron_crossover_weights

        return perceptron_crossover


    def __gt__(self, other):
        if(self.fitness>other.fitness):
            return True
        else:
            return False

    def __copy__(self):
        kwargs={
            "learn_rate":self.learn_rate,
            "max_iter":self.max_iter,
            "min_erro":self.min_erro,
            "verbose":self.verbose,
        }
        evolutionary_perceptron_copy=evolutionary_network(**kwargs)
        layers=[layer.__copy__() for layer in self.layers]

        evolutionary_perceptron_copy.layers=layers

        return evolutionary_perceptron_copy


def best_neural_networks(networks,size):
    for cont in range(0,len(networks)):
        for cont_2 in range(cont,len(networks)):
            if(networks[cont_2]>networks[cont]):
                aux=networks[cont]
                networks[cont]=networks[cont_2]
                networks[cont_2]=aux

    return networks[:size],networks[size:]

