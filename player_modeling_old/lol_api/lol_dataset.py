import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .cluster import Cluster,Cluster_feature,Fuzzy_cluster
from .decomposition import Decomposition
from .lol_methods import get_pos

from sklearn.cluster import KMeans,AffinityPropagation,MeanShift,MiniBatchKMeans
from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier,KernelDensity
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from mpl_toolkits.mplot3d import Axes3D

from .constants import URL_CATEGORICAL_FEATURES,URL_NUMERICAL_FEATURES,URL_CSV,DEFAULT_KMEANS_KWARGS,DEFAULT_PCA_KWARGS,URL_CSV_TEST


class api():
    def get_dataset(self,features):

        return self.Dataset.get(features)

    def pre_processamento(self):
        self.Dataset["posição"]=self.Dataset.apply(get_pos,1)
        self.Dataset = self.Dataset.dropna()

    def set_datasets(self,url_numerical_features,url_categorical_features):

        file_numerical_features=open(url_numerical_features,"r")
        file_categorical_features=open(url_categorical_features)

        numerical_features=[line.replace("\n","") for line in file_numerical_features]
        categorical_features=[line.replace("\n","") for line in file_categorical_features]

        features = []
        [features.append(feature) for feature in numerical_features]
        [features.append(feature) for feature in categorical_features]

        self.Dataset=self.Dataset[(self.Dataset.gameDuration>1800) & (self.Dataset.gameDuration<2300)]
        self.pre_processamento()

        self.Dataset_principal=self.Dataset.get(features)
        self.Dataset_numerico=self.Dataset.get(numerical_features)


    #set models

    def set_tree_classification_model(self,Cluster=None,dataX_decomposition=False,**tree_kwargs):
        if(Cluster==None):
            Cluster=self.Cluster
        if(dataX_decomposition):
            dataX=self.get_data_transformed()
        else:
            dataX=self.Cluster.cluster_dataset

        self.tree_classifiyer=DecisionTreeClassifier(**tree_kwargs)
        self.tree_classifiyer.fit(dataX,Cluster.model.labels_)

        return self.tree_classifiyer

    def set_knn_regressor_model(self,Cluster=None,dataX_decomposition=False,**knn_kwargs):
        if(Cluster==None):
            Cluster=self.Cluster
        if(dataX_decomposition):
            dataX=self.get_data_transformed()
        else:
            dataX=self.Cluster.cluster_dataset
        self.knn_regressor=KNeighborsRegressor(**knn_kwargs)
        self.knn_regressor.fit(dataX,Cluster.model.labels_)

        return self.knn_regressor

    def set_knn_classification_model(self,Cluster=None,dataX_decomposition=False,**knn_kwargs):
        if (Cluster == None):
            Cluster = self.Cluster
        if (dataX_decomposition):
            dataX = self.get_data_transformed()
        else:
            dataX = self.Cluster.cluster_dataset
        self.knn_classifiyer = KNeighborsClassifier(**knn_kwargs)
        self.knn_classifiyer.fit(dataX, Cluster.model.labels_)

        return self.knn_classifiyer


    def set_mlp_classification_model(self,Cluster=None,dataX_decomposition=False,**mlp_kwargs):
        if (Cluster == None):
            Cluster = self.Cluster
        if (dataX_decomposition):
            dataX = self.get_data_transformed()
        else:
            dataX = self.Cluster.cluster_dataset
        self.mlp_classifiyer= MLPClassifier(hidden_layer_sizes=(100,100,), activation="relu", solver="adam", alpha=0.0001,
                                            batch_size="auto", learning_rate="constant", learning_rate_init=0.001, power_t=0.5,
                                            max_iter=200, shuffle=True, random_state=7, tol=0.0001, verbose=False,
                                            warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False,
                                                 validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
        self.mlp_classifiyer.fit(dataX,Cluster.model.labels_)
        return self.mlp_classifiyer

    def set_svc_classifier_model(self,Cluster=None,dataX_decomposition=False,**svm_kwargs):
        if (Cluster == None):
            Cluster = self.Cluster
        if (dataX_decomposition):
            dataX = self.get_data_transformed()
        else:
            dataX = self.Cluster.cluster_dataset

        self.scv_classifier=SVC(random_state=1)
        self.scv_classifier.fit(dataX,Cluster.model.labels_)

        return self.scv_classifier

    def get_clusters_transformed(self):
        if("Decomposition" not in dir(self)):
            self.decomposition("pca",self.Dataset_numerico.columns,3,DEFAULT_PCA_KWARGS)

        cluster_labels=self.Cluster.model.labels_
        cluster_centroids=self.Cluster.model.cluster_centers_
        cluster_data_transform=self.Decomposition.dataset_transform



        data_clusters_transform = [[] for cont in range(len(cluster_centroids))]
        for cont in range(len(cluster_labels)):
            data_clusters_transform[cluster_labels[cont]].append(cluster_data_transform[cont])

        return data_clusters_transform,cluster_centroids

    def get_data_transformed(self,data=None):
        if("Decomposition" not in dir(self)):
            self.decomposition("pca", self.Dataset_numerico.columns, 3, DEFAULT_PCA_KWARGS)
        if(isinstance(data,np.ndarray) or isinstance(data,list)):
            return self.Decomposition.model.transform(data)
        else:
            return self.Decomposition.dataset_transform


    def get_cluster_by_features(self,features_labels,function_selection):
        dataset=self.get_dataset(features_labels)

        cluster_labels=self.Dataset.apply(function_selection,1).values
        cluster_labels_types=[]
        for label in cluster_labels:
            if(label not in cluster_labels_types):
                cluster_labels_types.append(label)

        cluster_model=Cluster_feature(dataset.values,cluster_labels,len(cluster_labels_types))

        cluster=Cluster(cluster_model,"feature_selection",features_labels,dataset.values)

        return cluster


    def __init__(self,url_csv=URL_CSV,url_numerical_features=URL_NUMERICAL_FEATURES,url_categorical_features=URL_CATEGORICAL_FEATURES):
        self.url_csv=url_csv
        self.Dataset=pd.read_csv(url_csv)
        self.set_datasets(url_numerical_features,url_categorical_features)


    #clutering and decomposition

    def cluster(self,model_name,features_labels,cluster_kwargs={}):

        if(model_name=="kmeans"):
            cluster_model=KMeans(**cluster_kwargs)
        elif(model_name=="affinitypropagation"):
            cluster_model=AffinityPropagation(**cluster_kwargs)
        elif(model_name=="meanshift"):
            cluster_model=MeanShift(**cluster_kwargs)
        elif(model_name=="minibatchkmeans"):
            cluster_model=MiniBatchKMeans(**cluster_kwargs)
        elif(model_name=="fuzzy"):
            cluster_model=Fuzzy_cluster(**cluster_kwargs)
        else:
            raise NameError("model name not finded")

        cluster_dataset = self.get_dataset(features_labels)
        cluster_model.fit(cluster_dataset.values)

        cluster=Cluster(cluster_model,model_name,features_labels,cluster_dataset)

        self.Cluster=cluster
        self.__setattr__("cluster_"+str(model_name),cluster_model)

        return cluster

    def decomposition(self,model_name,features_labels,n_componentes,kwargs_model={},standardize=False):
        if(model_name=="pca"):
            decomposition_model=PCA(n_componentes,**kwargs_model)
        else:
            raise NameError("model name not finded")

        dataset = self.get_dataset(features_labels)
        if(standardize):
            standard_decomposition_dataset = StandardScaler().fit_transform(dataset)
            transformed_dataset = decomposition_model.fit_transform(standard_decomposition_dataset)
        else:

            transformed_dataset=decomposition_model.fit_transform(dataset.values)

        decomposition=Decomposition(decomposition_model,model_name,n_componentes,features_labels,dataset,transformed_dataset)

        self.Decomposition=decomposition
        self.__setattr__("decomposition_"+str(model_name),decomposition_model)

        return decomposition



    #plots

    def plot_cluster(self,ax=None,title=None,colors=None,labels=None):
        if("Decomposition" not in dir(self)):
            self.decomposition("pca",self.Dataset_numerico.columns,3,DEFAULT_PCA_KWARGS)
        if("Cluster" not in dir(self)):
            self.cluster("kmeans",self.Dataset_numerico.columns,DEFAULT_KMEANS_KWARGS)
        if(ax==None):
            fig=plt.figure()
            ax=fig.add_subplot(111,projection="3d")
        data_clusters_transform,centroids=self.get_clusters_transformed()

        draw_clusters(ax, data_clusters_transform, "3d", title, colors, labels)

        return ax


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
