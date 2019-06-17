import pandas as pd
from lol_api.data.league_objects import champion
from lol_api.lol_methods import get_pos
from lol_api.data.data import save_csv_dataframe
from lol_api.constants import URL_NUMERICAL_FEATURES,URL_CATEGORICAL_FEATURES

NUMERICAL_FEATURES=[line.replace("\n","") for line in open(URL_NUMERICAL_FEATURES)]
CATEGORICAL_FEATURES=[line.replace("\n","") for line in open(URL_CATEGORICAL_FEATURES)]
FEATURES=CATEGORICAL_FEATURES[:]
[FEATURES.append(feature) for feature in NUMERICAL_FEATURES]

DICT_DATASETS=[{
    "file_name":"dataset_numerical_features",
    "url":"files/datasets",
    "keys":NUMERICAL_FEATURES
},{
    "file_name":"dataset_categorical_features",
    "url":"files/datasets",
    "keys":CATEGORICAL_FEATURES
},{
    "file_name":"dataset_principal",
    "url":"files/datasets",
    "keys":FEATURES
}]

def add_champion_info_columns(dataframe):
    champion_name_array = []
    champion_fist_type_array = []
    champion_second_type_array = []

    for champion_id in dataframe.get("champiom"):
        champion_inst=champion(champion_id)
        champion_name_array.append(champion_inst.name)
        champion_fist_type_array.append(champion_inst.primary_type)
        champion_second_type_array.append(champion_inst.secondary_type)

    dataframe["champion name"]=champion_name_array
    dataframe["champion primary type"]=champion_fist_type_array
    dataframe["champion secondary type"]=champion_second_type_array

    return dataframe

def set_position(dataframe):
    posicoes_array=[]
    for lane,role in zip(dataframe.get("lane"),dataframe.get("role")):
        posicoes_array.append(get_pos(lane,role))

    dataframe["position"]=posicoes_array

    return dataframe

def set_dataframes(dataframe,dicts_datasets):
    for dict_dataset in dicts_datasets:
        dataset = dataframe.get(dict_dataset["keys"])
        dataset.to_csv(dict_dataset["url"] + "/" + dict_dataset["file_name"] + ".csv",index=False)

def pre_processe_ranked_dataset(dataframe):
    add_champion_info_columns(dataframe)
    set_position(dataframe)
    set_dataframes(dataframe, DICT_DATASETS)
    dataframe.to_csv("files//datasets//ranked_dataset.csv", index=False)


