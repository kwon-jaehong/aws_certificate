## AWS CloudFront

- 오리진 가능
  - S3, `Ec2, ALB` 등
  - Ec2를 오리진으로 했을때는 `Ec2가 퍼블릭` 이여야 한다
    - CloudFront는 (프라이빗) VPC연결을 할 수 없으니까!

![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%EC%98%A4%EB%A6%AC%EC%A7%84.png)

- CloudFront는 엣지 로케이션에 각각 저장되기 때문에, `엣지 로케이션 수만큼 캐시가 생성` 됨
  - `캐시된 객체는 Cache Key로 식별/관리`됨
    - 캐시키는 기본적으로 호스트 네임 + 리소스 URL인데, 상황에따라 복잡하게 설정 가능
    - `캐시 키에 추가한 모든 HTTP 헤더,쿠키 쿼리 문자열은 오리진 요청에 자동으로 포함되어 전달됨`
  - 캐쉬된 객체의 TTL이 끝나기전에 `CreateInvalidation API`를 사용해서 캐쉬 무효화 할 수 있음

- 캐시 키에 추가된 정보 없이, 오리진 요청에 특별하게 보내려면? -> `오리진 요청 정책` 쓰면됨
  - 정책에서 사용자 지정 정보를 추가해서 오리진에 요청 보낼 수 있음
  - `예를 들어, API키 & 보안 헤더를 전달 할 경우`


![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%EC%BA%90%EC%8B%9C%EC%98%A4%EB%A6%AC%EC%A7%84%EC%9A%94%EC%B2%AD%EC%A0%95%EC%B1%851.png)

![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%EC%BA%90%EC%8B%9C%EB%AC%B4%ED%9A%A8%ED%99%941.png)


- CloudFront 또한 `국가 기준으로 제한` 할 수 있음

![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%EC%A7%80%EB%A6%AC%EC%A0%81%EC%A0%9C%ED%95%9C.png)


---------------------------
## CloudFront 서명 URL / 서명 쿠키

- CloudFront 배포를 `비공개로 설정`, 특정 사용자에게만 `콘텐츠 엑세스`
  - 이때 `서명 URL/쿠키`를 사용해서 제공 가능

- 서명 URL/쿠키를 사용하려면 아래와같은 조건을 설정해야됨
  - 클라이언트 IP 범위
  - 콘텐츠 `공유 URL 만료 날짜`
  - 믿을만한 생성자 ( 쿠키나 URL을 생성할 수 있는, `AWS 계정을 의미`함)




- 클라우드 프론트 서명 URL을 만들기 위해서는 키그룹을(비대칭키) `생성` 해야됨
  - `private key는 Ec2나 애플리케이션이 사용` (`서명용`)
  - public 키만 클라우드 프론트에 등록 (`검증용`)


![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%ED%82%A4%EA%B7%B8%EB%A3%B92.png)
![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%ED%82%A4%EA%B7%B8%EB%A3%B91.png)







- URL과 쿠키 차이
  - 여러 콘텐츠(파일) 지원
    - 서명된 URL은 파일 하나당, URL 하나
      - 공유할 파일이 100개면, 서명된 URL도 100개
    - 서명된 쿠키는 여러파일에 하나의 쿠키로 관리됨
      - 공유할 파일이 100개면, 서명된 쿠키 1개

- S3 서명된 URL Vs CloudFront 서명된 URL
  - 클라우드 프론트 서명된 URL은 오리진과 상관없이 경로 엑세스를 허용함
    - 서명된 URL을 만들면서, 콘텐츠 복제되는 것 같음(`추정임`)
  - 사용자가 직접 S3에 엑세스 할려는 경우 S3 서명된 URL을 이용해야됨

![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%EC%84%9C%EB%AA%85%EB%90%9CURL.png)

- 클라우드프론트의 오리진을 그룹화할 수 있음
  - 주오리진, 보조오리진을 구성해서, `장애조치를 구현`




- 필드 수준의 암호화도 가능함
  - 아래 예시 그림은 신용카드정보를 암호화하는 개념

![Alt text](../etc/image3/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%94%84%EB%A1%A0%ED%8A%B8_%ED%95%84%EB%93%9C%EC%88%98%EC%A4%80%EC%95%94%ED%98%B8%ED%99%94.png)



- CloudFront의 `실시간 로그는 Kinesis Data Streams에 실시간 전송 가능`


