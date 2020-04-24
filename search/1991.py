"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
"""

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def pre_order(node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

tree = {}
for i in range(int(input())):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])