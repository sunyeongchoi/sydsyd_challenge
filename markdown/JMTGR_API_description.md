## REST API - 수녕부분 

### GET /user/ALL

- 모든 사용자 정보 목록을 가져옴
- return: user[]



### POST /user/ALL

- 사용자 정보 저장
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST



### GET /user/Detail/\<str:email> - 뭘좀 바꿔서 다시 테스트 해봐야함

- 특정 사용자 정보 가져옴, 사용자 없으면 404 return
- email : 로그인 사용자 email
- 기능 
  - 사용자 존재 여부 확인
- return: user | HTTP_404_NOT_FOUND



### PUT /user/Detail/\<str:email> - 뭘좀 바꿔서 다시 테스트 해봐야함

- 특정 사용자 정보 수정
- email : 로그인 사용자 email
- body: {email: str(이메일-pk), interest: str(관심카테고리), name:str(사용자이름), phone_number: str(핸드폰번호)}
- 기능
  - 로그인 진행과정 > 이미 우리 사이트 데이터베이스에 존재하는 회원일 경우(혹시 정보가 바꼈을 수 있으니 update해줌)
  - 로그인 성공 후 > 회원 정보 수정 클릭 시
- return: HTTP_201_CREATED | HTTP_400_BAD_REQUEST





### GET /certificate/CertificatesFilter/

- 키워드에 해당하는 자격증 정보 조회
- parameter : { keyword : 검색어 }
- 기능 
  - 메인페이지 노출
  - 자격증 검색 기능 (키워드 : 카테고리명, 자격증명, 키워드 없을 시 전체 자격증 조회)
- return: certificate[] 또는 category[]+certificate[]



### GET /certificate/CertRecomByExaminee/

- 전체 자격증 중 **필기** 응시자 수 많은 순으로 8개씩 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByExamineeSil/ - 뭘좀 바꿔서 다시 테스트 해봐야함

- 전체 자격증 중 **실기** 응시자 수 많은 순으로 8개 조회
- 기능
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByInterest/ - 아직 테스트 중

- 회원 > 관심카테고리 > 해당 카테고리에 해당하는 자격증 중 인기자격증 8개 조회
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET /certificate/CertRecomByInterest/ - 아직 테스트 중

- 비회원 > 랜덤 카테고리 > 해당 카테고리에 해당하는 자격증 중 인기자격증 8개 조회
- 기능 
  - 메인페이지 노출
- return: certificate[]



### GET / certificate/OrderingFilter/ - 아직 테스트 중

- 시험 결과 날자가 임박한 자격증 졍렬
- 기능
  - 메인 페이지 노출
- return: certificateSchedule[]+certificate[]

