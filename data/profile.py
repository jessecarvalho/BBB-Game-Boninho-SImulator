from random import randint
filesPersonality = open('csvFiles/personalidades.csv', encoding="utf-8")
filesProfessions = open('csvFiles/profissoes.csv')
filesTest = open('csvFiles/provas.csv')

class Person:
    def __init__(self):
        pass

    def sorteador(self):
        return randint(0,15)

    def validador(self, list, sorteado, personalityList):
        if personalityList[sorteado] in list:
            return True
        else:
            return False

    def personality(self):
        self.personalityList = []
        self.personalityTraces = []
        self.personalityRead = filesPersonality.read()
        #Adiciona os textos do csv em uma lista
        for record in self.personalityRead.splitlines():
            self.personalityList.append(record)
        #Sorteia as personalidades
        for i in range(0, 3):
            self.actualTrace = self.sorteador()
            if self.validador(self.personalityTraces, self.actualTrace, self.personalityList) == True:
                self.personality()
            else:
                self.personalityTraces.append(self.personalityList[self.actualTrace])
        print(self.personalityTraces)




if __name__ == '__main__':
    Jonas = Person()
    Jonas.personality()