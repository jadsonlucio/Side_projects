def max(array):
    max_value=array[0]
    max_value_index=0

    for cont in range(len(array)):
        if(max_value<array[cont]):
            max_value=array[cont]
            max_value_index=cont

    return max_value,max_value_index