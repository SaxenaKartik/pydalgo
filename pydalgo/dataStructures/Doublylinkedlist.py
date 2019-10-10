
# Implementation of Doubly Linked list 
# Class Node: It creates node which is used by Class DoublyLinkedList
#
# node = Node() is not a member of doublylinkedlist class just because we have to create multiple Node instance per one
# doublyLinkedList. Node instance is created only when user enter a data


# 3 pointers are declared 1. head: points to first node always
# for doubly linked list  2. tail: points to last node always
# with tail pointer       3. current_node: varies position as per requirements


# 2 pointers are declared 1. head: points to first node always
# for doubly linked list  2. current_node: varies position as per requirements
# without tail pointer    



class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data 

class DoublyLinkedList:

    def __init__(self,head=None):
        self.head = head

    def insert_start(self, data):
    # 1 & 2: Allocate the Node & Put in the data 
        new_node = Node(data = data) 
      
        # 3. Make next of new node as head and previous as NULL 
        new_node.next = self.head 
        new_node.prev = None
      
        # 4. change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new_node 
      
        # 5. move the head to point to the new node 
        self.head = new_node  

    def insert_after(self, prev_node, data):
        # 1. check if the given prev_node is NULL 
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
  
        #2. allocate node  & 3. put in the data 
        new_node = Node(data = data) 
  
        # 4. Make next of new node as next of prev_node 
        new_node.next = prev_node.next
  
        # 5. Make the next of prev_node as new_node  
        prev_node.next = new_node 
  
        # 6. Make prev_node as previous of new_node 
        new_node.prev = prev_node 
  
        # 7. Change previous of new_node's next node */ 
        if new_node.next is not None: 
            new_node.next.prev = new_node 

    # Add a node at the end of the DLL 
    def insert_end(self, data): 
      
        # 1. allocate node 2. put in the data 
        new_node = Node(data = data) 
        last = self.head 
  
        # 3. This new node is going to be the  
        # last node, so make next of it as NULL 
        new_node.next = None
  
        # 4. If the Linked List is empty, then 
        #  make the new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node  
        while (last.next is not None): 
            last = last.next
  
        # 6. Change the next of last node  
        last.next = new_node 
        # 7. Make last node as previous of new node */ 
        new_node.prev = last 

    def printList(self, node): 
  
        print("\nTraversal in forward direction")
        while(node is not None): 
            print(str(node.data)+" ") 
            last = node 
            node = node.next
  
        # print("\nTraversal in reverse direction")
        # while(last is not None): 
        #     print(str(last.data)+" ") 
        #     last = last.prev 

    def delete_start(self):
        # 1. check if list was empty initially
        if self.head==None:
            print("List already empty!")
            return

        # 2. Assign new head 
        self.head = self.head.next
        # 3. make prev of new head to be None
        self.head.prev = None

    def delete_end(self):
        # 1. check if list was empty initially
        if self.head ==None:
            print("List already empty!")
            return 

        # 2. find node to be deleted
        node = self.head
        while node.next is not None:
            node = node.next
        # 3. clearing next pointer of node prev to node to be deleted
        node.prev.next = None

    def delete_after(self,prev_node):
        # 1. check if prev_node exists
        if prev_node==None:
            print("No such node exists in the list")
            return 

        # 2. deleting the node between two nodes
        if prev_node.next.next is not None:
            prev_node.next.next.prev = prev_node
            prev_node.next = prev_node.next.next
            return 

        # 3. clearing next pointer of node prev to the node deleted 
        prev_node.next = None



class DoublyLinkedList_with_TailPointer:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_start(self, data):
    # 1 & 2: Allocate the Node & Put in the data 
        new_node = Node(data = data) 
      
        # 3. Make next of new node as head and previous as NULL 
        new_node.next = self.head 
        new_node.prev = None
      
        # 4. change prev of head node to new node  
        if self.head is not None: 
            self.head.prev = new_node 
        else:
            self.tail = new_node
        # 5. move the head to point to the new node 
        self.head = new_node  

    def insert_after(self, prev_node, data):
        # 1. check if the given prev_node is NULL 
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
  
        #2. allocate node  & 3. put in the data 
        new_node = Node(data = data) 
  
        # If prev_node is the last node 
        if prev_node.next==None:
            self.tail = new_node
        # 5. Make next of new node as next of prev_node 
        new_node.next = prev_node.next
  
        # 6. Make the next of prev_node as new_node  
        prev_node.next = new_node 
  
        # 7. Make prev_node as previous of new_node 
        new_node.prev = prev_node 
  
        # 8. Change previous of new_node's next node */ 
        if new_node.next is not None: 
            new_node.next.prev = new_node 

    # Add a node at the end of the DLL 
    def insert_end(self, data): 
      
        # 1. allocate node 2. put in the data 
        new_node = Node(data = data) 
        last = self.tail
  
        # 3. This new node is going to be the  
        # last node, so make next of it as NULL 
        new_node.next = None
        
        # 4. If the Linked List is empty, then 
        #  make the new node as head 
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            self.tail = new_node
            return
  
        self.tail = new_node
        # 5. Else traverse till the last node  
        while (last.next is not None): 
            last = last.next
        # 6. Change the next of last node  
        last.next = new_node 
        # 7. Make last node as previous of new node */ 
        new_node.prev = last 

    def printList(self, node): 
  
        print("Traversal in forward direction")
        while(node is not None): 
            print(str(node.data)+" ") 
            last = node 
            node = node.next
  
        # print("\nTraversal in reverse direction")
        # while(last is not None): 
        #     print(str(last.data)+" ") 
        #     last = last.prev 

    def delete_start(self):
        # 1. check if list was empty initially 
        if self.head==None:
            print("List already empty!")
            return
        # 2. changing the head 
        self.head = self.head.next
        # 3. changing prev of new head 
        self.head.prev = None

    def delete_end(self):
        # 1. check if list was empty initially 
        if self.head ==None:
            print("List already empty!")
            return 

        # 2. set node to delete as tail
        node = self.tail
        # 3. set tail to node prev to the node deleted
        self.tail = node.prev
        # 4. clear the next pointer of node prev to the node deleted
        node.prev.next = None
  
    def delete_after(self,prev_node):
        # 1. check if prev_node exists
        if prev_node==None:
            print("No such node exists in the list")
            return 
        # 2. deleting the node between two nodes
        if prev_node.next.next is not None:
            prev_node.next.next.prev = prev_node
            prev_node.next = prev_node.next.next
            return 

        # 3. clear pointer of node prev to node deleted
        prev_node.next = None
        # 4. making new tail after deletion 
        self.tail = prev_node

#Start with empty list 
mylist1 = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
mylist1.insert_end(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
mylist1.insert_start(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
mylist1.insert_start(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
mylist1.insert_end(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
mylist1.insert_after(mylist1.head.next, 8) 
  
print ("Created DLL is: ") 
mylist1.printList(mylist1.head) 
print("Head = "+ str(mylist1.head.data))


# Delete 1
# So linked list becomes 7->8->6->4->None 
mylist1.delete_start()
print("After deleting the head")
mylist1.printList(mylist1.head) 

print("Head = "+ str(mylist1.head.data))

# Delete 4
# So linked list becomes 7->8->6->None 
mylist1.delete_end()
print("After deleting the tail")
mylist1.printList(mylist1.head) 

print("Head = "+ str(mylist1.head.data))


# Delete 8 
# So linked list becomes 7->6->None
mylist1.delete_after(mylist1.head)
print("After deleting after 7")
mylist1.printList(mylist1.head) 

print("Head = "+ str(mylist1.head.data))


mylist2 = DoublyLinkedList_with_TailPointer()

# Insert 6. So the list becomes 6->None 
mylist2.insert_end(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
mylist2.insert_start(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
mylist2.insert_start(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
mylist2.insert_end(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
mylist2.insert_after(mylist2.head.next, 8) 



print ("Created DLL with tail pointer is: ") 
mylist2.printList(mylist2.head) 
print("Head = "+ str(mylist2.head.data) + " Tail = " + str(mylist2.tail.data))

# Delete 1
# So linked list becomes 7->8->6->4->None 
mylist2.delete_start()
print("After deleting the head")
mylist2.printList(mylist2.head) 

print("Head = "+ str(mylist2.head.data) + " Tail = " + str(mylist2.tail.data))


# Delete 4
# So linked list becomes 7->8->6->None 
mylist2.delete_end()
print("After deleting the tail")
mylist2.printList(mylist2.head) 

print("Head = "+ str(mylist2.head.data) + " Tail = " + str(mylist2.tail.data))

# Delete 8 
# So linked list becomes 7->6->None
mylist2.delete_after(mylist2.head)
print("After deleting after 7")
mylist2.printList(mylist2.head) 

print("Head = "+ str(mylist2.head.data) + " Tail = " + str(mylist2.tail.data))