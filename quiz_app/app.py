from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates

import pandas as pd

df = pd.read_csv('./KO_CLF_quiz_data.csv')
df = df.sample(frac=1).reset_index(drop=True)

app = FastAPI()
templates = Jinja2Templates(directory='templates')


# https://streamls.tistory.com/entry/FastAPI-MySQL-CRUD-1 
# https://snacky.tistory.com/7
    

@app.get('/')
def get_login_form(request: Request):
    print(df.loc[0])
    return templates.TemplateResponse('index.html', 
                            context={'request':request,"data":"do"})


## 퀴즈 번호 받아오고, 답변 받아와야함, 틀렸을때 리다이렉트?

@app.post('/')
def login(username:str=Form(...), password:str=Form(...)):
    return {"username":username, "password":password}