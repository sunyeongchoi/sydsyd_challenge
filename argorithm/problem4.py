# 4번
# 참조 : https://jun-choi-4928.medium.com/javascript%EB%A1%9C-%EC%98%A4%EB%A6%84%EC%B0%A8%EC%88%9C%EC%9C%BC%EB%A1%9C-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4%EC%9D%84-%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC%EB%A1%9C-%EB%B3%80%ED%99%98%ED%95%98%EA%B8%B0-7263a9c8ba0f
class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def sortArrToTree(nums):
    if not nums: return None
    mid = len(nums)//2
    node = Node(nums[mid], sortArrToTree(nums[:mid]), sortArrToTree(nums[mid+1:]))
    return node

if __name__ == '__main__':
    print(sortArrToTree([-10,-3,0,5,9]))