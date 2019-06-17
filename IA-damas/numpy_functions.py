import numpy

def mult_scalar(vector_1,num):
    result=[value*num for value in vector_1]
    return result

def operation_vectors(vector_1,vector_2,char_opr):
    if(len(vector_1)==len(vector_2)):
        result=[]
        for value_1,value_2 in zip(vector_1,vector_2):
            if(char_opr=="+"):
                result.append(value_1+value_2)
            elif(char_opr=="-"):
                result.append(value_1-value_2)
            elif(char_opr=="*"):
                result.append(value_1*value_2)
            elif(char_opr=="/"):
                result.append(value_1/value_2)

        return result
    else:
        raise ValueError("vector one has a different size of vector two")


def get_sinal_vector(vector):
    result=[]
    for valor in vector:
        if(valor<0):
            result.append(-1)
        else:
            result.append(1)
    return result

def float_to_int(vector):
    result=[int(value) for value in vector]
    return result