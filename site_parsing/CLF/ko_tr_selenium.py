from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from tqdm import tqdm
from selenium import webdriver
import os
from selenium.webdriver.common.by import By




en_df = pd.read_csv('./T_CLF_quiz_data.csv')

en_df.rename(columns={"A":"en_A","B":"en_B","C":"en_C","D":"en_D","E":"en_E","F":"en_F","G":"en_G","H":"en_H","I":"en_I"},inplace=True)

browser = webdriver.Chrome()





# https://www.pragnakalp.com/python-tutorial-automate-google-translation-using-selenium/

# https://medium.com/analytics-vidhya/search-automation-in-google-translate-download-translations-with-selenium-3a8c8e136b0e

# https://www.geeksforgeeks.org/how-to-make-a-google-translation-api-using-python/




