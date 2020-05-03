from random import randint
from time import sleep

class prove:
    def __init__(self, participants):
        self.participants = participants

    def proveChoose(self, choose):
        self.prove = choose
        return self.prove

    def setParticipants(self, prove):
        for i in self.participants:
            if i.hability == prove:
                i.life = 2
            elif i.hability != prove:
                i.life = 1

    def event(self):
        while len(self.participants) > 1:
            random = randint(0, len(self.participants)-1)
            self.participants[random].life -= 1
            if self.participants[random].life == 0:
                print(f'O eliminado da rodada é: {self.participants[random].name}')
                sleep(1)
                self.participants.remove(self.participants[random])
        winner = self.participants[0]
        print(f'O vencedor é {winner.name}')
        return winner

