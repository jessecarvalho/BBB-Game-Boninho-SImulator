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
            return self.cast[idVote]

    def othersvote(self, leaderVote):
        idVote = randint(0, len(self.cast)-1)
        if self.cast[idVote] == self.leader or self.cast[idVote] == leaderVote:
            self.othersvote(leaderVote)
        else:
            return self.cast[idVote]
