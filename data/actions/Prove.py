# Imports necessários para rodar a aplicação
from random import randint
from time import sleep


class Prove:
    # Inicializador da classe
    def __init__(self, participants):
        # Contador setado em 0
        self.cont = 0
        # Lista de participantes criada inicialmente vazia
        self.participants = []
        # Adicionando participante a participante na lista vazia
        for i in participants:
            self.participants.append(i)


    # Definindo privilégios a partir de lista de hábilidades
    def setParticipants(self, prove):
        self.prove = prove
        self.privileged = []
        # Caso o participante tenha mais hábilidade para a prova
        # ele terá o dobro de chances de ganhar
        for i in self.participants:
            if i.hability == self.prove:
                self.privileged.append(i.name)
                i.life = 2
            elif i.hability != self.prove:
                i.life = 1

    #Rodando a prova
    def event(self):
        # Roteiro básico de exibição ao usuário
        print("----------------------------------------------------------")
        print(f"               A prova será de {self.prove}                  ")
        print("__________________________________________________________")
        if self.privileged:
            print(f'Os privilegiados pela escolha de prova serão: {self.privileged}')
        else:
            print("Não teremos privilegiados pela escolha da prova")
        # Realização da prova
        while len(self.participants) > 1:
            # Cada vez que while for rodado gera um número aleatório
            random = randint(0, len(self.participants)-1)
            # Jogador na posição gerada aleatóriamente perde um ponto
            self.participants[random].life -= 1
            # Caso o jogador não tenha mais ponto ele será eliminado da prova
            if self.participants[random].life == 0:
                self.cont += 1
                print(f'O {self.cont}º eliminado da prova foi: {self.participants[random].name}')
                #sleep(1)
                self.participants.remove(self.participants[random])
        # O último participante a sobrar leva a prova
        return self.participants[0]

    # Escolha de qual modalidade será a prova
    def actProve(self, proveType):
        self.proveType = proveType
        # Roteiro inicial de decisão do usuário
        print(f'          Escolha a prova do {proveType} dessa semana:         ')
        print("Para escolher digite o número ao lado da prova desejada")
        print("----------------------------------------------------------")
        print('-- 1 - Arremesso de Dardos --')
        print('-- 2 - Arremesso de bolas --')
        print('-- 3 - Velocidade --')
        print('-- 4 - Resistência --')
        print('-- 5 - Corrida --')
        print('-- 6 - Sorte --')
        # Usuário deverá decidir qual prova será realizada a partir do ID dela
        decision = int(input("> "))
        # A partir do id digitado o método retornara a prova escolhida
        if decision == 1:
            return "Arremesso de Dardos"
        elif decision == 2:
            return "Arremesso de bolas"
        elif decision == 3:
            return "Velocidade"
        elif decision == 4:
            return "Resistência"
        elif decision == 5:
            return "Corrida"
        elif decision == 6:
            return "Sorte"
        # Caso o digito esteja fora do esperado o método deverá rodar novamente
        else:
            print('Digito inválido')
            self.actProve(proveType)

    # Roteiro básico da prova do líder
    def leader(self):
        # Chamando o método de escolha da prova
        self.setParticipants(self.actProve("líder"))
        # Chamar o método de realização da prova
        # Setar o líder a partir do vencedor
        leader = self.event()
        print(f'{leader.name} venceu a prova e será o lider da semana!')
        print("_______________________________________________________")
        # Retornar líder
        return leader

    # Roteiro básico da prova do anjo
    def angel(self):
        # Chamando o método de escolha da prova
        self.setParticipants(self.actProve("anjo"))
        # Chamar o método de realização da prova
        # Setar o anjo a partir do vencedor
        angel = self.event()
        print(f'{angel.name} venceu a prova e será o lider da semana!')
        # Retornar o anjo
        return angel
