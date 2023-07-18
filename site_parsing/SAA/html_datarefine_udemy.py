from bs4 import BeautifulSoup
import re
import pandas as pd
import os
from tqdm import tqdm

# exam_category,exam_type,quiz_id,en_quiz_title,most_vote,correct,en_A,en_B,en_C,en_D,en_E,ko_quiz_title,ko_A,ko_B,ko_C,ko_D,ko_E,subject,choice_count

df = pd.DataFrame(columns=['exam_category',"exam_type","quiz_id",'en_quiz_title','most_vote',"correct","en_A","en_B","en_C","en_D","en_E","en_F","en_G","ko_quiz_title","ko_A","ko_B","ko_C","ko_D","ko_E","ko_G","subject","choice_count"])


choice_alphabet_list = ['A','B','C','D','E','F','G']
udemy_dir = "./ud"


for i in tqdm(range(1,7)):
    with open(os.path.join(udemy_dir,"Practice Exams _ AWS Certified Solutions Architect Associate _ Udemy_"+str(i)+".html"), "r", encoding="utf-8") as file:
        # 파일 내용 읽기
        html_data = file.read()
    # print("6 Practice Exams _ AWS Certified Cloud Practitioner CLF-C01 _ Udemy_"+str(i)+".html")

    soup = BeautifulSoup(html_data, "html.parser")

    div_elements = soup.find_all("form",class_=re.compile(r"mc-quiz-question--container"))

    for div in div_elements:
        input_row = {}
        correct_list = ""
        # quiz_id = div.find_all("span",string=re.compile(r"질문"))[0].text.replace("질문","").replace(":","").strip()
        input_row['quiz_id'] = ( (i-1)*65)+int(div.find_all("span",string=re.compile(r"질문"))[0].text.replace("질문","").replace(":","").strip())
        input_row['en_quiz_title'] = div.find_all("div",class_=re.compile(r"ud-text-bold mc-quiz-question--question"))[0].text.replace("\n","").strip()
        
        quiz_choices = div.find_all("li",class_=re.compile(r"mc-quiz-question--answer"))
        for j,choice in enumerate(quiz_choices):
            input_row["en_"+choice_alphabet_list[j]]= choice.text.replace("(정답)","").replace("(오답)","").strip()
            if choice.find("div",class_=re.compile(r"mc-quiz-answer--correctness"),string=re.compile(r"정답")) != None:
                correct_list += choice_alphabet_list[j]

        input_row['most_vote'] = correct_list
        input_row['correct'] = correct_list
        input_row['exam_category'] = "udemy"
        input_row['exam_type'] = "CLF-01"

        df.loc[len(df)] = input_row

# df.to_csv('./UDEMY_SAA_quiz_data.csv',index=False)







for i in tqdm(range(1,7)):
    with open(os.path.join(udemy_dir,"연습 시험 _ AWS 공인 솔루션 아키텍트 어소시에이트 _ 유데미_"+str(i)+".html"), "r", encoding="utf-8") as file:
        # 파일 내용 읽기
        html_data = file.read()

    soup = BeautifulSoup(html_data, "html.parser")

    div_elements = soup.find_all("form",class_=re.compile(r"mc-quiz-question--container"))

    for div in div_elements:
        index = ((i-1)*65)+int(div.find_all("span",string=re.compile(r"질문"))[0].text.replace("질문","").replace(":","").strip())-1

        df.loc[index,'ko_quiz_title'] = div.find_all("div",class_=re.compile(r"ud-text-bold mc-quiz-question--question"))[0].text.replace("\n","").strip()
        
        quiz_choices = div.find_all("li",class_=re.compile(r"mc-quiz-question--answer"))
        for j,choice in enumerate(quiz_choices):
            df.loc[index,"ko_"+choice_alphabet_list[j]]= choice.text.replace("(정답)","").replace("(오답)","").strip()



df['subject'] = 0
df.to_csv('./UDEMY_SAA_quiz_data.csv',index=False)


## 데이터 정제 부부분 넣자

print(0)



