from bs4 import BeautifulSoup
import requests, webbrowser

class Scraper:
    def __init__(self):

        print('+----------------------+')
        print('|                      |')
        print('|  Comic Book Scraper  |')
        print('|                      |')
        print('+----------------------+')

        self.menu()

    def menu(self):
        print('\n')
        print('(P)esquisar;')
        print('(T)todos os titulos;')
        print('(U)ltimos posts.')
        self.option = str.lower(input(''))

        if self.option == 'p':
            self.pesquisar()
        elif self.option == 't':
            self.titulos()
        elif self.option == 'u':
            self.ultimos()
        else:
            print('Opção invalida.')

    def pesquisar(self):
        ptitulo = input('Pesquisar: ')
        self.ptitulo = ptitulo.title().replace(' ', '%20')
        self.pURL = 'http://renegadoscomics.blogspot.com.br/search/label/' + self.ptitulo
        self.pReq = requests.get(self.pURL).content
        self.psoup = BeautifulSoup(self.pReq, 'lxml')

        self.phq = self.psoup.find_all('h3', {'class':'post-title entry-title'})
        for hq in self.phq:
            self.hqText = hq.get_text().replace('\n', '')
            self.hqLink = hq.a['href']
            print('{}'.format(self.hqText))

    def titulos(self):
        self.tURL = 'http://renegadoscomics.blogspot.com.br/'
        self.tReq = requests.get(self.tURL).content
        self.tsoup = BeautifulSoup(self.tReq, 'lxml')

        self.titulos = self.tsoup.find_all('div', {'class':'widget-content list-label-widget-content'})
        for ul in self.titulos:
            self.titulos = ul.find_all('li')
            for titulo in self.titulos:
                self.titulo = titulo.get_text()
                self.titulo = self.titulo.replace('\n', '')
                print(self.titulo)

    def ultimos(self):
        self.uUrl = 'http://renegadoscomics.blogspot.com.br/'
        self.uReq = requests.get(self.uUrl).content
        self.usoup = BeautifulSoup(self.uReq, 'lxml')

        self.ultimos = self.usoup.find_all('h3', {'class':'post-title entry-title'})
        for novo in self.ultimos:
            self.ultimos = novo.get_text().replace('\n', '')
            print(self.ultimos)
            

if __name__ == '__main__':
    Scraper()
