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

    kod_categories = {p : [] for p in kod_category_names.keys() }
    
    kod_dict = {}

    for subcategory in list(kod_category_names.keys()):
        fullsubcat = api.get(f"leaderboards/3dxz351y/category/wk6exjp2?var-2lg3r5en={subcategory}&embed=players,platform")
        kod_dict[f"{subcategory}"] = fullsubcat["runs"]["run"]
    
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
    
    kodAnyBoard = Board(2)

    for p in kod_dict["810g9gol"]:
        playername = players[p["players"][0]["id"]]
        kodAnyBoard.addRun(Run(playername["names"]["international"], p["times"]["primary_t"]))
    
    print(kodAnyBoard)

if __name__ == "__main__":
    main()
