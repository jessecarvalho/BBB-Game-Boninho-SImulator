from random import randint
from .Profile import Person
from time import sleep

# Classe Cast deverá criar e gerenciar o elenco
class Cast:
    # Método de inicialização da classe
    def __init__(self):
        # Número de participantes gerados aleatóriamente sendo no minimo 16
        # e no máximo 22
        self.numParticipant = randint(16, 22)
        # "vida" de cada participante setado incialmente em 0
        self.life = 0;
    # Método para criação do elenco
    def castGenerador(self):
        # Contador setado em 0
        i = 0
        # Lista vazia criada para armazenar o elenco
        self.castList = []
        # Gere o elenco e adiciona na lista
        while i < self.numParticipant:
            # Instância a classe Person
            self.Pessoa = Person()
            # Gera uma pessoa a partir da classe instanciada
            self.Pessoa.personGenerator()
            # Adiciona na lista
            self.castList.append(self.Pessoa)
            # Contador incrementado
            i += 1
        # Após fim de while retornar o elenco
        return self.castList
    # Método para exibir o elenco
    def show(self):
        # Contador setado em 1
        self.count = 1
        # Exibe ao player todas as infos sobre cada participante
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
            print("Pressione ENTER para passar para o próximo")
            input("> ")