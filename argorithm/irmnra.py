# 1번
# 참조 : https://niceman.tistory.com/11
# class Node:
#     def __init__(self, item):
#         self.val = item
#         self.next = None

# class LinkedList:
#     def __init__(self, item):
#         self.head = Node(item)

#     def add(self, item):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = Node(item)
    
#     def delete_duplicate(self):
#         cur = self.head
#         dict = {}
#         prev = None
#         while cur is not None:
#             if cur.val in dict:
#                 prev.next = cur.next
#             else:
#                 dict[cur.val] = True
#                 prev = cur
#             cur = cur.next
    
#     def printList(self):
#         cur = self.head
#         res = []
#         while cur is not None:
#             res.append(cur.val)
#             cur = cur.next
#         return str(res)

# if __name__ == '__main__':
#     li = LinkedList(3)
#     li.add(4)
#     li.add(5)
#     li.add(6)
#     li.add(4)
#     li.add(7)
#     li.add(4)
#     li.add(6)
#     li.add(6)
#     li.delete_duplicate()
#     print(li.printList())


# 2번

# from collections import defaultdict

# def remove_duplicate(arr):
#     dict = defaultdict(int)
#     for a in arr:
#         dict[a] += 1
#     return dict

# if __name__ == '__main__':
#     print(remove_duplicate([3,3,3,3,1,1,2,3,6]))



# 3번
# def change_str(str):
#     return str.strip().replace(" ", "%20")

# if __name__ == '__main__':
#     print(change_str("my name is sunyeong  "))


# 4번
# 참조 : https://jun-choi-4928.medium.com/javascript%EB%A1%9C-%EC%98%A4%EB%A6%84%EC%B0%A8%EC%88%9C%EC%9C%BC%EB%A1%9C-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4%EC%9D%84-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0-7263a9c8ba0f
# class Node(object):
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right

# def sortArrToTree(nums):
#     if not nums: return None
#     mid = len(nums)//2
#     node = Node(nums[mid], sortArrToTree(nums[:mid]), sortArrToTree(nums[mid+1:]))
#     return node

# if __name__ == '__main__':
#     print(sortArrToTree([-10,-3,0,5,9]))


# 5. 