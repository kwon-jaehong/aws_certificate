from bs4 import BeautifulSoup
import re
import pandas as pd
import os


def None_most_vote(most_vote,correct):
    
    if len(most_vote) == 0:
        most_vote = correct
    
    return most_vote



master_df = pd.DataFrame(columns=['exam_category',"quiz_id",'quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])





df = pd.DataFrame(columns=['exam_category',"quiz_id",'quiz_title','most_vote',"correct",'A','B','C','D','E','F','G','H','I'])
# df = pd.read_csv('./quiz.csv')


html_dir = "./exam_CLF"

for i in range(491,987):
    with open(os.path.join(html_dir,str(i)+".html"), "r", encoding="utf-8") as file:
        # 파일 내용 읽기
        html_data = file.read()





    soup = BeautifulSoup(html_data, "html.parser")

    ## 퀴즈 10개
    div_head = soup.find("div", class_="question-discussion-header")

    ## 퀴즈 아이디
    quiz_id =  div_head.find(text=re.compile(r"Question #")).text.replace("\t","").replace("\n","").replace("Question #:","").strip()


    div_body = soup.find("p", class_="card-text")
    quiz_title = div_body.text.replace("\t","").replace("\n","").strip()
    
    correct_str = ""
    sentence_dict = {}




# df = df.drop_duplicates(subset=['quiz_id'], keep=False).reset_index(drop=True)
# df.to_csv('./quiz_data.csv',index=False)




# soup = BeautifulSoup(html_data, "html.parser")


# ## 퀴즈 10개
# div_head = soup.find("div", class_="question-discussion-header")

# ## 퀴즈 아이디
# quiz_id =  div_head.find(text=re.compile(r"Question #")).text.replace("\t","").replace("\n","").replace("Question #:","").strip()



# # 바디 클래스 가져오기
# div_body = soup.find("p", class_="card-text")
# quiz_title = div_body.text.replace("\t","").replace("\n","").strip()
 
# correct_str = ""
# sentence_dict = {}



# ## 멀티플 초이스 가져오기
# choices = soup.find("div",class_="question-choices-container").find_all("li",class_=re.compile(r"multi-choice-item*"))

# for choice in choices:

#     choice_symbol = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[0]
#     choice_sentence = choice.text.replace("\t","").replace("\n","").replace("Most Voted","").strip(' ')[2:].strip(' ')
    
#     sentence_dict[choice_symbol] = choice_sentence
    
#     if len(choice.find_all("span",class_="badge badge-success most-voted-answer-badge")) > 0:

#         correct_str += choice_symbol
        
        
# print(sentence_dict)
        
# print(0)