from googletrans import Translator
import pandas as pd
from tqdm import tqdm
import time

# Translator 클래스 객체 선언 (translator라는 변수명은 마음대로 정해주면 됨)
translator = Translator()



def None_most_vote(most_vote,correct):
    
    if len(most_vote) == 0:
        most_vote = correct
    
    return most_vote

# en_ef = pd.read_csv('./T_CLF_quiz_data.csv')
# en_ef.rename(columns={"A":"en_A","B":"en_B","C":"en_C","D":"en_D","E":"en_E","F":"en_F","G":"en_G","H":"en_H","I":"en_I"},inplace=True)

en_ef = pd.read_csv('./KO_CLF_quiz_data.csv')
for i in tqdm(range(91,96)):


    if str(en_ef.loc[i,'en_quiz_title'])=="<NA>" or str(en_ef.loc[i,'en_quiz_title'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_quiz_title'] = str(translator.translate(str(en_ef.loc[i,'en_quiz_title']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_quiz_title'])
        time.sleep(0.5)
        

    if str(en_ef.loc[i,'en_A'])=="<NA>" or str(en_ef.loc[i,'en_A'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_A'] = str(translator.translate(str(en_ef.loc[i,'en_A']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_A'])
        time.sleep(0.5)

    
    
    if str(en_ef.loc[i,'en_B'])=="<NA>" or str(en_ef.loc[i,'en_B'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_B'] = str(translator.translate(str(en_ef.loc[i,'en_B']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_B'])
        time.sleep(0.5)
        
        
        
    if str(en_ef.loc[i,'en_C'])=="<NA>" or str(en_ef.loc[i,'en_C'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_C'] = str(translator.translate(str(en_ef.loc[i,'en_C']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_C'])
        time.sleep(0.5)
        
        
        
    if str(en_ef.loc[i,'en_D'])=="<NA>" or str(en_ef.loc[i,'en_D'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_D'] = str(translator.translate(str(en_ef.loc[i,'en_D']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_D'])
        time.sleep(0.5)
        
        
        
    if str(en_ef.loc[i,'en_E'])=="<NA>" or str(en_ef.loc[i,'en_E'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_E'] = str(translator.translate(str(en_ef.loc[i,'en_E']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_E'])
        time.sleep(0.5)
    
    
    
    if str(en_ef.loc[i,'en_F'])=="<NA>" or str(en_ef.loc[i,'en_F'])== "nan":
        pass
    else:
        en_ef.loc[i,'ko_F'] = str(translator.translate(str(en_ef.loc[i,'en_F']).strip(), src='en', dest='ko').text)
        print(en_ef.loc[i,'ko_F'])
        time.sleep(0.5)

    

en_ef.to_csv('./KO_CLF_quiz_data.csv',index=False)














