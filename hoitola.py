class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)

    def koira_ulos(self, koira):
        self.koirat.remove(koira)

    def listaa_koirat(self):
        for koira in self.koirat:
            print(f"Nimi: {koira.nimi}")

    def työntekijän_kierros(self):
        for koira in self.koirat:
            koira.hauku()
