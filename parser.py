import requests
from bs4 import BeautifulSoup


page = 1

while True:

    r = requests.get('http://tamashebi.net/page/' + str(page))

    html = BeautifulSoup(r.content, 'html.parser')

    games = html.select("#newsl > div:nth-child(2) > b > a")

    if(len(games) != 0):

        games_url_list = []
        for game in games:
            games_url_list.append(game.get('href'))

        for game_url in games_url_list:
            r = requests.get(game_url)
            html = BeautifulSoup(r.content, 'html.parser')
            game_title = html.select(
                "#newsl > div:nth-child(2) > b")[0].text
            game_content = html.select(
                ".attachment > a")

            print("Title: " + game_title + "\n" +
                  "Download Link " + game_content[0].get('href') + "\n")
        page += 1
    else:
        break
