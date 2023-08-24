## AWS CloudFormation




- CloudFormation의 `비용은 무료임`
- 파일 템플릿은 `json, yaml 지원`
- 모두 순서대로 인프라 자원이 생성됨
- `Stacks`으로 관리됨
  - 스택을 삭제하면 `클라우드포메이션에서 프로비저닝된 모든 리소스들이 삭제됨`
  - 스택으로 생성된 `AWS 리소스는 태그가 자동적으로 달림`
- `AWS 모든 서비스 지원은 안됨`

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



----------

## CloudFormation 내장 함수

- Ref
- GetAtt
- FindInMap
- ImportValue
- Join
- Sub
- 컨디션 조건문 (기타 등)
  - And
  - Equals
  - If
  - Not
  - Or



















































