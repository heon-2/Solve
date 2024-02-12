def solution(A,B):
    # 제일 작은 값과 제일 큰 값을 곱해야 최솟값.
    A.sort()
    B.sort(reverse=True)
    answer = 0
    length = min(len(A),len(B))
    for i in range(length) :
        answer += A[i] * B[i]
        
    return answer