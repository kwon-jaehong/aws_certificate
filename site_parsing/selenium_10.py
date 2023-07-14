from selenium import webdriver
import os
 
browser = webdriver.Chrome()

save_html_dir = "./exam_CLF"


site_str = "https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/"



for i in range(1,99):
    browser.get(site_str+str(i))
    html_data = browser.page_source
    
    f = open(os.path.join(save_html_dir,str(i).zfill(3)+".html"), 'w')
    f.write(html_data)
    f.close()
    