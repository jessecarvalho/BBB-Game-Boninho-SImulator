# Imports de classes externas
from classes import Cast
from actions import Prove
from classes import Elimination
from time import sleep

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
            if(decision == 1):
                # Chama a função que cria o elenco
                self.cast = self.createcast(True)
                break
            elif(decision == 2):
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
            if(decision == 1):
                # Recria o elenco caso usuario deseje
                self.createcast(True)
            elif(decision == 2):
                # Chama-se a função para exibir os participantes
                self.showcast()
            elif(decision == 3):
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
            # cria a instância da prova do lider do modelo provas
            self.leaderProve = Prove(self.cast)
            print("________________________________________________________")
            # executa a prova do lider armazenando o lider
            self.leader = self.leaderProve.leader()
            # cria a instância da prova do anjo do modelo provas
            self.angelProve = Prove(self.cast)
            # executa a prova do anjo armazenando o anjo
            self.angel = self.angelProve.angel()
            # Cria a instância de eliminações
            self.elimination = Elimination(self.cast, self.leader, self.angel)
            # Esse método irá trazer o imunizado
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
            print(f'Vamos montar o paredão dessa semana!')
            print("----------------------------------------------------------")
            print('...')
            sleep(3)
            print(f"O anjo imunizou {self.immunezed}")
            sleep(1)
            print(f"O voto do lider foi em: {self.leaderVote}")
            sleep(1)
            print(f"O grupo no confessionario votou em: {self.othersVote}")
            sleep(1)
            print(f"O terceiro a ir ao paredão é: {self.thirdVote}")
            sleep(1)
            # Método para eliminação
            print(f"Momento de tensão no sofá")
            sleep(1)
            print(f"Batimentos cardiacos: {self.leaderVote}: 120, {self.othersVote}: 95, {self.thirdVote}: 111")
            sleep(2)
            self.elimination.toeliminate()
            sleep(2)
            print("O tempo continua e vamos para mais uma semana")
            sleep(1)
            print("...")
            sleep(3)

if __name__ == '__main__':
    game = Game()
    game.main()
