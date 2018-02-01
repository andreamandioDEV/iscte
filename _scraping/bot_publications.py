# Autor do ficheiro: André Amândio
# Nº aluno: 14900
# UC: Linguagens de Programação 2017/2018
# Ficheiro: bot_publications.py
# Ultima modificação: 01/02/2018
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup 
import time 

def restore_name(str):
	return " ".join(str.split())

# classe PubScrap:
# 	- responsavel por executar pedido ajax para obter publicações dos docentes
class PubScrap():

	def __init__(self):
		return

	def scrap(_url, id_teacher, data_teacher):
		url = r''+_url     

		driver = webdriver.Firefox() 
		driver.get(url) 

		try:
			elem = driver.find_element_by_xpath("//*[@title='Visão Clássica']")
		except:
			driver.close() 
			return
	
		elem.click()

		time.sleep(2) 

		html = BeautifulSoup(driver.page_source, "lxml")

		driver.close() 

		table_html = html.find('div', attrs={'class': 'publications table-responsive'})
		pub_table = table_html.find('table', attrs={'class': 'medium striped whole-border'}).find_all('tr')
		for tr in pub_table:
			nTr = tr.find_all('td')
			i=0
			pub_year = ""
			pub_type = ""
			pub_authors = ""
			pub_title = ""
			pub_local = ""
			for td in nTr:
				if(i==0):
					pub_year = restore_name(td.getText())
				elif(i==1):
					pub_type = restore_name(td.getText())
				elif(i==2):
					pub_authors = restore_name(td.getText())
				elif(i==3):
					pub_title = restore_name(td.getText())
				elif(i==4):
					pub_local = restore_name(td.getText())
				i+=1

			if (pub_year != ''):
				data_teacher.append({
					'pub_year': pub_year,
					'pub_type' : pub_type,
					'pub_authors': pub_authors,
					'pub_title': pub_title,
					'pub_local': pub_local,
					'id_teacher': id_teacher
				})
