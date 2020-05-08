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
                self.cast = self.createcast()
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
                self.createcast()
            elif(decision == 2):
                self.showcast()
            elif(decision == 3):
                break
            else:
                print("Digito invalido")

    def createcast(self):
        cast = self.Cast.castGenerador()
        return cast

    def showcast(self):
        self.Cast.show()

    def toeliminate(self, leaderVote, othersVote, thirdPerson, cast):
        decision = input("> ")
        print(decision)

        if decision == leaderVote.name or decision == othersVote.name or decision == thirdPerson.name:
            for i in self.cast:
                if i.name == decision:
                    self.cast.remove(i)
        else:
            print("digite um valor válido!")
            self.toeliminate(leaderVote, othersVote, thirdPerson, cast)

    def main(self):
        self.start()
        while len(self.cast) > 3:
            print(len(self.cast))
            self.prove = Prove(self.cast)
            self.leader = self.prove.leader()
            self.elimination = Elimination(self.cast, self.leader)
            leaderVote = self.elimination.leadervote()
            othersVote = self.elimination.othersvote(leaderVote)
            thirdPerson = self.elimination.thirdperson(leaderVote, othersVote)
            print(f"O voto do lider foi em: {leaderVote.name}")
            print(f"O grupo no confessionario votou em: {othersVote.name}")
            print(f"O terceiro a ir ao paredão é: {thirdPerson.name}")
            self.toeliminate(leaderVote, othersVote, thirdPerson, self.cast)




if __name__ == '__main__':
    game = Game()
    game.main()
