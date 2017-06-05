from bs4 import BeautifulSoup
import requests
from tkinter import *
import webbrowser

class App:
    def __init__(self, master):
        master.title('Comic Book Scraper')

        #Entrada de pesquisa
        self.varSearch = StringVar()
        self.searchEnt = Entry(textvariable=self.varSearch)
        self.searchEnt.grid(row=1, column=0)

        #Botão para fazer a pesquisa
        self.searchBtn = Button(text='Search', command=self.searchHQ)
        self.searchBtn.grid(row=2, column=0)

        #Resultado da pesquisa
        self.resultFld = Listbox(width=50, selectmode=SINGLE)
        self.resultFld.grid(row=3, column=0)
        self.resultFld.bind('<<ListboxSelect>>', self.download)

        #Texto em cima da listbox com os titulos
        self.titlesLbl = Label(text='Titles')
        self.titlesLbl.grid(row=2, column=1)

        #Titulos
        self.titlesFld = Listbox(width=50, selectmode=SINGLE)
        self.titlesFld.grid(row=3, column=1)
        self.titlesFld.bind('<<ListboxSelect>>', self.viewHQ_)


    #Funções

    #Faz a busca e imprime o resultado
    def searchHQ(self):
        self.var = self.varSearch.get()
        self.var = self.var.title().replace(' ', '%20')
        self.urlHQ = 'http://renegadoscomics.blogspot.com.br/search/label/' + self.var
        self.reqHQ = requests.get(self.urlHQ).content
        self.soup = BeautifulSoup(self.reqHQ, 'lxml')

        self.comicbooks = self.soup.find_all('div', {'class':'post bar hentry'})
        for comicbook in self.comicbooks:
            self.listComicbooks = comicbook.find_all('h3', {'class':'post-title entry-title'})
            for comicbookName in self.listComicbooks:
                self.resultFld.insert(END, comicbookName.get_text())

    #Faz o download da HQ selecionada
    def download(self, result):
        self.getComicTxt = self.resultFld.get(self.resultFld.curselection()).replace('\n', '')

        self.getHQLink = self.soup.find('a', string=self.getComicTxt)
        self.HQLink = self.getHQLink['href']

        self.reqHQLink = requests.get(self.HQLink).content
        self.soupHQ = BeautifulSoup(self.reqHQLink, 'lxml')

        self.downLink = self.soupHQ.find_all('div', {'class':'separator'}, limit=1)
        for self.link in self.downLink:
            self.downHQLink = self.link.a['href']
            webbrowser.open(self.downHQLink)

    #Exibi as HQs de acordo com o titulo selecionado
    def viewHQ_(self, result):
        self.getTitleText = self.titlesFld.get(self.titlesFld.curselection()).title().replace('\n', '').replace(' ', '%20')
        self.urlHQ = 'http://renegadoscomics.blogspot.com.br/search/label/' + self.getTitleText
        self.reqHQ = requests.get(self.urlHQ).content
        self.soup = BeautifulSoup(self.reqHQ, 'lxml')

        self.comicbooks = self.soup.find_all('div', {'class':'post bar hentry'})
        for self.comicbook in self.comicbooks:
            self.listComicbooks = self.comicbook.find_all('h3', {'class':'post-title entry-title'})
            for self.comicbookName in self.listComicbooks:
                self.titlesFld.delete(0, END)
                self.titlesFld.insert(END, self.comicbookName.get_text())


root = Tk()
app = App(root)
root.mainloop()
