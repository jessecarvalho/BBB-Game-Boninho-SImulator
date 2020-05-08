from random import randint

class Elimination:
    def __init__(self, cast, leader, angel=None):
        self.cast = cast
        self.leader = leader

    def leadervote(self):
        idVote = randint(0, len(self.cast)-1)
        if self.cast[idVote] == self.leader:
            self.leadervote()
        else:
            self.leadervote = self.cast[idVote]
            return self.leadervote

    def othersvote(self, leaderVote):
        idVote = randint(0, len(self.cast)-1)
        if self.cast[idVote] == self.leader or self.cast[idVote] == leaderVote:
            self.othersvote(leaderVote)
        else:
            self.othersVote = self.cast[idVote]
            return self.othersVote

    def thirdperson(self, leaderVote, othersVote):
        idVote = randint(0, len(self.cast)-1)
        if self.cast[idVote] == leaderVote or self.cast[idVote] == othersVote or self.cast[idVote] == self.leader:
            self.thirdperson(leaderVote, othersVote)
        else:
            self.thirdVote = self.cast[idVote]
            return self.thirdVote
