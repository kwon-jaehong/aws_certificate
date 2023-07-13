from bs4 import BeautifulSoup
import re
import pandas as pd



# df = pd.DataFrame(columns=['exam_category',"quiz_id",'quiz_title','correct','A','B','C','D','E','F','G','H','I'])
df = pd.read_csv('./quiz.csv')

with open("AWS Certified Cloud Practitioner Exam – Free Exam Q&As, Page 26 _ ExamTopics.html", "r", encoding="utf-8") as file:
    # 파일 내용 읽기
    html_data = file.read()





soup = BeautifulSoup(html_data, "html.parser")


## 퀴즈 10개
div_elements = soup.find_all("div", class_="card exam-question-card")


for div in div_elements:
    
    correct_str = ""
    sentence_dict = {}
    
    ## 퀴즈 아이디
    quiz_id = div.find_all(text=re.compile(r"Question #\d+"))[0].replace("\n","").strip().replace("Question #","")
    # 바디 클래스 가져오기
    quiz_body = div.find("div",class_="card-body question-body")
    
    ## 퀴즈 질문
    quiz_title = quiz_body.find("p",class_="card-text").text.replace("\n","").strip()
    
    
    ## 멀티플 초이스 가져오기
    choices = quiz_body.find("div",class_="question-choices-container").find_all("li",class_=re.compile(r"multi-choice-item*"))
    
    for choice in choices:

        choice_symbol = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[0]
        choice_sentence = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[2:].strip(' ')
        
        sentence_dict[choice_symbol] = choice_sentence
        
        if len(choice.find_all("span",class_="badge badge-success most-voted-answer-badge")) > 0:

            correct_str += choice_symbol
        
        
        
    df.loc[len(df)] = {"exam_category":"examtopics","quiz_id":quiz_id,"quiz_title":quiz_title,"correct":correct_str,"A":sentence_dict.get('A'),"B":sentence_dict.get('B'),"C":sentence_dict.get('C'),"D":sentence_dict.get('D'),"E":sentence_dict.get('E'),"F":sentence_dict.get('F'),"G":sentence_dict.get('G'),"H":sentence_dict.get('H'),"I":sentence_dict.get('I')}
    

df.to_csv('./quiz.csv',index=False)
df2 = df.drop_duplicates(subset=['exam_category',"quiz_id"],keep=False).reset_index(drop=True)
print("temp.csv")