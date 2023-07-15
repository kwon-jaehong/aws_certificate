from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import json
from tqdm import tqdm

def None_most_vote(most_vote,correct,q_id):
    
    if str(most_vote)=="nan" and str(correct)=="nan":
        return None
    
    if len(most_vote) == 0:
        most_vote = correct
    
    return most_vote



master_df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'en_quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])






# df = pd.read_csv('./quiz.csv')


html_dir = "./exam_CLF"

for i in tqdm(range(491,987)):
    with open(os.path.join(html_dir,str(i)+".html"), "r", encoding="utf-8") as file:
        # 파일 내용 읽기
        html_data = file.read()

    df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'en_quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])

    correct_str = ""
    most_vote_str = ""

    soup = BeautifulSoup(html_data, "html.parser")

    ## 퀴즈 10개
    div_head = soup.find("div", class_="question-discussion-header")

    ## 퀴즈 아이디
    quiz_id =  div_head.find(string=re.compile(r"Question #")).text
    quiz_id = quiz_id.replace("\t","").replace("\n","").replace("Question #:","").strip()


    div_body = soup.find("p", class_="card-text")
    en_quiz_title = div_body.text.replace("\t","").replace("\n","").strip()

    correct_str = soup.find("span",class_="correct-answer").text
    
    
    sentence_dict = {}


    choices = soup.find("div",class_="question-choices-container").find_all("li",class_=re.compile(r"multi-choice-item*"))

    # most_vote_str =  soup.find("div",class_=re.compile(r"voted-answers-tally*")).find("script").contents[0]
    most_vote_list= json.loads( soup.find("div",class_=re.compile(r"voted-answers-tally*")).find("script").contents[0])
    
    
    temp = soup.find_all("div",class_=re.compile(r"vote-bar progress-bar bg-info*"))
    
    
    
    for item in most_vote_list:
        most_vote_str += item.get('voted_answers')
    
    for choice in choices:

        choice_symbol = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[0]
        choice_sentence = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[2:].strip(' ')
        
        sentence_dict[choice_symbol] = choice_sentence
        
    if quiz_id==str(i):
        df.loc[len(df)] = {"exam_category":"examtopics","exam_type":"CLF-01","quiz_id":quiz_id,"en_quiz_title":en_quiz_title,"most_vote":most_vote_str,"correct":correct_str,"A":sentence_dict.get('A'),"B":sentence_dict.get('B'),"C":sentence_dict.get('C'),"D":sentence_dict.get('D'),"E":sentence_dict.get('E'),"F":sentence_dict.get('F'),"G":sentence_dict.get('G'),"H":sentence_dict.get('H'),"I":sentence_dict.get('I')}
    else:
        df.loc[len(df)] = {"exam_category":"examtopics","exam_type":"CLF-01","quiz_id":str(i)}

    df["most_vote"] = df.apply(lambda x : None_most_vote(x["most_vote"], x["correct"],x["quiz_id"]) , axis = 1 )

    master_df = pd.concat([master_df,df], axis=0).reset_index(drop=True)
            


master_df = master_df.drop_duplicates(subset=['quiz_id'], keep=False).reset_index(drop=True)

null_list = master_df[master_df['en_quiz_title'].isnull()].quiz_id.tolist()

master_df.to_csv('./CLF_quiz_data.csv',index=False)