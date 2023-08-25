 ## AWS CloudWatch 메트릭


 - Ec2에 대한 기본 모니터링은 `5분 간격`, detailed(세부) monitoring 활성화 하면 `1분 간격`

- 사용자 지정 매트릭
  - `PutMetricData` API를 이용해서 사용자 메트릭을 푸시
  - StorageResolution API를 사용해 메트릭 캡쳐 간격을 조절
    - 캡쳐 기본값은 `1분`,  `1/5/10/30 초의 값 조절을 통해 수정 가능`
  - 푸시하는 방향이 `과거,미래 상관없음(중요!)`
    - 2시간 앞으로 푸시 해도, 2시간 뒤 자료로 볼 수있고, 클라우드와치에는 아무런 오류가 없음

------------------------

## AWS CloudWatch 로그


- 클라우드 와치 로그에이전트(`구식`), 클라우드와치 통합 에이전트(`최신`)을 이용해서 로그를 수집 할 수 있다. 
  - 단, `Ec2가 클라우드와치에 대한 IAM 역할이 있어야함`

- `ECS 와 Beanstalk은 기본적으로 로그 수집`을 한다

- 로그 필터를 통해, 특정 문구(예 ERROR)같은 로그만 볼 수 있다
- `logs insights를 통해 로그를 쿼리`하고 대시보디에 추가 가능



- 클라우드 워치 로그 `데이터 내보내기`
  - S3
    - 내보내기에 최대 12시간 까지 소요
    - `CreateExportTask API`를 사용함
    - `데이터 스트리밍이 불가능함`
  - CW 구독 필터(`Subscription Filter`)
    - S3와는 다르게 돈이 들지만, 빠르게 로그 스트리밍 가능

![Alt text](../etc/image3/cw_%EA%B5%AC%EB%8F%85%ED%95%84%ED%84%B01.png)


- 로그 다계정 통합도 가능함

![Alt text](../etc/image3/cw_%EB%8B%A4%EA%B3%84%EC%A0%95%ED%86%B5%ED%95%A9.png)




- 클라우드와치 알람
  - 소스는 메트릭이다.
    - 로그기반 알람을 생성하려면 `로그 -> 매트릭으로 변환` 한다음 알람
  - 알람 상태 3가지
    - OK (아무이상없음)
    - INSUFFICIENT_DATA (판단 데이터 부족)
    - ALARM (알람)

- 클라우드와치 `복합 알람`
  - 다수의 알람상태를 통합해 최종 결정을 내림
    - 알람의 노이즈를 줄일때 사용
  - `AND`와 `OR`를 조건사용 가능

![Alt text](../etc/image3/cw_%EB%B3%B5%ED%95%A9%EC%95%8C%EB%9E%8C.png)



-------------------


## AWS CloudWatch Synthetics Canary

- python, Node.js으로 작성되는 스크립트
- 일종의 `애플리케이션의 전반적인 상태확인 스크립트`
  - 사이트 제목 클릭, 장바구니 물건 추가 등
- Synthetics Canary 블루 프린트 제공 종류는 다음과 같다
  - HeartBeat Monitor 
    - URL 상태확인
  - API Canary
    - REST API 상태 확인
  - Broken Link checker
    - 인터넷 사이트 링크 테스트
  - Visual Monitoring
    - 베이스 스크린샷과 다른지 비교
  - `Canary Recoder`
    - 웹사이트에서의 동작을 기록하고, 스크립트를 자동으로 짜줌
  - `GUI Workflow Build`
    - 웹페이지에서 GUI기반으로 직접 액션함



----------------

## AWS EventBridge


- 이벤트 버스를 만들어야함 
- 아카이빙을 통해서, `이벤트 재현이 가능함`
- 서비스 자체에서 버스내 `이벤트를 분석하고, 스키마를 추론함`?






























