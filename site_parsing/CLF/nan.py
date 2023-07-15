
import pandas as pd
from tqdm import tqdm
import time
import numpy as np

en_ef = pd.read_csv('./KO_CLF_quiz_data.csv')

for i in tqdm(range(0,len(en_ef))):
    
    
    if len(str(en_ef.loc[i,'ko_quiz_title']))==1 and str(en_ef.loc[i,'ko_quiz_title'])=="난":
        en_ef.loc[i,'quiz_title'] = np.nan
        
    if len(str(en_ef.loc[i,'ko_A']))==1 and str(en_ef.loc[i,'ko_A'])=="난":
        en_ef.loc[i,'ko_A'] = np.nan

        
    if len(str(en_ef.loc[i,'ko_B']))==1 and str(en_ef.loc[i,'ko_B'])=="난":
        en_ef.loc[i,'ko_B'] = np.nan

        
    if len(str(en_ef.loc[i,'ko_C']))==1 and str(en_ef.loc[i,'ko_C'])=="난":
        en_ef.loc[i,'ko_C'] = np.nan

        
    if len(str(en_ef.loc[i,'ko_D']))==1 and str(en_ef.loc[i,'ko_D'])=="난":
        en_ef.loc[i,'ko_D'] = np.nan

        
    if len(str(en_ef.loc[i,'ko_E']))==1 and str(en_ef.loc[i,'ko_E'])=="난":
        en_ef.loc[i,'ko_E'] = np.nan

        
    if len(str(en_ef.loc[i,'ko_F']))==1 and str(en_ef.loc[i,'ko_F'])=="난":
        en_ef.loc[i,'ko_F'] = np.nan

        
    # if len(str(en_ef.loc[i,'ko_G']))==1 and str(en_ef.loc[i,'ko_G'])=="난":
    #     en_ef.loc[i,'ko_G'] = np.nan

        
    # if len(str(en_ef.loc[i,'ko_H']))==1 and str(en_ef.loc[i,'ko_H'])=="난":
    #     en_ef.loc[i,'H'] = np.nan

        
    # if len(str(en_ef.loc[i,'ko_I']))==1 and str(en_ef.loc[i,'ko_I'])=="난":
    #     en_ef.loc[i,'ko_I'] = np.nan

en_ef.to_csv('./KO_CLF_quiz_data.csv',index=False)
