def solution(sizes):
    for i in sizes :
        i.sort(reverse=True)
    sizes = sorted(sizes,key = lambda x:(x[0]),reverse=True)
    max1 = sizes[0][0]
    max2 = 0
    for i in sizes :
        max2 = max(i[1],max2)
    answer = max1 * max2
    return answer