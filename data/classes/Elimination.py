from random import randint

class Elimination:
    def __init__(self, cast, leader, angel):
        self.cast = cast
        self.leader = leader
        self.angel = angel

    def immunezed(self):
        idImmu = randint(0, len(self.cast) - 1)
        while self.cast[idImmu] == self.leader or self.cast[idImmu] == self.angel:
            idImmu = randint(0, len(self.cast) - 1)
        else:
            self.immunezed = self.cast[idImmu]
            return self.immunezed.name

    def leadervote(self):
        idVote = randint(0, len(self.cast) - 1)
        while self.cast[idVote] == self.leader or self.cast[idVote] == self.immunezed:
            idVote = randint(0, len(self.cast) - 1)
        else:
            self.leaderVote = self.cast[idVote]
            return self.leaderVote.name

    def othersvote(self):
        idVote = randint(0, len(self.cast)-1)
        while self.cast[idVote] == self.leader or self.cast[idVote] == self.leadervote or self.cast[idVote] == self.immunezed:
            idVote = randint(0, len(self.cast)-1)
        else:
            self.othersVote = self.cast[idVote]
            return self.othersVote.name

    def thirdperson(self):
        idVote = randint(0, len(self.cast)-1)
        while self.cast[idVote] == self.leadervote or self.cast[idVote] == self.othersVote or self.cast[idVote] == self.leader or \
                self.cast[idVote] == self.immunezed:
            idVote = randint(0, len(self.cast)-1)
        else:
            self.thirdVote = self.cast[idVote]
            return self.thirdVote.name

    def toeliminate(self):
        decision = input("> ")
        if decision == self.leaderVote.name or decision == self.othersVote.name or decision == self.thirdVote.name:
            for i in self.cast:
                if i.name == decision:
                    self.cast.remove(i)
        else:
            print("digite um valor válido!")
            self.toeliminate()
