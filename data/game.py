from classes import Cast
from actions import Prove
from classes import Elimination

class Game():
    def __init__(self):
        self.Cast = Cast()

    def start(self):
        while True:
            print("-- Escolha uma opção --")
            print("-- 1 -> Gerar elenco --")
            decision = int(input("> "))
            if(decision == 1):
                self.cast = self.createCast()
                break
            else:
                print("Digito invalido")
        while True:
            print("-- Elenco criado com sucesso! --")
            print("-- 1 -> Gerar outro elenco --")
            print("-- 2 -> Ver elenco --")
            print("-- 3 -> Avançar para primeira prova do lider --")
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
        cast = self.Cast.castGenerador()
        return cast

    def showCast(self):
        self.Cast.show()


    def main(self):
        self.start()
        self.prove = Prove(self.cast)
        self.leader = self.prove.leader()
        self.elimination = Elimination(self.cast, self.leader)
        leaderVote = self.elimination.leadervote()
        print(leaderVote.name)


if __name__ == '__main__':
    game = Game()
    game.main()
