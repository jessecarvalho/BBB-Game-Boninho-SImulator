# Imports de classes externas
from classes import Cast
from classes import Elimination
from classes import Events
from classes import Final
from actions import Prove
from time import sleep
from random import randint


# Criação da classe principal do jogo
class Game():
    # Inicializa o objeto
    def __init__(self):
        # Instância a classe Cast para criação do elenco
        self.Cast = Cast()
        self.leaderVote = False
        self.othersVote = False
        self.thirdVote = False
        self.immunezed = False

    # Inicializa o game com um inicio padronizado
    def start(self):
        # Menu de navegação do player
        while True:
            print("-- Escolha uma opção --")
            print("-- 1 -> Gerar elenco aleatóriamente --")
            print("-- 2 -> Escolher participantes --")
            decision = int(input("> "))
            if (decision == 1):
                # Chama a função que cria o elenco
                self.cast = self.createcast(True)
                break
            elif (decision == 2):
                self.cast = self.createcast(False)
                break
            else:
                print("Digito invalido")
        while True:
            # Menu de navegação do player
            print("-- Elenco criado com sucesso! --")
            print("-- Escolha uma opção --")
            print("-- 1 -> Gerar outro elenco aleatóriamente --")
            print("-- 2 -> Ver elenco --")
            print("-- 3 -> Avançar para primeira prova do lider --")
            decision = int(input("> "))
            if (decision == 1):
                # Recria o elenco caso usuario deseje
                self.createcast(True)
            elif (decision == 2):
                # Chama-se a função para exibir os participantes
                self.showcast()
            elif (decision == 3):
                break
            else:
                print("Digito invalido")

    def createcast(self, random):
        # Cria-se o elenco
        if random == True:
            cast = self.Cast.castGenerator()
        else:
            cast = self.Cast.newCastGenerator()
        return cast

    def showcast(self):
        # Exibe os participantes um a um ao player
        self.Cast.show()

    # Núcleo principal do jogo
    def main(self):
        # Chama a função start que traz o roteiro inicial
        self.start()
        print("           Bem vindo, vamos começar o jogo!          ")
        # Roteiro do jogo até a grande final
        while len(self.cast) > 3:
            self.immunezed = False
            self.leaderVote = False
            self.othersVote = False
            self.thirdVote = False
            # cria a instância da prova do lider do modelo provas
            self.leaderProve = Prove(self.cast)
            print("________________________________________________________")
            # executa a prova do lider armazenando o lider
            self.leader = self.leaderProve.leader()
            # cria a instância da prova do anjo do modelo provas
            sleep(3)
            self.angelProve = Prove(self.cast)
            # executa a prova do anjo armazenando o anjo
            self.angel = self.angelProve.angel()
            # Cria a instância de eliminações
            self.elimination = Elimination(self.cast, self.leader, self.angel)
            # Esse método irá trazer o imunizado
            if len(self.cast) > 4:
                while self.immunezed == False:
                    self.immunezed = self.elimination.immunezed()
            # A seguir executa-se métodos que iram gerar os votos e emparedados
            while self.leaderVote == False:
                self.leaderVote = self.elimination.leadervote()
            while self.othersVote == False:
                self.othersVote = self.elimination.othersvote()
            while self.thirdVote == False:
                self.thirdVote = self.elimination.thirdperson()
            # Exibição ao player dos emparedados e imunizado
            print("----------------------------------------------------------")
            print(f'Vamos montar o paredão dessa semana!')
            print("----------------------------------------------------------")
            sleep(3)
            print(f"O anjo imunizou {self.immunezed.name}") if self.immunezed is not False else ""
            sleep(1)
            print(f"O voto do lider foi em: {self.leaderVote.name}")
            sleep(1)
            print(f"O grupo no confessionario votou em: {self.othersVote.name}")
            sleep(1)
            print(f"O terceiro a ir ao paredão é: {self.thirdVote.name}")
            sleep(1)
            print("----------------------------------------------------------")
            # Intervenção divina?
            greatWall = [self.leaderVote, self.othersVote, self.thirdVote]
            self.elimination.intervention(greatWall)
            # Método para eliminação
            print(f"Momento de tensão no sofá")
            sleep(1)
            print(
                f"Batimentos cardiacos: {self.leaderVote.name}: {randint(80, 140)}, {self.othersVote.name}: {randint(80, 140)}, {self.thirdVote.name}: {randint(80, 140)}")
            sleep(2)
            self.elimination.toeliminate()
            sleep(2)
            print("O tempo continua e vamos para mais uma semana")
            sleep(1)
            print("...")
            print("Listamos para você os principais acontecimentos da semana: ")
            event = Events()
            event.eventsAct(self.cast)
            sleep(3)
        print("Na casa restam apenas mais 3.")
        print("Isso significa que chegamos na grande final!")
        finalists = []
        for i in self.cast:
            finalists.append(i)
        final = Final(self.cast)
        final.theFinal()
        print("Obrigado por jogar nosso joguinho")
        print("Desenvolvido por BlackHAts")


if __name__ == '__main__':
    game = Game()
    game.main()
