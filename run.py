class Run:
    def __init__(self, runner, time):
        self.runner = runner

        self.time = float(time)
        self.score = 0

    def __str__(self):
        return "runner: " + self.runner + ", time: " + str(self.time) + ", score: " + str(self.score)

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
