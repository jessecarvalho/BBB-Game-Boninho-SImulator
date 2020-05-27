import random
class Events:
    def __init__(self):
        self.events = open("csvFiles/eventos.csv", encoding="UTF-8")
        self.listEvents = []

    def readingFiles(self, file, list):
        # Separar cada registro dos arquivos a partir da quebra de linha
        for record in file.splitlines():
            # Adicionar linha a linha numa lista
            list.append(record)

    def eventsAct(self, personList):
        i = 0
        self.readingFiles(self.events.read(), self.listEvents)
        while i < random.randint(1, 5):
            person = random.choice(personList)
            event = random.choice(self.listEvents)
            point = int(event.split("=")[1]) * random.uniform(1.1, 2.8) / random.uniform(1.1, 2.8)
            event = event.split("=")[0]
            gender = "ele" if person.gender == "Masculino" else "ela"
            lastSupport = int(person.support)
            person.support = int(person.support + point)
            print('________________________________________________________')
            print(f"{person.name} {event}")
            print(f"Por conta disso {gender} ganhou popularidade saindo de {lastSupport}% e indo para {person.support}%") \
                if point > 0 else print(f"Por conta disso ele(a) perdeu:\
popularidade e viu seu apoio cair de {lastSupport}% para {person.support}%")
            i += 1
        return