## AWS CloudFormation




- CloudFormation의 `비용은 무료임`
- 파일 템플릿은 `json, yaml 지원`
- 모두 순서대로 인프라 자원이 생성됨
- `Stacks`으로 관리됨
  - 스택을 삭제하면 `클라우드포메이션에서 프로비저닝된 모든 리소스들이 삭제됨`
  - 스택으로 생성된 `AWS 리소스는 태그가 자동적으로 달림`
- `AWS 모든 서비스 지원은 안됨`
- 템플릿은 S3에서 참조됨 -> `클라우드포메이션용 S3 꼭 있어야함`


![Alt text](../etc/image3/cloudformation_%EC%98%A4%ED%86%A0%ED%83%9C%EA%B9%85.png)









- 템플릿에서 `블럭`의 구성요소
  - Resource
    - AWS 서비스 지정
    - 리소스는 필수요소
      - 리소스정의하지 않고는 `클라우드포메이션은 동작 못함`
    - `리소스양을 동적으로 못 만듬`, 모든 자원은 선언된 코드(파일)을 프로비저닝함
    - `!Ref`라는 함수를 사용해서 리소스(이름)을 참조 할 수 있음
  - Parameters
    - 클라우드포메이션에서 스택구성시 입력 변수 (동적임)
    - `!Ref`라는 함수를 사용해서 파라미터 값을 불러옴
    - AWS 제공 기본값이 있음 (아래그림 참조)

![Alt text](../etc/image3/cloudformation_%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0%EA%B8%B0%EB%B3%B8%EA%B0%92.png)


  - Mappings
    - 템플릿에서의 고정 변수
    - `사용되는 변수값을 미리 알수 있을때, 파라미터보다 맵핑이 더 유용하다`
    - `!FindInMap`을 사용해서 값을 가져옴


![Alt text](../etc/image3/cloudformation_%EB%A7%B5%ED%95%911.png)


  - outputs
    - `선택적으로 출력을 선언가능`
    - 다른 템플릿에서 참조할때 쓰임, 즉 `클라우드 템플릿을 연결할 수 있음`
    - 예를 들어 `생성된 VPC ID , 서브넷 ID 등`
    - A스택에서 출력을 사용하고, B스택에서 출력값을 사용하고 있으면, `A스택은 삭제 할 수 없다`
    - `Export` 블럭을 사용해서 내보내기를 활성화 시켜줘야한다
    - 다른 스택에서는 `ImportValue` 함수를 사용해서 아웃풋 값을 가져온다

![Alt text](../etc/image3/cloudformation_%EC%95%84%EC%9B%83%ED%92%8B1.png)
![Alt text](../etc/image3/cloudformation_%EC%95%84%EC%9B%83%ED%92%8B2.png)



  - ConditionaIs
    - `!Ref 참조 불가`
    - 아래 그림과 같이, 컨디션을 체크하고 -> true와 false로 볼륨 연결을 제어한다

![Alt text](../etc/image3/cloudformation_%EC%BB%A8%EB%94%94%EC%85%981.png)
![Alt text](../etc/image3/cloudformation_%EC%BB%A8%EB%94%94%EC%85%982.png)



  - Metadata
    - 말그대로 메타데이터
    - 클라우드 포메이션 디자이너에서 좌표값으로도 쓰임


- 그리고, 클라우드 포메이션을 위한 S3가 자동적으로 만들어진다.
  - 포메이션 스택을 파일 업로드 하면, 자동으로 S3에 저장된다 


- 기존 스택을 변경하면, 어떤 자원이 추가 되고 수정되었는지도 프리뷰도 해줌

![Alt text](../etc/image3/cloudformation_%EB%B3%80%EA%B2%BD%EB%B7%B0.png)





- 스택에 대한 정책을 사용해서 `특정 리소스`를 접근 하지 못하게도 가능 (오른쪽 정책 json 참조)
![Alt text](../etc/image3/cloudformation_%EC%8A%A4%ED%83%9D%EC%85%8B4.png)


----------

## CloudFormation 내장 함수

- GetAtt
  - GetAtt를 사용해 `리소스의 속성` 얻음

![Alt text](../etc/image3/cloudformation_%ED%95%A8%EC%88%981.png)

- Join
  - 값들 사이에 문자 추가해줌

![Alt text](../etc/image3/cloudformation_%ED%95%A8%EC%88%982.png)



- Sub
  - 문자열 바꿀때 씀

- 컨디션 조건문 (기타 등)
  - And
  - Equals
  - If
  - Not
  - Or

-----------------------------

## AWS CloudFormation Rollbacks

- `기본값으로` 스택 생성에 실패하면 롤백 작동 (`모든 자원 삭제`)
  - 롤백을 중지 할 수도 있음
- 스택이 업데이트된 경우라면? -> `이전 상태로 롤백`
  - `전체 롤백과, 실패한 자원만 롤백` 2가지 옵션이 있음


----------------------------------

## AWS CloudFormation 스택 알림

- 모든 스택 이벤트가 SNS주제로 보내진다


------------------



## AWS CloudFormation StackSet


- Cross Stack - 아웃풋으로 참조
- nested(중첩) 스택 - 스택을 묶음으로 관리
![Alt text](../etc/image3/cloudformation_%EC%8A%A4%ED%83%9D%EC%85%8B1.png)


- StackSet
  - 단일 CloudFormation 템플릿을 사용하여` AWS 계정 여러 지역에 스택을 만들 수 있는 기능`
  - 스택 생성 및 실행에 대한 `관리`를 하는것 (권한,역할,스택셋 생성,삭제 등)
  - 관리자 스택셋을 업데이트하면 -> 연결된 계정,모든 리전의 스택내용이 반영됨

--------------

## AWS CloudFormation drift

- 스택으로 생성된 `자원 구성변경을 감지` 하는것
  - 내가 만든 스택을 다른 사용자가 구성 변경을 하면? -> 큰일
  - `다른 사용자가 보안그룹에 포트 999 인바운드 추가 -> 감지됨`
- `모든 리소스를 감지 할 수 있진 않음`

- 아래 그림에서 Drift status에 수정됨이라고 뜸

![Alt text](../etc/image3/cloudformation_%EC%8A%A4%ED%83%9D%EC%85%8B2.png)

- 스택 기본값이랑, 실제 설정값이랑도 비교해서 보여줌
![Alt text](../etc/image3/cloudformation_%EC%8A%A4%ED%83%9D%EC%85%8B3.png)



































