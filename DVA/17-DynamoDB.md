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
    - 쓰는 만큼 나옴 (`하지만 프로비저닝모드보다는 비쌈`)




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



























