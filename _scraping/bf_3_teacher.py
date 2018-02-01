# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: bf_3_teacher.py
# Ultima modificação: 01/02/2018
import requests, json, time
from bs4 import BeautifulSoup
from bot_publications import *

def restore_name(str):
	return " ".join(str.split())

def mSoup(url):
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	return soup;

def mSoup_html(url):
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'html5lib')
	return soup;

#Message console
time_start = time.time()
print('Start scraping...')
mainUrl = "https://ciencia.iscte-iul.pt"
cv = "/cv"
teaching = "/teaching"
publications = "/publications"
other = "/other"
mainteacher = "https://www.iscte-iul.pt/curso/3/licenciatura-engenharia-informatica/docentes"

data_teacher = {}
data_teacher['teacher'] = []
data_teacher['affiliation'] = []
data_teacher['academic'] = []
data_teacher['uc'] = []
data_teacher['publications'] = []
id_teacher = 0

mySoup = mSoup(mainteacher)
teachers = mySoup.find_all('div', attrs={'class':'research-link top-buffer-5'})
for t in teachers:
	teacher_url = t.find('a')['href']
	url = teacher_url

	#Page: CV
	mySoup = mSoup(url)
	id_teacher = id_teacher + 1
	photo_url = mySoup.find('div', attrs={'class':'author-photo'}).find('img')['src']
	name = mySoup.find('div', attrs={'class':'author-name'}).find('div', attrs={'class':'name'}).getText()

	print('Testing: '+restore_name(name))


	authors_contact = mySoup.find('div', attrs={'class':'author-contacts-container'}).find_all('div', attrs={'class':'author-contact'})
	cc=0
	for c in authors_contact:
		phone = c.getText()
		cc=cc+1
		if (cc == 2):
			break

	
	cv_content = mySoup.find('div', attrs={'class':'content-section'}).find_all('div', attrs={'class':'author-profile-item'})
	for cv in cv_content:
		cv_title = cv.find('div', attrs={'class':'title'}).getText()
		cv_resume = cv.find('div', attrs={'class':'content'}).getText()
		if(cv_title== 'Resumo CV'):
			break

	data_teacher['teacher'].append({
		'id_teacher': id_teacher,
		'name': restore_name(name),
		'photo_url': (mainUrl+restore_name(photo_url)),
		'phone': restore_name(phone),
		'resume':restore_name(cv_resume)
		})

	#Affiliation table
	try:
		affiliation_content = mySoup.find('div', attrs={'class':'author-affiliations-content'}).find_all('div', attrs={'class':'author-affiliation'})
		for af in affiliation_content:
			affiliation_type = af.find('span', attrs={'class':'affiliation-type'}).getText()
			affiliation_unit = af.find('span', attrs={'class':'unit-affiliation'}).find('a').getText()
			affiliation_unit_url = af.find('span', attrs={'class':'unit-affiliation'}).find('a')['href']

			data_teacher['affiliation'].append({
				'affiliation_type': restore_name(affiliation_type),
				'affiliation_unit': restore_name(affiliation_unit),
				'affiliation_unit_url': (mainUrl+restore_name(affiliation_unit_url)),
				'id_teacher': id_teacher
				})
	except:
		print('FAIL: affiliation')
		pass

	#Academic table
	try:
		cv_academic_q_table = mySoup.find('div', attrs={'class':'content-section'}).find('table', attrs={'class':'medium whole-border'}).find_all('tr')
		for tr in cv_academic_q_table:
			nTr = tr.find_all('td')
			i=0
			ac_uni = ""
			ac_type = ""
			ac_course = ""
			ac_year = ""
			for td in nTr:
				if(i==0):
					ac_uni = restore_name(td.getText())
				elif(i==1):
					ac_type = restore_name(td.getText())
				elif(i==2):
					ac_course = restore_name(td.getText())
				elif(i==3):
					ac_year = restore_name(td.getText())
				i+=1
			if(ac_uni != ''):
				data_teacher['academic'].append({
					'university': ac_uni,
					'type' : ac_type,
					'course' : ac_course,
					'ac_year' : ac_year,
					'id_teacher': id_teacher
				})
	except:
		print('FAIL: academic')
		pass

	#Page: Teaching	
	try:
		mySoup = mSoup(url+teaching)
		uc_content = mySoup.find('div', attrs={'class':'content-section'}).find('div', attrs={'class':'author-profile-item'}).find('div', attrs={'class':'content'})
		uc_table = uc_content.find('table', attrs={'class':'medium striped whole-border'}).find_all('tr')
		for tr in uc_table:
			nTr = tr.find_all('td')
			i=0
			uc_name = ""
			uc_url = ""
			for td in nTr:
				uc = td.find('a')
				if(i==0):
					uc_name = restore_name(uc.getText())
					uc_url = uc['href']
				else:
					continue
				i+=1
			if(uc_name != ''):
				data_teacher['uc'].append({
					'name': uc_name,
					'url' : uc_url,
					'id_teacher': id_teacher
				})
	except:
		print('FAIL: teaching')
		pass

	#Page: Publications	
	try:
		pub_content = PubScrap.scrap(url+publications, id_teacher,data_teacher['publications'])
	except:
		print('FAIL: publications')
		pass


#Message console
print('Finish scraping.')
time_end = time.time()
print('Scraping time: '+str(((time_end - time_start)/60))+ ' minutos.')

print('Start json file...')
with open('3_teachers.json', 'w', encoding='utf8') as outfile:  
	json.dump(data_teacher, outfile)

#Message console
print('Finish json file.')