## AWS ECS


![Alt text](../etc/image3/ecs%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0.png)

- ECS 서비스에서 보통 `EFS를` 활용해서 공유 저장소로 많이쓴다
- 타입은 Ec2기반, Fargate 기반 2가지 존재
  - Ec2 기반
    - 각 EC2 `인스턴스에 ECS 에이전트를 실행 해야됨` 
      - 오토 스케일을 ECS에 등록하면, 생성된 Ec2에서 에이전트 자동 설치됨
    - ECS에이전트가 ->  ECS,ECR,CW log, SSM 파라미터 스토어 등 IAM 역할을 받음 
  - 파게이트
    - CPU와 RAM 요구사항대로 태스크 실행함


![Alt text](../etc/image3/ecs_ec2%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8.png)




- ECS Task Role
  - 아래 그림과 같이 Task role를 다양하게 하는 이유
    - 각 서비스별 역할 할당 (최소 권한)

![Alt text](../etc/image3/ecs_role_%ED%94%84%EB%A1%9C%ED%8C%8C%EC%9D%BC.png)


------------------


- ECS에서 `TASK 정의` -> 쿠버네티스에서 `deployment + service와 비슷함`
- 
![Alt text](../etc/image3/ecs%ED%83%9C%EC%8A%A4%ED%81%AC.png)

- ECS ASG는 오직 `컨테이너 관점임, CA(클러스터 오토스케일링) 되진` 않음

- ECS Ec2 Cluster cappacity provider는 -> ECS에서 새 태스크를 실행할 용량이 부족하면, `자동으로 EC2 ASG를 확장해줌`








- ECS 태스크 업데이트가 있을때는, 롤링 업데이트 됨
  - maximum percent는 v2를 배포할때 여분 컨테이너 갯수임

![Alt text](../etc/image3/ecs%EB%A1%A4%EB%A7%81%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B81.png)

![Alt text](../etc/image3/ecs%EB%A1%A4%EB%A7%81%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8.png)

![Alt text](../etc/image3/ecs%EB%A1%A4%EB%A7%81%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B82.png)








