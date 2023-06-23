#전위 순회
def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(ch1[node])
        preorder(ch2[node])
# 중위 순회
def inorder(node):
    if node != '.':
        inorder(ch1[node])
        print(node, end='')
        inorder(ch2[node])

# 후위 순회
def postorder(node):
    if node != '.':
        postorder(ch1[node])
        postorder(ch2[node])
        print(node, end='')


n = int(input())
ch1 = {}
ch2 = {}

for _ in range(n):
    p, c1, c2 = input().split()
    ch1[p] = c1
    ch2[p] = c2

preorder('A')
print()
inorder('A')
print()
postorder('A')