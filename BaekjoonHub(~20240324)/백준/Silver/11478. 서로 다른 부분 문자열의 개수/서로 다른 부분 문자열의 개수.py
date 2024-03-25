S = input()
ans = set()
leng = 0
while True :
    leng += 1
    if leng > len(S) :
        break
    for i in range(len(S)-leng+1) :
        ans.add(S[i:i+leng])
print(len(ans))
