from lol_api.lol_dataset import api

if __name__=="__main__":
    test=api(url_csv="files/datasets/ranked_dataset.csv")


    def select_lane(dict):
        if (dict['posição'] == "sup"):
            label = 0
        elif (dict['posição'] == "adc"):
            label = 1
        elif (dict['posição'] == "jg"):
            label = 2
        elif (dict['posição'] == "top"):
            label = 3
        else:
            label = 4
        return label


    position_cluster = test.get_cluster_by_features(test.Dataset_numerico.columns, select_lane)
    test.Cluster = position_cluster
    lane_cluster_transform, lane_cluster_centroids = test.get_clusters_transformed()