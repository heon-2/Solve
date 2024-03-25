N = int(input())

tree = dict()

for i in range(N) :
    root,left,right = map(str,input().split())
    tree[root] = [left,right]

# 전위순회
def preorder(x) :
    if x != '.' :
        print(x,end='')
        preorder(tree[x][0])
        preorder(tree[x][1])
preorder('A')
print()

# 중위순회
def inorder(x) :
    if x != '.' :
        inorder(tree[x][0])
        print(x,end='')
        inorder(tree[x][1])
inorder('A')
print()

# 후위순회
def postorder(x) :
    if x != '.' :
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x,end='')
postorder('A')
