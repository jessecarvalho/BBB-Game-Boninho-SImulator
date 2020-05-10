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
        while self.cast[id] == self.leader or self.cast[id] == self.angel:
            # Caso seja detectado o erro chamar novamente o método
            id = randint(0, len(self.cast) - 1)
        else:
            # Atribui o participante imunizado na variável
            self.immunezed = self.cast[id]
            # Retorna o nome do imunizado
            return self.immunezed.name

    # Método para gerar o voto do líder
    def leadervote(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast) - 1)
        # While para evitar possíveis erros de regra de negócio
        while self.cast[idVote] == self.leader or self.cast[idVote] == self.immunezed:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast) - 1)
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
        while self.cast[idVote] == self.leader or self.cast[idVote] == self.leadervote or self.cast[idVote] == self.immunezed:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast)-1)
        else:
            # Atribui o jogador mais votado na variável
            self.othersVote = self.cast[idVote]
            # Retorna o nome do mais votado
            return self.othersVote.name

    def thirdperson(self):
        # Gera o id aleatóriamente
        idVote = randint(0, len(self.cast)-1)
        # While para evitar possíveis erros de regra de negócio
        while self.cast[idVote] == self.leadervote or self.cast[idVote] == self.othersVote or self.cast[idVote] == self.leader or \
                self.cast[idVote] == self.immunezed:
            # Caso seja detectado o erro chamar novamente o método
            idVote = randint(0, len(self.cast)-1)
        else:
            # Atribui o terceiro emparedado na variável
            self.thirdVote = self.cast[idVote]
            # Retorna o nome do terceiro emparedado
            return self.thirdVote.name

    def toeliminate(self):
        # Recebe do usuário a escolha de quem eliminar
        decision = input("> ")
        # Verificador para descobrir se o usuário digitou o nome correto de um emparedadp
        if decision == self.leaderVote.name or decision == self.othersVote.name or decision == self.thirdVote.name:
            # Remover o participante
            for i in self.cast:
                if i.name == decision:
                    self.cast.remove(i)
        else:
            # Para o caso do usuário digitar um valor inválido
            print("digite um valor válido!")
            self.toeliminate()
