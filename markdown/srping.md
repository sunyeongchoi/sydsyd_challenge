## 스프링



#### [#](https://gyoogle.dev/blog/interview/웹.html#스프링이-뭔지-간단히-설명해보세요)스프링이 뭔지 간단히 설명해보세요

- 스프링릉 **경량**의 **제어역행**과 **관점지향** **컨테이너** 프레임워크이다.
  - 경량 : 전체 스프링의 크기는 1MB남짓한 하나의 JAR파일, 스프링에 의해 발생하는 부하는 무시해도 되는 수준
  - 제어역행 : 애플리케이션의 느슨한 결합을 도모한다.
  - 관점지향 : 스프링은 관점지향 프로그래밍을 위한 풍부한 지원을 한다.
  - 컨테이너 : 애플리케이션 객체의 생명주기와 설정을 포함하고 관리한다는 점에서 스프링은 일종의 컨테이너 이다.

- EJB기반으로 개발하지 않고 POJO기반으로 개발을 하더라도 가볍고 제어가 가능한 상오 관련이 적은 AOP를 지원하고 컨테이너를 통해 라이프사이클을 관리하고 xml기반으로 컴포넌트를 개발할 수 있도록 지원해주는 프레임웤

- 특징
  - 경량의 프레임웤(가볍다) - 무거운 EJB의 대체 기술
  - 설정 파일을 통해 의존관계를 주입하눈 DI지원(느슨한 결합도)
  - 공통 관심사항을 분리하는 AOP지원(트랜젝션, 로깅, 보안)
  - 특정 interface나 class를 상속받지 않아도 되는 POJO지원

- DI(Dependency Injection)
  - 객체 사이의 의존관계를 객제 자신이 아닌 외부(스프링 컨테이너)가 수행한다는 개념
- IOC(Inversion Of Control)
  - 프레임워크에 제어의 권한을 넘김으로써 클라이언트 코드가 신경써야 할 것을 주이는 전략
  - 프레임워크의 메소드가 프로그래머가 작성한 코드를 호출한다.
  - ![](C:\Users\user\Desktop\IOC.PNG)

​    ==> IOC로부터 DI개념이 생겼으며 두 개념은 같은 것임

- AOP(Aspect-Oriented Programming)

  - 공통 부분은 빼서 따로 관리

  - OOP를 더욱 OOP답게 만들어준다.

  - ![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010160522985.png)

  - ![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010160608510.png)

  - Filter/interceptor/AOP

    - ![](https://media.vlpt.us/images/sa833591/post/e52adfc5-f31b-43b8-beb5-e89fa0d6463a/Filter_Interceptor_AOP%ED%9D%90%EB%A6%842.jpg)

    - Filter 

      - Dispatcher Servlet영역에 들어가기 전 Front Controller 앞 범위에서 수행된다.
      - Controller 이후 자원 처리가 끝난 후 응답 처리에 대해서도 변경, 조작을 수행할 수 있다.
      - 일반적으로 인코딩 변환 처리, XSS방어를 개발할 대 사용

    - Interceptor

      - Filter는 스프링 컨텍스트 이전에 실행되어 스프링과 무관
      - 하지만 인터셉터의 경우에는 `DispatcherServlet`이 Controller를 호출하기 전, 후에 끼어들기 때문에 스프링 컨텍스트 내부에서 Controller에 관한 `요청`과 `응답`에 관여한다.
      - 스프링의 모든 @Bean에 접근가능

      > 👉 **Interceptor 실행메소드**
      >
      > - preHandler() - Controller 실행 전
      > - postHandler() - Controller 실행 후 view Rendering 실행 전
      > - afterCompletion() - view Rendering 이후

    - AOP

      - Controller처리 이후 주로 비지니스 로직에서 실행된다.
      - 주로 '로깅', '트랜잭션', '에러처리'등 비즈니스 단의 메서드에서 구체적인 조정이 필요할 때 사용
      - Filter와 Interceptor와 달리 메소드 전후 지점에서 자유롭게 설정 가능





#### [#](https://gyoogle.dev/blog/interview/웹.html#스프링이랑-스프링-부트는-차이점이-뭔가요)스프링이랑 스프링 부트는 차이점이 뭔가요?

스프링 부트는 스프링에서 사용하는 프로젝트를 간편하게 셋업할 수 있는 서브 프로젝트입니다. 독립 컨테이너에서 동작할 수 있기 때문에 임베디드 톰켓이 자동으로 실행되구요. 임베디드 컨테이너에서 애플리케이션을 실행시키기에는 다소 불안전해서 큰 프로젝트는 사용하지 않는 것이 좋습니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#mvc패턴이란)MVC패턴이란?

MVC 패턴은 코드의 재사용에 유용하며, 사용자 인터페이스와 응용 프로그램 개발에 소요되는 시간을 줄여주는 효과적인 설계 방식을 말합니다.

| Model      | 어플리케이션의 데이터와 비즈니스 로직을 담는 객체이다.       |
| ---------- | ------------------------------------------------------------ |
| View       | - Model의 정보를 사용자에게 표시한다.                        |
| Controller | - Model과 View의 중계역할<br />- 사용자의 요청을 받아 Model에 변경된 상태를 반영하고 응답하기 위한 View를 선택한다. |





#### [#](https://gyoogle.dev/blog/interview/웹.html#mvc1이랑-mvc2-패턴-차이에-대해-설명해주세요)MVC1이랑 MVC2 패턴 차이에 대해 설명해주세요.

모델1은 JSP페이지 안에서 로직 처리를 위해 자바 코드가 함께 사용됩니다. 요청이 오면, 직접 자바빈이나 클래스를 이용해 작업을 처리하고, 이를 클라이언트에 출력해줍니다. 구조가 단순한 장점이 있지만, JSP 내에서 html 코드와 자바 코드가 같이 사용되면서 복잡해지고 유지보수가 어려운 단점이 있습니다.

모델2는 이와는 다르게 모든 처리를 JSP에서만 담당하는 것이 아니라 서블릿을 만들어 역할 분담을 하는 패턴입니다. 요청 결과를 출력해주는 뷰만 JSP가 담당하고, 흐름을 제어해주고 비즈니스 로직에 해당하는 컨트롤러의 역할을 서블릿이 담당하게 됩니다. 이처럼 역할을 분담하면서 유지보수가 용이해지는 장점이 있지만 습득하기 힘들고 구조가 복잡해지는 단점도 있습니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#스프링-mvc-구조-흐름에-대해-과정대로-설명해보세요)스프링 MVC 구조 흐름에 대해 과정대로 설명해보세요.

- DispatcherServlet

  - Spring MVC Framework의 Front Controller, 웹요청과 응답의 Life Cycle을 주관한다.

- HandlerMapping

  - 웹요청시 해당 URL을 어떤 Controller가 처리할지 결정한다.

- Controller

  - 비지니스 로직을 수행하고 결과 데이터를 ModelAndView에 반영한다.

- ModelAndView

  - Controller가 수행결과를 반영하는 Model데이터 객체와 이동할 체이지 정보(또는 View객체)로 이루어져 있다.

- ViewResolver

  - 어떤 View를 선택할지 결정한다.

- View

  - 결과 데이터인 Model객체를 display한다.

- ![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010163508961.png)

- ![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201010163723599.png)

- 우선, 디스패처 서블릿이 클라이언트로부터 요청을 받으면, 이를 요청할 핸들러 이름을 알기 위해 핸들러맵핑에게 물어봅니다.

  핸들러맵핑은 요청 url을 보고 핸들러 이름을 디스패처 서블릿에게 알려줍니다. 이때 핸들러를 실행하기 전/후에 처리할 것들을 인터셉터로 만들어 줍니다.

  디스패처 서블릿은 해당 핸들러에게 제어권을 넘겨주고, 이 핸들러는 응답에 필요한 서비스를 호출하고 렌더링해야 하는 뷰 이름을 판단하여 디스패처 서블릿에게 전송해줍니다.

  디스패처 서블릿은 받은 뷰 이름을 뷰 리졸버에게 전달해 응답에 필요한 뷰를 만들라고 명령합니다.

  이때 해당하는 뷰는 디스패처 서블릿에게 받은 모델과 컨트롤러를 활용해 원하는 응답을 생성해서 다시 보내줍니다.

  디스패처 서블릿은 뷰로부터 받은 것을 클라이언트에게 응답해줍니다

  



#### [#](https://gyoogle.dev/blog/interview/웹.html#스프링-필터랑-인터셉터의-차이점은-뭔가요)스프링 필터랑 인터셉터의 차이점은 뭔가요?

- 실행되는 시점이 다르다.
- FIlter는 Web Application에 동록, Interceptor는 Spring의 Context에 등록
- Filter에서 예외가 발생하면 Web Application에서 처리해야 한다.
- Intercept에서 예외가 발생하면 `@ControllerAdvice`에서 `@ExcwptionHandler`를 사용해서 예외 처리 할 수 있다. 

필터와 인터셉터는 실행되는 시점에서 차이가 있습니다. 필터는 웹 애플리케이션에 등록을 하고, 인터셉터는 스프링의 context에 등록을 합니다. 따라서 컨트롤러에 들어가기 전 작업을 처리하기 위해 사용하는 공통점이 있지만, 호출되는 시점에서 차이가 존재합니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#ioc란)IOC란?

IOC란, 인스턴스의 생성부터 소멸까지 개발자가 아닌 컨테이너가 대신 관리해주는 것을 말합니다. 인스턴스 생성의 제어를 서블릿과 같은 bean을 관리해주는 컨테이너가 관리합니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#dispatcher-servlet이란)Dispatcher-Servlet이란?

서블릿 컨테이너에서 HTTP 프로토콜을 통해 들어오는 모든 요청을 제일 앞에서 처리해주는 프론트 컨트롤러를 말합니다.

따라서 서버가 받기 전에, 공통처리 작업을 디스패처 서블릿이 처리해주고 적절한 세부 컨트롤러로 작업을 위임해줍니다.

디스패처 서블릿이 처리하는 url 패턴을 지정해줘야 하는데, 일반적으로는 .mvc와 같은 패턴으로 처리하라고 미리 지정해줍니다.

디스패처 서블릿으로 인해 web.xml이 가진 역할이 상당히 축소되었습니다. 기존에는 모든 서블릿을 url 매핑 활용을 위해 모두 web.xml에 등록해 주었지만, 디스패처 서블릿은 그 전에 모든 요청을 핸들링해주면서 작업을 편리하게 할 수 있도록 도와줍니다. 또한 이 서블릿을 통해 MVC를 사용할 수 있기 때문에 웹 개발 시 큰 장점을 가져다 줍니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#di-dependency-injection-란)DI(Dependency Injection)란?

스프링 컨테이너가 지원하는 핵심 개념 중 하나로, 설정 파일을 통해 객체간의 의존관계를 설정하는 역할을 합니다.

각 클래스 사이에 필요로 하는 의존관계를 Bean 설정 정보 바탕으로 컨테이너가 자동으로 연결합니다.

객체는 직접 의존하고 있는 객체를 생성하거나 검색할 필요가 없으므로 코드 관리가 쉬워지는 장점이 있습니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#aop-aspect-oriented-programming-란)AOP(Aspect Oriented Programming)란?

공통의 관심 사항을 적용해서 발생하는 의존 관계의 복잡성과 코드 중복을 해소해줍니다.

각 클래스에서 공통 관심 사항을 구현한 모듈에 대한 의존관계를 갖기 보단, Aspect를 이용해 핵심 로직을 구현한 각 클래스에 공통 기능을 적용합니다.

간단한 설정만으로도 공통 기능을 여러 클래스에 적용할 수 있는 장점이 있으며 핵심 로직 코드를 수정하지 않고도 웹 애플리케이션의 보안, 로깅, 트랜잭션과 같은 공통 관심 사항을 AOP를 이용해 간단하게 적용할 수 있습니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#aop-용어들을-설명해보세요)AOP 용어들을 설명해보세요

Advice : 언제 공통 관심기능을 핵심 로직에 적용할지 정의

Joinpoint : Advice를 적용이 가능한 지점을 의미 (before, after 등등)

Pointcut : Joinpoint의 부분집합으로, 실제로 Advice가 적용되는 Joinpoint를 나타냄

Weaving : Advice를 핵심 로직코드에 적용하는 것

Aspect : 여러 객체에 공통으로 적용되는 공통 관심 사항을 말함. 트랜잭션이나 보안 등이 Aspect의 좋은 예





#### [#](https://gyoogle.dev/blog/interview/웹.html#dao-data-access-object-란)DAO(Data Access Object)란?

DB에 데이터를 조회하거나 조작하는 기능들을 전담합니다.

Mybatis를 이용할 때는, mapper.xml에 쿼리문을 작성하고 이를 mapper 클래스에서 받아와 DAO에게 넘겨주는 식으로 구현합니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#annotation이란)Annotation이란?

소스코드에 @어노테이션의 형태로 표현하며 클래스, 필드, 메소드의 선언부에 적용할 수 있는 특정기능이 부여된 표현법을 말합니다.

애플리케이션 규모가 커질수록, xml 환경설정이 매우 복잡해지는데 이러한 어려움을 개선시키기 위해 자바 파일에 어노테이션을 적용해서 개발자가 설정 파일 작업을 할 때 발생시키는 오류를 최소화해주는 역할을 합니다.

어노테이션 사용으로 소스 코드에 메타데이터를 보관할 수 있고, 컴파일 타임의 체크뿐 아니라 어노테이션 API를 사용해 코드 가독성도 높여줍니다.

- @Controller : dispatcher-servlet.xml에서 bean 태그로 정의하는 것과 같음.
- @RequestMapping : 특정 메소드에서 요청되는 URL과 매칭시키는 어노테이션
- @Autowired : 자동으로 의존성 주입하기 위한 어노테이션
- @Service : 비즈니스 로직 처리하는 서비스 클래스에 등록
- @Repository : DAO에 등록





#### [#](https://gyoogle.dev/blog/interview/웹.html#spring-jdbc란)Spring JDBC란?

- 기존의 JDBC장점과 단순성을 그대로 유지하면서도 단점을 극복할 수 있게 해준다.
- 내부적으로 반복적인 작업들을 대신 해줌
- Connection과 관련된 모든 작업을 알아서 진행(커넥션 열고 닫기)
- Spring JDBC를 사용하려면 먼저, DB커넥션을 가져오는 DataSource를 Bean으로 등록해야 한다.

- 데이터베이스 테이블과, 자바 객체 사이의 단순한 매핑을 간단한 설정을 통해 처리하는 것

- 기존의 JDBC에서는 구현하고 싶은 로직마다 필요한 SQL문이 모두 달랐고, 이에 필요한 Connection, PrepareStatement, ResultSet 등을 생성하고 Exception 처리도 모두 해야하는 번거러움이 존재했습니다.

- Spring에서는 JDBC와 ORM 프레임워크를 직접 지원하기 때문에 따로 작성하지 않아도 모두 다 처리해주는 장점이 있습니다.





#### [#](https://gyoogle.dev/blog/interview/웹.html#mybatis란)MyBatis란?

- 자바 오프젝트와 SQL문 사이의 자동 Mapping 기능을 지원하는 ORM프레임워크

- 복잡한 JDBC코드를 걷어내 깔끔한 소스코드를 유지할 수 있다.

- SQL을 XML파일로 관리

- java소스에서 XML태그의 id만 호출

- sqlSession을 통해 mapper를 불러서 사용한다.

- ![](https://t1.daumcdn.net/cfile/tistory/9994DE355C7222C802?download)

- 	@Repository
  	public class FundingAnswerDAOImpl implements FundingAnswerDAO {
  		@Autowired
  		private SqlSession session;
  	
  		@Override
  		public int contentInsert(FundingAnswer fundingAnswer) {
  			return session.insert("fundingAnswerMapper.contentInsert", fundingAnswer);
  		}
  	

- 설정파일로 분리하면, 수정할 때 설정파일만 건드리면 되므로 유지보수에 매우 좋습니다.

- 매개변수나 리턴 타입으로 매핑되는 모든 DTO에 관련된 부분도 모두 설정파일에서 작업할 수 있는 장점이 있습니다.

- fundingmapper.xml(Sql구문이 있는 파일)![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201011161756466.png)

- fundingDAOImpl.java![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201011161838531.png)

- mybatis-context.xml(mybatis설정관련 파일)![](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20201011162050397.png)

