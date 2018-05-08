class Node():
    def __init__(self, v):
        self.val = v
        self.next = None

    def get_next():
        return self.next

def print_ll(head):
    cur = head
    while cur is not None:
        print cur.val
        cur = cur.next

if __name__=='__main__':
    head = Node(1)
    head.next = Node(2)
    print_ll(head)
