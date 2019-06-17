from sklearn.decomposition import PCA,MiniBatchSparsePCA
from ..models.datasets import Data_model
from . import Models,Model

class Dimensionality_reduction_model(Model,PCA,MiniBatchSparsePCA,):
    base_type = "Dimensionality_reduction"

    def __init__(self,model_type=None,model_object=None,**kwargs):
        Model.__init__(self,model_type,model_object,**kwargs)

    def train(self,*args,**kwargs):
        self.transform_data=self.fit_transform(self.trainX)
        self.transform_data_model=Data_model("DataFrame",data=self.transform_data,columns=["component_"+str(cont)
                                                                  for cont in range(self.n_components)])

        self.trainX_model.add_children(self.transform_data_model)

    def transform_data(self, dataX):
        shape_dataX=dataX.values.shape[1]
        shape_trainDataX=self.trainX.shape[1]
        shape_nComponents=self.n_components

        if(shape_dataX==shape_trainDataX):
            return self.transform(dataX)
        elif(shape_dataX==shape_nComponents):
            return self.inverse_transform(dataX)
        else:
            raise ValueError("dataX shape is diferent from train data shape or component data shape")


    def __setitem__(self, key, value):
        if(isinstance(key,str)):
            self.__setattr__(key,value)


class Dimensionality_reduction_models(Models):
    root_model=Dimensionality_reduction_model
    submods_list=Dimensionality_reduction_model.__bases__

    def __init__(self):
        Models.__init__(self)

    def __setitem__(self, key, value):
        if(isinstance(key,str) and isinstance(value,Dimensionality_reduction_model)):
            self.add_model(key,value)
        else:
            raise ValueError("erro set dataset")

    @classmethod
    def is_dimensionality_reduction(cls, obj):
        if (isinstance(obj, Dimensionality_reduction_model)):
            return True
        elif (obj.__class__ in cls.model_class_list):
            return True
        else:
            return False

    @classmethod
    def set_data_model(cls, obj):
        if (isinstance(obj, Data_model)):
            return obj
        elif (obj.__class__ in cls.model_class_list):
            return Data_model(model_object=obj)
        else:
            raise Exception("object is not data_model or isn't add yet")

