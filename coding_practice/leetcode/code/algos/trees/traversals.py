class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def pre_order(root):
    if root is None:
        return None
    print root.data,
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root is None:
        return None
    in_order(root.left)
    print root.data,
    in_order(root.right)

    
def post_order(root):
    if root is None:
        return None
    post_order(root.left)
    post_order(root.right)
    print root.data,


# create nodes
root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

# setup children
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

pre_order(root)
print ''
in_order(root)
print ''
post_order(root)