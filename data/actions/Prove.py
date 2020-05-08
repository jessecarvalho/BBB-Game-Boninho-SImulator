from random import randint
from time import sleep


class Prove:
    def __init__(self, participants):
        self.cont = 0
        self.participants = []
        for i in participants:
            self.participants.append(i)

    def proveChoose(self, choose):
        self.prove = choose
        return self.prove

    def setParticipants(self, prove):
        self.prove = prove
        self.privileged = []
        for i in self.participants:
            if i.hability == self.prove:
                self.privileged.append(i.name)
                i.life = 2
            elif i.hability != self.prove:
                i.life = 1

    def event(self):
        print(f"A prova será de {self.prove}")
        print(f'Os privilegiados pela escolha de prova serão: {self.privileged}')
        while len(self.participants) > 1:
            random = randint(0, len(self.participants)-1)
            self.participants[random].life -= 1
            if self.participants[random].life == 0:
                self.cont += 1
                print(f'O {self.cont}º eliminado da rodada é: {self.participants[random].name}')
                sleep(0)
                self.participants.remove(self.participants[random])
        winner = self.participants[0]
        print(f'O vencedor é {winner.name}')
        return winner

    def actProve(self, proveType):
        print(f'-- Escolha a prova do {proveType} dessa semana: --')
        print('-- 1 - Arremesso de Dardos --')
        print('-- 2 - Arremesso de bolas --')
        print('-- 3 - Velocidade --')
        print('-- 4 - Resistência --')
        print('-- 5 - Corrida --')
        print('-- 6 - Sorte --')
        decision = int(input("> "))
        if decision == 1:
            return "Arremesso de Dardos"
        elif decision == 2:
            return "Arremesso de bolas"
        elif decision == 3:
            return "Velocidade"
        elif decision == 4:
            return "Resistência"
        elif decision == 5:
            return "Corrida"
        elif decision == 6:
            return "Sorte"
        else:
            print('Digito inválido')
            self.actProve(proveType)

    def leader(self):
        self.proveChoose("leader")
        self.setParticipants(self.actProve("leader"))
        leader = self.event()
        print(f'O lider da semana será: {leader.name}')
        return leader
