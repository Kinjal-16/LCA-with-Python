class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def lca(temp, x1,  x2):
    if(x1>temp.val and x2>temp.val):
        return lca(temp.right,x1,x2)
    elif(x1<temp.val and x2<temp.val):
        return lca(temp.left,x1,x2);
    else:
        return temp.val;










