import requests, json
from bs4 import BeautifulSoup

def restore_name(str):
	return " ".join(str.split())

#Message console
print('Start scraping...')

url = "https://www.iscte-iul.pt/curso/3/licenciatura-engenharia-informatica/apresentacao"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

data_presentation = {}
data_presentation['presentation'] = []

content = soup.find('div', attrs={'class': 'content-courses'})

subtitle = content.find('div', attrs={'class':'avec-bold'}).find('p').getText()
mainText = content.find('div', attrs={'class':'top-buffer-10'}).find('p').getText()
videoLink = content.find('iframe', attrs={'class':'degree-video'})['src']
directorMessage = content.find('div', attrs={'class':'quote'}).find('p').getText()


#print(content)
#print(subtitle)
#print(mainText)
#print(videoLink)
#print(directorMessage)

data_presentation['presentation'].append({
		'subtitle': restore_name(subtitle),
		'mainText': restore_name(mainText),
		'videoLink': restore_name(videoLink),
		'directorMessage': restore_name(directorMessage),
		})

#Message console
print('Finish scraping.')
print('Start json file...')
with open('3_presentation.txt', 'w', encoding='utf8') as outfile:  
    json.dump(data_presentation, outfile)
#ensure_ascii=False
#Message console
print('Finish json file.')