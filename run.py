class Run:
    def __init__(self, runner, time):
        self.runner = runner

        self.time = float(time)
        self.score = 0
        self.timeBonus = False
    

    def __str__(self):
        bonus = 0
        if self.timeBonus == True: bonus = 5000
        return "runner: " + self.runner + ", time: " + str(self.time) + ", score: " + str(self.score + bonus)

    def __gt__(self, other):
        return self.time > other.getTime()

    def __eq__(self, other):
        return self.time == other.getTime()

    def getRunner(self):
        return self.runner

    def getTime(self):
        return self.time

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = int(score)

    def setTimeBonus(self, boolio):
        self.timeBonus = bool(boolio)

    def getTimeBonus(self):
        return self.timeBouns
