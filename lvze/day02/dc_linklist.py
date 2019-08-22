
# 节点
class Node:
    def __init__(self,val,p = None):
        self.val = val
        self.next = self.prior = p

class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self,data):
        self.head = Node(data[0])
        p = self.head
        p.next = p.prior = p

        for i in data[1:]:
            node = Node(i)

            node.next = p.next
            p.next.prior = node
            p.next = node
            node.prior = p

            p = p.next



link = LinkList()
data = [1,2,3,4,5]
link.init_list(data)