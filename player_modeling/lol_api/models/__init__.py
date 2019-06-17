from pandas.core.internals import BlockManager

models=[]

class Model():
    base_type="Model"

    def set_atributes(self):
        pass

    def get_base_name(self):
        return self.base_type

    def get_model_name(self):
        return self.type.split("-")[1]

    def __init__(self,model_type=None,model_object=None,model_name=None,model_parents=[],**kwargs):

        if(model_type!=None):
            base_class=self.get_class_by_name(model_type)
            base_class.__init__(self,**kwargs)

            self.type=self.base_type+"-"+model_type

        elif(self.is_base_class(model_object)):
            name_class=model_object.__class__.__name__
            base_class=self.get_class_by_name(name_class)
            base_class.__init__(self)

            self.__dict__=dict(model_object.__dict__)
            self.type = self.base_type + "-" + name_class
        else:
            raise ValueError("error")


        if(model_name!=None):
            self.name=model_name
        else:
            self.name=self.type.split("-")[1]

        self.fited=False

        self.children=[]
        self.parents=model_parents


    def train(self,trainX_data_model,trainY_data_model=None,*args,**kwargs):
        self.trainX_model=trainX_data_model
        self.trainX=self.trainX_model.get_data()
        if(trainY_data_model==None):
            self._train(self.trainX,*args,**kwargs)
        else:
            self.trainY_model=trainY_data_model
            self.trainY=self.trainY_model.get_data()
            self._train(self.trainX,self.trainY, *args, **kwargs)


        self.fited=True

    def add_children(self,model):
        if(isinstance(model,Model)):
            self.children.append(model)
        else:
            raise ValueError("Error in add children")

    #overwritten methods

    def _train(self,trainX,trainY=None,*args,**kwargs):
        pass

    #class methods

    def get_bases_class(self):
        return self.__class__.__bases__

    def get_class_by_name(self,name):
        for base in self.get_bases_class():
            if(base.__name__==name):
                return base

        raise ValueError("class name not find")

    def get_name_by_class(self,base_class):
        for base in self.get_bases_class():
            if(base==base_class):
                return base.__name__

        raise ValueError("base class not find")


    def is_base_class(self,class_instance):
        for base in self.get_bases_class():
            if(isinstance(class_instance,base)):
                return True

        return False

class Models(list):
    root_model = Model
    submods_list = Model.__bases__

    def set_current_model(self,model_name):
        self.current_model=self[model_name]

    def get_models_name(self):
        models_name=[]
        [models_name.append(model.name) for model in self]

        self.names=models_name
        return self.names

    def __init__(self):

        list.__init__(self)
        self.current_model=None

    def add_model(self,model_name,model_object):
        if(isinstance(model_object,Model)):
            self.append(model_object)

            self.current_model=model_object
            self.__setattr__(model_name,model_object)

            model_object.name=model_name
        else:
            raise Exception("Model_object is not of type model")

    def get_model(self,model_name):
        return self.__getattribute__(model_name)

    def __setitem__(self, key, value):
        if(isinstance(key,str)):
            self.add_model(key,value)

    def __getitem__(self, item):
        if(isinstance(item,str)):
            for model in self:
                if(model.name==item):
                    return model


    @classmethod

    def is_model(cls,obj):
        if(isinstance(obj,cls.root_model)):
            return True
        elif(obj.__class__ in cls.submods_list):
            return True
        else:
            return False

    @classmethod

    def to_model(cls,obj):
        if(isinstance(obj,cls.root_model)):
            return obj
        elif(obj.__class__ in cls.submods_list):
            return cls.root_model(model_object=obj)
        else:
            raise Exception("object is not of type "+cls.root_model.base_type)


