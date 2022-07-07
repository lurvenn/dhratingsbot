from board import Board
from run import Run
import srcomapi
api = srcomapi.SpeedrunCom(); api.debug = 1
f = open("kod any.txt", "r")

importlist = []

for x in f:
    importlist.append(x.split("\t"))

f.close()
runlist = []
for x in importlist:
    runlist.append(Run(x[0],x[1]))



# unit tests
# runs
print("\n # test of runs, not part of a leaderboard")
print(importlist[0][1])
for x in runlist:
    print(x)

# boards
print("\n # test of boards")

leaderboard = Board()
for x in runlist:
    leaderboard.addRun(x)

print(leaderboard)


# srcom api test
# doesnt fucking work

gameid = "3dxz351y"

game = api.search(srcomapi.datatypes.Game, {"name": "dishonored"})[0]

print(" category test: " + str(game.categories[1].variables))
list = []
for x in game.runs:
    if x.categories.get("Knife of Dunwall"):
        list.append(x)
print(x)

print("asdf" + str(list))
gameid = "3dxz351y"
dh_runs = {}

print(dh_runs)
