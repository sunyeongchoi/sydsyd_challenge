## 거품정렬(버블정렬)

- 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
  - 인접한 2개의 레코드를 비교하여 크기가 순서대로 되어있지 않으면 서로 교환한다.



![img](https://blog.kakaocdn.net/dn/dju5Ov/btqLkLyfqTN/4fMu50jwoWs3lm5skeRSVk/img.png)



- 선택정렬과 기본 개념이 유사
- 버블정렬 c언어 코드

```
# include <stdio.h>
# define MAX_SIZE 5

// 버블 정렬
void bubble_sort(int list[], int n){
  int i, j, temp;

  for(i=n-1; i>0; i--){
    // 0 ~ (i-1)까지 반복
    for(j=0; j<i; j++){
      // j번째와 j+1번째의 요소가 크기 순이 아니면 교환
      if(list[j]<list[j+1]){
        temp = list[j];
        list[j] = list[j+1];
        list[j+1] = temp;
      }
    }
  }
}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {7, 4, 5, 1, 3};

  // 버블 정렬 수행
  bubble_sort(list, n);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```

- 장점
  - 구현이 매우 간단
- 단점
  - 일반적으로 자료의 교환작업이 자료의 이동작업보다 더 복잡하기 때문에 버블정렬은 단순성에도 불구하고 거의 쓰이지 않는다.
- 버블정렬 시간복잡도



![img](https://blog.kakaocdn.net/dn/bJyWIk/btqLuCTSK1h/SUkmypjdloBkYG4IBCDVZk/img.png)



 

## 선택정렬

- 첫 번째 자료를 두 번째 자료부터 마지막 자료까지 차례대로 비교하여 가장 작은 값을 찾아 첫 번째에 놓고, 두 번째 자료를 세 번째 자료부터 마지막 자료까지와 차례대로 비교하여 그 중 가장 작은 값을 찾아 두 번째 위치에 놓는 과정을 반복하며 정렬을 수행
- 1회전을 수행하고 나면 가장 작은 값의 자료가 맨 앞으로 오게 되므로 그 다음 회전에서는 두 번째 자료를 가지고 비교한다.
- 제자리 정렬 알고리즘 중 하나
  - 입력 배열(정렬되지 않은 값들) 이외에 다른 추가 메모리를 요구하지 않는 정렬 방법



![img](https://blog.kakaocdn.net/dn/efjEoO/btqLopV5Sky/l70XriAt0sep2sqK7KueTk/img.png)



 

- 선택 정렬 c언어 코드

```
# include <stdio.h>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )
# define MAX_SIZE 5

// 선택 정렬
void selection_sort(int list[], int n){
  int i, j, least, temp;

  // 마지막 숫자는 자동으로 정렬되기 때문에 (숫자 개수-1) 만큼 반복한다.
  for(i=0; i<n-1; i++){
    least = i;

    // 최솟값을 탐색한다.
    for(j=i+1; j<n; j++){
      if(list[j]<list[least])
        least = j;
    }

    // 최솟값이 자기 자신이면 자료 이동을 하지 않는다.
    if(i != least){
        SWAP(list[i], list[least], temp);
    }
  }
}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {9, 6, 7, 3, 5};

  // 선택 정렬 수행
  selection_sort(list, n);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```

 

- 장점
  - 자료 이동횟수가 미리 결정된다.
- 단점
  - 안정성을 만족하지 않는다.
  - 즉, 값이 같은 레코드가 있는 결루에 상대적인 위치가 변경될 수 있다.
- 선택정렬 시간복잡도



![img](https://blog.kakaocdn.net/dn/dsjWqX/btqLpTbiLTD/qxAwPvB9ro4fX4z6luVEm0/img.png)



 

## 삽입정렬

- 두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후 자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬하는 알고리즘
- 즉, 두 번쨰 자료는 첫 번째 자료, 세 번째 자료는 주번째와 첫 번째 자료, 네번째 자료는 세 번쨰, 주번쨰, 첫 번째 자료와 비교한 후 자료가 삽입될 위치를 찾는다. 자료가 삽입될 위치를 찾았다면 그 위치에 자료를 삽입하기 위해 자료를 한 칸씩 뒤로 이동시킨다.
- 처음 key값은 두 번째 자료부터 시작한다.
- 자료의 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘



![img](https://blog.kakaocdn.net/dn/q3soM/btqLwfqdwW6/qfGPeHbF1nUiSkI6EkHdik/img.png)



 

- 삽입정렬 c언어 코드

```
# include <stdio.h>
# define MAX_SIZE 5

// 삽입 정렬
void insertion_sort(int list[], int n){
  int i, j, key;

  // 인텍스 0은 이미 정렬된 것으로 볼 수 있다.
  for(i=1; i<n; i++){
    key = list[i]; // 현재 삽입될 숫자인 i번째 정수를 key 변수로 복사

    // 현재 정렬된 배열은 i-1까지이므로 i-1번째부터 역순으로 조사한다.
    // j 값은 음수가 아니어야 되고
    // key 값보다 정렬된 배열에 있는 값이 크면 j번째를 j+1번째로 이동
    for(j=i-1; j>=0 && list[j]>key; j--){
      list[j+1] = list[j]; // 레코드의 오른쪽으로 이동
    }

    list[j+1] = key;
  }
}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {8, 5, 6, 2, 4};

  // 삽입 정렬 수행
  insertion_sort(list, n);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
```

 

- 장점
  - 대부분의 레코드가 이미 정렬되어 있는 경우에 매우 효율적일 수 있다.
  - 레코드의 수가 적을 경우 알고리즘 자체가 매우 간단하므로 다른 복잡한 정렬 방법보다 유리할 수 있다.
- 단점
  - 비교적 많은 레코드들의 이동을 포함한다.
  - 레코드 수가 많고 레코드 크기가 클 경우에 적합하지 않다.



![img](https://blog.kakaocdn.net/dn/cexXxI/btqLyMBwtom/UicxpYukQbKWGtGDNtQKv0/img.png)



 

## 힙정렬



![img](https://blog.kakaocdn.net/dn/bIE1KE/btqLwKxYZUG/R6wr5fokEo2LoyKV8HIePk/img.png)



- 최대 힙 트리나 최소 힙 트리를 구성해 정렬을 하는 방법
- 내림차순 정렬 - 최대 힙 구성, 오름차순 정렬 - 최소 힙 구성
- 정렬해야 할 N개의 요소들로 최대 힙(완전 이진 트리 형태)을 만든다. -> 한번에 하나씩 요소를 힙에서 꺼내서 배열의 뒤부터 저장 -> 삭제되는 요소들(최댓값부터)은 값이 감소되는 순서로 정렬되게 된다.

## 1. 최대 힙의 삽입

\1. 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 이어서 삽입한다.

\2. 새로운 노드를 부모 노드들과 교환해서 힙의 성질을 만족시킨다.

\- 아래의 최대힙에 새로운 요소 8을 삽입해보자



![img](https://blog.kakaocdn.net/dn/d1xlKF/btqLzXpUP4a/y0OaqOVWPed4pr4XyymXVK/img.png)



##  

- c언어를 이용한 최대힙 삽입연산

```
/* 현재 요소의 개수가 heap_size인 힙 h에 item을 삽입한다. */
// 최대 힙(max heap) 삽입 함수
void insert_max_heap(HeapType *h, element item){
  int i;
  i = ++(h->heap_size); // 힙 크기를 하나 증가

  /* 트리를 거슬러 올라가면서 부모 노드와 비교하는 과정 */
  // i가 루트 노트(index: 1)이 아니고, 삽입할 item의 값이 i의 부모 노드(index: i/2)보다 크면
  while((i != 1) && (item.key > h->heap[i/2].key)){
    // i번째 노드와 부모 노드를 교환환다.
    h->heap[i] = h->heap[i/2];
    // 한 레벨 위로 올라단다.
    i /= 2;
  }
  h->heap[i] = item; // 새로운 노드를 삽입
}
```

 

## 2. 최대힙의 삭제

\1. 최대 힙에서 최댓값은 루트 노드이므로 노드가 삭제된다.

   \- 최대 힙에서 삭제 연산은 최댓값을 가진 요소를 삭제하는 것이다.

\2. 삭제된 루트 노드에는 힙의 마지막 노드를 가져온다.

\3. 힙을 재구성한다.



![img](https://blog.kakaocdn.net/dn/bC65op/btqLveGTkKN/GxdXvfXkacGiKaMvKWfQJK/img.png)



 

- c언어를 이용한 최대힙 삭제 연산

```
// 최대 힙(max heap) 삭제 함수
element delete_max_heap(HeapType *h){
  int parent, child;
  element item, temp;

  item = h->heap[1]; // 루트 노드 값을 반환하기 위해 item에 할당
  temp = h->heap[(h->heap_size)--]; // 마지막 노드를 temp에 할당하고 힙 크기를 하나 감소
  parent = 1;
  child = 2;

  while(child <= h->heap_size){
    // 현재 노드의 자식 노드 중 더 큰 자식 노드를 찾는다. (루트 노드의 왼쪽 자식 노드(index: 2)부터 비교 시작)
    if( (child < h->heap_size) && ((h->heap[child].key) < h->heap[child+1].key) ){
      child++;
    }
    // 더 큰 자식 노드보다 마지막 노드가 크면, while문 중지
    if( temp.key >= h->heap[child].key ){
      break;
    }

    // 더 큰 자식 노드보다 마지막 노드가 작으면, 부모 노드와 더 큰 자식 노드를 교환
    h->heap[parent] = h->heap[child];
    // 한 단계 아래로 이동
    parent = child;
    child *= 2;
  }

  // 마지막 노드를 재구성한 위치에 삽입
  h->heap[parent] = temp;
  // 최댓값(루트 노드 값)을 반환
  return item;
}
```

 

- 장점
  - 시간 복잡도가 좋다.
  - 힙 정렬이 가장 유용한 경우는 전체 자료를 정렬하는 것이 아니라 **가장 큰 값 몇개만 필요할 때** 이다.

 



![img](https://blog.kakaocdn.net/dn/4Gzp0/btqLwK6amjA/jkd6Za5J6qpD5KNtDBJGuk/img.png)



 

 

 

- 단순(구현 간단)하지만 비효율적인 방법
  - 삽입정렬, 선택정렬, 버블정렬
- 복잡하지만 효율적인 방법
  - 퀵정렬, 힙정렬, 합병정렬, 기수정렬

 

 

## 이분탐색

- 탐색기법 중 하나로 원하는 탐색 범위를 두 부분으로 분할해서 찾는 방식
- 전부를 탐색하는 탐색속도에 비해 빠름
- left, right, mid값으로 탐색하는 것 (mid값은 (left + right) / 2 으로 잡아주고 우리가 검색하고자 하는 값과 mid값을 비교
- c언어를 이용한 이분탐색 코드

```
#include <stdio.h>
 
int main(void){
 
    int findN;
    int result = 0;
    //처음int는 다음 정점 마지막 int 값어치
 
    int A[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 15 };
 
    scanf("%d", &findN);
    int left = 0, right =  9;
 
 
    while (left <= right){
 
        int mid = (left + right) / 2;
        if (A[mid] > findN)
            right = mid - 1;
        else if (A[mid] < findN)
            left = mid + 1;
        else
        {
            result = mid;
            break;
        }
    }
    printf("%d\n", result);
    return 0;
}
```

 

 

참고

[gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html](https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)