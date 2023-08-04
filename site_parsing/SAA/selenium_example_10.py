from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
 
 
browser = webdriver.Chrome()

save_html_dir = "./exam_CLF"


site_str = "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate-saa-c03/view/"




for i in range(1,99):
    browser.get(site_str+str(i))

    
    body = browser.find_element(By.TAG_NAME,'body')
    
    # webdriver.ActionChains(browser).send_keys_to_element(body).send_keys(Keys.SHIFT,Keys.F10).perform()

    body.send_keys(Keys.SHIFT,Keys.F10)
    
    
    import time
    time.sleep(2000)
    
    html_data = browser.page_source
    
    
    f = open(os.path.join(save_html_dir,str(i).zfill(3)+".html"), 'w')
    f.write(html_data)
    f.close()
    