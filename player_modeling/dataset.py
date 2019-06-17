import pandas as pd
from time import sleep
from lol_api.data.league_match import Match
from lol_api.data import league_data
from pre_process import pre_processe_ranked_dataset





def get_matchs_results(account_id,platformId):
    gamesResults=[]
    matches=league_data.get_matchs(account_id,platformId)
    cont=0
    for match in matches:
        cont=cont+1
        try:
            gameId=match["gameId"]
            gameResult=league_data.get_match(gameId,platformId)
            gamesResults.append(gameResult)
            print("Match:"+str(cont))
        except:
            print("entrou")
            sleep(300)
    return gamesResults

def criar_dataset(player_nick,player_plataformId,max_matchs=700):

    matchs_ids=[]
    matchs=[]
    players_ids=[]

    players_ids.append(league_data.get_account_id(player_nick,player_plataformId))

    for player_id in players_ids:
        if(len(matchs)<max_matchs):
            matchs_results = get_matchs_results(player_id, "kr")
            for match_result in matchs_results:
                match = Match(match_result)
                if(not match.gameId in matchs_ids and match.map.mapId==11):
                    matchs.append(match)
                    matchs_ids.append(match.gameId)
                    print("partida:" + str(len(matchs)))

                for team in match.teams:
                    for player in team.players:
                        if(not player.accountId in players_ids):
                            players_ids.append(player.accountId)
        else:
            break

    pandas_dataset=[]
    for match in matchs:
        try:
            pandas_match=match.to_pandas()
            pandas_dataset.append(pandas_match)
        except:
            pass

    dataset=pd.concat(pandas_dataset,ignore_index=True)

    return dataset


if __name__=="__main__":
    ranked_dataset=criar_dataset("hide on bush","kr","files//ranked_dataset")
    ranked_dataset.to_csv("files//ranked_dataset//test.csv")
