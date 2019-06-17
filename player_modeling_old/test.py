from lol_api.lol_dataset import api, draw_clusters
from lol_api.lol_methods import get_pos

import matplotlib.pyplot as plt

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

if __name__=="__main__":
    test=api()

    #pca
    decomposition=test.decomposition("pca",test.Dataset_numerico.columns,3,{"random_state":7,"svd_solver":"full"})
    print(str(sum(decomposition.decomposition_model.explained_variance_ratio_)))

    # plot kmeans clusters
    kmeans_cluster = test.cluster("affinitypropagation", test.Dataset_numerico.columns, {"preference":-2})
    kmeans_cluster_transform, kmeans_cluster_centroids = test.get_clusters_transformed()

    draw_clusters(kmeans_cluster_transform)

    # plot lane clusters
    position_cluster = test.get_cluster_by_features(test.Dataset_numerico.columns, ["lane", "role"], select_lane)
    test.Cluster = position_cluster
    lane_cluster_transform, lane_cluster_centroids = test.get_clusters_transformed()
    draw_clusters(lane_cluster_transform[1:], labels=["sup", "adc", "jg", "top", "mid"])

    print(position_cluster.cluster_model.cluster_centers_)

    plt.show()
