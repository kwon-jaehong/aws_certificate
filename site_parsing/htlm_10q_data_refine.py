from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from tqdm import tqdm

def None_most_vote(most_vote,correct):
    
    if len(most_vote) == 0:
        most_vote = correct
    
    return most_vote



master_df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])


# df = pd.read_csv('./quiz.csv')


html_dir = "./exam_CLF"





for i in tqdm(range(1,50)):
    df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])

    with open(os.path.join(html_dir,str(i).zfill(3)+".html"), "r", encoding="utf-8") as file:
        # 파일 내용 읽기
        html_data = file.read()


    soup = BeautifulSoup(html_data, "html.parser")


    ## 퀴즈 10개
    div_elements = soup.find_all("div", class_="card exam-question-card")


    for div in div_elements:
        
        most_vote_str = ""
        correct_str =""
        
        sentence_dict = {}
        
        ## 퀴즈 아이디
        quiz_id = div.find_all(text=re.compile(r"Question #\d+"))[0].replace("\n","").strip().replace("Question #","")
        # 바디 클래스 가져오기
        quiz_body = div.find("div",class_="card-body question-body")
        
        ## 퀴즈 질문
        quiz_title = quiz_body.find("p",class_="card-text").text.replace("\n","").strip()
        
        
        ## example 사이트 공식 정답
        correct_str = quiz_body.find("span",class_="correct-answer").text
        
        
        ## 멀티플 초이스 가져오기
        choices = quiz_body.find("div",class_="question-choices-container").find_all("li",class_=re.compile(r"multi-choice-item*"))
        
        
        
        
        for choice in choices:

            choice_symbol = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[0]
            choice_sentence = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[2:].strip(' ')
            
            sentence_dict[choice_symbol] = choice_sentence
            
            if len(choice.find_all("span",class_="badge badge-success most-voted-answer-badge")) > 0:
                most_vote_str += choice_symbol
            
            
        df.loc[len(df)] = {"exam_category":"examtopics","exam_type":"CLF-01","quiz_id":quiz_id,"quiz_title":quiz_title,"most_vote":most_vote_str,"correct":correct_str,"A":sentence_dict.get('A'),"B":sentence_dict.get('B'),"C":sentence_dict.get('C'),"D":sentence_dict.get('D'),"E":sentence_dict.get('E'),"F":sentence_dict.get('F'),"G":sentence_dict.get('G'),"H":sentence_dict.get('H'),"I":sentence_dict.get('I')}

    df["most_vote"] = df.apply(lambda x : None_most_vote(x["most_vote"], x["correct"]) , axis = 1 )




    master_df = pd.concat([master_df,df], axis=0).reset_index(drop=True)
    
    
master_df2 = pd.read_csv('./CLF_quiz_data.csv')

master_df = pd.concat([master_df,master_df2], axis=0).reset_index(drop=True)


master_df = master_df.astype({'quiz_id':'int'})
master_df.sort_values(by=['quiz_id'])
master_df = master_df.drop_duplicates(subset=['quiz_id'], keep=False).reset_index(drop=True)



master_df.to_csv('./T_CLF_quiz_data.csv',index=False)


