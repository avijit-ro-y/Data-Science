#Create linklist and find its length
class Nodee:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
        
def get_lenght(head):
    length=0
    curr=head
    while curr!=None:
        length+=1
        curr=curr.next
    return length
if __name__=="__main__":

    head = Nodee(1)
    head.next = Nodee(3)
    head.next.next = Nodee(1)
    head.next.next.next = Nodee(2)
    head.next.next.next.next = Nodee(1)

    print("Count of nodes is", get_lenght(head))
    
#Given a linklist and add a data infront of a link list
class Nodee:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None

def insert_at_front(head, new_data):

    new_node = Nodee(new_data)
    new_node.next = head
    head=new_node
    return head

def print_list(head):
    curr = head
    while curr !=None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    head = Nodee(2)
    head.next = Nodee(3)
    head.next.next = Nodee(4)
    head.next.next.next = Nodee(5)

    print("Original Linked List:", end="")
    print_list(head)

    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insert_at_front(head, data)
    print_list(head)
    
#Given a linklist and add a data at the end of a link list
class Nodee:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None

def insert_at_end(head, new_data):
    new_node = Nodee(new_data)
    curr=head
    while curr.next !=None:
        curr=curr.next
    curr.next = new_node
    return head

def print_list(head):
    curr = head
    while curr !=None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    head = Nodee(2)
    head.next = Nodee(3)
    head.next.next = Nodee(4)
    head.next.next.next = Nodee(5)

    print("Original Linked List:", end="")
    print_list(head)

    print("After inserting Nodes at the end:", end="")
    data = 1
    head = insert_at_end(head, data)
    print_list(head)
    
#Given a linklist and add a data at K th of a link list
class Nodee:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None

def insert_at_kth_position(head, new_data,k):
    new_node = Nodee(new_data)
    curr=head
    i=0
    while i < k-1:
        i+=1
        curr=curr.next
    new_node.next=curr.next
    curr.next = new_node
    return head

def print_list(head):
    curr = head
    while curr !=None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    head = Nodee(2)
    head.next = Nodee(3)
    head.next.next = Nodee(4)
    head.next.next.next = Nodee(5)

    print("Original Linked List:", end="")
    print_list(head)

    print("After inserting Nodes at kth:", end="")
    data = 1
    k=2
    head = insert_at_kth_position(head, data,k)
    print_list(head)
    