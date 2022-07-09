from run import Run

## want this to contain the runs from different categories, might be a bit hard codey
class Board:
    def __init__(self, bonusMultiplier):
        self.runs = []
        self.bonus = int(bonusMultiplier)


    def addRun(self, run):
        if len(self.runs) > 0:
            exists = False
            for r in self.runs:
                if r.getRunner() == run.getRunner():
                    exists = True
            if not exists:
                self.runs.append(run)

        else:
            self.runs.append(run)



    def __str__(self):
        self.calculateBaseScore()
        self.calculateBonus()

        output = "Board: \n"
        i = 0
        for x in self.runs:
            i+=1
            output+= str(i) +  " " +str(x) + "\n"
        return output

    # Bonus based on your relative time to rekky, 5k added if run is faster than than 1/bonus compared to rekky
    def calculateBonus(self):
        rekky = sorted(self.runs)[0]
        for x in self.runs:
            if x.getScore() >= rekky.getScore()/self.bonus:
                x.setTimeBonus(True)
                


    def calculateBaseScore(self):
        self.runs.sort()
        comp= Run("mathtest",9999999999999999)
        for x in self.runs:
            if x.getTime() < comp.getTime():
                comp = x
                x.setScore(105000)
            else:
                x.setScore(100000*(float(comp.getTime() / x.getTime())) + 5000)
