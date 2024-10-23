class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, count=1):
        for i in range(count):
            print(f"{self.nimi}: {self.haukahdus}")
