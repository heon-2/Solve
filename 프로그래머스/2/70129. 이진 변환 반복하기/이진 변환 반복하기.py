def solution(s):
    answer = []
    zero,translation = 0,0 
    while True :
        if s == "1" :
            return [translation,zero]
        one = 0
        s = list(s)
        for i in s :
            if i == '0' :
                zero += 1
            else :
                one += 1
        s = str(bin(one)[2:])
        translation += 1
