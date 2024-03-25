import sys
input = sys.stdin.readline

while True :
    arr = input().rstrip('\n')
    if arr == '0':
        break
    r_arr = arr[::-1]
    if int(arr) == int(r_arr) :
        print('yes')
    else:
        print('no')


# str으로 인풋받으면 마지막에 개행문자('\n')이 들어감.
