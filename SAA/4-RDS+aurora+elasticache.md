----------------------------
## RDS

<br>

제공되는 제품군은

```
postgres
mysql
mariadb
oracle
microsoft sql server
```

<br>
<br>

- `오로라는 aws에서 만든(독점) 데이터베이스 이다`

<br>
<br>

왜 관리형 서비스로 RDS를 써야되? ec2 쓰면 안됨?
- 자동적으로 os 패치 업데이트, 프로비저닝을 aws에서 해줌
- 백업,복구,모니터링도 aws에서 해줌
- 수평, 수직 스케일링도 가능
- 서비스에서 사용하는 RDS 스토리지는 EBS임 (`gp2 또는 io1` 유형의 볼륨을 가짐)
- EBS니까 당연, `RDS 스냅샷`도 만들 수 있음
- `하지만 ec2처럼 SSH로 인스턴스에 직접 접근을 할수가 없다!!!!!!!!!!!!`


RDS 스토리지 오토 스케일링
- RDS 오토스케일링이 감지해서 `스토리지를 확장해줌`
  - 예) 빈공간 10% 이하면 확장하도록 설정
- 무한대로 늘어나는걸 방지하기 위해, 최대 사이즈는 정해줘야함


<br>
<br>
<br>

-------------------------------
## RDS 읽기 복제본과 멀티 AZ

읽기 전용 복제본
- 읽기만 가능 (쓰기 X)
- `최대 15개` 까지 만들수 있음 (`다른 리전, AZ에도 생성 가능`) 
- 마스터 RDS (읽기/쓰기 가능한)와 읽기 복제본 사이에는 `비동기 복제`가 발생함 
- 읽기복사본을 -> `RDB DB로 승격 할 수도 있음`

![Alt text](../etc/image2/rds%EC%9D%BD%EA%B8%B0%EB%B3%B5%EC%A0%9C%EB%B3%B81.png)


읽기 복사 네트워크 트래픽 비용
- 다른 AZ 비동기 복사는 무료
- 다른 리전은 유료

![Alt text](../etc/image2/rds%EC%9D%BD%EA%B8%B0%EB%B3%B5%EC%A0%9C%EB%B3%B82.png)







멀티 AZ 운영
- `주로 재해 복구에 사용 (고가용성)`
- 마스터 DB, 스탠바이 DB로 구성 (스탠바이는 오직, `대기 목적만 수행, 읽고 쓰기 안됨`)
- 읽기 복제본과 다르게 `동기식 복사`를 통해 스탠바이 DB 구성
- one dns name을 갖기 때문에 마스터 DB가 죽어도 DNS는 안바뀜
- 장애 조치는 따로 필요없음, 마스터가 죽으면, 스탠바이가 승격됨
- 싱글 AZ -> 멀티 AZ `바꿀 수 있음`
- *`멀티 AZ 클러스터`*  와는 다른 개념임
- 멀티 AZ는 활성화 상태의 데이터베이스 종류와 상관 없이 `동일한 연결 문자열`을 유지

![Alt text](../etc/image2/rds%EC%9D%BD%EA%B8%B0%EB%B3%B5%EC%A0%9C%EB%B3%B83.png)



--------------------
## RDS Custom

- RDS에서는 운영체제나 사용자 지정 기능을 엑세스 할 수 없었지만, `RDS Custom`에서는 가능함
- `MSSQL, Oracle`만 커스텀 가능
- OS 및 DB 사용자 지정 기능 액세스 할 수 있음
  - DB 내부 구성 설정, 패치 적용, SSH 또는 SSM사용해 인스턴스에 접근 가능
  - 커스텀으로 운영하려면, AWS에서 관리하는 `Automation mode를 꺼두는게 좋음`

![Alt text](../etc/image2/rds%EC%BB%A4%EC%8A%A4%ED%85%80.png)


----------------------

## RDS 공동 책임 모델

<br>

AWS 책임
- 빠른 프로비저닝
- `오토 백업, 복구, 업그레이드, 운영 패치` 등 사용자 책임이 아니라, AWS 책임이 된다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
- `모니터링, 알림 또한 aws` 책임이다
- 왜냐하면 `완전 관리형` 서비스 이기 때문이다

<br>
<br>

물론, ec2로 사용자가 직접 구성 할 수 있으나.... 복원 백업, 패치 등은 사용자 책임이 된다 = `AWS 완전관리형이 아님`

<br>

----------


## AWS Aurora - 오로라

<br>

- `AWS에서 만든 데이터베이스`
- RDS와 엔진의 동작 방식은 똑같음, 하지만 `RDS의 다중 AZ처럼 운영됨`
  - 즉, 마스터 DB(읽기/쓰기 가능)와 읽기전용 DB가 있음
  - 읽기 전용 복제본들은, `리전간 복제를 지원`
- 지원 기술은 `mysql,  postgresql` 두가지만 지원함
- 오로라는 `RDS` 성능보다 3~5배 향상된 퍼포먼스를 제공함
- DB 스토리지는 자동적으로 확장함 `10GB로 시작해서`, `128TB까지`
  - 스케일링을 수동으로 설정안해줘서 좋음
  - 단일 볼륨에 사용하지 않고, 수백개의 볼륨 사용 (`스토리지를 분산하여 사용함`)
- RDS보다 20%비쌈....... 그리고 프리티어가 아님...
- `읽기 복제본 15개`까지 가능
- 장애 복구가, 다중 AZ RDS 보다 `빠름`
- DB복제한다고 해서 성능 이슈는 없음


![Alt text](../etc/image2/%EC%98%A4%EB%A1%9C%EB%9D%BC1.png)




오로라의 고가용성의 예
- 내가 DB에 무슨일을 할 때마다, `3AZ에서 6개의` 복제본이 활성화됨
- 장애가 터지면, Peer-to-peer 복제를 백엔드에서 자동으로 진행됨


Peer to Peer
- 중앙 서버를 거치지 않고 `클라이언트 컴퓨터끼리 직접 통신`하는 방식을 통칭한다.





오로라 DB 클러스터
- `쓰기/읽기 엔드포인트가 존재함`
- `사용자 지정 엔드포인트`로 DB 사용을 조절 할 수 있음

![Alt text](../etc/image2/rds%EC%BB%A4%EC%8A%A4%ED%85%80.png)


![Alt text](../etc/image2/%EC%98%A4%EB%A1%9C%EB%9D%BC2.png)



오로라 서버리스
- 용량을 미리 안정해도 됨
- 비정기적, 간헐적, 예측 불허한 워크로드에 적합
- 매 초당 비용 지불



![Alt text](../etc/image2/rds%EC%BB%A4%EC%8A%A4%ED%85%80%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8.png)





오로라 멀티 마스터
- 마스터 여러개


오로라 글로벌 DB
- 모든 쓰기 및 읽기는 `하나의 기본 리전에서` 진행
- 읽기전용 리전을 `5개`까지 설정 할 수 있고, `1초 미만으로 마스터 <-> 읽기전용 복제됨`
  - 각 리전마다 `16개` 까지 복제본 생성 가능



오로라 머신러닝
- AWS내의 머신 러닝 서비스와 통합을 지원함
- `세이지 메이커, comprehend`
- 예) 쿼리 치면 -> 답변줌

![Alt text](../etc/image2/rds%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%ED%86%B5%ED%95%A9.png)



<정리 정돈 필요>





<br>
<br>


-------------------------
## RDS&오로라 Backups


RDS 백업
- 자동 백업
  - 매일 `DB 전체 백업`
  - 5분마다 트랜잭션 로그 백업
    -` 5분전 어떤 시점으로도 복구 가능`
  - 백업 유지 기간은 `1~35`일, `0`일을 설정해서 비활성화도 가능
- 수동 백업 - DB 스냅샷
  - 원하는만큼 `오랫동안 보존 가능`



오로라 백업
- 자동 백업
  - 백업 유지 기간은 `1~35`일, `비활성화는 없음`
  - 정해진 `시간 범위 내의` 어떤 시점으로든 복구 가능
- 수동 백업 - 스냅샷
  - RDS랑 같음

RDS&오로라 복구
- `S3로 부터 mysql RDS 복원 가능`
  - 온프라미스 디비 백업
  - 백업파일을 s3에 업로드
  - RDS로 복구 하면 됨
- `S3로 부터 mysql 오로라 복원 가능`
  - 온프라미스 디비 백업, `percona Xtrabackup 소프트웨어 사용하면` 됨
  - 파일을 s3에 업로드
  - 오로라로 복구



------------------------------
## RDS & 오로라 보안

- RDS와 오로라는 KSM을 사용해 마스터와, 모든 복제본들의 저장 데이터가 암호화 됨
  - DB를 처음 만들때 `암호화 옵션은 선택임`
  - `마스터 DB가 암호화 안되어있으면 -> 읽기 복제본도 암호화`는 할 수 없음
- 클라이언트와 DB강의 TLS 즉, `전송중 암호화`는 기본적으로 되어있음
- `IAM 역할`을 이용해 DB 접속 가능
- `보안 그룹`을 사용해 네트워크 엑세스 통제
  - 특정 포트, IP 허용 및 차단
- `audit log`(감사 로그)를 활성화 시키면, 클라우드 와치에 로그 남음, `장기간 보관`하고 싶으면 s3에 보내야함


-----------------------
## RDS proxy

- RDS 프록시는 `서버리스`, `오토스케일링 가능하고`, `고가용성임`
- `Mysql, postgreSQL, 마리아DB` 지원
- 프록시는 `DB에 IAM 인증을 통해서만 인스턴스 - RDS 접근 가능` (IAM 인증강제)
  - AWS `secrets manager`에 자격증명 보관됨
  - `퍼블릭 액세스 절대로 불가`
- 왜 DB 프록시가 필요한가?
  - 애플리케이션내에서 `DB 커넥션 풀을 형성하고, 공유 할 수 있음` -> 연결 간소화
  - 프록시에서 DB 접근을 모아서, DB 자원사용에 대한 부담을 줄일 수 있음
  - 장애난 DB `알아서 걸러줌`



![Alt text](../etc/image2/rds%ED%94%84%EB%A1%9D%EC%8B%9C.png)


----------------------------
## AWS Elasticache - 엘라스틱 캐시


- `레디스`를 예로 들수있고, 인메모리 데이터 베이스라, 짧은 지연시간 = 높은 성능을 자랑한다
- 예전에 hit한 쿼리를 저장하고 있다가, 똑같이 불러와줌 (똑같은 쿼리는 검색안해도 됨)
- `완전 관리형`
- `RDS 부하를 줄이는데 도움`
- 문제에 인메모리 관련 내용 나오면, 무조건 엘라스틱 캐시임
- 엘라스틱 캐시는 `IAM 인증을 지원하지 않음` 

 
![Alt text](../etc/image2/%EC%97%98%EB%9D%BC%EC%8A%A4%ED%8B%B1%EC%BA%90%EC%8B%9C.png)


Redis
- `읽기 복제본, 고가용성`
- AOF를 사용해 데이터 내구성 확보, 백업과 복원 기능 있음
- redis를 생성할때 비밀번호나 토큰 설정 가능
- SSL 보안 지원 가능
- 게임 리더보드
  - 레디스는 기본적으로 데이터가 정렬되어 운영된다

Memcached
- 다중 노드 파티셔닝 사용( sharding - 샤딩 )
- 가용성 X, 복제도 안함, 지속적인 캐시가 아님
- 노 백업, 노 복원, 멀티 스레드 아키텍쳐임
- SASL이라는 SSL보다 상위 버젼의 인증을 함



엘라스틱 캐시 패턴
- Lazy Loading
  - 모든 읽기 데이터가 캐시됨 
  - 캐시 히트없을때 발생
- write through 
  - DB에서 데이터를 업데이트할 때마다, 캐시에 데이터를 추가하거나 업데이트
- Session store
  - 인터넷 접속의 세션 저장소로 활용 가능






![Alt text](../etc/image2/%EC%97%98%EB%9D%BC%EC%8A%A4%ED%8B%B1%EC%BA%90%EC%8B%9C2.png)


<br>
<br>
<br>

---------------------






