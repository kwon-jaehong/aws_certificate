from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
import re
from bs4 import BeautifulSoup

save_html_dir = "./exam_CLF"

# browser = webdriver.Firefox()
browser = webdriver.Chrome()
# query_base = "Exam AWS Certified Cloud Practitioner topic 1 question 986 discussion"
query_base = 'Exam AWS Certified Cloud Practitioner topic 1 question "'


pattern = r'^https://www.examtopics.com/'


search_list = ['870', '873', '876', '878', '879', '889', '896', '897', '898', '904', '905', '921', '925', '932', '956', '957', '975', '976']
except_list = []


for i in search_list:
    
    # if os.path.exists(os.path.join(save_html_dir,str(i).zfill(3)+".html")) or i in except_list:
    #     pass
    if i in except_list:
        pass
    else:
        
        query_text = query_base + str(i) + '" discussion'
        quiz_number_pattern = str(i)





        browser.get("https://www.google.com")
        time.sleep(0.5) ## 0.5초
        
        
        element = browser.find_element("name", "q") #검색창 html의 name이 'q'여서 q다
        element.send_keys(query_text)               #검색 단어를 입력한다
        element.submit()                 

        time.sleep(0.5)
        
        
        html_data = browser.page_source
        soup = BeautifulSoup(html_data, "html.parser")
        
        
        example_url = ""
        href_list = soup.find_all('a', href=True) 
        for href in href_list:
            if re.match(pattern, href['href']) :
                print("매칭 맞음:",href['href'],str(i))
                # if re.search(quiz_number_pattern, href['href']):
                    # print("숫자 맞음:",href['href'])
                if re.search(quiz_number_pattern, href['href']):
                    example_url = href['href']
                # print(href['href'])
                    break
        
        if len(example_url)==0:
            pass
        else:
            browser.get(example_url)
            time.sleep(0.5)
            html_data = browser.page_source
            f = open(os.path.join(save_html_dir,str(i).zfill(3)+".html"), 'w')
            f.write(html_data)
            f.close()


        