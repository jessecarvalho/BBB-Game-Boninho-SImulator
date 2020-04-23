from random import randint


class Person:
    def __init__(self, nome):
        self.filesPersonality = open('csvFiles/personalidades.csv', encoding="utf-8")
        self.filesProfessions = open('csvFiles/profissoes.csv', encoding="utf-8")
        self.filesTest = open('csvFiles/provas.csv', encoding="utf-8")
        self.name = nome
        self.personalityList = []
        self.tempList = []
        self.personalityTraces = []
    def numbersGenerator(self, limit):
        tempNumber = randint(0, limit)
        return tempNumber

    def readingFiles(self, file, list):
        for record in file.splitlines():
            list.append(record)

    def personality(self):
        self.personalityRead = self.filesPersonality.read()
        #Adiciona os textos do csv em uma lista
        for record in self.personalityRead.splitlines():
            self.personalityList.append(record)
        #Sorteia as personalidades
        i = 0
        while i < 3:
            self.personalityId = self.numbersGenerator(15)
            if self.personalityId in self.tempList:
                pass
            else:
                self.personalityTraces.append(self.personalityList[self.personalityId])
                self.tempList.append(self.personalityId)
                i += 1
        print(f'Os principais traços de: {self.name} são: {self.personalityTraces}')
        self.filesPersonality.close()


    def profession(self):
        self.professionRead = self.filesProfessions.read()
        self.professionList = []
        for record in self.professionRead.splitlines():
            self.professionList.append(record)
        self.professionId = self.numbersGenerator(1)
        self.profession = self.professionList[self.professionId]
        print(f'A profissão de {self.name} atualmente é: {self.profession}')
        self.filesProfessions.close()

    def hability(self):
        self.habilityRead = self.filesTest.read()
        self.habilityList = []
        self.readingFiles(self.habilityRead, self.habilityList)
        self.habilityId = self.numbersGenerator(5)
        self.hability = self.habilityList[self.habilityId]
        print(f"A principal hábilidade de {self.name} é: {self.hability}")
        self.filesTest.close()


if __name__ == '__main__':
    Jonas = Person("Jessé")
    Jonas.personality()
    Jonas.profession()
    Jonas.hability()
    Mariana = Person("Lary")
    Mariana.personality()
    Mariana.profession()
    Mariana.hability()

