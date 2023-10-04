def solution(t, p):
    len_p=len(p)
    
    temp_list = []
    
    for i in range(0,len(t)-len_p+1):
        temp_list.append(int(t[i:i+len_p]))    
    
    
    answer = 0
    for i in range(0,len(temp_list)):
        if temp_list[i] <= int(p):
            answer+=1
            
    return answer


solution("500220839878","7")