from random import randint

# Classe para geração inidivdual dos personagens
class Person:
    # Método de inicialização
    def __init__(self):
        # Abertura de todos os itens csv
        self.filesPersonalityFem = open('csvFiles/personalidadesFem.csv', encoding="utf-8")
        self.filesPersonalityMasc = open('csvFiles/personalidadesMasc.csv', encoding="utf-8")
        self.filesProfessionsMasc = open('csvFiles/profissoesMasc.csv', encoding="utf-8")
        self.filesProfessionsFem = open('csvFiles/profissoesFem.csv', encoding="utf-8")
        self.filesTest = open('csvFiles/provas.csv', encoding="utf-8")
        self.filesEmojiMasc = open('csvFiles/emojisMasc.csv', encoding="utf-8")
        self.filesEmojiFem = open('csvFiles/emojisFem.csv', encoding="utf-8")
        self.filesNameMasc = open('csvFiles/nomesMasc.csv', encoding="utf-8")
        self.filesNameFem = open('csvFiles/nomesFem.csv', encoding="utf-8")
        # Inicialização de listas
        self.personalityList = []
        self.tempList = []
        self.personalityTraces = []

    # Gerador de números aleatórios
    def numbersGenerator(self, limit):
        tempNumber = randint(0, limit)
        return tempNumber

    # Método de leitura dos arquivos csv
    def readingFiles(self, file, list):
        # Separar cada registro dos arquivos a partir da quebra de linha
        for record in file.splitlines():
            # Adicionar linha a linha numa lista
            list.append(record)

    # Gerador de genêro
    def gender(self):
        # Inicialmente genêros podem ser masculinos ou femininos
        self.genderList = ['Masculino', 'Feminino']
        # GenderId gere um número aleatório para aleatorizar a seleção de genêro
        self.genderId = self.numbersGenerator(len(self.genderList)-1)
        # Atributo genêro do personagem recebe o valor da lista na posição sorteada
        self.gender = self.genderList[self.genderId]

    #Gerador de nomes
    def name(self):
        # Lista inicializada
        self.nameList = []
        # Rota para o caso do personagem ser do genêro masculino
        if (self.gender == "Masculino"):
            # Chamar metodo de leitura para ler nome a nome
            self.readingFiles(self.filesNameMasc.read(), self.nameList)
            # Chamar o método de geração de números aleatórios para gerar id do nome
            self.nameId = self.numbersGenerator(len(self.nameList) - 1)
            # Adiciona nome gerado a váriavel nome
            self.name = self.nameList[self.nameId]
            # Fecha arquivo csv
            self.filesNameMasc.close()
        # Rota caso o personagem seja do genêro feminino
        else:
            # Chamar metodo de leitura para ler nome a nome
            self.readingFiles(self.filesNameFem.read(), self.nameList)
            # Chamar o método de geração de números aleatórios para gerar id do nome
            self.nameId = self.numbersGenerator(len(self.nameList) - 1)
            # Adiciona nome gerado a váriavel nome
            self.name = self.nameList[self.nameId]
            # Fecha arquivo csv
            self.filesNameFem.close()

    # Método gerador de personalidade
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

    # Método gerador de profissao
    def profession(self):
        # Rota para o genêro masculino
        if (self.gender == "Masculino"):
            # Realizar a leitura do arquivo csv
            self.professionRead = self.filesProfessionsMasc.read()
            # inicializar lista de profissao
            self.professionList = []
            # Adicionar profissões do arquivo csv em uma lista
            for record in self.professionRead.splitlines():
                self.professionList.append(record)
            # Gerador de id
            self.professionId = self.numbersGenerator(len(self.professionList)-1)
            # Gere a profissão a partir do id
            self.profession = self.professionList[self.professionId]
            # Fecha o arquivo csv
            self.filesProfessionsMasc.close()
        # Rota para o genêro feminino
        else:
            # Realizar a leitura do arquivo csv
            self.professionRead = self.filesProfessionsFem.read()
            # inicializar lista de profissao
            self.professionList = []
            # Adicionar profissões do arquivo csv em uma lista
            for record in self.professionRead.splitlines():
                self.professionList.append(record)
            # Gerador de id
            self.professionId = self.numbersGenerator(len(self.professionList) - 1)
            # Gere a profissão a partir do id
            self.profession = self.professionList[self.professionId]
            # Fecha o arquivo csv
            self.filesProfessionsFem.close()

    # Método gerador de melhor prova
    def hability(self):
        # Inicializar lista
        self.habilityList = []
        # Realizar leitura do arquivo csv
        self.readingFiles(self.filesTest.read(), self.habilityList)
        # Gerar id
        self.habilityId = self.numbersGenerator(len(self.habilityList)-1)
        # Gerar personalidade a partir do ID
        self.hability = self.habilityList[self.habilityId]
        # Fechar arquivo csv
        self.filesTest.close()

    def emoji(self):
        # Rota masculino
        if (self.gender == "Masculino"):
            # Inicializar lista
            self.emojiList = []
            # Realizar leitura do arquivo csv
            self.readingFiles(self.filesEmojiMasc.read(), self.emojiList)
            # Gerar id
            self.emojiId = self.numbersGenerator(len(self.emojiList) - 1)
            # Gerar emoji a partir do ID
            self.emoji = self.emojiList[self.emojiId]
            # Fechar arquivo csv
            self.filesEmojiMasc.close()
        # Rota Feminino
        else:
            # Inicializar lista
            self.emojiList = []
            # Realizar leitura do arquivo csv
            self.readingFiles(self.emojisRead, self.emojiList)
            # Gerar id
            self.emojiId = self.numbersGenerator(len(self.emojiList) - 1)
            # Gerar emoji a partir do ID
            self.emoji = self.emojiList[self.emojiId]
            # Fechar arquivo csv
            self.filesEmojiFem.close()

    # Método gerador de seguidores nas redes sociais
    def followers(self):
        self.followers = self.numbersGenerator(100000)

    # Método gerador de carinho do público
    def favoritism(self):
        self.favoritism = self.numbersGenerator(20)

    # Método para gerenciar a criação de pessoas
    def personGenerator(self):
        self.gender()
        self.name()
        self.personality()
        self.profession()
        self.hability()
        self.emoji()
        self.followers()
        self.favoritism()



