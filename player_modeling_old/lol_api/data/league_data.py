from time import sleep
from . import data
from riot_observer import RiotObserver

import os


CACHE_URL=os.path.dirname(__file__)+"//cache"

MAX_REQUESTS=20
MIX_SLEEP_TIME=60

w = RiotObserver('RGAPI-a6c17ecb-a127-43d5-9b92-6c19456439b7')

champions_data=data.read_json_file(CACHE_URL+"//champions_data.txt")

def get_account_id(account_name,platformId,cont_requests=0):
    try:
        result=w.get_summoner_by_name(account_name,platformId)
        return result["accountId"]
    except:
        cont_requests=cont_requests+1
        sleep(cont_requests*MIX_SLEEP_TIME)
        if(cont_requests<MAX_REQUESTS):
            return get_account_id(account_name,platformId,cont_requests)
        else:
            raise ValueError("max requests")

def get_match(match_id,platformId,cont_requests=0):
    try:
        result=w.get_match(match_id=match_id, region=platformId)
        return result
    except Exception as e:
        cont_requests = cont_requests + 1
        sleep(cont_requests * MIX_SLEEP_TIME)
        if (cont_requests < MAX_REQUESTS):
            return get_match(match_id, platformId, cont_requests)
        else:
            raise ValueError("max requests")

def get_matchs(account_id,platformId,cont_requests=0):
    try:
        result=w.get_recent_matchlist(account_id=account_id, region=platformId)
        return result["matches"]
    except:
        print("erro")
        cont_requests = cont_requests + 1
        sleep(cont_requests * MIX_SLEEP_TIME)
        if (cont_requests < MAX_REQUESTS):
            return get_matchs(account_id, platformId, cont_requests)
        else:
            raise ValueError("max requests")

def get_champion_data(champion_id,cache=True,region="kr",tags="all",cont_requests=0):
    if(cache):
        champion_data=champions_data["data"][str(champion_id)]
    else:
        try:
            champion_data=w.static_get_champion(champion_id,region,tags=tags)
        except:
            cont_requests=cont_requests+1
            sleep(cont_requests * MIX_SLEEP_TIME)
            if(cont_requests<MAX_REQUESTS):
                return get_champion_data(champion_id,cache,region,tags,cont_requests)
            else:
                raise ValueError("max requets")

    return champion_data

def get_all_champion_data(region,cont_requests=0):
    try:
        data=w.static_get_champion_list(region=region,tags="all",data_by_id=True)
        return data
    except:
        cont_requests=cont_requests+1
        sleep(cont_requests * MIX_SLEEP_TIME)
        if(cont_requests<MAX_REQUESTS):
            return get_all_champion_data(region,cont_requests)
        else:
            raise ValueError("max requests")


if __name__=="__main__":
    get_champion_data(10)
