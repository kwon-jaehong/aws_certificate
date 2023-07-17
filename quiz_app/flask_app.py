from flask import Flask, render_template, request,session
import pandas as pd
import random

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = 'mrjaehong'

df_path = "./UDEMY_CLF_quiz_data.csv"
df = pd.read_csv(df_path)

# 여기서 하나의 거대한 DF를 만들어야 함

def quiz_data_refine(p_df_series):
    p_df_series = p_df_series.dropna()
    return dict(p_df_series)


@app.route('/')
def start_test():

    session.modified=True
    session['solution_history'] = {}
    session['current_quiz_count'] = 1
    session['quize_pointer'] = 1
    session['hide_EN_quiz'] = False
    session['hide_EN_choice'] = False
    session['hide_KO_quiz'] = False
    session['hide_KO_choice'] = False
    session['quize_index_list'] = random.sample(range(0,len(df)),len(df))
    quiz_data= quiz_data_refine(df.loc[session['quize_index_list'][session['quize_pointer']]])


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
    
    
    quiz_data= quiz_data_refine(df.loc[session['quize_index_list'][session['quize_pointer']]])
    


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
    

    quiz_data= quiz_data_refine(df.loc[session['quize_index_list'][session['quize_pointer']]])

    return render_template('index.html', quiz_data=quiz_data)












@app.route('/check', methods=['POST'])
def check():
    session.modified=True
    # dict_list = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    quiz_data= quiz_data_refine(df.loc[session['quize_index_list'][session['quize_pointer']]])
    
    
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
                
                
                
    ## 라디오버튼 체크 유지용
    quiz_data['A_C'] = request.form.get('A', False)
    quiz_data['B_C'] = request.form.get('B', False)
    quiz_data['C_C'] = request.form.get('C', False)
    quiz_data['D_C'] = request.form.get('D', False)
    quiz_data['E_C'] = request.form.get('E', False)
    quiz_data['F_C'] = request.form.get('F', False)
    
    
    
    
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
    
    correct_answer_check = 1
    for item in ch_list:
        if item in correct_list:
            correct_answer_check = 2
        else:
            correct_answer_check = 1
            break

    quiz_data['is_correct'] = correct_answer_check
    
    
    ## 히스토리 요걸로 바꿔야함
    # df.loc[session['quize_index_list'][session['quize_pointer']],'quiz_id']
    
    if session['solution_history'].get(str(df.loc[session['quize_index_list'][session['quize_pointer']],'quiz_id']))==None:
        session['solution_history'][str(df.loc[session['quize_index_list'][session['quize_pointer']],'quiz_id'])] = int(quiz_data['is_correct'])
        
    c_count = 0
    for key,val in session['solution_history'].items():
        if val==2:
            c_count +=1
    quiz_data['c_count'] = c_count
    
    
    return render_template('index.html', quiz_data=quiz_data)


if __name__ == '__main__':
    app.run()
