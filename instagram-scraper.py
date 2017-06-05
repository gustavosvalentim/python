from bs4 import BeautifulSoup
import requests
import os, sys

class InstagramScraper:
    def __init__(self, url):

        self.url = url
        self.get_html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.get_html, 'lxml')

        try:
            self.prop = self.soup.find('meta', {'property':'og:video'})
        except:
            self.prop = self.soup.find('meta', {'property':'og:image'})

        self.link = self.prop['content']
        self.newlink = self.link.replace('https://', '').replace('http://', '').replace('/', '')

        self.foto = requests.get(self.link).content

        with open(self.newlink, 'wb') as foto:
            foto.write(self.foto)


if __name__ == '__main__':
    url = input('URL: ')
    InstagramScraper(url)
