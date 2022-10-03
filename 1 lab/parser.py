import json
import requests
from bs4 import BeautifulSoup as BS

page = 1
data = {}
data['game'] = []
while page < 15:
    request = requests.get("https://stopgame.ru/news/all/p" + str(page))
    html = BS(request.content, 'html.parser')
    items = html.select(".items > .article-summary")

    if (len(items)):
        for element in items:
            text = element.select(".caption > a")
            link = element.find("a").get('href')
            img = element.find('img').get('src')
            data['game'].append({
                'text': text[0].text,
                'link': "https://stopgame.ru" + link,
                'image': img
            })
        page += 1
    else:
        break


with open('1 lab/games.json', 'w') as file:
    json.dump(data, file)
