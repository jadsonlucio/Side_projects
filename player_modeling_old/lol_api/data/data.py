import json

def read_json_file(url_file):
    with open(url_file) as file:
       return json.load(file)

def save_csv_dataframe(dataframe,url_file):
    dataframe.drop(['unnamed 0'],axis=1)
    dataframe.to_csv(url_file)