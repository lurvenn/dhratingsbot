class Run:
    def __init__(self, runner, time):
        self.runner = runner


        ## terrible but cba to rewrite until i know what format the src api uses
        minutelist = time.split(":")
        minute = minutelist[0]

        secondlist = minutelist[1].split(".")
        second = secondlist[0]

        if len(secondlist) != 2:
            mss = 0
        else:
            mss = secondlist[1]

        self.time = int(mss)+int(second)*1000+int(minute)*60*1000
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
