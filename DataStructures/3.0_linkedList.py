# Starting Data Structure Linked List
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def delteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data == key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("in linked list")
            return
        new_node=node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self, new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head =new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def displayList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if(__name__=="__main__"):
    linList=linkedList()
    linList.append(1)
    linList.append(2)
    linList.push(3)
    linList.append(0)
    linList.displayList()
    print(end="")
    linList.delteNode(1)
    linList.displayList()
