# Given a link list ,remove the kth node from the end

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head==None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next !=None:
            temp = temp.next
        temp.next = Node(data)

    def print_list(self):
        temp = self.head
        while temp !=None:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")
        
    def get_length(self):
        temp, length = self.head, 0
        while temp:
            length += 1
            temp = temp.next
        return length        
        

    def deleteNthNodeFromEnd(self, n):
        length_ = self.get_length()
        nodeFromBeginning = length_ - n + 1

        prev = None
        temp = self.head
        for _ in range(1, nodeFromBeginning):
            prev = temp
            temp = temp.next

        if prev is None:
            self.head = self.head.next  # Deleting the first node
        else:
            prev.next = prev.next.next

ll1 = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll1.append(val)

k = int(input("Enter the position (k) from the end to remove: "))
ll1.deleteNthNodeFromEnd(k)

print("Linked List after Deletion:")
ll1.print_list()



#Determine if the linklist has a cycle
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head==None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next !=None:
            temp = temp.next
        temp.next = Node(data)

    def has_cycle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


ll1 = LinkedList()
for val in [1, 3, 4, 3]:
    ll1.append(val)
    
ll1.head.next.next.next = ll1.head.next  # Manually creating a cycle

if ll1.has_cycle():
    print("The linked list contains a cycle.")
else:
    print("The linked list does not contain a cycle.")


# Pelindrome Linklist
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head==None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next !=None:
            temp = temp.next
        temp.next = Node(data)

    def is_palindrome(self):

        # Step 1: Find middle (slow will point to middle)
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare first and second halves
        first, second = self.head, prev  # prev is the new head of reversed half
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next

        return True


ll1 = LinkedList()
for val in [1, 2, 3, 2, 1]:
    ll1.append(val)

if ll1.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
