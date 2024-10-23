from koira import Koira
from hoitola import Hoitola

koira = Koira("Musti", 2022)
koira2 = Koira("Hevonen", 1800, "🐴 hirnuu")
koira3 = Koira("Koira 3", 1)

hoitola = Hoitola()
hoitola.koira_sisään(koira)
hoitola.koira_sisään(koira3)
hoitola.listaa_koirat()

for i in range(10):
    koira = Koira(f"Koira {i}", i, "Hau hau" * i)
    hoitola.koira_sisään(koira)

print("------")
#hoitola.listaa_koirat()
#hoitola.koira_ulos(koira)

hoitola.koira_sisään(koira2)
#hoitola.listaa_koirat()

hoitola.työntekijän_kierros()