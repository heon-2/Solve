# 배열에 들어갈 숫자 개수
N = int(input())
# 배열 만들기
arr = list(map(int,input().split()))
# 이분 탐색 사용을 위해 오름차순 정렬
arr.sort()

# M개의 탐색할 숫자와 리스트 입력받기
F = int(input())
find = list(map(int,input().split()))

# 이분 탐색을 위한 함수 
def binary_search(left,right,x) :
    # 존재하는지 찾기 위해 flag 세워두기
    flag = False
    
    # 왼쪽값이 오른쪽 값보다 작거나 같을 동안
    while left <= right :
        # 중간 값은 왼쪽과 오른쪽의 중간
        mid = (left+right)//2
        # 만약 중간값이 찾는 값과 동일하다면,flag = True로 바꾸고 break
        if arr[mid] == x :
            flag = True
            break
        # 그렇지 않은 경우 만약 중간값이 찾는 값보다 크다면,
        # 중간값을 기준으로 왼쪽만 탐색하면 됨.
        elif arr[mid] > x :
            right = mid-1
        # 중간값이 찾는값보다 작다면
        # 중간값을 기준으로 오른쪽만 탐색하면 됨.
        elif arr[mid] < x :
            left = mid+1
    return flag
# 찾고자 하는 각각의 숫자에 대해 함수에 입력하고
for i in find :
    # 만약 flag가 True면 찾고자 하는 숫자를 찾은 것이므로 1출력
    if binary_search(0,N-1,i) :
        print(1)
    # flag가 False면 못 찾은 것이므로 0을출력함.
    else :
        print(0)
