class Node():
    def __init__(self, v):
        self.val = v
        self.next = None

    def get_next():
        return self.next

def merge_lists(l1, l2):
    head = Node(None)
    prev = head
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1:
        prev.next = l1
    else:
        prev.next = l2
        
    return head.next

def print_ll(head):
    cur = head
    while cur is not None:
        print cur.val
        cur = cur.next

if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(3)
    l2 = Node(2)
    l3 = merge_lists(l1,l2)
    print_ll(l3)