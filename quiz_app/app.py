from fastapi import FastAPI, Request,Form,Response
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

import pandas as pd
import numpy as np

global df
df = pd.read_csv('./CLF_quiz_data.csv')


## 여기서 하나의 거대한 DF를 만들어야함


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="sadkjioazxczxcskdio")
templates = Jinja2Templates(directory='templates')


# https://streamls.tistory.com/entry/FastAPI-MySQL-CRUD-1 
# https://snacky.tistory.com/7

async def quiz_data_refine(p_df_series):
    p_df_series = p_df_series.dropna()      
    return dict(p_df_series)




global quize_pointer
global current_quiz_count
global solution_history
global quize_index_list

quize_pointer = 0
current_quiz_count = 0
solution_history = []
mdf = df.sample(frac=1).reset_index(drop=True)
quize_index_list = mdf['quiz_id'].to_list()

@app.get('/')
async def start_test(request: Request):
    
    



    request.session["Hide_EN_quiz"] = False
    request.session["Hide_EN_choice"] = False
    request.session["Hide_KO_quiz"] = False
    request.session["Hide_KO_choice"] = False

    request.session["Hide_KO_choice"] = mdf['quiz_id'].to_list()

    
    quiz_data = await quiz_data_refine(mdf.loc[quize_pointer])
    
    print(quiz_data)
    return templates.TemplateResponse('index.html', 
                            context={'request':request,"quiz_data":quiz_data})

#     request.session.pop("name", None)
#  http://0.0.0.0:8000 


## 퀴즈 번호 받아오고, 답변 받아와야함
@app.post('/')
# async def refresh_display(request: Request,ch1: bool = Form(False),ch2: bool = Form(False)):
async def refresh_display(request: Request):
    
    global current_quiz_count
    global quize_pointer
    global quize_index_list

    
    current_quiz_count +=1
    quize_pointer += 1
    quize_pointer = quize_pointer % len(df)
    
    quiz_data = await quiz_data_refine(mdf.loc[quize_pointer])



    return templates.TemplateResponse('index.html', 
                            context={'request':request,"quiz_data":quiz_data})
    
# 결과 65개 몇퍼센트 맞았나
# 보기 섞기 기능도 넣어야됨