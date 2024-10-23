class Auto:
    def __init__(self, rekisteritunnus, väri):
        self.aseta_rekisteritunnus(rekisteritunnus)
        #self.color = väri
        self.aseta_väri(väri)

    # magic method
    # kun Auto luokan instanssia tulostetaan print(auto) komennolla
    # https://rszalski.github.io/magicmethods/
    def __str__(self):
        return f" huhhei Auto {self.rekisteritunnus} väri on {self.color}"

    def aseta_väri(self, väri):
        #sql = f"UPDATE cars SET color = {väri} WHERE id = {self.id}"
        self.color = väri

    def aseta_rekisteritunnus(self, tunnus):
        self.rekisteritunnus = tunnus

class Parkkihalli:
    def __init__(self, autot):
        self.autot = []

    def maalaa(self, auto, väri):
        index = self.autot.index(auto)
        self.autot[index].aseta_väri(väri)

class Maalaamo:
    def maalaa(self, auto, väri):
        auto.aseta_väri(väri)

maalaamo = Maalaamo()

auto = Auto("ABC-123", "sininen")
print(auto)

auto2 = Auto("XYZ-123", "musta")
maalaamo.maalaa(auto2, "oranssi")
print(auto)
print(auto2)

