

- DNS의 작동 원리는 아래 그림과 같다 
  - 여러 탑레벨,세컨드 레벨 도메인 네임서버를 거쳐, 목적지 IP를 받아옴
  
![Alt text](../etc/image3/DNS%EC%84%9C%EB%B2%84%EC%9E%91%EB%8F%99%EC%9B%90%EB%A6%AC.png)


--------------------

## AWS Route 53


- `EC2는 DNS의 별칭을 사용할 수 없음`
  - IP는 괜찮음






-----------------------------------

## AWS Route 53 라우팅 - 헬스체크

- DNS의 장애 조치를 자동화하기 위한 사전 작업
- 헬스 체크 지표는 클라우드 와치나 직접 구성도 가능함
  - 헬스체크 직접 구성에 HTTP/S, TCP 가능함
  - 서버 반환값이 상태 코드일 경우, 200이나 300처럼 지정가능 (성공 상태)
  - 서버 반환값이 `텍스트일 경우 앞부분 5120Byte 확인`해서 판단 도 함

![Alt text](../etc/image3/route53-%ED%97%AC%EC%8A%A4%EC%B2%B4%ED%81%AC1.png)

<br><br><br><br>

- 헬스 체크를 그룹화 하여 관리도 가능
  - 예를 들어, 서울리전에 인스턴스 100개중 30개만 헬스체크 성공하면 성공 판단

![Alt text](../etc/image3/route53-%ED%97%AC%EC%8A%A4%EC%B2%B4%ED%81%AC2.png)


- 프라이빗존에 AWS 리소스가 있을 경우, 클라우드 워치 + 알람으로 헬스체크 기능 할 수 있음
  - 왜 이렇게함? -> `퍼블릭 엔드 포인트를 알 수 없으니까`

![Alt text](../etc/image3/route53-%ED%97%AC%EC%8A%A4%EC%B2%B4%ED%81%AC3.png)



-------------------

## AWS Route 53 라우팅 - Failover 장애조치 라우팅

- 기본적으로 `Active-Passive` 형태임, 본 서버(Primary)가 돌고, 세컨 서버는 대기 
- 본서버와, 보조서버가 각각 하나씩만 있음

![Alt text](../etc/image3/route53-%EB%9D%BC%EC%9A%B0%ED%8C%85-%EC%9E%A5%EC%95%A0%EC%A1%B0%EC%B9%981.png)


![Alt text](../etc/image3/route53-%EB%9D%BC%EC%9A%B0%ED%8C%85-%EC%9E%A5%EC%95%A0%EC%A1%B0%EC%B9%982.png)


----------------

## AWS Route 53 라우팅 - Geolocation 지리기반 라우팅

- `사용자 위치를 기반`으로 라우팅
- 디폴트 리젼은 있어야함



------------------------

## AWS Route 53 라우팅 - Geoproximity 정책 지리 근접 라우팅

- 위치기반 + 가중치 라우팅


-------------------------

## AWS Route 53 라우팅 - IP-based

- IP 주소를 기반으로 라우팅 -> CIDR 블록 지정


---------------------------------

## AWS Route 53 라우팅 - multi-Value 다중값 라우팅

- `DNS 쿼리 결과를 다중 값으로 주는거임`
  - 최대 `8개` 레코드 반환 


