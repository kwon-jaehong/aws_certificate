import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Chrome()

lang_code = 'ko'

time_sp = 1

en_df = pd.read_csv('./T_CLF_quiz_data.csv')

en_df.rename(columns={"A":"en_A","B":"en_B","C":"en_C","D":"en_D","E":"en_E"},inplace=True)
en_df = en_df.drop(['F','G','H','I'], axis=1)

# .replace("%","percent")


serch_dict = {"en_quiz_title":"ko_quiz_title","en_A":"ko_A","en_B":"ko_B","en_C":"ko_C","en_D":"ko_D","en_E":"ko_E"}

i = 0
time_sp=1


browser.get("https://translate.google.co.in/?sl=en&tl="+lang_code)


while i < len(en_df):
    tqdm.write(str(i))
    try:
        for key,val in serch_dict.items():
            if str(en_df.loc[i,key])=="<NA>" or str(en_df.loc[i,key])== "nan":
                pass
            else:
                input = en_df.loc[i,key]
                search = browser.find_element(By.CLASS_NAME, "er8xn")
                search.send_keys(input)
                time.sleep(3)
                
                output = browser.find_element(By.CLASS_NAME,'HwtZe').text.replace("\n","").strip()
                if len(output)==0:
                    raise
                en_df.loc[i,val] = output
                
                
                print(en_df.loc[i,val])
                search.send_keys(Keys.CONTROL + "a")
                time.sleep(0.1)
                search.send_keys(Keys.DELETE)
                
                
        en_df.to_csv('./KO_CLF_quiz_data.csv',index=False,encoding='utf-8-sig')
        i+=1    
    except Exception as e:
        print(e)
        browser.get("https://translate.google.co.in/?sl=en&tl="+lang_code)
        time.sleep(1)
        pass
    
    

en_df.to_csv('./KO_CLF_quiz_data.csv',index=False,encoding='utf-8-sig')
























# https://www.pragnakalp.com/python-tutorial-enmate-google-translation-using-selenium/

# https://medium.com/analytics-vidhya/search-enmation-in-google-translate-download-translations-with-selenium-3a8c8e136b0e

# https://www.geeksforgeeks.org/how-to-make-a-google-translation-api-using-python/




