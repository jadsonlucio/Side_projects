from sklearn.cluster import KMeans,AffinityPropagation,MeanShift
from . import Models,Model
from .datasets import Data_model

from ..libs.clustering import Feature_clustering,Fuzzy_cluster
from ..libs.numpy_function import mean

class Cluster_model(Model,KMeans,AffinityPropagation,MeanShift,Feature_clustering,Fuzzy_cluster):
    base_type="cluster"

    def set_cluster_centroids(self):
        model_name=self.get_model_name()
        if(model_name=="MeanShift" or model_name=="Feature_clustering"):
            self.cluster_centers_=[sum(cluster_dataset)/len(cluster_dataset) for cluster_dataset in self.cluster_data]

    def set_data_clusters(self):
        clusters_data=[[] for cont in range(0,self.n_clusters)]
        for cluster_data,cluster_label in zip(self.trainX,self.labels_):
            clusters_data[cluster_label].append(clusters_data)


        self.cluster_data=clusters_data
        self.cluster_data_model=Data_model("DataFrame",data=clusters_data,columns=["cluster_"+str(cont)
                                                                 for cont in range(0,self.n_clusters)])

    def set_atributes(self):
        if(self.fited):
            self.set_data_clusters()
            self.set_cluster_centroids()
        else:
            raise ValueError("model not fit")

    def __init__(self,cluster_type=None,cluster_object=None,**kwargs):
        Model.__init__(self,cluster_type,cluster_object,**kwargs)


    def _train(self,*args,**kwargs):
        self.fit(self.trainX)

class Cluster_models(Models):
    root_model = Cluster_model
    submods_list = Cluster_model.__bases__

    def __init__(self):
        Models.__init__(self)

    def __setitem__(self, key, value):
        if(isinstance(key,str) and isinstance(value,Cluster_models)):
            self.add_model(key,value)
        else:
            raise ValueError("erro set dataset")




