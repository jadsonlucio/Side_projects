class neural_network():
    def get_network_config(self):
        pass

    def get_layer(self, index):
        pass

    def __init__(self,learn_rate=0.1,max_iter=200,min_erro=0.01,verbose=1):
        self.learn_rate=learn_rate
        self.max_iter=max_iter
        self.min_erro=min_erro
        self.verbose=verbose

        self.layers=None

    def add_layer(self,layer):
        pass

    def train(self):
        pass

    def fit(self,trainX,trainY):
        pass

    def predict(self, dataX):
        pass

    def evaluate(self, dataX, dataY):
        pass