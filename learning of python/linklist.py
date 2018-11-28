class Listnode:
    def __init__(self,x):
        self.data=x
        self.next=None
class SingleList:
    def __init__(self):
        self.head=None
        self.tail=None
    def addnode(self,item):
        if not isinstance(item,Listnode):
            Listnode(item)
        if self.head==None:
            self.head=item
        else:
            self.tail.next=item
        self.tail=item
    def count(self):
        count=0
        current_node=self.head
        while current_node is not None:
            count+=1
            current_node=current_node.next
        return count
    def output_node(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next
node1=Listnode(5)
node2=Listnode(9)
node3=Listnode(18)
a=SingleList()
a.addnode(node1)
a.addnode(node3)
a.addnode(node2)
a.output_node()
l=a.count()
print(l)