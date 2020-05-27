from random import randint
from time import sleep

class Elimination:
    def __init__(self, cast, leader, angel):
        self.cast = cast
        self.leader = leader
        self.angel = angel
        self.immune = "innative"

    # Método para gerar o jogador imunizado
    def immunezed(self):
        # Gera o id aleatóriamente baseado no tamanho do elenco
        id = randint(0, len(self.cast) - 1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[id] == self.leader or self.cast[id] == self.angel:
            # Caso seja detectado o erro chamar novamente o método
            id = randint(0, len(self.cast) - 1)
            return False
        else:
            # Atribui o participante imunizado na variável
            self.immune = self.cast[id]
            # Retorna o nome do imunizado
            return self.immune

    # Método para gerar o voto do líder
    def leadervote(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast) - 1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[idVote] == self.leader or self.cast[idVote] == self.immune:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast) - 1)
            return False
        else:
            # Atribui o voto do lider na variável
            self.leaderVote = self.cast[idVote]
            # Retorna o nome do indicado pelo líder
            return self.leaderVote
    # Método para gerar o voto popular
    def othersvote(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast)-1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[idVote] == self.leader or self.cast[idVote] == self.leaderVote or self.cast[idVote] == self.immune:
            # Caso seja detectado o erro chamar novamente o método
            return False
        else:
            # Atribui o jogador mais votado na variável
            self.othersVote = self.cast[idVote]
            # Retorna o nome do mais votado
            return self.othersVote

    def thirdperson(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast)-1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[idVote] == self.leaderVote or self.cast[idVote] == self.othersVote or self.cast[idVote] == self.leader or \
                self.cast[idVote] == self.immune:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast)-1)
            return False
        else:
            # Atribui o terceiro emparedado na variável
            self.thirdVote = self.cast[idVote]
            # Retorna o nome do terceiro emparedado
            return self.thirdVote

    def intervention(self, greatWall):
        sleep(1)
        print("Neste momento, você irá intervir a favor de um participante.")
        sleep(3)
        print("Escolha o participante que você deseja intervir pelo número que ele representa")
        sleep(3)
        cont = 0
        for i in greatWall:
            cont += 1
            print(f"{cont} para apoiar {i.name}")
        self.vote = input("> ")
        print(self.vote)
        if 0 < int(self.vote) <= 3:
            self.vote = greatWall[int(self.vote)-1]
            print(self.vote.name)
        else:
            print("Você deve digitar um valor de 1 a 3")
            sleep(3)
            self.intervention(greatWall)

    def toeliminate(self):
        if self.leaderVote == self.vote:
            self.leaderVote.support += 10
        if self.othersVote == self.vote:
            self.othersVote.support += 10
        if self.thirdVote == self.vote:
            self.thirdVote.support += 10
        if self.leaderVote.support < self.othersVote.support and self.leaderVote.support < self.thirdVote.support:
            self.eliminated = self.leaderVote
        elif self.leaderVote.support < self.othersVote.support < self.thirdVote.support:
            self.eliminated = self.othersVote
        else:
            self.eliminated = self.thirdVote
        print(f"Após um longo discurso o eliminado da semana é revelado, pode vir {self.eliminated.name}")
        if self.leaderVote == self.vote:
            self.leaderVote.support -= 10
        if self.othersVote == self.vote:
            self.othersVote.support -= 10
        if self.thirdVote == self.vote:
            self.thirdVote.support -= 10
        for i in self.cast:
            if i == self.eliminated:
                self.cast.remove(i)

