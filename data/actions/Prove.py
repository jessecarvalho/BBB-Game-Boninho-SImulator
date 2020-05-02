from random import randint

class prove:
    def __init__(self, participants):
        self.participants = participants

    def proveChoose(self, choose):
        self.prove = choose
        return self.prove

    def setParticipants(self, prove):
        for i in self.participants:
            if i.hability == prove:
                i.life = 3
            elif i.hability != prove:
                i.life = 1
            print(i.life, i.name)

    def event(self):
        while len(self.participants) > 1:
            random = randint(0, len(self.participants)-1)
            self.participants[random].life = 0
            if self.participants[random].life == 0:
                self.participants.remove(self.participants[random])
        print(self.participants[0].name)

