#Sachin Sharma
#9999794754

import scrapy
import requests
import bs4
import mysql.connector


res=requests.get("https://dmoz-odp.org")

soup=bs4.BeautifulSoup(res.text,'html.parser')

page1_links = []

for link in soup.find_all('a',href=True):

	page1_links.append(link['href'])


final = []
social_list=[]
for link in range(len(page1_links)):
	if page1_links[link].startswith('h')==True:

	        
	    social_list.append(page1_links[link])
	elif page1_links[link].startswith('http')==False:
	    final.append(page1_links[link])

final.remove('/')

new_finals = []
	    
for j in range(len(final)):

	if final[j].startswith('/') and final[j].endswith('/'):

	    n = 'https://dmoz-odp.org' + final[j]

	    new_finals.append(n)

for m in range(len(final)):

	if final[m].endswith('.html'):

	  	l = 'https://dmoz-odp.org' + final[m]

	  	new_finals.append(l)





links_list=new_finals+ social_list



conn= mysql.connector.connect(host='localhost',user='root',passwd='atgworld',database = 'Sachin')
mycursor=conn.cursor()

mycursor.execute("""DROP TABLE IF EXISTS links_tb2""")
mycursor.execute("CREATE TABLE links_tb2(links VARCHAR(300))")




query = "INSERT INTO links_tb2 (links) VALUES (%s)"
mycursor.executemany(query, [(list_item, ) for list_item in links_list])

conn.commit()







