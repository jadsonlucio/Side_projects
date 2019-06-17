def get_pos(lane,role=None):
    pos=None
    if(role=="DUO_SUPPORT"):
        pos="sup"
    elif(role=="DUO_CARRY"):
        pos="adc"
    if(lane=="JUNGLE"):
        pos="jg"
    elif(lane=="TOP"):
        pos="top"
    elif(lane=="MIDDLE"):
        pos="mid"

    return pos