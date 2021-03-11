import sys
input = sys.stdin.readline

def greedy(n, distance, price):
    min = price[0]
    sum = min*distance[0]
    for i in range(1, n-1):
        if min > price[i]:
            min = price[i]
        sum += min*distance[i]
    return sum 

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

if __name__ == '__main__':
    print(greedy(n, distance, price))
