import numpy as np

random_seed=1

def change_random_seed():
    global random_seed
    random_seed=random_seed+1

    np.random.seed(random_seed)

def inicialize_random_number(size_weights,maximo=None,minimo=None):
    change_random_seed()
    weights = np.random.random(size_weights)
    if(maximo!=None and minimo!=None):
        valor_max=max(weights)
        valor_min=min(weights)
        weights = (weights - valor_min) / (valor_max - valor_min)
        weights = minimo + (maximo - minimo) * weights
    else:
        weights=weights*2-1

    return weights

def get_len(obj):
    if(isinstance(obj,float) or isinstance(obj,int)):
        return 1
    else:
        return len(obj)


def get_shape(array):
    len_obj=get_len(array[0])
    cont=0
    for obj in array:
        if(len_obj!=get_len(obj)):
            raise ValueError("Object array["+str(cont)+"] has a different size of the other")
        cont=cont+1

    return len_obj

def probability(value):
    if(value>1):
        value=value/100

    max_number=1000
    number = np.random.randint(1, max_number)
    min_number=value*1000

    if(number>=min_number):
        return True
    else:
        return False


#dataset functions

def create_train_test(array,percentage_train=0.75):
    size_train=int(len(array)*percentage_train)
    return array[:size_train],array[size_train:]

def categorical_text_to_number(list_text,dict):
    result=[]
    for text in list_text:
        result.append([dict[text]])

    return result
