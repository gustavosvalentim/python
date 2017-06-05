from bs4 import BeautifulSoup
import requests
from datetime import datetime

estado = input('Estado: ')
cidade = input('Cidade: ')

estado = estado.lower()
cidade = cidade.lower().replace(' ', '-')

url = 'http://tempo.clic.com.br/' + estado + '/' + cidade
reqUrl = requests.get(url)
content = reqUrl.content
soup = BeautifulSoup(content, 'lxml')

temp = soup.find('span', {'class':'temperature_now'})
temp = temp.get_text().replace('\n', '').replace(' ', '')
cli = soup.find('g', {'class':'groupCloud'})
cli = cli.title.get_text()
ven = soup.find('span', {'class':'windSpeedModule'})
ven = ven.get_text().replace('\n', '').replace(' ', '')
day_d = {'Monday':'Segunda-Feira', 'Tuesday':'Terça-Feira', 'Wednesday':'Quarta-Feira', 'Thursday':'Quinta-Feira', 'Friday':'Sexta-Feira', 'Saturday':'Sábado', 'Sunday':'Domingo'}
date = datetime.now().strftime('%d/%m/%Y %I:%M%p')


print('\n')
print('%s, %s' % (cidade.capitalize(), estado.upper()))
print('Temperatura de %s' % (temp))
print('Tempo %s' % (cli.lower()))
print('Ventos de %s' % (ven))
print(day_d[datetime.now().strftime('%A')] + ' ' + date)
