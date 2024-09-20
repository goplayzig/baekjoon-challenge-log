import sys

tree = {}

def add_node(root, left, right):

    if root not in tree:
        tree[root] = [None, None]
    
    if left != '.':
        tree[root][0] = left

    if right != '.':
        tree[root][1] = right
        
def in_order_traversal(root):
    if root:
        in_order_traversal(tree[root][0])
        print(root, end='')
        in_order_traversal(tree[root][1])

def pre_order_traversal(root):
    if root:
        print(root, end='')
        pre_order_traversal(tree[root][0])
        pre_order_traversal(tree[root][1])

def post_order_traversal(root):
    if root:
        post_order_traversal(tree[root][0])
        post_order_traversal(tree[root][1])
        print(root, end='')        

N = int(sys.stdin.readline())
nodeList = []
for i in range(0, N):
    nodes = sys.stdin.readline().split()
    root = nodes[0]
    left = nodes[1]
    right = nodes[2]
    add_node(root, left, right)

pre_order_traversal('A')
print('')
in_order_traversal('A')
print('')
post_order_traversal('A')
