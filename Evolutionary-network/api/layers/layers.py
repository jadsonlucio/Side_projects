from ..neurons import neurons
from ..numpy_functions import np

class layer():
    def __init__(self,input_size,number_neurons,activation_function="relu"):
        self.number_neurons=number_neurons
        self.input_size=input_size
        self.activation_function=activation_function

        self.neurons=[neurons.neuron(input_size,activation_function) for cont in range(number_neurons)]

    def get_neoron(self,index):
        return self.neurons[index]

    def get_output_layer(self,input_array):
        result=[]
        input_array=np.array(input_array)
        ndim=input_array.ndim
        input_array=list(input_array)
        if(ndim==1):
            for neuron in self.neurons:
                result.append(neuron.get_output_function(input_array))

        elif(ndim==2):
            for input in input_array:
                line=[]
                for neuron in self.neurons:
                    line.append(neuron.get_output_function(input))
                result.append(line)
        else:
            raise ValueError("number of dimensions of input array is bigger than 2")

        return result

    def set_neurons_weights(self,learn_rate,expected_values_array):
        if(len(expected_values_array)==len(self.neurons)):
            list_error=[]
            for neuron,expected_value in zip(self.neurons,expected_values_array):
                erro=neuron.set_weights(learn_rate,expected_value)
                list_error.append(abs(erro))

            return list_error
        else:
            raise ValueError("size of expected array is different of the neurons number")


    def __copy__(self):
        layer_copy=layer(self.input_size,self.number_neurons,self.activation_function)
        neurons_copy=[neuron.__copy__() for neuron in self.neurons]
        layer_copy.neurons=neurons_copy

        return layer_copy