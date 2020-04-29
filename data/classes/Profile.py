from random import randint


class Person:
    def __init__(self):
        self.filesPersonalityFem = open('../csvFiles/personalidadesFem.csv', encoding="utf-8")
        self.filesPersonalityMasc = open('../csvFiles/personalidadesMasc.csv', encoding="utf-8")
        self.filesProfessionsMasc = open('../csvFiles/profissoesMasc.csv', encoding="utf-8")
        self.filesProfessionsFem = open('../csvFiles/profissoesFem.csv', encoding="utf-8")
        self.filesTest = open('../csvFiles/provas.csv', encoding="utf-8")
        self.filesEmojiMasc = open('../csvFiles/emojisMasc.csv', encoding="utf-8")
        self.filesEmojiFem = open('../csvFiles/emojisFem.csv', encoding="utf-8")
        self.filesNameMasc = open('../csvFiles/nomesMasc.csv', encoding="utf-8")
        self.filesNameFem = open('../csvFiles/nomesFem.csv', encoding="utf-8")
        self.personalityList = []
        self.tempList = []
        self.personalityTraces = []

    def numbersGenerator(self, limit):
        tempNumber = randint(0, limit)
        return tempNumber

    def readingFiles(self, file, list):
        for record in file.splitlines():
            list.append(record)

    def gender(self):
        self.genderList = ['Masculino', 'Feminino']
        self.genderId = self.numbersGenerator(len(self.genderList)-1)
        self.gender = self.genderList[self.genderId]

    def name(self):
        if (self.gender == "Masculino"):
            self.nameRead = self.filesNameMasc.read()
            self.nameList = []
            self.readingFiles(self.nameRead, self.nameList)
            self.nameId = self.numbersGenerator(len(self.nameList) - 1)
            self.name = self.nameList[self.nameId]
            self.filesNameMasc.close()
        else:
            self.nameRead = self.filesNameFem.read()
            self.nameList = []
            self.readingFiles(self.nameRead, self.nameList)
            self.nameId = self.numbersGenerator(len(self.nameList) - 1)
            self.name = self.nameList[self.nameId]
            self.filesNameFem.close()

    def personality(self):
        if (self.gender == "Masculino"):
            self.personalityRead = self.filesPersonalityMasc.read()
            #Adiciona os textos do csv em uma lista
            for record in self.personalityRead.splitlines():
                self.personalityList.append(record)
            #Sorteia as personalidades
            i = 0
            while i < 3:
                self.personalityId = self.numbersGenerator(len(self.personalityList)-1)
                if self.personalityId in self.tempList:
                    pass
                else:
                    self.personalityTraces.append(self.personalityList[self.personalityId])
                    self.tempList.append(self.personalityId)
                    i += 1
            self.filesPersonalityMasc.close()
        else:
            self.personalityRead = self.filesPersonalityFem.read()
            # Adiciona os textos do csv em uma lista
            for record in self.personalityRead.splitlines():
                self.personalityList.append(record)
            # Sorteia as personalidades
            i = 0
            while i < 3:
                self.personalityId = self.numbersGenerator(len(self.personalityList) - 1)
                if self.personalityId in self.tempList:
                    pass
                else:
                    self.personalityTraces.append(self.personalityList[self.personalityId])
                    self.tempList.append(self.personalityId)
                    i += 1
            self.filesPersonalityFem.close()

    def profession(self):
        if (self.gender == "Masculino"):
            self.professionRead = self.filesProfessionsMasc.read()
            self.professionList = []
            for record in self.professionRead.splitlines():
                self.professionList.append(record)
            self.professionId = self.numbersGenerator(len(self.professionList)-1)
            self.profession = self.professionList[self.professionId]
            self.filesProfessionsMasc.close()
        else:
            self.professionRead = self.filesProfessionsFem.read()
            self.professionList = []
            for record in self.professionRead.splitlines():
                self.professionList.append(record)
            self.professionId = self.numbersGenerator(len(self.professionList) - 1)
            self.profession = self.professionList[self.professionId]
            self.filesProfessionsFem.close()

    def hability(self):
        self.habilityRead = self.filesTest.read()
        self.habilityList = []
        self.readingFiles(self.habilityRead, self.habilityList)
        self.habilityId = self.numbersGenerator(len(self.habilityList)-1)
        self.hability = self.habilityList[self.habilityId]
        self.filesTest.close()

    def emoji(self):
        if (self.gender == "Masculino"):
            self.emojisRead = self.filesEmojiMasc.read()
            self.emojiList = []
            self.readingFiles(self.emojisRead, self.emojiList)
            self.emojiId = self.numbersGenerator(len(self.emojiList) - 1)
            self.emoji = self.emojiList[self.emojiId]
            self.filesEmojiMasc.close()
        else:
            self.emojisRead = self.filesEmojiFem.read()
            self.emojiList = []
            self.readingFiles(self.emojisRead, self.emojiList)
            self.emojiId = self.numbersGenerator(len(self.emojiList) - 1)
            self.emoji = self.emojiList[self.emojiId]
            self.filesEmojiFem.close()

    def followers(self):
        self.followers = self.numbersGenerator(100000)

    def favoritism(self):
        self.favoritism = self.numbersGenerator(20)

    def personGenerator(self):
        self.gender()
        self.name()
        self.personality()
        self.profession()
        self.hability()
        self.emoji()
        self.followers()
        self.favoritism()



if __name__ == '__main__':
    Pessoa = Person("Jessé")
    Pessoa.personGenerator()


