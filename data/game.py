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
        self.Cast.castGenerador()

    def actProve(self, proveType):
        newProve = Prove.prove(self.Cast.castList)
        print(f'-- Escolha a prova do {proveType} dessa semana: --')
        print('-- 1 - Arremesso de Dardos --')
        print('-- 2 - Arremesso de bolas --')
        print('-- 3 - Velocidade --')
        print('-- 4 - Resistência --')
        print('-- 5 - Corrida --')
        print('-- 6 - Sorte --')
        decision = int(input("> "))
        if decision == 1:
            prove = newProve.proveChoose("Arremesso de Dardos")
        elif decision == 2:
            prove = newProve.proveChoose("Arremesso de bolas")
        elif decision == 3:
            prove = newProve.proveChoose("Velocidade")
        elif decision == 4:
            prove = newProve.proveChoose("Resistência")
        elif decision == 5:
            prove = newProve.proveChoose("Corrida")
        elif decision == 6:
            prove = newProve.proveChoose("Sorte")
        else:
            print('Digito inválido')
            self.actProve(proveType)
        newProve.setParticipants(prove)
        return newProve.event().name


    def showCast(self):
        self.Cast.show()

    def main(self):
        self.start()
        leader = game.actProve("lider")
        print(f'O lider da semana será: {leader}')
        angel = game.actProve("anjo")
        print(f'O anjo da semana será: {angel}')


if __name__ == '__main__':
    game = Game()
    game.main()
