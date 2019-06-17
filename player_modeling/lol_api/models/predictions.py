from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier
from . import Models,Model
from ..models.datasets import Data_model


class Regression_model(Model,KNeighborsRegressor):
    def __init__(self,model_type=None,model_object=None,**kwargs):
        Model.__init__(model_type,model_object,**kwargs)

    def prediction(self,dataX):
        return self.predict(dataX)

    def _train(self,*args,**kwargs):
        self.fit(self.trainX,self.trainY)


class Classification_model(Model,KNeighborsClassifier):
    def __init__(self,model_type=None,model_object=None,**kwargs):
        Model.__init__(model_type, model_object, **kwargs)

    def prediction(self,dataX):
        return self.predict(dataX)

    def _train(self,*args,**kwargs):
        self.fit(self.trainX,self.trainY)


class Regression_models(Models):
    root_model = Regression_model
    submods_list = Regression_model.__bases__

    def __init__(self):
        Models.__init__(self)

    @classmethod

    def is_Regression(cls,model_object):
        if(isinstance(model_object,Regression_model)):
            return True
        else:
            return False

class Classification_models(Models):
    root_model = Classification_model
    submods_list = Classification_model.__bases__

    def __init__(self):
        Models.__init__(self)

    @classmethod

    def is_Classification(cls,model_object):
        if(isinstance(model_object,Classification_model)):
            return True
        else:
            return False





