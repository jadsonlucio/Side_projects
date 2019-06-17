from lol_api.lol_dataset import API
from lol_api.models.datasets import Data_model


if __name__=="__main__":
    test=API()
    test["dataframe"]=Data_model(url_file="files//datasets//ranked_dataset.csv")
    modelo=test["dataframe"]
    print(modelo)