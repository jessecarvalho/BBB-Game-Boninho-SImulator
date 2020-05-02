from random import randint
from .Profile import Person

class Cast:
    def __init__(self):
        self.numParticipant = randint(16, 22)
        self.life = 0;
    def castGenerador(self):
        i = 0
        self.castList = []
        while i < self.numParticipant:
            self.Pessoa = Person()
            self.Pessoa.personGenerator()
            self.castList.append(self.Pessoa)
            i += 1
    def show(self):
        self.count = 1
        for i in self.castList:
            print(f'{self.count}º participante')
            print(f'Nome: {i.name}')
            print(f'Genero: {i.gender}')
            print(f'Traços de personalidade: {i.personalityTraces}')
            print(f'Profissiões: {i.profession}')
            print(f'Habilidades: {i.hability}')
            print(f'Emoji: {i.emoji}')
            print(f'Seguidores: {i.followers}')
            print(f'Favoritismo: {i.favoritism}')
            print('-----------------------------')
            self.count += 1





if __name__ == '__main__':
    cast = Cast()
    cast.castGenerador()