# from board import Board
from run import Run
import srcomapi, srcomapi.datatypes as dt


def main():
    api = srcomapi.SpeedrunCom()
    api.debug = 1

    # with open("kod any.txt", "r") as f:
    #     importlist = [x.split("\t") for x in f]

    # runlist = [(Run(x[0], x[1])) for x in importlist]

    # unit tests
    # runs
    # print("\n # test of runs, not part of a leaderboard")
    # print(importlist[0][1])
    # for x in runlist:
    #     print(x)
    #
    # # boards
    # print("\n # test of boards")
    #
    # leaderboard = Board()
    # for x in runlist:
    #     leaderboard.addRun(x)
    #
    # print(leaderboard)

    # srcom api test
    # doesnt fucking work

    # gameid = "3dxz351y"


    ## Split up the categories
    game = api.search(srcomapi.datatypes.Game, {"name": "dishonored"})[0]
    dh1_runs = {}

    for p in game.categories:
        dh1_runs[p.name] = api.get(
            f"leaderboards/{game.id}/"
            f"category/{p.id}?embed=variables,players,platform"
        )
    
    players = {}
    ## Kod handling
    for p2 in dh1_runs.keys():
        for p in dh1_runs[p2]["players"]["data"]:
            if p["rel"] != "guest":
                players[p["id"]] = p 
   
        kod = dh1_runs["Knife of Dunwall"]

    kod_variables = kod["variables"]["data"]

    assert len(kod_variables) == 1
    kod_category = kod_variables[0]

    kod_category_values =  {'5q8jr6yl': 'Any%', 'mlnpkwo1': 'All Collectibles', '810g9gol': 'Non-Lethal / Ghost', '9qjvev7q': '100%'}
    kod_categories = {p : [] for p in kod_category_values.keys() }
    
    for run in kod["runs"]:
        run = run["run"]

        category_value = run["values"][kod_category["id"]]
        label = kod_category["values"]["values"][category_value]["label"]

        runner_id = run["players"][0]["id"]
        runner_name = players[runner_id]["names"]["international"]

        time = run["times"]["primary_t"]
        # TODO: Also handle guests?
        print(f"{label}: {runner_name}, {time}")

    # print(kod.runs[1][comment])
    # print(game.categories[1].runs)

    # print("lmao " + str(game.categories[1]))
    # print(" category test: " + str(game.categories[1].kod_variables))
    # list = []
    # for x in game.runs:
    #     if x.categories.get("Knife of Dunwall"):
    #         list.append(x)
    # print(x)
    #
    # print("asdf" + str(list))
    # gameid = "3dxz351y"
    # dh_runs = {}
    #
    # print(dh_runs)


if __name__ == "__main__":
    main()
