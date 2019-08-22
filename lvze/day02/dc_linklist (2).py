#!/usr/bin/python

#双向循环链表

class Node(object):
    def __init__(self,val,p = None):
        self.val = val
        self.next = p
        self.prior = p

class LinkList(object):
    def __init__(self):
        self.head = None

    # 链表的初始化
    def initlist(self,data):
        self.head = Node(0)

        p = self.head
        p.next = p.prior = p
        
        for i in data:
            node = Node(i)

            node.next = p.next
            p.next.prior = node
            p.next = node
            node.prior = p

            p = p.next

    #遍历链表
    def show(self):
        p = self.head.prior

        while p != self.head:
            print(p.val,' ',end = '')
            p = p.prior
        print()

    # 获取链表长度
    def getlength(self):
        p = self.head
        length = 0
        while p.next != self.head:
            length += 1
            p = p.next

        return length


    # 判断链表是否为空
    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    #清空
    def clear(self):
        self.head = None


    # 在某个位置插入节点
    def insert(self,index,item):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('index is error')
            return

        p = self.head
        j = 0

        while p.next != self.head and j < index:
            p = p.next
            j += 1

        q = Node(item,p)
        q.next = p.next
        p.next.prior = q
        p.next = q
        q.prior = p

    # 删除某个位置的元素  
    def delete(self,index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print('Linklist is empty')
            return
        
        p = self.head
        j = 0
        while p.next != self.head and j < index:
            p = p.next
            j += 1

        if p.next == self.head:
            print('indes is error')
        else:
            p.next.next.prior = p
            p.next = p.next.next

    # 查找操作，返回相应位置  
    def index(self,value):
        if self.is_empty():
            print('Linklist is empty')
            return
        p = self.head.next
        i = 0
        while p != self.head and not (p.val == value):
            p = p.next
            i += 1

        if p == self.head:
            return -1
        else : 
            return i

