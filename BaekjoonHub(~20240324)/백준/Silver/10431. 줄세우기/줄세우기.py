T = int(input())
for _ in range(1,T+1) :
    tc,*student = list(map(int,input().split()))
    line = [student[0]]
    step = 0
    for i in range(1,len(student)) :
        if student[i] > max(line) :
            line.append(student[i])
        else :
            for j in range(len(line)) :
                if student[i] > line[j] :
                    continue
                elif student[i] < line[j] :
                    step += len(line)-j
                    line.insert(j,student[i])
                    break
    print(tc,step)