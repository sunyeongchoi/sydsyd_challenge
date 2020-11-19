# REST API란

### 장점

1. 코드의 재활용성이 높아진다.

2. 백과 프론트를 완전히 분리할 수 있다.

3. 기존 방식에선 한 페이지에 하나의 클래스밖에 할당하지 못해 코드의 중복이 발생함 --> REST API에서는 한 페이지당 여러 개의 API 사용

   ![Image for post](https://miro.medium.com/max/714/1*TO0TvI68lSu9y8Vzm2vm2g.png)

   - 핵심은 한 HTML&JS페이지가 여러  API에서 정보를 받을 수 있다는 점
   - 기존 정보 송수신의 틀을 깨야 REST API를 이해할 수 있다.
   - 1개의 API가 100개, 1000개, 10만 개의 페이지에서 활용될 수 있다



### 사용법

- https://www.django-rest-framework.org/tutorial/quickstart/#quickstart 우선 이 공식문서 참조
- REST API를 사용해도 Template을 위한 Views코드는 작성해야 한다.

   
