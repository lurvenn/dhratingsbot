from run import Run

## want this to contain the runs from different categories, might be a bit hard codey
class Board:
    def __init__(self):
        self.runs = []

    def addRun(self, run):
        self.runs.append(run)
        self.calculatescore()

    def __str__(self):
        output = ""
        for x in self.runs:
            output+= str(x) + "\n"
        return output

    def calculatescore(self):
        self.runs.sort()
        comp= Run("mathtest","99:99.999")
        for x in self.runs:
            if x.getTime() < comp.getTime():
                comp = x
                x.setScore(100000)
            else:
                x.setScore(100000*(float(comp.getTime() / x.getTime())))
