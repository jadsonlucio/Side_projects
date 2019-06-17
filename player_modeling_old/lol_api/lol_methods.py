import numpy as np

def get_pos(dict):
    pos=np.nan
    if(dict['role']=="DUO_SUPPORT"):
        pos="sup"
    elif(dict['role']=="DUO_CARRY"):
        pos="adc"
    if(dict['lane']=="JUNGLE"):
        pos="jg"
    elif(dict['lane']=="TOP"):
        pos="top"
    elif(dict['lane']=="MIDDLE"):
        pos="mid"

    return pos