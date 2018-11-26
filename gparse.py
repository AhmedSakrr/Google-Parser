from urllib.parse import unquote
from bs4 import BeautifulSoup
from requests import get


class Rezult:
    def __init__(self, name, url, desc):
        self.name = name
        self.url = url
        self.desc = desc


class GoogleParser:
    ''' Class for parse information from Google\n
    what - search query\n
    pages - pages for parse
    '''

    def __init__(self, what, pages=0):
        self.output = []
        self.__pages = pages if pages != 0 else pages - 1
        self.__query = what
        self.__search()


    def __search(self):
        i = 0

        while True:
            r = get('https://www.google.dk/search?q=' +
                    self.__query + '&start=' + str(i*10)).text
            self.__parse(r)
            i += 1

            if i > self.__pages:
                break


    def __parse(self, html):
        try:
            soup = BeautifulSoup(html, features="html5lib")
            rezult = soup.find('div', {'id': 'search'})
            rows = rezult.findAll('div', {'class': 'g'})
        except:
            return

        for row in rows:
            try:
                data = row.find('h3', {'class': 'r'})
                temp = data.find('a')
                link = temp['href']
                link = unquote((link[7:]).split('&sa')[0])
                name = temp.get_text()

                data = row.find('span', {'class': 'st'})
                desc = data.get_text()

                del data, temp

                self.output.append(Rezult(name, link, desc))
            except:
                pass