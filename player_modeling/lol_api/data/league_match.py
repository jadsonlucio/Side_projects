from . import league_objects
import pandas as pd

class Match():
    def __init__(self,match_dict):
        self.atributes={}
        for key,value in zip(match_dict.keys(),match_dict.values()):
            if(key=="seasonId"):
                self.season=league_objects.season(value)
                self.atributes["season"]=self.season
            elif(key=="mapId"):
                self.map=league_objects.map(value,match_dict["gameMode"],match_dict["gameType"])
                self.atributes["map"]=self.map
            elif(key=="teams"):
                self.teams = [Team(team_dict,match_dict["participants"],match_dict["participantIdentities"]) for team_dict in value]
                self.atributes["teams"]=self.teams
            elif(key=="participants" or key=="participantIdentities" or key=="gameMode" or key=="gameType"):
                pass
            else:
                self.__setattr__(key, value)
                self.atributes[key] = value

    def to_pandas(self):
        dataframes=[]
        for team in self.teams:
            pandas_team=team.to_pandas()
            for key,value in zip(self.atributes.keys(),self.atributes.values()):
                if(key!="teams" and key!="platformId"):
                    pandas_team.insert(0,key,str(value))

            dataframes.append(pandas_team)

        return pd.concat(dataframes,ignore_index=True)

class Team():

    def get_atributes(self):
        result={}

    def relative_atributes(self,atribute_name):
        values=[player.stats.atributes[atribute_name] for player in self.players]
        sum_values=sum(values)
        if(sum_values!=0):
            relative_values=[value/sum_values for value in values]
        else:
            relative_values = [value / 1 for value in values]

        return relative_values

    def __init__(self,team_dict,participants,participantIdentities):
        self.atributes={}
        for key, value in zip(team_dict.keys(), team_dict.values()):
            if(key=="bans"):
                self.bans = [ban(ban_dict) for ban_dict in value]
                self.atributes["bans"]=self.bans
            else:
                self.__setattr__(key,value)
                self.atributes[key]=value
        self.players = [player(player_dict,play_account_dict["player"]) for player_dict,play_account_dict in
                zip(participants,participantIdentities) if (player_dict["teamId"]==self.atributes["teamId"])]
        self.atributes["players"]=self.players

    def add_relative_atributes(self,dataframe):
        relative_atributes=["goldEarned","kills","assists","deaths","longestTimeSpentLiving","magicDamageDealt","magicDamageDealtToChampions","magicalDamageTaken","neutralMinionsKilled","physicalDamageDealt","physicalDamageDealtToChampions","physicalDamageTaken","totalDamageDealt","totalDamageTaken","totalDamageDealtToChampions","totalHeal","totalMinionsKilled","trueDamageDealt","trueDamageDealtToChampions","trueDamageTaken","visionScore","wardsPlaced","visionWardsBoughtInGame","timeCCingOthers","totalTimeCrowdControlDealt"]

        for atribute in relative_atributes:
            dataframe.insert(1,value=self.relative_atributes(atribute),column="rel_"+atribute)


        return dataframe

    def to_pandas(self):
        dataframe=pd.DataFrame([player.get_atributes() for player in self.players])
        return self.add_relative_atributes(dataframe)

class player():

    def get_atributes(self):
        result = {}
        for key, value in zip(self.atributes.keys(), self.atributes.values()):
            if (key=="championId" or key=="spell1Id" or key=="spell2Id"):
                result[key] = str(value)
            elif (key == "stats"):
                stats_atributes=self.stats.get_atributes()
                for key, value in zip(stats_atributes.keys(),stats_atributes.values()):
                    result[key] = value
            else:
                result[key] = value

        return result

    def __init__(self,participant_dict,participant_account_dict):
        self.atributes={}
        for key,value in zip(participant_dict.keys(),participant_dict.values()):
            if(key=="championId"):
                self.champiom = league_objects.champion(value)
                self.atributes["champion"]=self.champiom
            elif(key=="spell1Id"):
                self.speell_1 = league_objects.speell(value)
                self.atributes["spell_1"]=self.speell_1
            elif(key=="spell2Id"):
                self.speell_2 = league_objects.speell(value)
                self.atributes["spell_2"]=self.speell_2
            elif(key=="stats"):
                self.stats = stats(value,participant_dict["timeline"])
                self.atributes["stats"]=self.stats
            elif(key=="teamId" or key=="timeline"):
                pass
            else:
                self.__setattr__(key,value)
                self.atributes[key]=value
        for key,value in zip(participant_account_dict.keys(),participant_account_dict.values()):
            self.__setattr__(key, value)
            self.atributes[key] = value

    def __str__(self):
        pass

class stats():

    def get_atributes(self):
        result={}
        for key,value in zip(self.atributes.keys(),self.atributes.values()):
            if("item" in key):
                result[key]=str(value)
            elif(key=="timeline"):
                timeline_atributes=self.timeline.get_atributes()
                for key,value in zip(timeline_atributes.keys(),timeline_atributes.values()):
                    result[key]=value
            else:
                result[key]=value

        return result

    def __init__(self,stats_dict,timeline_dict):
        self.atributes={}

        for key,value in zip(stats_dict.keys(),stats_dict.values()):
            if(key=="item0" or key=="item1" or key=="item2" or key=="item3" or key=="item4" or key=="item5" or key=="item6"):
                item=league_objects.item(value)
                self.__setattr__(key,item)
                self.atributes[key]=item
            elif(key=="participantId"):
                pass
            else:
                self.__setattr__(key,value)
                self.atributes[key]=value

        self.timeline=timeline(timeline_dict)
        self.atributes["timeline"]=self.timeline

    def __str__(self):
        pass

class timeline():

    def get_atributes(self):
        return self.atributes

    def __init__(self,timeline_dict):
        self.atributes={}
        for key,value in zip(timeline_dict.keys(),timeline_dict.values()):
            self.__setattr__(key,value)
            self.atributes[key]=value

    def __str__(self):
        pass

class ban():
    def __init__(self,ban_dict):
        self.champion=league_objects.champion(ban_dict["championId"])
        self.pickTurn=ban_dict["pickTurn"]

    def __str__(self):
        return str(self.champion)


