import sys
input = sys.stdin.readline
N,C = map(int,input().split())
lst = list(map(int,input().split()))
# 이분 탐색을 위한 정렬
lst.sort()

def binary_search(left,right,x) :
    while left <= right :
        mid = (left+right) // 2
        if lst[mid] == x :
            return 1
        elif lst[mid] < x :
            left = mid + 1
        elif lst[mid] > x :
            right = mid - 1
    return 0

# 1개를 찾을 때 처음에는 in 함수를 사용했었는데,
# 이것도 이진탐색으로 찾아내면 빠르겠다는 것을 늦게 알았음.
if binary_search(0,N-1,C) :
    print(1)
    exit(0)

else :
    flag = 0

    # 2개일 때 찾기 (x,y)
    left,right = 0, N-1
    while left < right :
        summ = lst[left] + lst[right]
        if summ > C :
            right -= 1
        elif summ < C :
            target = C-summ
            if binary_search(left,right,target) :
                if target != lst[left] and target != lst[right] :
                    flag = 1
                    break
            left += 1
        else :
            flag = 1
            break

    print(flag)


