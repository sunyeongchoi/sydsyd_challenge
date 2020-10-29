## <퀵 정렬>

- **불안정 정렬**
- 다른 원소와의 바교만으로 정렬을 수행하는 **비교정렬**
- 분할 정복 알고리즘 --> 매우 빠른 수행속도
  - 합병 정렬과 달리 리스트를 **비균등하게** 분할
- 분할정복방법
  - 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
  - 대개 순환 호출을 이용하여 구현
- 과정 설명
  - \1. 리스트 안에 있는 한 요소를 선택. --> **피벗** 이라고 한다.
  - \2. 피벗을 중심으로 왼쪽 : 피벗보다 작은 요소들, 오른쪽 : 피벗보다 큰 요소들로 옮겨진다.
  - \3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬
    - 분할된 부분 리스트에 대하여 순환호출을 이용하여 정렬을 반복
    - 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복
  - \4. 부분 리스트들이 더이상 분할이 불가능 할 때 까지 반복



![img](https://blog.kakaocdn.net/dn/btQKJi/btqLZJ0RvO9/d5E6plojKjzpn0GZiOVrk1/img.png)



 

 

- 하나의 리스트를 피벗을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬할 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법
- 퀵정렬의 단계
  - **분할 :** 입력 배열을 피벗을 기준으로 비균등하게 2개의 부분 배열로 분할
  - **정복 :** 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지 않으면 순환호출을 이용하여 다시 분할 정복방법 적용
  - **결합 :** 정렬된 부분 배열들을 하나의 배열에 합병한다.
  - 순환 호출이 한번 진행될 때마다 최소한 하나의 피벗을 최종적으로 위치가 정해지므로, 이 알고리즘으 납ㄴ드시 끝난다는 것을 보장할 수 있다.



![img](https://blog.kakaocdn.net/dn/ZxDM4/btqL1oPK8z0/tspDyJbpqB1YRYfBlYHmzK/img.png)



 

- 장점
  - 속도가 빠르다.
    - 시간 복잡도가 O(nlog2n)를 가지는 다른 정렬 알고리즘과 비교했을 때 가장 빠르다.
  - 추가 메모리 공간을 필요로 하지 않는다.
    - 퀵 정렬은 O(logn)만큼의 메모리를 필요로 한다.
- 단점
  - 정렬된 리스트에 대해서는 퀵 정렬의 분할에 의해 오히려 수행시간이 더 많이 걸린다.
    - 퀵 정렬의 불균형 분할을 방지하기 위해 피벗을 선택할 떄 더욱 리스트를 균등하게 분할할 수 있는 데이터를 선택한다. 
    - EX) 리스트 내의 몇 개의 데이터 중에서 크기순으로 중간 값을 피벗으로 선택한다.

 



![img](https://blog.kakaocdn.net/dn/25JmV/btqLZJNkQvH/avUJzXEwLB3OYJKnytJfqK/img.png)



 

- **퀵 정렬 C언어 코드**

```
# include <stdio.h>
# define MAX_SIZE 9
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

// 1. 피벗을 기준으로 2개의 부분 리스트로 나눈다.
// 2. 피벗보다 작은 값은 모두 왼쪽 부분 리스트로, 큰 값은 오른쪽 부분 리스트로 옮긴다.
/* 2개의 비균등 배열 list[left...pivot-1]와 list[pivot+1...right]의 합병 과정 */
/* (실제로 숫자들이 정렬되는 과정) */
int partition(int list[], int left, int right){
  int pivot, temp;
  int low, high;

  low = left;
  high = right + 1;
  pivot = list[left]; // 정렬할 리스트의 가장 왼쪽 데이터를 피벗으로 선택(임의의 값을 피벗으로 선택)

  /* low와 high가 교차할 때까지 반복(low<high) */
  do{
    /* list[low]가 피벗보다 작으면 계속 low를 증가 */
    do {
      low++; // low는 left+1 에서 시작
    } while (low<=right && list[low]<pivot);

    /* list[high]가 피벗보다 크면 계속 high를 감소 */
    do {
      high--; //high는 right 에서 시작
    } while (high>=left && list[high]>pivot);

    // 만약 low와 high가 교차하지 않았으면 list[low]를 list[high] 교환
    if(low<high){
      SWAP(list[low], list[high], temp);
    }
  } while (low<high);

  // low와 high가 교차했으면 반복문을 빠져나와 list[left]와 list[high]를 교환
  SWAP(list[left], list[high], temp);

  // 피벗의 위치인 high를 반환
  return high;
}

// 퀵 정렬
void quick_sort(int list[], int left, int right){

  /* 정렬할 범위가 2개 이상의 데이터이면(리스트의 크기가 0이나 1이 아니면) */
  if(left<right){
    // partition 함수를 호출하여 피벗을 기준으로 리스트를 비균등 분할 -분할(Divide)
    int q = partition(list, left, right); // q: 피벗의 위치

    // 피벗은 제외한 2개의 부분 리스트를 대상으로 순환 호출
    quick_sort(list, left, q-1); // (left ~ 피벗 바로 앞) 앞쪽 부분 리스트 정렬 -정복(Conquer)
    quick_sort(list, q+1, right); // (피벗 바로 뒤 ~ right) 뒤쪽 부분 리스트 정렬 -정복(Conquer)
  }

}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {5, 3, 8, 4, 9, 1, 6, 2, 7};

  // 퀵 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 8)
  quick_sort(list, 0, n-1);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```

 

- 퀵 정렬 python 코드

```
def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [ item for item in data[1:] if pivot > item ]
    right = [ item for item in data[1:] if pivot <= item ]
    
    return qsort(left) + [pivot] + qsort(right)
```

 

## <병합 정렬>

- 안정정렬
- 분할정복 알고리즘
  - 문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략
  - 순환 호출을 이용
- 과정 설명
  - \1. 리스트의 길이가 0또는 1이면 이미 정렬된 것으로 본다.
  - \2. 그렇지 않은 경우에는 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
  - \3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬
  - \4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병
- 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 된게 하는 방법
- 합병정렬 단계
  - 분할 : 입력 배열을 같은 크기의 2개의 부분 배열로 분할
  - 정복 : 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지 않으면 순환호출을 이용해 다시 분할정복방법 적용
  - 결합 : 정렬된 부분 배열들을 하나의 배열에 합병
- 합병정렬 과정
  - 추가적인 리스트 필요
  - 각 부분 배열을 정렬할 때도 합병 정렬을 순환적으로 호출하여 적용
  - 합병 정렬에서 실제로 정렬이 이루어지는 시점은 2개의 리스트를 합병하는 단계



![img](https://blog.kakaocdn.net/dn/Kc15N/btqL1ovsVyj/m80LD1GejIN6kkc0Lke8Uk/img.png)



 

- 단점
  - 만약 레코드를 배열로 구성하면, 임시 배열이 필요하다.
    - 제자리 정렬이 아니다.
  - 레코드들의 크기가 큰 경우에는 이동 횟수가 많으므로 매우 큰 시간적 낭비를 초래한다.
- 장점
  - 안정적인 정렬 방법
    - 데이터의 분포에 영향을 덜 받는다. => 입력데이터가 무엇이든 간에 정렬되는 시간을 동일
  - 만약 레코드를 연결리스트로 구성하면, 링크 인덱스만 변경되므로 데이터의 이동은 무시할 수 있을 정도로 작아진다.
    - 제자리 정렬로 구현할 수 있다.
  - 따라서 크기가 큰 레코드를 정렬할 경우에 연결 리스트를 사용한다면, 합병정렬은 퀵 정렬을 포함한 다른 어떤 정렬 방법보다 효율적이다.



![img](https://blog.kakaocdn.net/dn/HTn8r/btqL5AuI1Hi/9NAiLqx2awjPKUW6JCjRk0/img.png)



 

 

- **합병정렬 C언어 코드**

```
# include <stdio.h>
# define MAX_SIZE 8
int sorted[MAX_SIZE] // 추가적인 공간이 필요

// i: 정렬된 왼쪽 리스트에 대한 인덱스
// j: 정렬된 오른쪽 리스트에 대한 인덱스
// k: 정렬될 리스트에 대한 인덱스
/* 2개의 인접한 배열 list[left...mid]와 list[mid+1...right]의 합병 과정 */
/* (실제로 숫자들이 정렬되는 과정) */
void merge(int list[], int left, int mid, int right){
  int i, j, k, l;
  i = left;
  j = mid+1;
  k = left;

  /* 분할 정렬된 list의 합병 */
  while(i<=mid && j<=right){
    if(list[i]<=list[j])
      sorted[k++] = list[i++];
    else
      sorted[k++] = list[j++];
  }

  // 남아 있는 값들을 일괄 복사
  if(i>mid){
    for(l=j; l<=right; l++)
      sorted[k++] = list[l];
  }
  // 남아 있는 값들을 일괄 복사
  else{
    for(l=i; l<=mid; l++)
      sorted[k++] = list[l];
  }

  // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
  for(l=left; l<=right; l++){
    list[l] = sorted[l];
  }
}

// 합병 정렬
void merge_sort(int list[], int left, int right){
  int mid;

  if(left<right){
    mid = (left+right)/2 // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
    merge_sort(list, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
    merge_sort(list, mid+1, right); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
    merge(list, left, mid, right); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
  }
}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {21, 10, 12, 20, 25, 13, 15, 22};

  // 합병 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 7)
  merge_sort(list, 0, n-1);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```

 

- 합병정렬 python코드

```
# 데이터 리스트 앞뒤로 자르는 코드
def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)

# 머지하는 코드
# left 와 right 의 리스트 데이터를 정렬해서 sorted_list 라는 이름으로 return 하기
def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged
```

 

# BFS와 DFS

- 너비 우선 탐색 (Breadth First Search): 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식

  한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 순회함

- 깊이 우선 탐색 (Depth First Search): 정점의 자식들을 먼저 탐색하는 방식

  한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순화함



![img](https://blog.kakaocdn.net/dn/rtx92/btqL9rDIU1Y/cGO96N4jlt25ra388zw51k/img.png)



## 너비 우선 탐색 BFS

```
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
```

 

### 알고리즘 구현

- 자료구조 큐를 활용한다. need_visit 큐와 visited 큐, 두 개의 큐를 생성!

```
def bfs(graph, start_node):
    visited, need_visit = list(), list()     
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
```

일반적인 BFS 시간 복잡도는 노드의 수 V, 간선의 수 E 일때 while need_visit이 V+E 번 수행한다.

시간복잡도는 O(V+E)

## 깊이 우선 탐색 DFS



![img](https://blog.kakaocdn.net/dn/cFf86m/btqL6HA1IAL/m4KMdIUKSS055DDNkqzrF0/img.png)



```
def bfs(graph, start_node):
    visited, need_visit = list(), list()     
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
```

### 알고리즘 구현

자료구조 스택과 큐를 활용한다. need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성!

BFS는 두개의 큐를 활용하지만 DFS는 스택과 큐를 사용한다. 그 이유는 뒤에서부터 pop하기 때문에 최근순으로 순회함.

```
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
```

일반적인 DFS 시간 복잡도는 노드의 수 V, 간선의 수 E 일때 while need_visit은 V+E 번 수행

시간 복잡도 : O(V+E)

## 문제!

DFS(깊이우선탐색)로 1번 노드부터 탐색한다고 할 때 방문하는 노드의 순서는?

(단, 여러 개의 노드들이 연결되어 있는 경우, 작은 노드번호를 기준으로 먼저 순회한다.)



![img](https://blog.kakaocdn.net/dn/VlcjB/btqL8mix2tJ/Qog15mgInDkUW2EHlN0sDK/img.png)



 

- 답

  1, 2, 4, 7, 5, 6, 3

# 동적 계획법과 분할 정복

## 동적계획법 (DP 라고 많이 부름)

입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘

- 상향식 접근법으로, 가장 최하위 해답을 구한 후, 이를 저장하고, 해당 결과값을 이용해서 상위 문제를 풀어가는 방식

- Memoization 기법을 사용함

  Memoization (메모이제이션) 이란: 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술

- 문제를 잘게 쪼갤 때, 부분 문제는 중복되어, 재활용됨

  예: 피보나치 수열

## 분할 정복

- 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
- 하양식 접근법으로, 상위의 해답을 구하기 위해, 아래로 내려가면서 하위의 해답을 구하는 방식
  - 일반적으로 재귀함수로 구현
- 문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않음
  - 예: 병합 정렬, 퀵 정렬 등

## 공통점

문제를 쪼개서, 가장 작은 단위로 분할하여 해결

## 차이점

- 동적 계획법

  부분 문제는 중복되어, 상위 문제 해결 시 재활용 된다.

  메모이제이션 기법을 사용한다. (부분 문제의 해답을 재활용하여 최적화)

- 분할 정복

  부분 문제는 서로 중복되지 않는다.

  메모이제이션 기법을 사용하지 않는다.