class SinglyLL:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = SinglyLL(1)
node1 = SinglyLL(2)
node2 = SinglyLL(3)
node3 = SinglyLL(7)

Head.next = node1
node1.next = node2
node2.next = node3

print(Head)

#Traverse through list - O(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next

#display linked list - O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)


#search node value - O(n)

def search(head,val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

print(search(Head, 1))
print(search(Head, 4))
print(search(Head, 3))