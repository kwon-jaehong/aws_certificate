from selenium import webdriver
 
# browser = webdriver.Firefox()
browser = webdriver.Chrome()
 
browser.get("https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/view/27/")  


temp = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
print(0)



# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# print(0)