from googletrans import Translator
import pandas as pd
from tqdm import tqdm


# Translator 클래스 객체 선언 (translator라는 변수명은 마음대로 정해주면 됨)
translator = Translator(timeout=80)



master_df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])


def None_most_vote(most_vote,correct):
    
    if len(most_vote) == 0:
        most_vote = correct
    
    return most_vote

en_ef = pd.read_csv('./T_CLF_quiz_data.csv')

for i in tqdm(range(0,len(en_ef))):

    
    if str(en_ef.loc[i,'quiz_title'])!="nan":
        en_ef.loc[i,'quiz_title'] = translator.translate(en_ef.loc[i,'quiz_title'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'A'])!="nan":
        en_ef.loc[i,'A'] = translator.translate(en_ef.loc[i,'A'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'B'])!="nan":
        en_ef.loc[i,'B'] = translator.translate(en_ef.loc[i,'B'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'C'])!="nan":
        en_ef.loc[i,'C'] = translator.translate(en_ef.loc[i,'C'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'D'])!="nan":
        en_ef.loc[i,'D'] = translator.translate(en_ef.loc[i,'D'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'E'])!="nan":
        en_ef.loc[i,'E'] = translator.translate(en_ef.loc[i,'E'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'F'])!="nan":
        en_ef.loc[i,'F'] = translator.translate(en_ef.loc[i,'F'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'G'])!="nan":
        en_ef.loc[i,'G'] = translator.translate(en_ef.loc[i,'G'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'H'])!="nan":
        en_ef.loc[i,'H'] = translator.translate(en_ef.loc[i,'H'], src='en', dest='ko').text
        
    if str(en_ef.loc[i,'I'])!="nan":
        en_ef.loc[i,'I'] = translator.translate(en_ef.loc[i,'I'], src='en', dest='ko').text
    
    

en_ef.to_csv('./KO_CLF_quiz_data.csv',index=False)














