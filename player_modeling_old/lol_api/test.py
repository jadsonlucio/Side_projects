from lol_api.lol_dataset import api,draw_clusters
from lol_api.lol_methods import get_pos
from lol_api.cluster import Fuzzy_cluster

import matplotlib.pyplot as plt

def select_win(win):
    if(win==True):
        return 0
    elif(win==False):
        return 1


def select_lane(array):
    lane=array[0]
    role=array[1]
    pos=get_pos(lane,role)
    label=0
    if(pos=="sup"):
        label=1
    elif(pos=="adc"):
        label=2
    elif(pos=="jg"):
        label=3
    elif(pos=="top"):
        label=4
    elif(pos=="mid"):
        label=5
    return label

def plot_win(api):
    cluster = api.get_cluster_by_features(test.Dataset_numerico.columns,"win", select_win)
    api.Cluster=cluster
    api.plot_cluster(labels=["vitoria","derrota"])

def plot_kmean_cluster(api):
    api.cluster("kmeans",test.Dataset_numerico.columns,{"n_clusters":5,"random_state":0})
    api.plot_cluster()


def plot_lane_cluster(api):
    cluster = api.get_cluster_by_features(test.Dataset_numerico.columns,["lane","role"], select_lane)
    api.Cluster=cluster
    api.plot_cluster(labels=["sem informação","sup","adc","jg","top","mid"])


def test_knn(_api):
    knn_dataframe=api("files/test.csv","files/clustering numerical features.txt","files/clustering categorical features.txt")

    numerical_features=knn_dataframe.Dataset_numerico.values
    knn_model=_api.knn_regressor

    knn_dataframe.Dataset_numerico.insert(0,column="resultado",value=knn_dataframe.Dataset.get("win"))
    knn_dataframe.Dataset_numerico.insert(0, column="resultado_previsto", value=knn_model.predict(numerical_features))
    knn_dataframe.Dataset_numerico.to_csv("..//files//knn_resultados.csv")

def test_fuzzy(_api):
    fcp_matrix=[]
    for cont in range(2,20):
        _api.cluster("fuzzy",test.Dataset_numerico.columns,{"ncenters":cont})
        _api.plot_cluster()
        fcp_matrix.append(_api.Cluster.model.fcp)
    print(fcp_matrix)
    _api.plot_cluster()
    plt.show()


if __name__=="__main__":
    test=api("../files/datasets/ranked_dataset.csv","../files/dicionarios e caracteristicas/clustering numerical features.txt","../files/dicionarios e caracteristicas/clustering categorical features.txt")
    test.decomposition("pca",test.Dataset_numerico.columns,3,{"random_state":0})
    test_fuzzy(test)
