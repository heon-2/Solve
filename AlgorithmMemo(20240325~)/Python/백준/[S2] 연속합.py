n = int(input())
numbers = list(map(int,input().split()))
max_number = -10e9
start,end = 0,0

while start == len(numbers) and end == len(numbers) :
    summ = sum(numbers[start:end+1])
    if summ > max_number :
        max_number = summ
        end += 1
