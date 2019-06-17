import numpy
import skfuzzy as fuzz

from lol_api.libs.numpy_function import max

class Fuzzy_cluster():
    def __init__(self,n_centers=5,indice_fuzificacao=2,error=0.005,max_iter=1000,init=None,random_seed=1):
        self.n_centers=n_centers
        self.indice_fuzificacao=indice_fuzificacao
        self.error=error
        self.max_iter=max_iter
        self.init=init
        self.fited=False

        self.data=None
        self.cluster_data=None

        self.cluster_centers_=[[] for cont in range(n_centers)]
        self.labels_=None

    def fit(self,dataX):
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
            numpy.transpose(dataX), self.n_centers, self.indice_fuzificacao, self.error, self.max_iter, self.init)
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
        self.cluster_data=[[] for cont in range(self.n_centers)]
        for point,label in zip(self.data,self.labels_):
            self.cluster_data[label].append(point)

class Feature_clustering():
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

    def __init__(self,n_centers):
        self.n_centers=n_centers
        self.cluster_centers_=None
        self.cluster_data=None
        self.labels_=None



    def fit(self,X,y=None,**kwargs):
        pass