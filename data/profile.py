from random import randint


class Person:
    def __init__(self, nome):
        self.filesPersonality = open('csvFiles/personalidades.csv', encoding="utf-8")
        self.filesProfessions = open('csvFiles/profissoes.csv', encoding="utf-8")
        self.filesTest = open('csvFiles/provas.csv', encoding="utf-8")
        self.filesEmoji = open('csvFiles/emojis.csv', encoding="utf-8")
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
            self.personalityId = self.numbersGenerator(len(self.personalityList)-1)
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
        self.professionId = self.numbersGenerator(len(self.professionList)-1)
        self.profession = self.professionList[self.professionId]
        print(f'A profissão de {self.name} atualmente é: {self.profession}')
        self.filesProfessions.close()

    def hability(self):
        self.habilityRead = self.filesTest.read()
        self.habilityList = []
        self.readingFiles(self.habilityRead, self.habilityList)
        self.habilityId = self.numbersGenerator(len(self.habilityList)-1)
        self.hability = self.habilityList[self.habilityId]
        print(f"A principal hábilidade de {self.name} é: {self.hability}")
        self.filesTest.close()

    def emoji(self):
        self.emojisRead = self.filesEmoji.read()
        self.emojiList = []
        self.readingFiles(self.emojisRead, self.emojiList)
        self.emojiId = self.numbersGenerator(len(self.emojiList)-1)
        self.emoji = self.emojiList[self.emojiId]
        print(f'Emoji: {self.emoji}')

    def seguidores(self):
        self.seguidores = self.numbersGenerator(10000000)
        print(f'Seguidores: {self.seguidores:,}')

    def favoritismo(self):
        self.favoritismo = self.numbersGenerator(20)
        print(f'Favoritismo: {self.favoritismo}% ')

    def geradorPessoa(self):
        self.personality()
        self.profession()
        self.hability()
        self.emoji()
        self.seguidores()
        self. favoritismo()

if __name__ == '__main__':
    Pessoa = Person("Jessé")
    Pessoa.geradorPessoa()


