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


    kod_category_names =  {'5q8jr6yl': 'Any%', 'mlnpkwo1': 'All Collectibles', '810g9gol': 'Non-Lethal / Ghost', '9qjvev7q': '100%'}
    dish_category_names = {'21gvo861': 'Any%', 'jqz8yp2q': 'All Collectibles', 'klrv6poq': 'Non-Lethal / Ghost', '21d9ozpq': '100%', '4qyd8p6q': 'Legacy'}
    bw_category_names = {'jq6ngnvl': 'Any%', '5lmvwv8l': 'All Collectibles', '81wzrzm1': 'Non-Lethal / Ghost', 'zqok2k5l': '100%'}
    
    # Kod handling

    kod = dh1_runs["Knife of Dunwall"]
<<<<<<< HEAD

    kod_categories = {p : [] for p in kod_category_names.keys() }
    
    kod_dict = {}

    for subcategory in list(kod_category_names.keys()):
        fullsubcat = api.get(f"leaderboards/3dxz351y/category/wk6exjp2?var-2lg3r5en={subcategory}&embed=players,platform")
        kod_dict[f"{subcategory}"] = fullsubcat["runs"]
    
    # kod_category = kod_variables[0]
    # for run in kod["runs"]:
    #     run = run["run"]

    #     category_value = run["values"][kod_category["id"]]
    #     label = kod_category["values"]["values"][category_value]["label"]

    #     runner_id = run["players"][0]["id"]
    #     runner_name = players[runner_id]["names"]["international"]

    #     time = run["times"]["primary_t"]
    #     # TODO: Also handle guests?
    #     print(f"{label}: {runner_name}, {time}")

    # for run in kod["runs"]:
    #     run = run["run"]
    #     for x in kod["variables"]["data"]:
    #         if x["is-subcategory"] == True:
    #             for b in list(x["values"]["values"].keys()):
    #                 if list(run["values"].values())[0] == b:
    #                    kod_categories[b].append(run)
=======
    kod_categories = {p : [] for p in kod_category_names.keys() }
    
    # Category Sort: Appending of runs to each category list
    for r in kod["runs"]:
        run = r["run"]
        
        # Get run category string value
        run_category = list(run["values"].values())[0]
        # Get all category string values
        categories = list(kod["variables"]["data"][0]["values"]["values"].keys())
        
        # Append run to category list where category values match
        for category in categories:
            if run_category == category:
                kod_categories[category].append(run)
    # End of Category Sort -Luke / Xais
  
    kodAnyBoard = Board(2)
    for p in kod_categories["mlnpkwo1"]:    # Change this here to see the different categories (as per the kod categories string values...
        # "810g9gol" is empty and so is broken)
        playername = players[p["players"][0]["id"]]
        kodAnyBoard.addRun(Run(playername["names"]["international"], p["times"]["primary_t"]))
>>>>>>> b7e87c759c61461c78f68b0cc5425a975cbee43e
    
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

    kodtable = {}
    marklist = {}

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
        
        if score > 0 :
            kodtable[player["names"]["international"]] = score
            marklist = sorted(kodtable.items(), key=lambda x:x[1], reverse = True)
            sortdict = dict(marklist)

    print("Kod Scores succcaaas: \n")
    for i in range(len(list(sortdict.values()))):
        print(f"{i+1}   {list(sortdict.keys())[i]} {list(sortdict.values())[i]}")


if __name__ == "__main__":
    main()
