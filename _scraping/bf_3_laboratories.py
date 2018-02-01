import requests, json
from bs4 import BeautifulSoup

def restore_name(str):
	return " ".join(str.split())

#Message console
print('Start scraping...')

url = "https://www.iscte-iul.pt/contents/investigar/209/laboratorios"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

data_laboratories = {}
data_laboratories['laboratories'] = []

content = soup.find('div', attrs={'class': 'components col-image'})

labs = content.find_all('div', attrs={'class': 'row-wrapper'})
for lab in labs:
	l = lab.find('div', attrs={'class': 'col-wrapper'})
	l_title = l.find('div', attrs={'class': 'agendaTitle'}).getText()
	par = l.find_all('p')
	l_info =""
	for p in par:
		l_info = l_info + restore_name(p.getText()) + '\n'
	l_ul = ""
	if (l.find('ul')):
		li = l.find('ul').find_all('li')
		for line in li:
			l_ul = l_ul + line.getText() +'; '
		#l_ul = l.find('ul')

	data_laboratories['laboratories'].append({
			'title': restore_name(l_title),
			'info': restore_name(l_info),
			'list': l_ul,
			})

#Message console
print('Finish scraping.')
print('Start json file...')

with open('3_laboratories.json', 'w', encoding='utf8') as outfile:  
    json.dump(data_laboratories, outfile)

#Message console
print('Finish json file.')