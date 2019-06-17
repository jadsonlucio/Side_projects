from pandas import DataFrame,Series
from pandas import read_csv
from pandas.core.internals import BlockManager

from . import Models,Model



class Data_model(Model,DataFrame):
    base_type="Data"

    def __init__(self,model_type=None,model_object=None,url_file="",**kwargs):
        if(model_type==None and model_object==None):
            model_object=read_csv(url_file,**kwargs)
        if(isinstance(model_type,BlockManager)):
            model_object=DataFrame(model_type)
            model_type=None

        Model.__init__(self,model_type,model_object,**kwargs)

    def split_train(self,train_size,test_size):
        if(train_size+test_size==1):
            train_size=int(self.size*train_size)
            test_size=int(self.size*test_size)

            train=self[:train_size]
            test=self[-test_size:]

            train.parents.append(self)
            test.parents.append(self)

            self.add_children(train)
            self.add_children(test)

            self.train=train
            self.test=test

            return train,test

        else:
            raise ValueError("train and test doesn't sum 1")

    @property
    def _constructor(self):
        return Data_model


class Data_models(Models):
    root_model = Data_model
    submods_list = Data_model.__bases__

    def __init__(self):
        Models.__init__(self)

    def __setitem__(self, key, value):
        if(isinstance(key,str) and isinstance(value,Data_model)):
            self.add_model(key,value)
        else:
            raise ValueError("erro set dataset")

