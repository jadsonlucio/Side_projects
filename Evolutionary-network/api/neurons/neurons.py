import math
from .. import numpy_functions

#Activations functions
def relu(x):
    if(x<=0):
        return 0
    else:
        return x


def tanh(x):
    return 1/(1+math.e**(-x))

def linear(x,threshold=0):
    if(x>threshold):
        return 1
    else:
        return 0


dict_activation_functions={
    "relu":relu,
    "tanh":tanh,
    "linear":linear
}

class neuron():

    def get_output_function(self,input_array):
        weighted_sum=0
        input_array=list(input_array)

        if(self.bias):
            input_array.insert(0,1)

        for value, weight in zip(input_array, self.weights):
            weighted_sum = weighted_sum + value * weight

        self.output=dict_activation_functions[self.activation_function](weighted_sum)
        self.input_array=input_array

        return self.output

    def set_weights(self,learn_rate,expected_value):
        if(self.output!=None):
            erro=expected_value-self.output
            cont=0
            for value,weight in zip(self.input_array,self.weights):
                self.weights[cont]=self.weights[cont]+learn_rate*erro*value
                cont=cont+1
            return erro
        else:
            raise ValueError("Output isn't calculate yet")

    def __init__(self,input_size,activation_function="relu",bias=True):
        self.activation_function=activation_function
        self.input_size=input_size
        self.output=None
        self.input_array=None
        self.bias=True

        if(bias):
            self.weights=numpy_functions.inicialize_random_number(input_size+1)
        else:
            self.weights=numpy_functions.inicialize_random_number(input_size)


    def __copy__(self):
        neuron_copy=neuron(self.input_size,self.activation_function,self.bias)
        neuron_copy.weights=self.weights[:]

        return neuron_copy

    def __str__(self):
        pass