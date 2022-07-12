from run import Run
import srcomapi, srcomapi.datatypes as dt
from board import Board

def main():
    api = srcomapi.SpeedrunCom()
    api.debug = 1

    # gameid = "3dxz351y"


    ## Split up the categories
    game = api.search(srcomapi.datatypes.Game, {"name": "dishonored"})[0]
    dh1_runs = {}

    for p in game.categories:
        dh1_runs[p.name] = api.get(
            f"leaderboards/{game.id}/"
            f"category/{p.id}?embed=variables,players,platform"
        )

    # get all player names for dh1 into a dict [id]:name
    players = {}
    for p2 in dh1_runs.keys():
        for p in dh1_runs[p2]["players"]["data"]:
            if p["rel"] == "user":
                players[p["id"]] = p 

    # category ids
    # dish = '5dw6mp02'
    # kod = 'wk6exjp2'
    # bw = 'n2y9p11d'

    category_names = {
        'wk6exjp2' : {'5q8jr6yl': 'Any%', 'mlnpkwo1': 'All Collectibles', '810g9gol': 'Non-Lethal / Ghost', '9qjvev7q': '100%'},
        '5dw6mp02' : {'21gvo861': 'Any%', 'jqz8yp2q': 'All Collectibles', 'klrv6poq': 'Non-Lethal / Ghost', '21d9ozpq': '100%', '4qyd8p6q': 'Legacy'},
        'n2y9p11d' : {'jq6ngnvl': 'Any%', '5lmvwv8l': 'All Collectibles', '81wzrzm1': 'Non-Lethal / Ghost', 'zqok2k5l': '100%'},
    }   
    kod_category_names =  {'5q8jr6yl': 'Any%', 'mlnpkwo1': 'All Collectibles', '810g9gol': 'Non-Lethal / Ghost', '9qjvev7q': '100%'}
    dish_category_names = {'21gvo861': 'Any%', 'jqz8yp2q': 'All Collectibles', 'klrv6poq': 'Non-Lethal / Ghost', '21d9ozpq': '100%', '4qyd8p6q': 'Legacy'}
    bw_category_names = {'jq6ngnvl': 'Any%', '5lmvwv8l': 'All Collectibles', '81wzrzm1': 'Non-Lethal / Ghost', 'zqok2k5l': '100%'}
    
    # Kod handling

    kod_dict = {}
    # for category in list(category_names.keys()):
    #     for subcategory in list(kod_category_names.keys()):
    #         fullsubcat = api.get(f"leaderboards/3dxz351y/category/wk6exjp2?var-2lg3r5en={subcategory}&embed=players")
    #         kod_dict[f"{subcategory}"] = fullsubcat["runs"]


    for subcategory in list(kod_category_names.keys()):
        fullsubcat = api.get(f"leaderboards/3dxz351y/category/wk6exjp2?var-2lg3r5en={subcategory}&embed=players")
        kod_dict[f"{subcategory}"] = fullsubcat["runs"]
   
    dish_dict = {}
    for subcategory in list(dish_category_names.keys()):
        fullsubcat = api.get(f"leaderboards/3dxz351y/category/5dw6mp02?var-789x6138={subcategory}&embed=players")
        dish_dict[f"{subcategory}"] = fullsubcat["runs"]
    
    bw_dict = {}
    for subcategory in list(bw_category_names.keys()):
        fullsubcat = api.get(f"leaderboards/3dxz351y/category/n2y9p11d?var-wl3109v8={subcategory}&embed=players")
        bw_dict[f"{subcategory}"] = fullsubcat["runs"]
 
  
    kodAnyBoard = Board(2)
    kodACBoard = Board(2)
    kodNLGBoard = Board(2)
    kodHundoBoard = Board(2)

    for p in kod_dict["5q8jr6yl"]:
        playername = players[p["run"]["players"][0]["id"]]
        kodAnyBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))
    
    for p in kod_dict["mlnpkwo1"]:
        playername = players[p["run"]["players"][0]["id"]]
        kodACBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    for p in kod_dict["810g9gol"]:
        playername = players[p["run"]["players"][0]["id"]]
        kodNLGBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    for p in kod_dict["9qjvev7q"]:
        playername = players[p["run"]["players"][0]["id"]]
        kodHundoBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    # dishonored cat

    dishAnyBoard = Board(2)
    dishACBoard = Board(2)
    dishNLGBoard = Board(2)
    dishHundoBoard = Board(2)
    dishLegacyBoard = Board(2)

    

    for p in dish_dict["21gvo861"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            dishAnyBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    for p in dish_dict["jqz8yp2q"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            dishACBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))
        
    for p in dish_dict["klrv6poq"]:
        if p["run"]["players"][0]["rel"] == "user":

            playername = players[p["run"]["players"][0]["id"]]
            dishNLGBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    for p in dish_dict["21d9ozpq"]:
        if p["run"]["players"][0]["rel"] == "user":

            playername = players[p["run"]["players"][0]["id"]]
            dishHundoBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))
    
    for p in dish_dict["4qyd8p6q"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            dishLegacyBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    # bw
    
    bwAnyBoard = Board(2)
    bwACBoard = Board(2)
    bwNLGBoard = Board(2)
    bwHundoBoard = Board(2)

    bw_category_names = {'jq6ngnvl': 'Any%', '5lmvwv8l': 'All Collectibles', '81wzrzm1': 'Non-Lethal / Ghost', 'zqok2k5l': '100%'}
    
    for p in bw_dict["jq6ngnvl"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            bwAnyBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))
    
    for p in bw_dict["5lmvwv8l"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            bwACBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))

    for p in bw_dict["81wzrzm1"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            bwNLGBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))    

    for p in bw_dict["zqok2k5l"]:
        if p["run"]["players"][0]["rel"] == "user":
            playername = players[p["run"]["players"][0]["id"]]
            bwHundoBoard.addRun(Run(playername["names"]["international"], p["run"]["times"]["primary_t"]))
    
    game_dict = {}
    tempdict = {}
    for player in list(players.values()):
        score = 0
        
        for run in kodAnyBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in kodACBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in kodNLGBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in kodHundoBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()

        for run in dishAnyBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in dishACBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in dishNLGBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in dishHundoBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in dishLegacyBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        
        for run in bwAnyBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in bwACBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in bwNLGBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()
        for run in bwHundoBoard.getRuns():
            if player["names"]["international"] == run.getRunner():
                score += run.getScore()

        if score > 0 :
            tempdict[player["names"]["international"]] = score
            game_dict = dict(sorted(tempdict.items(), key=lambda x:x[1], reverse = True))

    print("Kod Scores succcaaas: \n")
    for i in range(len(list(game_dict.values()))):
        print(f"{i+1}   {list(game_dict.keys())[i]} {list(game_dict.values())[i]}")


if __name__ == "__main__":
    main()
