import requests
import json

class TVShow:
    def __init__(self, show):
        self.show = show

    def print_name(self):
        print(self.show['name'])

    def print_genres(self):
        for genre in self.show['genres']:
            print(f" - {genre}")

    def print_language(self):
        print(self.show['language'])

class Channel:
    def __init__(self, shows):
        self.shows = shows

    def print_all_show_information(self):
        for tv in self.shows:
            tv.print_name()
            tv.print_genres()
            tv.print_language()


class GetShowsFromAPI:
    def get(self, keyword):
        # try blockissa yritämme suorittaa jotain toimintoa...
        try:
            url = f"https://api.tvmaze.com/search/shows?q={keyword}"

            vastaus = requests.get(url)
            return vastaus.json()
        # ... mikäli ei onnistu ja koodi heittää (throws) virheen
        # tässä saamme sen kiinni ja voimme palauttaa tyhjän taulukon,
        # jotta ohjelma ei kaadu
        # https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        except requests.exceptions.RequestException as e:
            #print(e)

            # tässä kannattaa palauttaa tyhjä taulukko,
            # jotta alla oleva for-in loop jatkaa toimimista
            return []

#hakusana = input("Hakusana: ")

hakusana = "cat"

search = GetShowsFromAPI()
tulos = search.get(hakusana)
#print(json.dumps(tulos, indent=2))

if len(tulos) == 0:
    print("Ei hakutuloksia")

shows = []
for arvo in tulos:
    tv = TVShow(arvo['show'])
    shows.append(tv)

channel = Channel(shows)
channel.print_all_show_information()
