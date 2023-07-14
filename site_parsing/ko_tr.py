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

en_ef = pd.read_csv('./KO_CLF_quiz_data.csv')

# en_ef['A']=en_ef['A'].astype('string')
# en_ef['B']=en_ef['B'].astype('string')
# en_ef['C']=en_ef['C'].astype('string')
# en_ef['D']=en_ef['D'].astype('string')
# en_ef['E']=en_ef['E'].astype('string')
# en_ef['F']=en_ef['F'].astype('string')
# en_ef['G']=en_ef['G'].astype('string')
# en_ef['H']=en_ef['H'].astype('string')
# en_ef['I']=en_ef['I'].astype('string')

for i in tqdm(range(0,313)):


    if str(en_ef.loc[i,'quiz_title'])!="<NA>":
        en_ef.loc[i,'quiz_title'] = str(translator.translate(str(en_ef.loc[i,'quiz_title']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    time.sleep(0.5)
    if str(en_ef.loc[i,'A'])!="<NA>":
        en_ef.loc[i,'A'] = str(translator.translate(str(en_ef.loc[i,'A']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    time.sleep(0.5)
    if str(en_ef.loc[i,'B'])!="<NA>":
        en_ef.loc[i,'B'] = str(translator.translate(str(en_ef.loc[i,'B']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'C'])!="<NA>":
        en_ef.loc[i,'C'] = str(translator.translate(str(en_ef.loc[i,'C']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'D'])!="<NA>":
        en_ef.loc[i,'D'] = str(translator.translate(str(en_ef.loc[i,'D']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'E'])!="<NA>":
        en_ef.loc[i,'E'] = str(translator.translate(str(en_ef.loc[i,'E']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'F'])!="<NA>":
        en_ef.loc[i,'F'] = str(translator.translate(str(en_ef.loc[i,'F']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'G'])!="<NA>":
        en_ef.loc[i,'G'] = str(translator.translate(str(en_ef.loc[i,'G']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'H'])!="<NA>":
        en_ef.loc[i,'H'] = str(translator.translate(str(en_ef.loc[i,'H']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
        
    if str(en_ef.loc[i,'I'])!="<NA>":
        en_ef.loc[i,'I'] = str(translator.translate(str(en_ef.loc[i,'I']).strip(), src='en', dest='ko').text)
        time.sleep(0.5)
    
    

en_ef.to_csv('./KO_CLF_quiz_data.csv',index=False)














