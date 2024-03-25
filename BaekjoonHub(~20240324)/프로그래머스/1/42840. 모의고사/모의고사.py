def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt_one,cnt_two,cnt_three = -1,-1,-1
    answer = [0,0,0]
    for i in range(len(answers)) :
        cnt_one += 1
        cnt_two += 1
        cnt_three += 1
        cnt_one %= 5
        cnt_two %= 8
        cnt_three %= 10
        if answers[i] == one[cnt_one] :
            answer[0] += 1
        if answers[i] == two[cnt_two] :
            answer[1] += 1
        if answers[i] == three[cnt_three] :
            answer[2] += 1
    maxx = max(answer)
    final = []
    for i in range(3) :
        if answer[i] == maxx :
            final.append(i+1)
    final.sort()
    
        
    
    return final