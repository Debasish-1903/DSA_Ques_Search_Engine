import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

s = Service("C:\webdrivers")   

# Intantiate the webdriver
driver = webdriver.Chrome(service = s) 

HEADING_CLASS = ".mr-2.text-label-1"
BODY_CLASS = ".px-5.pt-4"
# path to "./Qdata" -> current folder ke andar Qdata
QDATA_FOLDER = "Qdata"


def get_problem_links():

    arr=[]
    with open("lc_pb_links_clean.txt","r") as file:

        for line in file:
            arr.append(line)


        return arr
        

"""
"os.path.join()" is used to construct a valid path by joining individual path components together.

Here's how os.path.join() works:

1. It takes the first path component as the base directory or path segment.
2. It iteratively appends the remaining components to the base path, separated by the appropriate path separator based on the underlying operating system.
3. It constructs the final path by joining all the components together.

Using os.path.join() helps ensure that your code is portable and works correctly across different platforms. It handles the differences in path separators automatically, making your code more robust and less prone to errors when working with file and directory paths.
"""

# add problem number(acc. to leetcode) & name to "index.txt" in (QDATA_FOLDER = Qdata) folder
def add_problem_name_to_index_file(text):
   # It constructs the path to the index file by joining the QDATA_FOLDER variable (which holds the path to a directory) with the filename "index.txt" using the os.path.join() function.
    index_file_path=os.path.join(QDATA_FOLDER,"index.txt")
    with open(index_file_path,"a") as index_file:
        index_file.write(text+"\n")


# add problem link to "Qindex.txt" in (QDATA_FOLDER = Qdata) folder
def add_pblinks_to_Qindex_file(text):

    index_file_path=os.path.join(QDATA_FOLDER,"Qindex.txt")
    with open(index_file_path,"a",encoding="utf-8",errors="ignore") as Qindex_file:
        Qindex_file.write(text)



def create_file_and_add_problem_text_to_file(file_name,text):
    folder_path=os.path.join(QDATA_FOLDER,file_name)
    os.makedirs(folder_path,exist_ok=True)
    file_path=os.path.join(folder_path,file_name+".txt")
    with open(file_path,"w",encoding="utf-8",errors="ignore")as new_file:
        new_file.write(text)




def get_page_data(url,index):
    try:
        driver.get(url)
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, BODY_CLASS)))
        time.sleep(1)
        heading = driver.find_element(By.CSS_SELECTOR, HEADING_CLASS)
        body = driver.find_element(By.CSS_SELECTOR, BODY_CLASS)
        print(heading.text)

        if (heading.text):
            add_problem_name_to_index_file(heading.text)
            add_pblinks_to_Qindex_file(url)
            create_file_and_add_problem_text_to_file(str(index), body.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False
    
'''index = 2201
arr = get_problem_links()

for link in arr:
    success = get_page_data(link, index)
    if (success):
        index = index+1


driver.quit()'''

index = 1
arr = get_problem_links()
starting_index = 2201

for i in range(starting_index, len(arr)):
    link = arr[i]
    success = get_page_data(link, index)
    if success:
        index += 1

    starting_index += 1

driver.quit()
