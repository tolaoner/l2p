# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:06:10 2019

@author: tolao
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
#def writeHtmlFunc(pagename):
#pagename='https://www.newegg.com/global/de-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1642222&recaptcha=pass'
my_url='https://www.newegg.com/global/de-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1642222&recaptcha=pass'
uClient=urlopen(my_url)#openning up the connection, dowloading the page
page_html=uClient.read()#reading the page
uClient.close#closing the page
page_soup=soup(page_html,'html.parser')#html parsing
#print(page_soup.h1)
containers=page_soup.findAll('div',{'class':'item-container'})#takes all the divs that are created with the item_container class
print(len(containers))
gpu_file=open('GPUS.csv', 'w')
headers='Brand, Name, Price\n'
gpu_file.write(headers)
for container in containers:
    brandDiv=container.find('div',{'class':'item-branding'})
    brand=brandDiv.a.img['title'] #find('a',{'class':'item-brand'})
    #brand_real=brandA.img['title']
    title_container=container.find('a',{'class':'item-title'})
    title=title_container.text
    price_container=container.find('li',{'class':'price-current'})
    price=price_container.text
    price2=price.partition('\n')[2]
    a=len(price2)-5
    price3=price2[1:a]
    price4=price3.strip()
    #print(type(price))
    #print(f'{brand},,{title},,{price4}')
    gpu_file.write(brand+','+title.replace(',','|') +','+ price4.replace(',','.'))# +'\n')
gpu_file.close()
#writeHtmlFunc('https://www.newegg.com/global/de-en/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=1642222&recaptcha=pass')
'''for b in range(17):
    if b==0:
        gpu_file.write(headers)
        c=''
        page='https://www.newegg.com/global/de-en/Desktop-Graphics-Cards/SubCategory/ID-48'+c+'?Tid=1642222'
        writeHtmlFunc(pagename=page)
        #print(page)
    elif b==1:
        continue
    else:
        d='/Page-'+str(b)
        page='https://www.newegg.com/global/de-en/Desktop-Graphics-Cards/SubCategory/ID-48'+d+'?Tid=1642222'
        writeHtmlFunc(pagename=page)
        #print(page)'''



