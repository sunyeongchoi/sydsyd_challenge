# 1번
# 참조 : https://niceman.tistory.com/11

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)
    
    def delete_duplicate(self):
        cur = self.head
        dict = {}
        prev = None
        while cur is not None:
            if cur.val in dict:
                prev.next = cur.next
            else:
                dict[cur.val] = True
                prev = cur
            cur = cur.next
    
    def printList(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)

if __name__ == '__main__':
    li = LinkedList(3)
    li.add(4)
    li.add(5)
    li.add(6)
    li.add(4)
    li.add(7)
    li.add(4)
    li.add(6)
    li.delete_duplicate()
    print(li.printList())

