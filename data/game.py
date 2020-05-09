# Imports de classes externas
from classes import Cast
from actions import Prove
from classes import Elimination

# Criação da classe principal do jogo
class Game():
    # Inicializa o objeto
    def __init__(self):
        # Instância a classe Cast para criação do elenco
        self.Cast = Cast()

    # Inicializa o game com um inicio padronizado
    def start(self):
        # Menu de navegação do player
        while True:
            print("-- Escolha uma opção --")
            print("-- 1 -> Gerar elenco --")
            decision = int(input("> "))
            if(decision == 1):
                # Chama a função que cria o elenco
                self.cast = self.createcast()
                break
            else:
                print("Digito invalido")
        while True:
            # Menu de navegação do player
            print("-- Elenco criado com sucesso! --")
            print("-- 1 -> Gerar outro elenco --")
            print("-- 2 -> Ver elenco --")
            print("-- 3 -> Avançar para primeira prova do lider --")
            decision = int(input("> "))
            if(decision == 1):
                # Recria o elenco caso usuario deseje
                self.createcast()
            elif(decision == 2):
                # Chama-se a função para exibir os participantes
                self.showcast()
            elif(decision == 3):
                break
            else:
                print("Digito invalido")

    def createcast(self):
        # Cria-se o elenco
        cast = self.Cast.castGenerador()
        return cast

    def showcast(self):
        # Exibe os participantes um a um ao player
        self.Cast.show()

    # Núcleo principal do jogo
    def main(self):
        # Chama a função start que traz o roteiro inicial
        self.start()
        # Roteiro do jogo até a grande final
        while len(self.cast) > 3:
            print(len(self.cast))
            # cria a instância da prova do lider do modelo provas
            self.leaderProve = Prove(self.cast)
            # executa a prova do lider armazenando o lider
            self.leader = self.leaderProve.leader()
            # cria a instância da prova do anjo do modelo provas
            self.angelProve = Prove(self.cast)
            # executa a prova do anjo armazenando o anjo
            self.angel = self.angelProve.angel()
            # Cria a instância de eliminações
            self.elimination = Elimination(self.cast, self.leader, self.angel)
            # A seguir executa-se métodos que iram gerar os votos e emparedados
            leaderVote = self.elimination.leadervote()
            othersVote = self.elimination.othersvote()
            thirdPerson = self.elimination.thirdperson()
            # Esse método irá trazer o imunizado
            immunezed = self.elimination.immunezed()
            # Exibição ao player dos emparedados e imunizado
            print(f"O anjo imunizou {immunezed}")
            print(f"O voto do lider foi em: {leaderVote}")
            print(f"O grupo no confessionario votou em: {othersVote}")
            print(f"O terceiro a ir ao paredão é: {thirdPerson}")
            # Método para eliminação
            self.elimination.toeliminate()




if __name__ == '__main__':
    game = Game()
    game.main()
