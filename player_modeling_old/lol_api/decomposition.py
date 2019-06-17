class Decomposition():
    def __init__(self,model,model_name,model_ncomponents,features_labels,dataset,transformed_dataset):
        self.model=model
        self.model_name=model_name
        self.model_ncomponents=model_ncomponents
        self.features_labels=features_labels
        self.dataset=dataset
        self.dataset_transform=transformed_dataset
