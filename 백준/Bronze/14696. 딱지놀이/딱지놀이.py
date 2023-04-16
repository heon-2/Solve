def battle(A,B) :
    if A.count(4) > B.count(4) :
        print('A')
    elif A.count(4) < B.count(4) :
        print('B')
    elif A.count(4) == B.count(4) :
        if A.count(3) > B.count(3) :
            print('A')
        elif A.count(3) < B.count(3) :
            print('B')
        elif A.count(3) == B.count(3) :
            if A.count(2) > B.count(2) :
                print('A')
            elif A.count(2) < B.count(2) :
                print('B')
            elif A.count(2) == B.count(2) :
                if A.count(1) > B.count(1) :
                    print('A')
                elif A.count(1) < B.count(1) :
                    print('B')
                elif A.count(1) == B.count(1) :
                    print('D')

N = int(input())
for i in range(N) :
    a,*pic_a = map(int,input().split())
    b,*pic_b = map(int,input().split())
    battle(pic_a,pic_b)