import pandas as pd
from tqdm import tqdm
import numpy as np

def str_lower(en):
    if type(en)!=str:
        return en
    else:
        return en.replace(" ","").lower().replace("aws","").replace("amazon","")

def check_str(en,ch_dict,ko):
    if ch_dict.get(str_lower(en)) != None:
        if ch_dict.get(str_lower(en))!=np.nan:
            return en
        return ch_dict.get(str_lower(en))
    else:
        return ko
    

df = pd.read_csv('./KO_CLF_quiz_data.csv')

df['subject'] = 0
df['subject'] = df['subject'].astype(int) 

df['choice_count'] = 0
df['choice_count'] = df['choice_count'].astype(int) 

df.dropna(subset=['en_quiz_title'],inplace=True)



# index = df.duplicated(['en_quiz_title']).to_list()
# df.duplicated(['en_quiz_title']).value_counts()

## 중복 문제 제거
df = df.drop_duplicates(['en_quiz_title'])






## 선택지 갯수 셈
def count_choice(x):
    list_str = ['A','B','C','D','E','F','G','H','I']
    count = 0
    for temp in list_str:
        if type(x.get('en_'+temp))==str:
            count +=1
    
    return count
df["choice_count"] = df.apply(lambda x : count_choice(x) , axis = 1 )


    



word_df = pd.read_csv('./영어유지.csv')
word_df = word_df.drop_duplicates(['en'])
word_df = word_df.sort_values(by='en')

word_df.to_csv('./영어유지.csv',index=False)




word_df["en"] = word_df.apply(lambda x : str_lower(x["en"]) , axis = 1 )
word_dict = dict(zip(word_df['en'], word_df['replace']))



## 보기만 적용
df["ko_A"] = df.apply(lambda x : check_str(x["en_A"],word_dict,x["ko_A"]) , axis = 1 )
df["ko_B"] = df.apply(lambda x : check_str(x["en_B"],word_dict,x["ko_B"]) , axis = 1 )
df["ko_C"] = df.apply(lambda x : check_str(x["en_C"],word_dict,x["ko_C"]) , axis = 1 )
df["ko_D"] = df.apply(lambda x : check_str(x["en_D"],word_dict,x["ko_D"]) , axis = 1 )
df["ko_E"] = df.apply(lambda x : check_str(x["en_E"],word_dict,x["ko_E"]) , axis = 1 )
df["ko_F"] = df.apply(lambda x : check_str(x["en_F"],word_dict,x["ko_F"]) , axis = 1 )



df.to_csv('./CLF_quiz_data.csv',index=False)

print(0)