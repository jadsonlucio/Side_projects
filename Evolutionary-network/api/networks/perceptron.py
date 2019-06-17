from .. import numpy_functions
from ..layers.layers import layer
from .neural_network import neural_network


class perceptron_network(neural_network):

    def get_network_config(self):
        config=[]
        for layer in self.layers:
            config.append(layer.number_neorons)

        return tuple(config)

    def get_layer(self,index):
        layer=self.layers[index]
        return layer


    def test_set(self,trainX,trainY):
        cont=0
        for input,output in zip(trainX,trainY):
            if(len(input)!=self.layers[0].input_size):
                raise ValueError("size of trainX["+str(cont)+"] is diferent of the fist layer size input")
            elif(len(output)!=self.layers[-1].number_neorons):
                raise ValueError("size of trainY[" + str(cont) + "] is diferent of the last layer neurons size")
            cont=cont+1


    def add_layer(self,layer):
        self.layers.append(layer)

    def __init__(self,learn_rate=0.1,max_iter=200,min_erro=0.01,verbose=1):
        neural_network.__init__(self)
        self.learn_rate=learn_rate
        self.max_iter=max_iter
        self.min_erro=min_erro
        self.verbose=verbose
        self.layers=[]
        self.fited=False


    def train(self):
        epochs_cont = 0
        while(True):
            epochs_cont=epochs_cont+1
            total_error=0
            for input,output in zip(self.trainX,self.trainY):
                self.predict(input)
                layer_error=self.layers[-1].set_neorons_weights(self.learn_rate,output)
                total_error=total_error+sum(layer_error)

            if(self.verbose):
                print("iter "+str(epochs_cont)+" total error:"+str(total_error))

            if(epochs_cont>=self.max_iter or total_error<self.min_erro):
                break


    def predict(self,dataX):
        output_layer=self.layers[0].get_output_layer(dataX)
        for layer in self.layers[1:]:
            output_layer=layer.get_output_layer(output_layer)

        return output_layer


    def fit(self,trainX,trainY):
        if(len(self.layers)==0):
            input_size=numpy_functions.get_shape(trainX)
            outout_size=numpy_functions.get_shape(trainY)
            self.add_layer(layer(outout_size,"relu",input_size))

        self.trainX = trainX
        self.trainY = trainY
        self.test_set(trainX, trainY)
        self.train()
        self.fited = True

    def evaluate(self,dataX,dataY):
        pass

    def __str__(self):
        pass

def test_function():
    perceptron = perceptron_network()
    perceptron.fit([[1, 1], [0, 1], [1, 0], [0, 0]], [[0], [0], [1], [1]])
    print(perceptron.predict([1, 1]))
    print(perceptron.get_layer(0).get_neoron(0).weights)

if __name__=="__main__":
    test_function()
