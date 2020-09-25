# 문제

### **문항1**

다음 조건을 만족하는 도커 이미지를 Docker Hub에 등록하고 이미지의 이름을 제출합니다. 가상머신은 쿠버네티스 실습에 사용한 가상머신을 사용하며, 해당 가상머신의 IP는 **192.168.111.110**입니다.

1. Docker Hub에서 Star가 2,000개 이상인 nginx 이미지를 기반으로 컨테이너를 실행합니다. 

2. 컨테이너 생성 시 호스트의 7988 포트와 컨테이너의 80 포트를 맵핑 해 줍니다.

3. 컨테이너에 아래 조건을 만족하는 hello.html 파일을 생성합니다. 

   a. nginx의 웹 루트 디렉터리는 "/usr/share/nginx/html/" 입니다.

   b. 파일 저장 경로는 접속 URL 경로를 참고하여 정의합니다.

   c. hello.html 내용은 다음과 같습니다. (홍길동 대신 본인 이름으로 대체)	

   <html><head> 

   	<meta charset="utf-8"></head><body> <h1>클라우드반 **홍길동**입니다.</h1></body></html>
   	    
   	</meta>

   4. 본인의 PC에서 브라우저로 http://192.168.111.110:7988/cloud/hello.html로 접속하면, 아래와 같은 결과가 출력됩니다. ![img](https://lh5.googleusercontent.com/VI91gbOFrayXGEKdi3nDZBym-sE0oMFmxEu86Xqv2n4ry3eLIfDuKT3cXPkKedcyEuYGpArNag6bgvMhjPVwzONdgre1-1Cp75qbRiHtYy9yG_OM2cG9WZ4QtPj1COgJFpCNn_1w)

   5. 컨테이너를 커밋해서 hello 이미지를 생성하고, 생성한 이미지를 Docker Hub에 등록합니다. 

   6. Docker Hub에 등록한 hello 이미지의 이름을 Docker Hub ID와 함께 제출합니다. 

      예: myanjini/hello:latest

      

#### **평가기준**

- Docker Hub에 이미지를 가져오고, 등록할 수 있다.
- Docker Container 실행 옵션을 이해하고 사용하는 능력이 있다.
- 호스트의 경로와 웹 루트의 경로 간의 관계를 이해하고 이를 활용하는 능력이 있다.
- 호스트와 컨테이너간 파일 교환 방법을 이해하고 수행하는 능력이 있다.



### **문항2**

다음 조건을 만족하는 쉘 스크립트 파일(backup.sh)과 crontab 파일에 들어갈 내용을 기술하시오.

1. 매월 16일 새벽 3시 20분에 /home 디렉터리 전체를 백업해서 /backup 디렉터리에 저장합니다.

2. 백업 파일은 "backup.년.월.일.tar.xz" 형식으로 생성합니다. 

   예: backup.2020.09.24.tar.xz

3. 백업 기능은 /root/backup.sh 쉘 스크립트 파일로 구현하고, cron에 등록해서 주기적으로 실행합니다.

4. 쉘 스크립트 파일의 소유자는 root입니다.

   

   [backup.sh],[crontab]을 작성하라!



#### **평가기준**

- crontab 형식을 이해하고 구성하는 능력이 있다.
- 쉘 스크립트를 이해하고 작성하는 능력이 있다.
- 파일의 소유자와 권한에 대해 이해하고 구성하는 능력이 있다.
- 파일 압축 및 묶음을 이해하고 실행하는 능력이 있다.



### **문항3**

구글 문서에서 "9월 13일 과제" 내용을 보완하여 제출하시오.



 Jenkins의 exec-ansible-serverspec 프로젝트에서 ENVIRONMENT 파라미터를 production으로 설정 후 빌드한 결과 화면을 스크린 샷을 떠서 아래 주소에 등록하시오.



https://docs.google.com/spreadsheets/d/1yJQYo2yE5TBMHRM5CaJ_XvKryVVyk1Iaro1XXPx1LrU/edit?usp=sharing





#### **평가기준**

- DevOps 구현을 위한 도구를 설치하고 실행할 수 있다.
- Jenkins, Serverspec, Ansible 등을 이용하여 인프라를 자동으로 구성, 배포할 수 있다.
- Jenkins의 파이프라인 프로젝트를 생성할 수 있다.
- 파라미터에 따라 프로젝트 빌드를 다원화할 수 있다.


### **문항4**

다음은 생성한 컨피그맵을 파드에서 사용하는 과정입니다.

5번과 같은 결과가 나올 수 있도록 2번의 YAML 파일(selective-env-from-configmap.yml)을 작성하시오.

\### 1

$ kubectl create configmap cftest --from-literal userid=tester --from-literal userpw=password --from-literal userrole=normal

\### 2

$ vi selective-env-from-configmap.yml을 작성하시오


\### 3

$ kubectl apply -f selective-env-from-configmap.yml
\### 4

$ kubectl get podsNAME     READY  STATUS  RESTARTS  AGEcftest-pod  1/1   Running  0     37s
\### 5

$ kubectl exec cftest-pod -- env | grep ENVENV_USERID=testerENV_USERPW=password

#### **평가기준**

- 컨피그맵을 생성하고 사용할 수 있다. 
- 컨피그맵의 일부를 파드의 환경변수로 설정할 수 있다.
- 쿠버네티스 오브젝트를 YAML 파일로 정의할 수 있다.
- kubectl 명령어를 이해하고 사용할 수 있다.





# 답

### 1번

suoung0716/hello:latest

### 2번

[backup.sh]

#!/bin/bash
set $(date)
fname="backup$1$2$3tar.xz"
tar cfJ /backup/$fname /home



-------------------------------------------------------------------------
[crontab]

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

20   03   16   *   *    root    /root/backup.sh



### 4번

vagrant@ubuntu:~$ cat selective-env-from-configmap.yml
apiVersion: v1
kind: Pod
metadata:
  name: cftest-pod
spec:
  containers:

    - name: cftest-container
      image: busybox
      args: ['tail','-f','/dev/null']
      env:
        - name: ENV_USERID
          valueFrom:
            configMapKeyRef:
              name: cftest
              key: userid
        - name: ENV_USERPW
          valueFrom:
            configMapKeyRef:
              name: cftest
              key: userpw