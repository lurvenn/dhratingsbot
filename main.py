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
    
    print(kodAnyBoard)

if __name__ == "__main__":
    main()
