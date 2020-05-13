from random import randint

listPersonality = []
listPersonality2 = []
listPersonality3 = []
trace = []
cont = 0
listRandom = []

def teste():
    files1 = open('personalidades2-3.csv', encoding="utf-8")
    files2 = open('personalidades3-3.csv', encoding="utf-8")


def readingFiles(file, list):
    # Separar cada registro dos arquivos a partir da quebra de linha
    for record in file.splitlines():
        # Adicionar linha a linha numa lista
        list.append(record)

def random(list):
    random = randint(0, len(list)-1)
    return list[random]

def a():
    personalityList = []
    points = 0
    files = open('personalidades1-3.csv', encoding="utf-8")
    files2 = open('personalidades2-3.csv', encoding="utf-8")
    files3 = open('personalidades3-3.csv', encoding="utf-8")
    readingFiles(files.read(), listPersonality)
    listRandom.append(random(listPersonality))
    readingFiles(files2.read(), listPersonality2)
    listRandom.append(random(listPersonality2))
    readingFiles(files3.read(), listPersonality3)
    listRandom.append(random(listPersonality3))
    for record in listRandom:
        personalityList.append(record[0:(record.find("="))])
        points += float(record[(record.find("="))+1:])
    points = points * 10 * 3 / 4
    print(personalityList)
    print(f"Apoio da audiencia: {int(points)}%")

def personality(self):
    # Rota para caso o genêro seja masculino
    if (self.gender == "Masculino"):
        # Chamar metodo de leitura para ler todas as personalidades possíveis
        self.personalityRead = self.filesPersonalityMasc.read()
        # Adiciona o conteúdo do csv em uma lista
        for record in self.personalityRead.splitlines():
            self.personalityList.append(record)
        # Gera o contador de personalidade setado em 0
        i = 0
        # Enquanto estiver menos de 3 personalidades armazenadas
        while i < 3:
            # Gerador de id
            self.personalityId = self.numbersGenerator(len(self.personalityList)-1)
            # Caso a personalidade já estiver adicionada continuar para gerar outra
            if self.personalityId in self.tempList:
                pass
            # Caso não esteja adicionada adicionar e atualizar o contador
            else:
                self.personalityTraces.append(self.personalityList[self.personalityId])
                self.tempList.append(self.personalityId)
                i += 1
        # Após fim de geração fechar o arquivo csv
        self.filesPersonalityMasc.close()
    else:
        # Chamar metodo de leitura para ler todas as personalidades possíveis
        self.personalityRead = self.filesPersonalityFem.read()
        # Adiciona o conteúdo do csv em uma lista
        for record in self.personalityRead.splitlines():
            self.personalityList.append(record)
        # Gera o contador de personalidade setado em 0
        i = 0
        # Enquanto estiver menos de 3 personalidades armazenadas
        while i < 3:
            # Gerador de id
            self.personalityId = self.numbersGenerator(len(self.personalityList) - 1)
            # Caso a personalidade já estiver adicionada continuar para gerar outra
            if self.personalityId in self.tempList:
                pass
            # Caso não esteja adicionada adicionar e atualizar o contador
            else:
                self.personalityTraces.append(self.personalityList[self.personalityId])
                self.tempList.append(self.personalityId)
                i += 1
        # Após fim de geração fechar o arquivo csv
        self.filesPersonalityFem.close()


if __name__ == '__main__':
    a()