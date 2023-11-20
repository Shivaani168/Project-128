from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver 

service = Service(executable_path='./chromedriver.exe') 
browser = webdriver.Chrome(service=service) 
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():     
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table=soup.find("table",attrs={"class","wikitable sortable jquery-tablesorter"})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')

    for row in table_rows:
        table_cols=row.find_all('td')
        
        temp_list=[]

        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)
scrape()

stars_data=[]

for i in range(0,len(scraped_data)):
    Star_names=scraped_data[i][1]
    Distance=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]

    required_data=[Star_names,Distance,Mass,Radius]
    stars_data.append(required_data)

# Define Header
headers = ['Star_name','Distance','Mass','Radius']

# Define pandas DataFrame   
star_df_1=pd.DataFrame(stars_data,columns=headers)
# Convert to CSV
star_df_1.to_csv('Scrapped_data.csv',index=True,index_label="id")