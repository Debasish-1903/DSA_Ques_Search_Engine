from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

selenium_service = Service('C:\webdrivers')
driver = webdriver.Chrome(service=selenium_service)


page_URL="https://leetcode.com/problemset/all/?page="

def get_a_tags():
    page_source=driver.page_source
    soup=BeautifulSoup(page_source,'html.parser')

    a_tags=soup.find_all("a")
    pb_links_uc=[]

    for link in a_tags:
        try:
            if "/problem" in link.get("href"):
                pb_links_uc.append(link.get("href"))



        except:pass

    pb_links_uc=list(set(pb_links_uc))  
    return pb_links_uc

def get_all_links(url,total_no_of_pages):

    driver.get(url)   
    time.sleep(10)

    all_links=[]   
    for i in range(1,total_no_of_pages+1):
        all_links+=get_a_tags()

        if i!=total_no_of_pages:
            X_PATH="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/nav/button[10]"
            button=driver.find_element("xpath",X_PATH)
            button.click()
            time.sleep(10)

    all_links=list(set(all_links))   
    return all_links

total_no_of_pages=55
links=[]
links=get_all_links(page_URL,total_no_of_pages) 

with open('lc_pb_links_ucf.txt','a')as f:
    for j in links:
        f.write('https://leetcode.com'+j+'\n')


driver.quit()        
