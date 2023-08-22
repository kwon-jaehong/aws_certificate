## AWS와 CICD

- CodeCommit : 소스 저장소
- CodePipeline : 코드에서 빈스택등의 파이프라인 자동화  (전과정 컨트롤)
- CodeBuild : 코드를 구축 및 테스트 자동화
- CodeDeploy : 코드를 `Ec2,온프라미스 장비, 람다, ECS 등` 자동 배포(`빈스택 배포 아님!`) 
- CodeStar : 개발을 위한 소프트웨어 위에 명시한 소프트웨어를 하나로 관리/그룹화 가능
- CodeArtifact : 소프트웨어 패키지를 저장,게시,공유
- CodeGuru : 머신러닝을 써서, 코드 리뷰 해주고 성능 체크


![Alt text](../etc/image3/cicd_%EC%86%8C%EA%B0%9C.png)



----------------------------------

## AWS CodeCommit

- 이거 왜씀?
  - 완전관리, 고가용성, 보안, 프로젝트 `사이즈에 제한 없음`
  - IAM을 이용한 엑세스 제어
  - 저장된 코드는 `KMS를 이용해서 암호화됨`
  - 저장소를 공유할때, 절대 SSH 키를 공유해서는 안되고, IAM역할을 생성 & STS를 통해 다른계정과 공유해야됨
  - `저장소 인증 관련 2가지`
    - SSH Key 사용
    - HTTPS 사용 (AWS 인증서)


- 코드커밋을 쓰려면, IAM > 유저 > 자격증명에서 comdecommit 키를 발급 받아야한다
![Alt text](../etc/image3/cicd_codecommit_IAM%EC%9E%90%EA%B2%A9%EC%A6%9D%EB%AA%85.png)



----------------------------
## AWS CodePipeline

- CICD를 위한 비주얼 워크플로 도구
- 소스는 Codecommit, ECR, S3, bitbucket, github 등 있음
- 빌드는 CodeBuild, jenkins,CloudBase, Teamcity 등을 선택 가능
- 테스트는 CodeBuild, AWS Device Farm 등 서드파티 지원
- 배포는 Codedeploy, Elastic Beanstalk, CloudFormation, ECS, S3 등 가능
- 파이프라인의 `결과물 -> 아티팩트는 s3에 저장`되고, 다음단계로 전달됨
- `CW이벤트 브릿지로` 파이프라인 실패, 스테이지 실패등에 대한 알림을 받을 수 있음
- 불편한점...  `IAM 역할을 필요에 맞게 셋팅 해야됨 (S3 통신, 빈스텍, 코드 커밋 등) `

- 파이프라인 시각화
![Alt text](../etc/image3/cicd_%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8ui.png)

- 파이프라인 추가를 할 수 있다. (깃랩 CICD처럼 스테이지 매니징 가능)
- `Stage에 여러 액션 그룹이 있을 수 있다`.

![Alt text](../etc/image3/cicd_%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%80%EC%95%A1%EC%85%98%EA%B7%B8%EB%A3%B9.png)




- 파이프라인 콜 하는 방법 (3가지)
  - event 방식 `(기본값)`
    - 이벤트가 발생하면, 바로 실행하기 때문에 매우 빠름
  - webhook
    - 이벤트 방법의 이전 버젼, 코드파이프라인의 엔드포인트를 노출 시켜야함

  - polling
    - 코드파이프라인이 정기적으로 저장소를 체크함 (비추함)

![Alt text](../etc/image3/cicd%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%EC%BD%9C.png)



- 또한 파이프라인 중간에 `수동 승인`기능이 있다
  - `수동 승인의 소유자는 aws`
  - 수동 승인을 하기위해서, 사용자의 수동승인 권한이 2개 필요하다
    - getpipeline (파이프라인 확인)
    - putApprovalresult (수동 승인버튼 권한)
  - 그림에서 보다 시피 SNS로 사용자에게 알림 가능

![Alt text](../etc/image3/cicd_%EC%88%98%EB%8F%99%EB%B2%84%ED%8A%BC.png)




- 클라우드 포메이션과 통합해서 테스트 서버를 올려서 테스트 할 수도 있음

![Alt text](../etc/image3/cicd_%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8%ED%8F%AC%EB%A9%94%EC%9D%B4%EC%85%98.png)

-----------------------------------

## AWS CodeBuild

- 소스는 코드커밋, s3, 빗버킷, 깃랩등
- `buildspec.yml` 파일을 통해 빌드 실행 (루트에 위치해야됨)
  - buildspec.yml의 모든 명령을 실행 (`일종의 Dockerfile`)
- 빌드에 관련된 로그는 s3, cw logs에 저장됨
- 빌드환경은 `파이썬, 자바, docker 등` 지원
- 소스코드 + docker 이미지를 활용해 빌드 시작

![Alt text](../etc/image3/cicd_%EB%B9%8C%EB%93%9C%EC%9E%91%EB%8F%99%EB%B0%A9%EC%8B%9D.png)




- buildspec.yml파일 내용
  - `AWS ssm 파라미터 스토어` 변수도 끌어오기 가능
  - `AWS 시크릿 매니저` 연동도 가능
  - 전체적으로 깃랩 CICD처럼 생겻음
  - 4가지 페이즈로 나누어져 있음
    - install : 환경/패키지 설치
    - pre_build : 빌드직전 실행되는 명령어
    - build : 빌드 명령어
    - post_build : 빌드 다된후 마무리 작업
  - `캐시는 어떤 파일의 종속성을 S3에 캐시 저장하면, 빌드할때 불러와 빌드 속도를 높임`

![Alt text](../etc/image3/cicd_%EB%B9%8C%EB%93%9C%ED%8C%8C%EC%9D%BC%EC%98%88%EC%8B%9C.png)


- code 빌드를 `로컬`에서도 실행 가능
  - 단, `코드빌드 에이전트를 깔아야됨`

- 기본적으로 CodeBuild는 VPC 밖에서 실행됨
  - VPC 밖에서 실행되면, VPC안의 애플리케이션과 통신 할 수 없음
  - VPC id,서브넷 ID, 보안 그룹 ID를 설정해서 VPC안에서 빌드 가능

![Alt text](../etc/image3/cicd_vpc%EB%82%B4%EB%B6%80%EB%B9%8C%EB%93%9C.png)

---------------------
## AWS CodeDeploy
- 코드를 `Ec2, 온프라미스 장비, 람다, ECS 등` 자동 배포
  - 모든 Ec2 인스턴스가 빈스택처럼 관리되지 않음
- 대상이 되는 장비에 `CodeDeploy Agent`를 설치
- 애플리케이션을 배포하는 법을 설명하는 `appspec.yml`을 사용 
- 에이전트는 CodeDeploy에 poll을 하고있고, 무슨 작업을 해야되는지 대기상태에 있음

![Alt text](../etc/image3/cicd_deploy%EC%A0%84%EA%B0%9C%EB%8F%84.png)


- CodeDeploy 구성 요소
  - Application 
    - 유니크한 이름의 컨테이너





























