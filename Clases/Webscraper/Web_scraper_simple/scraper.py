import requests
from bs4 import BeautifulSoup

URL = "https://www.elespectador.com/"

def run():
    response = requests.get(URL)

    if response.status_code == 200:
        
        soup = BeautifulSoup (response.content)
        titles_div = soup.find_all ('div', attrs= {
            'class': 'Card-title'
        })

        titles= []
        for title_div in titles_div:
            title = title_div.find('a').find('h3')
            if title:
                title = title.get_text()
                titles.append(title)

        with open('results.txt', 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(title)
                f.write('\n')

    else:
        print('Ocurrió un error:', response.status_code)

if __name__ == "__main__":
    run()
            