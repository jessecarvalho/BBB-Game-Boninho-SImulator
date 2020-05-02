from classes import Cast
from actions import Prove

class Game():
    def __init__(self):
        self.Cast = Cast()

    def start(self):
        while True:
            print("-- Escolha uma opção --")
            print("-- 1 -> Gerar elenco --")
            decision = int(input("> "))
            if(decision == 1):
                self.createCast()
                break
            else:
                print("Digito invalido")
        while True:
            print("-- Elenco criado com sucesso! --")
            print("-- 1 -> Gerar outro elenco --")
            print("-- 2 -> Ver elenco --")
            print("-- 3 -> Avançar --")
            decision = int(input("> "))
            if(decision == 1):
                self.createCast()
            elif(decision == 2):
                self.showCast()
            elif(decision == 3):
                break
            else:
                print("Digito invalido")

    def createCast(self):
        self.Cast.castGenerador()

    def showCast(self):
        self.Cast.show()

    def main(self):
        self.start()
        game.prove()

    def prove(self):
        leaderProve = Prove.prove(self.Cast.castList)
        prove = leaderProve.proveChoose("Sorte")
        leaderProve.setParticipants(prove)
        leaderProve.event()




if __name__ == '__main__':
    game = Game()
    game.main()
