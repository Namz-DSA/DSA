class Node:
    def __init__(self, val, next = None):
        self.next = next
        self.val = val
    
    def __str__(self):
        return str(self.val)

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3


def display(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    
    return ' -> '.join(elements)



def deleteNode(head,target):
    prev = None
    curr = head
    while curr:
        if curr.val == target:
            if prev == None:
                return curr.next
            else:
                prev.next = curr.next
                return head
        
        prev = curr
        curr = curr.next
            
    return head

print(display(head))
head = deleteNode(head,3)
print(display(head))