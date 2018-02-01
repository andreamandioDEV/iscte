# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: bf_3_uc.py
# Ultima modificação: 01/02/2018
# Refs: http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
import requests, json
from bs4 import BeautifulSoup

def restore_name(str):
	return " ".join(str.split())

#Message console
print('Start scraping...')

url = "https://www.iscte-iul.pt/curso/3/licenciatura-engenharia-informatica/planoestudos"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

data_ucs = {}
data_ucs['uc'] = []

uc_tr = soup.find_all('tr', attrs={'class': 'yearsemester-info'})
i=0;
for uc in uc_tr:
	uc_name = uc.find('a', attrs={'class':'curricular-course-text'}).getText()
	uc_language = uc.find('span', attrs={'class':'lang-value'}).getText()
	uc_etcs = uc.find('span', attrs={'class':'ects-value'}).getText()
	uc_desc = soup.find_all('tr', attrs={'class': 'curricular-info'})[i].find_all('p', attrs={'class':'curricular-course-text'})
	#print(len(uc_desc))
	i+=1
	uc_optional = 0
	uc_style = 1
	if (i <= 6):
		uc_year = 1
		uc_semester = 1
	elif(i>6 and i<=11):
		uc_year = 1
		uc_semester = 2
	elif(i>11 and i<=16):
		uc_year = 2
		uc_semester = 1
	elif(i>16 and i<=21):
		uc_year = 2
		uc_semester = 2
	elif(i>21 and i<=26):
		uc_year = 3
		uc_semester = 1
	elif(i>26 and i<=31):
		uc_year = 3
		uc_semester = 2
	elif(i>31 and i<=33):
		uc_year = 1
		uc_semester = 2
		uc_style = 2
	elif(i>33 and i<=55):
		uc_year = 1
		uc_semester = 2
		uc_optional = 1
		uc_style = 2

	
	uc_goals = uc_desc[0].getText()
	uc_program = uc_desc[1].getText()
	uc_evaluation = uc_desc[2].getText()

	if (uc_language == 'Português'):
		uc_language = 1
	else:
		uc_language = 2

	data_ucs['uc'].append({
		'name': restore_name(uc_name),
		'etcs': restore_name(uc_etcs),
		'semester': uc_semester,
		'year': uc_year,
		'goals': restore_name(uc_goals),
		'program': restore_name(uc_program),
		'evaluation_process': restore_name(uc_evaluation),
		'program': restore_name(uc_program),
		'language': uc_language,
		'uc_style': uc_style,
		'uc_optional': uc_optional
		})

#Message console
print('Finish scraping.')
print('Start json file...')

with open('3_ucs.txt', 'w', encoding='utf8') as outfile:  
	json.dump(data_ucs, outfile)

#Message console
print('Finish json file.')