import numpy as np
import matplotlib.pyplot as plt

from .models.clusters import Cluster_models
from .models.datasets import Data_models
from .models.dimensionality_reduction import Dimensionality_reduction_models
from .models.predictions import Regression_models,Classification_models

from mpl_toolkits.mplot3d import Axes3D


class API():

    #set predict models

    def set_knn_regressor_model(self,name_cl,name_data_model=None,name_model_reduction=None,**knn_kwargs):
        pass

    def get_clusters_transformed(self):
        pass

    def get_data_transformed(self,data=None):
        pass

    def get_cluster_by_features(self,features_labels,cluster_selection_features,function_selection):
        pass


    def __init__(self):
        self.dataset = Data_models()
        self.cluster = Cluster_models()
        self.dimensionality_reduction = Dimensionality_reduction_models()
        self.regression = Regression_models()
        self.classification = Classification_models()

        self.models_list=[self.dataset,self.cluster,self.dimensionality_reduction,
                                              self.regression,self.classification]

    def __setitem__(self, key, value):
        if(isinstance(key,str)):
            for models in self.models_list:
                if(models.is_model(value)):
                    models[key]=models.to_model(value)

    def __getitem__(self, item):
        if(isinstance(item,str)):
            for models in self.models_list:
                if(item in models.get_models_name()):
                    return models[item]

def draw_clusters(ax,clusters_data,projection,title=None,colors=None,labels=None):

    if(title!=None):
        ax.set_title(title)
    if(colors==None):
        colors = plt.cm.rainbow(np.linspace(0,1,len(clusters_data)))

    cont = 0
    for data,color in zip(clusters_data,colors):
        x = []
        y = []
        z = []
        for data_point in data:
            x.append(data_point[0])
            y.append(data_point[1])
            if(projection=="3d"):
                z.append(data_point[2])
        if(labels!=None):
            label=labels[cont]
        else:
            label="cluster "+str(cont)
        if(projection=="3d"):
            ax.scatter(x, y, z, c=color, marker='o', label=label)
        else:
            ax.scatter(x, y, c=color, marker='o', label=label)
        ax.legend()
        cont = cont + 1


    return ax

def draw_fuzzy(ax,clusters_data,clusters_probabilitys,projection,title=None,colors=None,labels=None):
    if(title!=None):
        ax.set_title(title)
    if(colors==None):
        colors = plt.cm.rainbow(np.linspace(0,1,len(clusters_probabilitys[0])))

    cont = 0
    for cluster_point,cluster_probability in zip(clusters_data,clusters_probabilitys):
        try:
            x = [cluster_point[0]]
            y = [cluster_point[1]]
            z = [cluster_point[2]]
            new_color=np.array([0,0,0,0])
            for color,probability in zip(colors,cluster_probability):
                new_color=new_color+color*probability

            if(projection=="3d"):
                ax.scatter(x, y, z, c=new_color, marker='o')
            else:
                ax.scatter(x, y, c=new_color, marker='o')
            ax.legend()
            cont = cont + 1
        except:
            pass

    return ax


if __name__=="__main__":
    teste=api()
