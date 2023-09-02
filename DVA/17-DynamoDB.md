## AWS DynamoDB

- 완전관리형 서비스
- NoSQL 기반이기에 `SUM,AVG 등 집계 연산 불가능`
- 다이나모DB는 수평적 확장을 함
- 다이나모DB도 스탠다드, `Infreequent Access(IA)` `두 가지 테이블 클래스가 있음`
- 테이블에서 아이템의 최대값은 `400KB` (행 데이터)






- 파티션키 - 중요 (`해쉬 전략`)
  - 아이템(행 데이터)의 `유니크한 값`

![Alt text](../etc/image3/dynamo_%ED%8C%8C%ED%8B%B0%EC%85%98%ED%82%A41.png)

- 정렬 키 - 옵션
  - 파티션키와 조합하여, primary key(기본키)를 생성

![Alt text](../etc/image3/dynamo_%ED%8C%8C%ED%8B%B0%EC%85%98%ED%82%A42.png)






-------------------------------

## AWS DynamoDB 실습

- `DB를 만드는것이 아니라, 테이블을 만드는것임`

![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B51.png)
![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B52.png)
![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B53.png)
![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B54.png)






- AWS 한글버젼에서는 아이템 -> `항목`으로 행 데이터를 추가 가능

![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B55.png)
![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B56.png)
![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B57.png)









- 만약 같은 `파티션키만`를 이용해 생성하면 오류남

![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B58.png)













- `테이블에 정렬키가 있으면, 파티션키 데이터가 같아도 상관 없음`
  - 즉, 파티션키와 정렬키가 다르기만 하면 됨

![Alt text](../etc/image3/dynamo_%EC%8B%A4%EC%8A%B59.png)




----------------------------------------

## AWS DynamoDB WCU / RCU

- DynamoDB 읽기/쓰기 용량 모드가 있음
  - `24시간 마다 프로비저닝 <-> 온디맨드 바꿀 수 있음`


  - 프로비저닝 모드
    - 오토 스케일링 지원
    - 미리 자원을 지정, 지정해둔 용량보다 넘어서도 `burst capacity(버스팅 용량)`으로 일시적으로 사용가능함
      - 버스팅 용량이 다 소진되면, `ProvisionedThroughputExceededException` 에러 발생함 (프로비저닝 처리량 초과 예외)



  - 온디멘드 모드
    - 읽기 쓰기 모드가 `자동으로 업/다운`
    - 쓰는 만큼 나옴 (`프로비저닝보다 2.5배 비쌈`)




- WCU 계산방법 
  - 초당 1KB 쓰기 = 용량 1
  - 초당 0.5KB라면 올림 함
  - 예시
    - 만약 초당 여러 사람들이 총합 3KB를 쓰면 WCU = 3 예약해야됨
    - 초당 1.5KB 쓰면(`올림`해서), `2 WCU 사용`









- DynamoDB `읽기모드`는 2가지 모드가 있음
  - Eventually Consistent Read (최종적 일관된 읽기 모드) - `기본값`
    - 다이나모DB에서 `데이터`를 쓰기 후, 분산된 DB에 복제가 진행 안됬을 경우 데이터를 못 읽을 수도 있음 (`데이터를 쓰고 100ms내 읽기 상황`)



  - Strongly Consistent Read (강력한 읽관된 읽기 모드)
    - 방금 막 쓴 데이터를 읽을 경우 사용
    - 다이나모DB API에서 `ConsistentRead`라는 변수 = `True`로 둬야함
    - 방식은 `RCU를 2번 진행하기 떄문임`


![Alt text](../etc/image3/dynamo_RCU1.png)





- RCU 계산 방식
  - 4KB (강력한 읽기 기준)
  - `4KB 기준으로 올림함`

![Alt text](../etc/image3/dynamo_RCU2.png)









- DynamoDB 파티션 분배
  - 다이나모 DB를 검색전, `파티션키는 해시 함수를 통해 분산된다`
  - 그래서 파티션 분배에 관한 공식이 있지만, 굳이 외우지 않아도 됨
  - `RCU와 WCU는 파티션 수에 걸쳐 고르게 분배됨`

![Alt text](../etc/image3/dynamo_%ED%8C%8C%ED%8B%B0%EC%85%981.png)





- 다이나모DB 처리량 에러
  - `ProvisionedThroughputExceededException`에러 발생함
  - 원인
    - 핫 키 (파티션키)
    - 핫 파티션
    - 아주 큰 아이템(항목) -> RCU와 WCU 보다 넘는 많은 아이템들을 쓰기/읽기 작업을 하려는 경우


  - 해결법
    - 지수 백오프 전략 사용
    - 파티션키를 최대한 많이 분산해서 구성
    - 읽기 작업일 경우, DAX (DynamoDB Accelerator) 사용


-----------------------------------------------
## AWS DynamoDB API

- 쓰기 API
  - putitem
    - 기본키가 같은 새 항목(아이템)을 만들거나, `완전히 교체/업데이트`


  - Updateitem
    - 기존 항목의 속성을 편집, 기존항목이 없으면 새항목 추가
    - 속성 몇가지만 편집할뿐, `모든 속성을 업데이트 하진 않음` => 변경된 사항만 저장
    - Atomic counters 와 함께 사용


  - Conditional Writes
    - 조건이 충족되엇을때만 쓰기/업데이트/삭제 가능
    - 아이템에 동시 접근시 사용하면 도움이 됨
    - 다이나모 성능에 아무런 영향이 없음






- 읽기 API
  - Getitem
    - 기본키를 기반으로 데이터 읽음
    - 기본키 + 정렬키로도 읽음
    - 읽기는 2가지 모드로 됨, 최종적 일관된 읽기, 강력한 일관된 읽기
    - API에 `ProjectionExpression` 적용 가능, `이값을 통해 아이템의 속성 몇가지만 받을 수도 있음`


  - DB 쿼리
    - KeyConditionExpression
      - 파티션 키 or 정렬키를 통해 데이터 쿼리 가능
    - FilterExpression
      - 쿼리 데이터가 반환되기전 필터링 수행
      - `파티션키 + 정렬키 사용 못함`
      - 오직 non-key 속성에 사용할 수 있음
    - 쿼리는 아이템(항목)을 반환 하는데, `Limit` 매개변수에 따라 가져올 수 있는 항목 수가 제한됨
    - 리턴하는 항목들의 `최대 크기는 1MB임`
      - 더 가져오고 싶으면, pagination(페이지형태)로 가져올 수는 있음
    - `로컬 보조인덱스, 글로벌 보조 인덱스 쿼리 가능`


  - DB Scan 
    - 쿼리가 특정한 파티션키, 정렬키로 데이터를 불러오는 것이라면, `Scan은 테이블 전체를 읽음`
    - 스캔도 최대 1MB 데이터를 반환함, 똑같이 페이지형태로 다 가져올 수는 있음
    - 병렬 Scan 지원
    - FilterExpression와 ProjectionExpression 함께 사용도 가능함




- 삭제 API
  - Deleteitem
    - 항목 삭제
    - 조건부 삭제도 가능함

  - DelteTable
    - 테이블에 있는 모든걸 삭제
    - 테이블 삭제가 아님!, `테이블에 있는 모든 항목 삭제임`






- 배치 작업
  - 배치작업 => 일괄작업이라, 어떤 작업은 실패할 수도 있지만, 실패한 작업 항목은 다시시도하면됨

  - BatchWriteItem
    - 호출 한번에 `최대 25번의 putitem 또는 deleteitem 실행 가능` (updateitem 실행 불가)
    - `최대 16MB 데이터를 기록`, 항목마다 400KB는 같음
    - 항목을 업데이트는 불가 => 데이터를 갈아치우는것 이지 업데이트가 아님 (따로 updateitem 써야함)
    - 쓰기 작업이 실패하면 `Unprocesseditems`라는 것을 사용해, 지수백오프 전략으로 쓰기 배치를 지속적으로 수행 가능

  - BatchGetitem
    - 하나이상의 테이블에서 항목이 반환되며, `최대 100개의 항목과 16MB 데이터만 가능`
      - 병렬로 읽기가 됨
    - 읽기 작업이 실패하면 `UnprocessedKeys`라는 것을 사용해, 지수백오프 전략으로 읽기 배치를 지속적으로 수행 가능




- partiQL
  - 다이나모 DB에서 SQL 쿼리를 실행하는 API
  - 파티QL로 `여러테이블의 항목 삽입/출력/삭제 가능` 
    - `단, Join은 안됨`











































