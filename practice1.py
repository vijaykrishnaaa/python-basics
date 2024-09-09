class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class linklist:
    def __init__(self):
        self.head=None
    def insert(self,newdata):
        if self.head==None:
            self.head=newdata
        else:
            currentnode=self.head
            while True:
                if currentnode.next==None:
                    break
                currentnode=currentnode.next
            currentnode.next=newdata
            newdata.prev=currentnode
    def printLL(self):
        currentnode=self.head
        while currentnode !=None:
            print(currentnode.data)
            currentnode=currentnode.next

linkedlist=linklist()

node1=node("vijay")
node2=node("reddy")

linkedlist.insert(node1)
linkedlist.insert(node2)

linkedlist.printLL()