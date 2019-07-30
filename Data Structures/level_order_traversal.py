# -*- coding: utf-8 -*-
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def height(root):
    if root is None:
        return 0

    ldepth = height(root.left)
    rdepth = height(root.right)

    if (ldepth > rdepth):
        return ldepth + 1 
    
    else:
        return rdepth + 1

def levelOrder(root):
    #Write your code here
    h = height(root)
    for d in range(1, h+1):
        givenLevel(root, d)

def givenLevel(root, level):
    if root is None:
        return
    
    if level == 1:
        print(root.info, end = " ")

    elif level > 1:
        givenLevel(root.left, level - 1)
        givenLevel(root.right, level - 1)




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)

