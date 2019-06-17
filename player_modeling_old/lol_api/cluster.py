import numpy
import skfuzzy as fuzz

from .numpy_function import max

class Cluster():
    def __init__(self,cluter_model,model_name,features,cluster_dataset):
        self.model=cluter_model
        self.model_name=model_name
        self.features=features
        self.cluster_dataset=cluster_dataset



class Cluster_feature():
    def set_centroids(self):
        if(self.cluster_data==None):
            self.set_clusters_data()

        self.cluster_centers_=[]
        for cluster in self.cluster_data:
            array=numpy.array(cluster)
            cluster_center=sum(array)/len(array)
            self.cluster_centers_.append(cluster_center)


    def set_clusters_data(self):
        self.cluster_data=[[] for cont in range(self.labels_size)]
        for point,label in zip(self.data,self.labels_):
            self.cluster_data[label].append(point)

    def __init__(self,data,cluster_labels,labels_size):
        self.data=data
        self.labels_size=labels_size
        self.labels_=cluster_labels
        self.cluster_centers_=None
        self.cluster_data=None
        self.set_centroids()


class Fuzzy_cluster():
    def __init__(self,ncenters=5,indice_fuzificacao=2,error=0.005,max_iter=1000,init=None,random_seed=1):
        self.ncenters=ncenters
        self.indice_fuzificacao=indice_fuzificacao
        self.error=error
        self.max_iter=max_iter
        self.init=init
        self.fited=False

        self.data=None
        self.cluster_data=None

        self.cluster_centers_=[[] for cont in range(ncenters)]
        self.labels_=None

    def fit(self,dataX):
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
            numpy.transpose(dataX), self.ncenters, self.indice_fuzificacao, self.error, self.max_iter, self.init)
        self.cluster_centers_=cntr
        self.fuzzy_partitioned_matrix=u
        self.fpc=fpc
        self.data=dataX

        self.set_labels()
        self.set_clusters_data()

    def set_labels(self):
        self.transpose_fuzzy_partitioned_matrix=numpy.transpose(self.fuzzy_partitioned_matrix)
        self.labels_=[]
        for array in self.transpose_fuzzy_partitioned_matrix:
            max_value,max_value_index=max(array)
            self.labels_.append(max_value_index)


    def set_clusters_data(self):
        self.cluster_data=[[] for cont in range(self.ncenters)]
        for point,label in zip(self.data,self.labels_):
            self.cluster_data[label].append(point)
