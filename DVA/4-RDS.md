## AWS RDS

-  RDS인스턴스에 기본적으로 SSH 접근 불가 (AWS 관리형이니까)
-  RDS는 `스토리지` 오토 스케일링을 지원함(물론 활성화해야됨)


<br><br><br><br>

- 읽기 전용 복제본
  - mysql, 마리아, PostgreSQL은 최대 `15개 까지 생성`, `다른 리전,AZ` 든 상관없음
  - 오라클, SQL server 는 `최대 5개까지` 생성 가능
  - 비동기 복제
  - 읽기 복제본을 -> 기본 DB로 승격도 가능은 함
  - 동일 리전의 다른 AZ일때, 복사 비용 들지 않음
  - 다른 리전일때는 비용 발생

<br><br>

- 다중 AZ 배포
  - RDB의 고가용성을 목표
  - 동기식 복제
  - 싱글-Az -> 다중-Az 전환할때, `데이터베이스 다운 타임 없음`


--------

## AWS Aurora

- `인스턴스는 설정 가능`, 하지만 스토리지 용량은 `알아서 늘어남` (프로비저닝 X)
- 장애조치는 기존 RDS 다중 AZ보다 `빠름`
- 하지만 RDS보다 20% 비쌈
- 스토리지 분산 저장 방식임 (수백개의 볼륨에 분산 저장)
- 자동 장애 복구

 
- 읽기 복제본
  - 오로라는 `15개`까지 생성 가능
  - `리전간 읽기 전용 복제본 복사 지원`
  - 읽기 복제본 오토 스케일링 기능은 활성화 시켜야함



![Alt text](../etc/image3/%EC%98%A4%EB%A1%9C%EB%9D%BC1.png)

----------------------

## RDS & Aurora 보안
- KMS를 사용해서 DB 데이터를 암호화 해야됨
- 암호화 되지 않은 DB는, 스냅샷 -> 스냅샷 암호화 복구로 진횅해야됨


--------------------------------

## RDS 프록시

- 서버리스 서비스
- RDS 프록시를 사용하면, 애플리케이션이 데이터베이스 접점을 줄일 수 있음
- RDS 프록시 서비스는 `MySQL, postgreSQL, mariaDB` 지원 (오로라도 다 지원됨)
- RDS 프록시가 `DB 인증도 대신 해줌`
- RDS 프록시는 공개적으로 엑세스 불가, `오직 VPC에서만 액세스 가능`


![Alt text](../etc/image3/%ED%94%84%EB%A1%9D%EC%8B%9C.png)


------------------
## AWS ElastiCache 

- 엘라스틱캐쉬 쓰려면, 코드를 많이 바꿔야함



엘라스틱 캐시 패턴 3가지
- `Lazy Loading / Cache-Aside / lazy Population` 
  - 캐시가 미스일때 발생함
    - 캐쉬 미스이면, 총3번의 RDS DB 호출이 일어남
  - 다른 경로로, `RDS데이터가 업데이트 되면 대응 불가` (여전히 엘라스틱은 기존 RDS 데이터 가지고 있으므로)


![Alt text](<../etc/image3/Lazy Loading.png>)
![Alt text](<../etc/image3/Lazy Loading2.png>)


- `write through` 
  - 애플리케이션이 `RDS DB를 수정할 떄마다`, 캐시에 업데이트
  - `쓰기작업에 대한 패널티 존재` (RDS 한번, 캐쉬 한번)
  - 캐시


![Alt text](<../etc/image3/write through.png>)
![Alt text](<../etc/image3/write through2.png>)


- `Cache Evictions and Time-to-live(TTL) 셋팅`
  - 이건 기법이 아니라, 설정중에 하나임
  - 캐시 메모리가 꽉 찾을때 `Cache Evictions`방법을 사용
  - LRU (recently used) - 최신 데이터 놔두기
  - 명시적으로 어떤 데이터 삭제
  - 5분간 데이터 유지


------------------------------------
## AWS MemoryDB for Redis

- `Redis와 호환되는 API가 있는 데이터 베이스`
  - 엘라스틱캐시 redis랑은 다른 서비스
- 초당 1억 6천만건의 요청을 처리하는 초고속 성능 제공
- 일종의 인메모리 RDS 오로라 느낌?
- 다중 Az 트랜잭션 지원
