N = int(input())
word_lst = []
for i in range(N) :
    word_lst.append(input())
word_lst.sort()
word_lst.sort(key=lambda x:len(x), reverse = False)
answer = []
for i in word_lst :
    if i not in answer :
        answer.append(i)

for i in answer :
    print(i)