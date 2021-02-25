import sys
input = sys.stdin.readline
n = int(input())

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = left
        self.right = right

tree = {}
for _ in range(n):
    node, left, right = input().strip().split()
    tmp = Node(data=node)
    tmp.left = left
    tmp.right = right
    tree[node] = tmp

result1 = []
def pre_order(node):
    result1.append(node)
    tmp = tree[node]
    if tmp.left != '.':
        pre_order(tmp.left)
    if tmp.right != '.':
        pre_order(tmp.right)

result2 = []
def in_order(node):
    tmp = tree