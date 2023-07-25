from flask import Flask, render_template, request,session
import pandas as pd
import random





app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = 'mrjaehong'

df_path = "./UDEMY_SAA_quiz_data2.csv"
df = pd.read_csv(df_path)


delet_list = pd.read_csv('./UDEMY_SAA_quiz_data2_correct.csv')['맞춘id'].to_list()
## 아는 문제 삭제
df = df[~df['quiz_id'].isin(delet_list)]

## 답 섞기
def shuffle_choice(p_df_series):
    choice_list = []
    
    str_list = ['A','B','C','D','E','F','G','H','I']
    correct_list = list(p_df_series.get('most_vote'))
    correct_str = ""
    
    for i in str_list:
        if p_df_series.get('en_'+i)!=None:
            choice_list.append([i,p_df_series.get('en_'+i),p_df_series.get('ko_'+i),i in correct_list])
    
    
    shuffle_choice_list = random.sample(list(range(0,len(choice_list))), len(choice_list))
    
    for i,item_index in enumerate(shuffle_choice_list):
        p_df_series['en_'+str_list[i]] = choice_list[item_index][1]
        p_df_series['ko_'+str_list[i]] = choice_list[item_index][2]
        if choice_list[item_index][3] == True:
            correct_str += str_list[i]

    p_df_series['most_vote'] = correct_str
    # print(choice_list)
    return p_df_series

def quiz_data_refine(p_df_series):
    p_df_series = p_df_series.dropna()
    
    ## 답 바꾸기
    p_df_series = shuffle_choice(p_df_series)
    
    return dict(p_df_series)


@app.route('/')
def start_test():

    session.modified=True
    session['solution_history'] = {}
    session['current_quiz_count'] = 0
    session['quize_pointer'] = 0
    session['hide_EN_quiz'] = False
    session['hide_EN_choice'] = False
    session['hide_KO_quiz'] = False
    session['hide_KO_choice'] = False
    
    q_list = df['quiz_id'].tolist()
    
    ## 퀴즈 섞기
    random.shuffle(q_list)
    
    session['quize_index_list'] = q_list
    
    global quiz_data
    quiz_data= quiz_data_refine(df[df['quiz_id']==q_list[session['quize_pointer']]].iloc[0])


    return render_template('index.html',quiz_data=quiz_data)


# 퀴즈 번호 받아오고, 답변 받아와야 함
@app.route('/next', methods=['POST'])
def next():
    session.modified=True
    session['current_quiz_count'] += 1
    session['quize_pointer'] += 1
    session['quize_pointer'] = session['quize_pointer'] % len(df)
    


    request.form.get('A', False)
    request.form.get('B', False)
    request.form.get('C', False)
    request.form.get('D', False)
    request.form.get('E', False)
    request.form.get('F', False)
    request.form.get('G', False)
    
    # df[df['quiz_id']==q_list[session['quize_pointer']]].iloc[0]
    global quiz_data
    quiz_data= quiz_data_refine(df[df['quiz_id']==session['quize_index_list'][session['quize_pointer']]].iloc[0])
    


    return render_template('index.html', quiz_data=quiz_data)




@app.route('/previous', methods=['POST'])
def previous():
    session.modified=True
    # session['current_quiz_count'] -= 1
    session['quize_pointer'] -= 1
    session['quize_pointer'] = session['quize_pointer'] % len(df)
    
    request.form.get('A', False)
    request.form.get('B', False)
    request.form.get('C', False)
    request.form.get('D', False)
    request.form.get('E', False)
    request.form.get('F', False)
    request.form.get('G', False)
    
    global quiz_data
    quiz_data= quiz_data_refine(df[df['quiz_id']==session['quize_index_list'][session['quize_pointer']]].iloc[0])

    return render_template('index.html', quiz_data=quiz_data)












@app.route('/check', methods=['POST'])
def check():
    session.modified=True
    # dict_list = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    global quiz_data
    # quiz_data= quiz_data_refine(df[df['quiz_id']==session['quize_index_list'][session['quize_pointer']]].iloc[0])
    
    
    ## 정답이 quiz_data['most_vote']안에 있어야함
    correct_list = list(set(list(quiz_data['most_vote'])))
    
    ch_list = []
    if bool(request.form.get('A', False))==True:
        ch_list.append('A')
    if bool(request.form.get('B', False))==True:
        ch_list.append('B')
    if bool(request.form.get('C', False))==True:
        ch_list.append('C')
    if bool(request.form.get('D', False))==True:
        ch_list.append('D')
    if bool(request.form.get('E', False))==True:
        ch_list.append('E')
    if bool(request.form.get('F', False))==True:
        ch_list.append('F')
    if bool(request.form.get('F', False))==True:
        ch_list.append('G')
                
                
                
    ## 라디오버튼 체크 유지용
    quiz_data['A_C'] = request.form.get('A', False)
    quiz_data['B_C'] = request.form.get('B', False)
    quiz_data['C_C'] = request.form.get('C', False)
    quiz_data['D_C'] = request.form.get('D', False)
    quiz_data['E_C'] = request.form.get('E', False)
    quiz_data['F_C'] = request.form.get('F', False)
    quiz_data['G_C'] = request.form.get('G', False)
    
    
    
    
    subject = request.form.get('subject', -1)
    if int(subject)==-1 or int(subject)==0:
        pass
    else:
        #서브젝트 csv 저장해야됨
        quiz_data['subject']= subject
        df.loc[session['quize_index_list'][session['quize_pointer']],'subject'] = subject
        df.to_csv(df_path,index=False)
        pass
    
    
    # 퍼센트 및 넥스트시 
    
    correct_answer_check = 1 # 틀림 1 맞음 2
    for item in ch_list:
        if item in correct_list:
            correct_answer_check = 2
        else:
            correct_answer_check = 1 #하나라도 틀리면 틀림
            break

    quiz_data['is_correct'] = correct_answer_check
    
    

    
    if session['solution_history'].get(str(session['quize_index_list'][session['quize_pointer']]))==None:
        session['solution_history'][str(session['quize_index_list'][session['quize_pointer']])] = int(quiz_data['is_correct'])
        
    c_count = 0
    for key,val in session['solution_history'].items():
        if val==2:
            c_count +=1
    quiz_data['c_count'] = c_count
    
    
    return render_template('index.html', quiz_data=quiz_data)


if __name__ == '__main__':
    app.run()
