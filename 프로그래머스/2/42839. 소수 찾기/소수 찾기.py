# import math
# def solution(numbers):
#     answer = []
#     global num_lst
#     num_lst = []
#     numbers = list(numbers)
#     # 순열 조합 구하기
#     for level in range(1,len(numbers)+1) :
#         used = [False] * (len(numbers)+1)
#         dfs(level,[],numbers,used)
#     num_lst = list(set(num_lst))
#     # 구한 숫자들이 소수인지 판별하기
#     maxx = max(num_lst)
#     isPrimeNumber = [True]*(maxx+1)
#     # 구한 숫자들의 최댓값까지 중 소수인 숫자 걸러내기
#     for i in range(2,int(math.sqrt(maxx))+1) :
#         v = i
#         while True :
#             v += i
#             if v > maxx :
#                 break
#             isPrimeNumber[v] = False
#         # for j in range(2,maxx+1) :
#         #     if i != j and j % i == 0 :
#         #         isPrimeNumber[j] = False
#     for i in num_lst :
#         if i>1 and isPrimeNumber[i] :
#             answer.append(i)
#     return len(answer)
# def dfs(level,path,numbers,used) :
#     if len(path) == level :
#         num = int(''.join(path))
#         num_lst.append(num)
#         return
#     for i in range(len(numbers)) :
#         if not used[i] :
#             used[i] = True
#             dfs(level,path+[numbers[i]],numbers,used)
#             used[i] = False
#     return


primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer