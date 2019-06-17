from . import league_data
class champion():
    def __init__(self, championId):
        self.championId = championId
        if(championId>0):
            self.data=self.get_chapion_data_by_id(championId)
            self.atributes = {}
            for key, value in zip(self.data.keys(), self.data.values()):
                if(key=="skins"):
                    self.skins=[skin(skin_dict["id"]) for skin_dict in value]
                elif(key=="tags"):
                    self.primary_type=value[0]
                    if(len(value)>1):
                        self.secondary_type=value[1]
                    else:
                        self.secondary_type=None
                else:
                    self.__setattr__(key,value)
                self.atributes[key]=value

    def get_name(self):
        return self.data["name"]

    def get_style(self):
        pass

    def __str__(self):
        return str(self.championId)

    @classmethod
    def get_chapion_data_by_id(cls,champion_id):
        return league_data.get_champion_data(champion_id,True)


class speell():
    def __init__(self, spell1Id):
        self.speellId = spell1Id

    def __str__(self):
        return str(self.speellId)


class map():
    def __init__(self, mapId,gameMode,gameType):
        self.mapId = mapId
        self.gameMode=gameMode
        self.gameType=gameType

    def __str__(self):
        return str(self.mapId)

class season():
    def __init__(self,seasonId):
        self.seasonId=seasonId

    def __str__(self):
        return str(self.seasonId)

class item():
    def __init__(self,itemId):
        self.itemId=itemId

    def __str__(self):
        return str(self.itemId)

class skin():
    def __init__(self,skinId):
        self.skinId=skinId

