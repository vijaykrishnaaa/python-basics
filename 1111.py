class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverseandprint(head):
        currentnode=head
        while currentnode is not None:
            print(currentnode.data,end="->")
            currentnode=currentnode.next
        print("NULL")


node1=node(1)
node2=node(4)
node3=node(5)
node4=node(7)
node5=node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

traverseandprint(node1)