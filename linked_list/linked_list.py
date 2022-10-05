from node import Node 

class LinkedList(object):

    def __init__(self):
        self.head = None 

    def size(self) -> int:
        sz = 0 
        while self.head:
            sz += 1
            self.head = self.head.next
        return sz  
    
    def empty(self) -> bool:
        return self.size() == 0
    
    def value_at(self, index) -> int:
        curr = self.head 
        while index > 0 and curr.next:
            curr = curr.next 
            index -= 1     
        return curr.val 

    def push_front(self,value) -> None:
        tmp = self.head 
        self.head = Node(value)
        self.head.next = tmp 
    
    def pop_front(self) -> int:
        tmp = self.head 
        self.head = self.head.next 
        return tmp.val

    def push_back(self, value) -> None:
        trav = self.head 
        while trav.next:
            trav = trav.next 
        trav.next = value
        return trav

    def pop_back(self) -> int:
        trav = self.head 
        while trav.next.next:
            trav = trav.next 
        tmp = trav.next 
        trav.next = None 
        return tmp.val
    
    def front(self):
        return self.head 

    def back(self):
        trav = self.head 
        while trav.next :
            trav = trav.next 
        return trav 

    def reverse(self):
        prev, curr = None, self.head 
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev
    
    def __str__(self):
        curr = self.head 
        s = ''
        while curr:
            s += str(curr.val) + ' -> '
            curr = curr.next 
        return s


def main():
    ll = LinkedList()
    ll.head = Node(10)
    first = Node(20)
    second = Node(30)
    third = Node(40)

    ll.head.next = first
    first.next = second
    second.next = third
    
    # print(ll.value_at(3))
    
    # ll.push_front(5)
    # print(ll)

    # print(ll.pop_back())
    # print(ll)

    # print(ll.front().val)
    # print(ll.back().val)

    ll.reverse()
    print(ll)


main()

    
