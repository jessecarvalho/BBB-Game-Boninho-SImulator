from random import randint

class Elimination:
    def __init__(self, cast, leader, angel):
        self.cast = cast
        self.leader = leader
        self.angel = angel

    # Método para gerar o jogador imunizado
    def immunezed(self):
        # Gera o id aleatóriamente baseado no tamanho do elenco
        id = randint(0, len(self.cast) - 1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[id] == self.leader or self.cast[id] == self.angel:
            # Caso seja detectado o erro chamar novamente o método
            id = randint(0, len(self.cast) - 1)
            self.immunezed()
        else:
            # Atribui o participante imunizado na variável
            self.immune = self.cast[id]
            # Retorna o nome do imunizado
            return self.immune.name

    # Método para gerar o voto do líder
    def leadervote(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast) - 1)
        print(self.cast[idVote].name, self.leader.name, self.immune.name)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[idVote] == self.leader or self.cast[idVote] == self.immune:
            print('sa')
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast) - 1)
            self.leaderVote()
        else:
            # Atribui o voto do lider na variável
            self.leaderVote = self.cast[idVote]
            # Retorna o nome do indicado pelo líder
            return self.leaderVote.name
    # Método para gerar o voto popular
    def othersvote(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast)-1)
        # While para evitar possíveis erros de regra de negócio
        print(self.cast[idVote].name, self.leader.name, self.leaderVote.name, self.immune.name)
        if self.cast[idVote] == self.leader or self.cast[idVote] == self.leaderVote or self.cast[idVote] == self.immune:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast)-1)
            print('a')
            self.othersVote()
        else:
            # Atribui o jogador mais votado na variável
            self.othersVote = self.cast[idVote]
            # Retorna o nome do mais votado
            return self.othersVote.name

    def thirdperson(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast)-1)
        # While para evitar possíveis erros de regra de negócio
        if self.cast[idVote] == self.leaderVote or self.cast[idVote] == self.othersVote or self.cast[idVote] == self.leader or \
                self.cast[idVote] == self.immune:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast)-1)
            self.thirdperson()
        else:
            # Atribui o terceiro emparedado na variável
            self.thirdVote = self.cast[idVote]
            # Retorna o nome do terceiro emparedado
            return self.thirdVote.name

    def toeliminate(self):
        if self.leaderVote.support > self.othersVote.support and self.leaderVote.support > self.thirdVote.support:
            self.eliminated = self.leaderVote
        elif self.leaderVote.support < self.othersVote.support and self.othersVote.support > self.thirdVote.support:
            self.eliminated = self.othersVote
        else:
            self.eliminated = self.thirdVote
        for i in self.cast:
            if i == self.eliminated:
                print(i.name)
                self.cast.remove(i)

