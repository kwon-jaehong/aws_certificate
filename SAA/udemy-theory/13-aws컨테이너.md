## AWS ECS



- NLB,ALB 등 로드밸런서 연동해서 씀

EC2 시작 타입
- ec2 기반에서 컨테이너서비스 하는거임
- 내가 사용할 Ec2를 미리 프로비저닝 해야됨
- Ec2에 `ECS 에이전트를 설치해야됨` 

![Alt text](../../etc/image2/ecsec2.png)


fargate 시작 타입
- 자원 프로비저닝 X
- `서버리스`임





ECS IAM role
- EC2타입으로 ECS를 구성하려면, `EC2 Instance Profile` IAM 역할을 생성 해줘야한다
  - ec2 인스턴스가, SSM, ECR ECS 등에 접근용도
- `ECS Task 역할`은 다른것임
  - 컨테이너에 역할을 부여하는 개념

![Alt text](../../etc/image2/ecs%EC%97%AD%ED%95%A0.png)


ECS 데이터 볼륨 (EFS)
- 주로 `EFS` 씀
- EFS + 파게이트 = 서버리스 
- `S3는 마운트 될수 없음`


ECS Task
- 쿠버네티스 yaml deploy처럼 컨테이너를 배포하기 위한 기능
- 애플리케이션 타입이 Service = 계속 실행, Task = 실행완료 후 종료


ECS 오토 스케일링
- ECS 오토스케일링 != Ec2 오토스케일링임
  - 컨테이너를 늘리는거지, ECS에 사용되는 ec2 인스턴스를 늘리는게 아님
    - 예) 엔진엑스 컨테이너 100개 생성하면, Ec2 1개 프로비저닝에서 서비스될수 없다
- 그래서 이런거 신경쓰기 싫으면, 파게이트 써야함
- ECS cluster capacity provider (용량 공급자) = 카펜터 





-------------------------------------
## AWS App Runner

- `완전관리형`, 규모에 따라, 웹 애플리케이션 API 배포를 도움
- 컨테이너 & 소스 코드만 있어도 됨
- `쉬운 ECS 시스템` - 컨테이너 기반의 beanstalk 느낌
- `신속한 프로덕션 배포`가 필요할때 사용
- 파게이트로 실행됨



















































