# -*- coding: utf-8 -*-
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

nodes = []

def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    nodes.append(root.data)
    inOrderTraversal(root.right)

def check_binary_search_tree_(root):
    inOrderTraversal(root)
    for i in range(1,len(nodes)):
        if nodes[i] <= nodes[i - 1]:
            return False
    return True
