from time import sleep

class Final:
    def __init__(self, finalists):
        self.finalists = finalists

    def theFinal(self):
        print("Após uma longa temporada chegamos na grande final!")
        print("A final será decidida pelos telespectadores")
        print("Mas o seu voto irá dar uma grande vantagem ao seu favorito")
        print("Portanto, escolha, qual dos três terá seu voto?")
        i = 0
        while i < len(self.finalists):
            print(f"{i+1} para votar em: {self.finalists[i].name}")
            i += 1
        self.vote = int(input("> "))
        if 0 < self.vote <= 3:
            self.playerChoose = self.finalists[self.vote-1]
            print(f"Voto computado com sucess em {self.playerChoose.name}!")
        else:
            print("Voto inválido! Vote apenas digitando de 1 a 3!")
            sleep(2)
            self.theFinal()
        for i in self.finalists:
            if i == self.playerChoose:
                i.support += 10
        if self.finalists[0].support > self.finalists[1].support and self.finalists[0].support > self.finalists[2].support:
            print(self.finalists[0].name)
        elif self.finalists[1].support > self.finalists[2].support:
            print(self.finalists[1].name)
        else:
            print(self.finalists[0].name)
