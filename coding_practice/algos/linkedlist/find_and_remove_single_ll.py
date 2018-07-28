class Node:
    def __init__(self, v, n):
        self.val = v
        self.next = n
    
def remove_node(head, v):
    if head is None:
        return None
    cur = head
    prev = None
    while(cur is not None):
        if cur.val == v:
            break
        else:
            prev = cur
            cur = cur.next
    if prev is None:
        head = head.next
    else:
        prev.next = cur.next

    return head

def print_list(head):
    cur = head
    while(cur is not None):
        print cur.val
        cur = cur.next

if __name__ == '__main__':
    head = Node(1,None)
    head.next = Node(2, None)
    head.next.next = Node(3, None)
    print_list(head)
    #head = remove_node(head, 1)
    #head = remove_node(None, 1)
    print 'After removing!!'
    print_list(head)
