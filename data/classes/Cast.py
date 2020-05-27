from random import randint
from .Profile import Person
from time import sleep

# Classe Cast deverá criar e gerenciar o elenco
class Cast:
    # Método de inicialização da classe
    def __init__(self):
        # "vida" de cada participante setado incialmente em 0
        self.life = 0
    # Método para criação do elenco


    def newShow(self, person):
        print(f'Nome: {person.name}')
        print(f'Genero: {person.gender}')
        print(f'Traços de personalidade: {person.personalityList}')
        print(f'Profissião: {person.profession}')
        print(f'Habilidades: {person.hability}')
        print(f'Emoji: {person.emoji}')
        print(f'Seguidores: {person.followers}')
        print(f'% de apoiadores: {person.support}')
        print('-----------------------------')

    def totalParticipants(self):
        print("Quantos participantes irão participar desta edição?")
        numParticipantes = int(input("> "))
        if 6 <= numParticipantes <= 22:
            print("Número de participantes cadastrado.")
            self.numParticipant = numParticipantes
        else:
            print("Por favor, o elenco terá de ter no minimo 6 e no máximo 22 participantes.")
            print("--------------------------------------------------------------------------")
            self.totalParticipants()

    def newCastGenerator(self):
        self.totalParticipants()
        i = 0
        self.castList = []
        while i < self.numParticipant:
            self.Pessoa = Person()
            self.Pessoa.personGenerator()
            self.newShow(self.Pessoa)
            print("Para aprovar o candidato digite 's' ")
            print("Para reprova-lo digite 'n'")
            decision = input("> ")
            if decision == "s" or decision =="S":
                print('-----------------------------')
                print("Candidato aprovado!")
                print('-----------------------------')
                self.castList.append(self.Pessoa)
                i += 1
                print(f"Faltam apenas {self.numParticipant - i} candidatos para fechar o elenco!")
            else:
                print('-----------------------------')
                print("Candidato Reprovado!")
                print('-----------------------------')
        return self.castList

    def castGenerator(self):
        self.totalParticipants()
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
            print(f'Traços de personalidade: {i.personalityList}')
            print(f'Profissião: {i.profession}')
            print(f'Habilidades: {i.hability}')
            print(f'Emoji: {i.emoji}')
            print(f'Seguidores: {i.followers}')
            print(f'% de apoiadores: {i.support}')
            print('-----------------------------')
            self.count += 1
            print("Pressione ENTER para passar para o próximo")
            input("> ")