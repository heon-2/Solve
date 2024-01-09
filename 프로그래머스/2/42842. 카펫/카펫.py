def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1) :
        # print(i)
        # 노란색의 약수일 때,
        if yellow % i == 0 :
            h,w = i, yellow // i
            # 전체 사각형의 격자 개수
            rect = (w+2) * (h+2)
            # 감싸고 있는 격자의 개수는 전체 사각형에서 안에 있는 격자 개수
            outlayer = rect - h*w
            if outlayer == brown :
                return [w+2,h+2]
                break
            
