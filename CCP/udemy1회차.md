
---------------------
27. 기존 온프레미스 IT 인프라에 비해 AWS 클라우드가 제공하는 이점은 무엇입니까? (2개 선택)


설명
Correct options:

Trade capital expense for variable expense - In a traditional on-premises environment, you have to invest heavily in data centers and servers before you know how you’re going to use them. With Cloud Computing, you can pay only when you consume computing resources, and pay only for how much you consume.

Eliminate guessing on your infrastructure capacity needs - When you make a capacity decision before deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With Cloud Computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes’ notice. You can Stop guessing capacity.

Incorrect options:

Make a capacity decision before deploying an application, to reduce costs - As explained above, when you make a capacity decision before deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity.

Provide lower latency to applications by maintaining servers on-premises - Maintaining servers on-premises involves costly capital expenses and costly ongoing expenses to maintain, manage and upgrade them.

Increase speed and agility by keeping servers and other required resources ready before time in your data centers - This again is indicative of maintaining on-premises infrastructure which is neither a cost-effective or time effective way of managing the resources.

Reference:

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html


자본 비용을 가변 비용으로 전환 - 기존의 온프레미스 환경에서는 데이터 센터와 서버를 사용하는 방법을 알기 전에 데이터 센터와 서버에 막대한 투자를 해야 합니다. 클라우드 컴퓨팅을 사용하면 컴퓨팅 리소스를 사용할 때만 비용을 지불하고 사용한 만큼만 비용을 지불하면 됩니다.

인프라 용량 요구 사항에 대한 추측 제거 - 애플리케이션을 배포하기 전에 용량 결정을 내리면 값비싼 유휴 리소스를 사용하거나 제한된 용량을 처리하게 되는 경우가 많습니다. 클라우드 컴퓨팅을 사용하면 이러한 문제가 사라집니다. 필요한 만큼의 용량에 액세스할 수 있으며 몇 분 전에 통지하면 필요에 따라 확장 및 축소할 수 있습니다. 용량 추측을 중지할 수 있습니다.

잘못된 옵션:

비용 절감을 위해 애플리케이션을 배포하기 전에 용량 결정 - 위에서 설명한 것처럼 애플리케이션을 배포하기 전에 용량을 결정할 때 종종 값비싼 유휴 리소스를 사용하거나 제한된 용량을 처리하게 됩니다.

서버를 온프레미스로 유지 관리하여 애플리케이션에 대한 대기 시간 단축 - 서버를 온프레미스로 유지 관리하려면 비용이 많이 드는 자본 비용과 이를 유지 관리, 관리 및 업그레이드하기 위한 비용이 많이 드는 지속적인 비용이 필요합니다.

데이터 센터에서 미리 서버 및 기타 필수 리소스를 준비하여 속도와 민첩성을 높입니다. 이는 리소스를 관리하는 데 비용 효율적이거나 시간 효율적인 방법이 아닌 온프레미스 인프라를 유지 관리해야 함을 나타냅니다.

참조:



 Trade capital expense for variable expense =  일정한 비용 대신 가변 비용으로의 영업 자본 투자를 의미합니다.

  "영업 자본 비용"이라고 한글로 표현할 수 있습니다. 이 용어는 기업이 제품 또는 서비스를 생산하고 판매하는 데 필요한 자본 투자를 의미합니다. 영업 자본 비용은 제조 설비, 재고, 기계 및 장비 구매 등의 비용을 포함합니다. 이러한 비용은 기업이 생산 활동을 확장하거나 업데이트하고 경쟁력을 유지하기 위해 필요한 자금을 나타냅니다.


-> 인프라 용량 요구 사항에 대한 추측 제거를 생각 했어야 되고... 3번 데이터 센터에서 미리 보기는 말이 안됨....

---------------------------------------

28.AWS Well-Architected 프레임워크의 안정성 원칙의 일부인 조직 변경 관리를 촉진하는 데 사용할 수 있는 AWS 서비스는 무엇입니까? (3개 선택)




설명
올바른 옵션:

클라우드의 안정성에 대한 세 가지 모범 사례 영역(기초, 변경 관리, 실패 관리)이 있습니다. 변경 사항이 시스템에 미치는 영향을 파악하면(변경 관리) 능동적으로 계획을 세울 수 있고 모니터링을 통해 용량 문제 또는 SLA 위반으로 이어질 수 있는 경향을 신속하게 식별할 수 있습니다.

AWS Config - AWS Config는 AWS 리소스의 구성을 평가, 감사 및 평가할 수 있는 서비스입니다. Config는 AWS 리소스 구성을 지속적으로 모니터링하고 기록하며 원하는 구성에 대해 기록된 구성 평가를 자동화할 수 있습니다.

AWS Config 작동 방식:  - https://aws.amazon.com/config/ 를 통해

AWS CloudTrail - AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는 서비스입니다. CloudTrail을 사용하면 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록하고 지속적으로 모니터링하고 유지할 수 있습니다. CloudTrail은 AWS Management Console, AWS SDK, 명령줄 도구 및 기타 AWS 서비스를 통해 수행된 작업을 포함하여 AWS 계정 활동의 이벤트 기록을 제공합니다.

CloudTrail 작동 방식:  - https://aws.amazon.com/cloudtrail/ 을 통해

Amazon CloudWatch - Amazon CloudWatch는 DevOps 엔지니어, 개발자, 사이트 안정성 엔지니어(SRE) 및 IT 관리자를 위해 구축된 모니터링 및 관찰 가능성 서비스입니다. CloudWatch는 애플리케이션을 모니터링하고, 시스템 전체의 성능 변화에 대응하고, 리소스 활용을 최적화하고, 운영 상태에 대한 통합 보기를 얻기 위한 데이터 및 실행 가능한 통찰력을 제공합니다.

잘못된 옵션:

AWS Trusted Advisor - AWS Trusted Advisor는 비용 최적화, 보안, 내결함성, 서비스 제한 및 성능 개선에 대한 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공하는 온라인 도구입니다.

Amazon Inspector - Amazon Inspector는 AWS에 배포된 애플리케이션의 보안 및 규정 준수를 개선하는 데 도움이 되는 자동화된 보안 평가 서비스입니다. Amazon Inspector는 노출, 취약성 및 모범 사례와의 편차에 대해 애플리케이션을 자동으로 평가합니다.

Amazon GuardDuty - Amazon GuardDuty는 AWS 계정을 보호하기 위해 악의적인 활동 및 무단 동작을 모니터링하는 위협 탐지 서비스입니다. GuardDuty는 AWS CloudTrail(계정의 AWS 사용자 및 API 활동), Amazon VPC 흐름 로그(네트워크 트래픽 데이터) 및 DNS 로그(이름 쿼리 패턴)에서 AWS 계정에 걸쳐 수십억 개의 이벤트를 분석합니다. 이 서비스는 EC2와 같은 인스턴스 수준 관리가 아닌 AWS 계정 수준 액세스를 위한 것입니다. GuardDuty는 OS 취약성을 확인하는 데 사용할 수 없습니다.

참조:

https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf

https://aws.amazon.com/config/

https://aws.amazon.com/cloudtrail/



-> 안정성에 대한 개념 적립 부족


-------------------

29. 다음 중 클라우드 컴퓨팅의 장점은 무엇입니까? (3개 선택)

설명
올바른 옵션:

엄청난 규모의 경제의 이점

가변 비용에 대한 무역 자본 비용

단 몇 번의 클릭만으로 몇 분 만에 세계로 진출하고 전 세계 여러 지역에 애플리케이션을 배포하십시오.

시험 알림:

클라우드 컴퓨팅의 다음 6가지 장점을 확인하십시오. https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud 를 통해 기존 온프레미스 설정과 비교하여 클라우드 컴퓨팅의 이점에 대한 질문을 받게 될 것입니다. -computing.html

잘못된 옵션:

데이터 센터 구축 및 유지 관리에 비용 지출 - 클라우드 컴퓨팅을 사용하면 인프라가 아닌 비즈니스를 차별화하는 프로젝트에 집중할 수 있습니다. 클라우드 공급자가 처리하므로 데이터 센터를 구축하고 유지 관리하는 데 돈을 쓸 필요가 없습니다.

인프라 용량 요구 사항에 대한 몇 개월 계획 할당 - 클라우드 컴퓨팅을 사용하면 인프라 용량 요구 사항을 추측할 필요가 없습니다. 필요한 만큼의 용량에 액세스할 수 있으며 몇 분 전에 통지하면 필요에 따라 확장 및 축소할 수 있습니다. 인프라 계획에 몇 개월을 할당할 필요가 없습니다.

가변 비용을 자본 비용으로 교환 - 클라우드 컴퓨팅을 사용하면 실제로 자본 비용을 가변 비용으로 교환할 수 있습니다.

참조:

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html


-> 가변 비용 영어 몰랏슴


--------------------------------------------

31. 다음 중 타사 소프트웨어와의 AWS 상호 운용성에 대한 지침, 구성 및 문제 해결에 대한 액세스를 제공하는 AWS Support 플랜은 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS Enterprise Support - AWS Enterprise Support는 고객이 클라우드에서 결과를 달성하고 성공을 찾을 수 있도록 돕는 데 중점을 둔 컨시어지와 같은 서비스를 고객에게 제공합니다. 엔터프라이즈 지원을 통해 환경 상태를 자동으로 관리하는 고품질 엔지니어, 도구 및 기술, 애플리케이션 및 사용 사례의 맥락에서 제공되는 컨설팅 아키텍처 지침, 전담 기술 계정 관리자(TAM)로부터 연중무휴 기술 지원을 받을 수 있습니다. ) 사전 예방/예방 프로그램 및 AWS 주제 전문가에 대한 액세스를 조정합니다. 많은 일반 운영 체제, 플랫폼 및 애플리케이션 스택 구성 요소와의 AWS 상호 운용성에 대한 지침, 구성 및 문제 해결에 액세스할 수 있습니다.

AWS Business Support - AWS에 프로덕션 워크로드가 있고 특정 사용 사례의 맥락에서 기술 지원 및 아키텍처 지침에 대한 연중무휴 전화, 이메일 및 채팅 액세스를 원하는 경우 AWS Business Support를 사용해야 합니다. AWS Trusted Advisor 모범 사례 확인에 대한 전체 액세스 권한이 있습니다. 많은 일반 운영 체제, 플랫폼 및 애플리케이션 스택 구성 요소와의 AWS 상호 운용성에 대한 지침, 구성 및 문제 해결에 액세스할 수 있습니다.

시험 알림:

시험에서 최소한 몇 가지 질문을 예상할 수 있으므로 AWS Developer Support, AWS Business Support, AWS Enterprise On-Ramp Support 및 AWS Enterprise Support 플랜 간의 차이점을 검토하십시오.

- https://aws.amazon.com/premiumsupport/plans/ 를 통해

잘못된 옵션:

AWS 기본 지원 - AWS 기본 지원은 다음에 대한 액세스만 제공합니다.

고객 서비스 및 커뮤니티 - 고객 서비스, 문서, 백서 및 지원 포럼에 연중무휴로 액세스할 수 있습니다. AWS Trusted Advisor - 성능을 높이고 보안을 개선하기 위한 모범 사례에 따라 리소스를 프로비저닝하기 위한 핵심 Trusted Advisor 검사 및 지침에 액세스합니다. AWS 상태 - 계정 상태 대시보드: AWS 서비스 상태에 대한 개인화된 보기 및 리소스가 영향을 받을 때 알림.

AWS Developer Support - AWS에서 초기 개발을 테스트하거나 수행 중이고 업무 시간 중에 이메일 기반 기술 지원을 받으려면 AWS Developer Support 플랜을 사용해야 합니다. 이 플랜은 다양한 사용 사례, 워크로드 또는 애플리케이션에 서비스를 사용하는 방법에 대한 일반적인 지침도 지원합니다. 이 플랜으로는 인프라 이벤트 관리에 액세스할 수 없습니다.

이 두 계획 모두 타사 소프트웨어와의 AWS 상호 운용성에 대한 지침, 구성 및 문제 해결에 대한 액세스를 지원하지 않습니다.

AWS 기업 지원 - 이것은 구성 옵션이며 산만함으로 추가되었습니다.

참조:

https://aws.amazon.com/premiumsupport/plans/

-> 영어 뜻 몰랏고, 1개만 선택햇음

-----------------------------------------------------------------------------------------------



36. 다음 중 비용 최적화를 위해 예약을 지원하는 AWS 서비스는 무엇입니까? (3개 선택)


설명
올바른 옵션:

아마존 엘라스틱 컴퓨트 클라우드(아마존 EC2)

아마존 다이나모DB

Amazon 관계형 데이터베이스 서비스(Amazon RDS)

다음 AWS 서비스는 예약을 지원하여 비용을 최적화합니다.

Amazon EC2 예약 인스턴스(RI): Amazon EC2 예약 인스턴스(RI)를 사용하여 용량을 예약하고 실행 중인 온디맨드 인스턴스에 비해 인스턴스 사용량에 대한 할인을 받을 수 있습니다.

Amazon DynamoDB 예약 용량: Amazon DynamoDB 읽기 및 쓰기 처리량에 대한 요구 사항을 예측할 수 있는 경우 예약 용량은 DynamoDB 프로비저닝 처리 용량의 정상 가격에 비해 상당한 비용 절감 효과를 제공합니다.

Amazon ElastiCache 예약 노드: Amazon ElastiCache 예약 노드는 예약하려는 각 캐시 노드에 대해 저렴한 일회성 결제 옵션을 제공하고 해당 노드에 대한 시간당 요금을 크게 할인받을 수 있습니다.

Amazon RDS RI: Amazon EC2 RI와 마찬가지로 Amazon RDS RI는 선결제 없음, 부분 선결제 또는 전체 선결제 조건을 사용하여 구매할 수 있습니다. 모든 예약 인스턴스 유형은 Aurora, MySQL, MariaDB, PostgreSQL, Oracle 및 SQL Server 데이터베이스 엔진에서 사용할 수 있습니다.

Amazon Redshift 예약 노드: Amazon Redshift 클러스터를 장기간 지속적으로 실행하려는 경우 예약 노드 상품 구매를 고려해야 합니다. 이러한 오퍼링은 온디맨드 가격에 비해 상당한 절감 효과를 제공하지만 컴퓨팅 노드를 예약하고 1년 또는 3년 기간 동안 해당 노드에 대한 비용을 지불해야 합니다.

잘못된 옵션:

Amazon DocumentDB - Amazon DocumentDB(MongoDB와 호환됨)는 MongoDB 워크로드를 지원하는 빠르고 확장 가능하며 가용성이 높고 완벽하게 관리되는 문서 데이터베이스 서비스입니다. 문서 데이터베이스인 Amazon DocumentDB를 사용하면 JSON 데이터를 쉽게 저장, 쿼리 및 인덱싱할 수 있습니다.

AWS Lambda - AWS Lambda를 사용하면 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있습니다. 사용한 컴퓨팅 시간에 대해서만 비용을 지불합니다.

Amazon Simple Storage Service(Amazon S3) - Amazon Simple Storage Service(Amazon S3)는 업계 최고의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스입니다.

이러한 AWS 서비스 중 어느 것도 비용 최적화를 위한 예약을 지원하지 않습니다.

참조:

https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf


-> RDB중 예약 인스턴스 지원하는거 확인



-------------------------------------------------------------------------------------------------------


40. 금융 서비스 회사는 AWS 계정 활동이 거버넌스, 규정 준수 및 감사 규범을 충족하는지 확인하려고 합니다. 클라우드 실무자로서 이 사용 사례에 대해 어떤 AWS 서비스를 추천하시겠습니까?

설명
올바른 옵션:

AWS CloudTrail

CloudTrail을 사용하여 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록, 모니터링 및 유지할 수 있습니다. CloudTrail은 AWS Management Console, AWS SDK, 명령줄 도구 및 기타 AWS 서비스를 통해 수행된 작업을 포함하여 AWS 계정 활동의 이벤트 기록을 제공합니다.

CloudTrail 작동 방식:  - https://aws.amazon.com/cloudtrail/ 을 통해

잘못된 옵션:

AWS Config - AWS Config는 AWS 리소스의 구성을 평가, 감사 및 평가할 수 있는 서비스입니다. Config는 AWS 리소스 구성을 지속적으로 모니터링하고 기록하며 원하는 구성에 대해 기록된 구성 평가를 자동화할 수 있습니다.

Amazon CloudWatch - Amazon CloudWatch는 DevOps 엔지니어, 개발자, 사이트 안정성 엔지니어(SRE) 및 IT 관리자를 위해 구축된 모니터링 및 관찰 가능성 서비스입니다. CloudWatch는 애플리케이션을 모니터링하고, 시스템 전체의 성능 변화에 대응하고, 리소스 활용을 최적화하고, 운영 상태에 대한 통합 보기를 얻기 위한 데이터 및 실행 가능한 통찰력을 제공합니다. 이것은 탄력적 시스템 구축을 위한 훌륭한 서비스입니다.

AWS Trusted Advisor - AWS Trusted Advisor는 비용 최적화, 보안, 내결함성, 서비스 제한 및 성능 개선에 대한 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공하는 온라인 도구입니다.

시험 알림:

CloudWatch, CloudTrail, Config 중 하나를 선택하라는 사용 사례가 표시될 수 있습니다. 이 엄지 손가락 규칙을 기억하십시오-

리소스 성능 모니터링, 이벤트 및 경고를 생각하십시오. CloudWatch를 생각하십시오.

계정별 활동 및 감사를 생각합니다. CloudTrail을 생각하십시오.

리소스별 변경 기록, 감사 및 규정 준수를 생각합니다. 구성을 생각합니다.

참조:

https://aws.amazon.com/cloudtrail/


->  규정 준수 및 감사 규범을 충족하는지 확인하려고 합니다를 잘봤어야함



--------------------------

43. 다음 중 기본적으로 암호화가 활성화된 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

AWS CloudTrail 로그

AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는 서비스입니다. AWS CloudTrail을 사용하여 AWS 계정에 대한 AWS API 호출 및 기타 활동을 기록하고 선택한 Amazon Simple Storage Service(Amazon S3) 버킷의 로그 파일에 기록된 정보를 저장할 수 있습니다. 기본적으로 CloudTrail에서 S3 버킷으로 전달하는 로그 파일은 Amazon S3 관리형 키(SSE-S3)로 서버 측 암호화를 사용하여 암호화됩니다.

잘못된 옵션:

Amazon Elastic File System(Amazon EFS) - Amazon Elastic File System(Amazon EFS)은 AWS 클라우드 서비스 및 온프레미스 리소스와 함께 사용할 수 있는 간단하고 확장 가능하며 완전히 관리되는 탄력적인 NFS 파일 시스템을 제공합니다. Amazon EFS는 파일 시스템에 대해 전송 데이터 암호화와 유휴 데이터 암호화라는 두 가지 형태의 암호화를 지원합니다. 이것은 선택적 기능이며 필요한 경우 사용자가 활성화해야 합니다.

Amazon Elastic Block Store(Amazon EBS) - Amazon Elastic Block Store(EBS)는 언제 어디서나 처리량과 트랜잭션 집약적인 워크로드 모두에 대해 Amazon Elastic Compute Cloud(EC2) 인스턴스와 함께 사용하도록 설계된 사용하기 쉬운 고성능 블록 스토리지 서비스입니다. 규모. 암호화(미사용 및 전송 중)는 EBS의 선택적 기능이며 사용자가 활성화해야 합니다.

Amazon Relational Database Service(Amazon RDS) - Amazon Relational Database Service(Amazon RDS)는 Amazon RDS DB 인스턴스를 암호화할 수 있습니다. 유휴 상태에서 암호화되는 데이터에는 DB 인스턴스의 기본 스토리지, 자동 백업, 읽기 전용 복제본 및 스냅샷이 포함됩니다. RDS용 암호화는 추가 기능이며 사용자가 이를 활성화해야 합니다.

참조:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html


-> 이건... 진짜 몰랏음

--------------------------------


45. 다음 중 AWS Organizations에서 AWS 계정을 제거하는 것과 관련된 올바른 설명은 무엇입니까?

설명
올바른 옵션:

AWS 계정은 독립 실행형 계정으로 작동할 수 있어야 합니다. 그래야만 AWS 조직에서 제거할 수 있습니다.

독립 실행형 계정으로 작동하는 데 필요한 정보가 계정에 있는 경우에만 조직에서 계정을 제거할 수 있습니다. 독립 실행형으로 만들려는 각 계정에 대해 AWS 고객 계약에 동의하고 지원 계획을 선택하고 필요한 연락처 정보를 제공 및 확인하고 현재 결제 방법을 제공해야 합니다. AWS는 결제 방법을 사용하여 계정이 조직에 연결되지 않은 동안 발생하는 청구 가능한(AWS 프리 티어 아님) AWS 활동에 대해 요금을 청구합니다.

잘못된 옵션:

계정을 제거하려면 AWS Support에 지원 티켓을 제출하십시오 . AWS Support는 AWS Organizations에서 AWS 계정을 제거하는 데 도움을 줄 필요가 없습니다.

AWS 계정은 AWS Systems Manager에서 제거할 수 있습니다 . AWS Systems Manager는 AWS의 인프라에 대한 가시성과 제어를 제공합니다. Systems Manager는 통합 사용자 인터페이스를 제공하므로 여러 AWS 서비스의 운영 데이터를 볼 수 있으며 명령 실행, 패치 관리, AWS 클라우드 및 온프레미스 인프라에서 서버 구성과 같은 운영 작업을 자동화할 수 있습니다. Systems Manager는 AWS Organizations에서 AWS 계정을 제거하는 데 사용할 수 없습니다.

AWS 계정에는 연결된 서비스 제어 정책(SCP)이 없어야 합니다. 그래야만 AWS 조직에서 제거할 수 있습니다. - 이것은 AWS 계정을 제거하기 위한 전제 조건이 아닙니다. AWS 계정의 보안 주체는 더 이상 조직에 정의된 서비스 제어 정책(SCP)의 영향을 받지 않습니다. 이는 해당 SCP에 의해 부과된 제한이 사라지고 계정의 사용자 및 역할이 이전보다 더 많은 권한을 가질 수 있음을 의미합니다.

참조:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html


-> 이건 진짜 몰랏음

---------------

47. IT 회사의 DevOps 팀은 500GB의 데이터를 EC2 인스턴스에서 같은 지역의 S3 버킷으로 옮기고 있습니다. 다음 중 이 데이터 전송에 대한 올바른 요금을 캡처하는 시나리오는 무엇입니까?

설명
올바른 옵션:

회사는 이 데이터 전송에 대해 비용을 청구하지 않습니다.

AWS에는 컴퓨팅, 스토리지 및 아웃바운드 데이터 전송이라는 세 가지 기본 비용 동인이 있습니다. 대부분의 경우 인바운드 데이터 전송 또는 동일한 리전 내 다른 AWS 서비스 간의 데이터 전송에 대한 요금은 없습니다. 아웃바운드 데이터 전송은 서비스 간에 집계된 다음 아웃바운드 데이터 전송 요금으로 청구됩니다.

AWS 요금에 따라 동일한 리전 내의 S3 인스턴스와 EC2 인스턴스 간의 데이터 전송에는 요금이 부과되지 않으므로 EC2 인스턴스에서 동일한 리전의 S3 버킷으로 500GB의 데이터를 이동하는 데 데이터 전송 요금이 부과되지 않습니다.

잘못된 옵션:

회사는 EC2 인스턴스로부터의 아웃바운드 데이터 전송에 대해서만 비용을 청구합니다.

회사는 S3 버킷으로의 인바운드 데이터 전송에 대해서만 비용을 청구합니다.

회사는 EC2 인스턴스의 아웃바운드 데이터 전송과 S3 버킷으로의 인바운드 데이터 전송에 대해 요금을 부과합니다.

이 세 가지 옵션은 설명의 앞부분에서 제공된 세부 정보와 상충되므로 이러한 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/s3/pricing/

https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf

-> 이것도 몰랏음

-----------------------------------------------------------------

48. 다음 AWS Support 계획 중 자습형 실습이 포함된 온라인 교육에 대한 액세스를 제공하는 것은 무엇입니까?


설명
올바른 옵션:

AWS 엔터프라이즈 지원

AWS는 각 고객의 요구에 따라 AWS Developer Support, AWS Business Support, AWS Enterprise On-Ramp Support 및 AWS Enterprise Support 플랜의 4가지 지원 플랜을 제공합니다. 모든 AWS 고객을 위한 기본 지원 계획이 포함되어 있습니다.

AWS Enterprise Support 플랜은 고객이 클라우드에서 결과를 달성하고 성공을 찾을 수 있도록 돕는 데 중점을 둔 컨시어지와 같은 서비스를 고객에게 제공합니다. AWS Enterprise Support를 사용하면 자습형 실습을 통한 온라인 교육, 고품질 엔지니어의 24x7 기술 지원, 환경 상태를 자동으로 관리하는 도구 및 기술, 컨설팅 아키텍처 지침, 지정된 기술 계정 관리자(TAM)를 이용할 수 있습니다. 사전 예방/예방 프로그램 및 AWS 주제 전문가에 대한 액세스를 조정합니다.

AWS 엔터프라이즈 지원 플랜 오퍼링:  - https://aws.amazon.com/premiumsupport/plans/enterprise/ 를 통해

잘못된 옵션:

AWS Developer Support - AWS에서 초기 개발을 테스트하거나 수행 중이고 업무 시간 동안 기술 지원을 받고 빌드 및 테스트할 때 일반적인 아키텍처 지침을 받으려면 AWS Developer Support 플랜을 사용해야 합니다.

AWS Business Support - AWS에 프로덕션 워크로드가 있고 특정 사용 사례의 맥락에서 기술 지원 및 아키텍처 지침에 연중무휴로 액세스하려는 경우 AWS Business Support 플랜을 사용해야 합니다.

AWS Enterprise On-Ramp 지원 - AWS에 프로덕션/비즈니스에 중요한 워크로드가 있고 연중무휴로 기술 지원을 받고 싶고 클라우드에서 성장하고 최적화하기 위한 전문가 지침이 필요한 경우 AWS Enterprise On-Ramp 지원 계획을 사용해야 합니다. AWS Trusted Advisor 모범 사례 확인에 대한 전체 액세스 권한이 있습니다.

이 세 가지 지원 계획 중 어느 것도 자습식 랩이 포함된 온라인 교육에 대한 액세스를 제공하지 않습니다.

참조:

https://aws.amazon.com/premiumsupport/plans/

https://aws.amazon.com/premiumsupport/plans/enterprise/

-> 답은 맞췃지만, 무슨말인지 모름

--------------------------------------------------------

49. AWS 클라우드 채택 프레임워크(AWS CAF)에 따르면 기업이 AWS 클라우드로의 마이그레이션을 계획하고 조직 혁신의 일환으로 고객 문의 및 피드백에 더 잘 대응하기 위해 수행해야 하는 두 가지 작업은 무엇입니까? (2개 선택)



설명
올바른 옵션:

AWS Cloud Adoption Framework(AWS CAF)는 AWS 경험과 모범 사례를 활용하여 AWS를 혁신적으로 사용하여 비즈니스 성과를 디지털 방식으로 전환하고 가속화하도록 지원합니다. AWS CAF는 성공적인 클라우드 전환을 뒷받침하는 특정 조직 기능을 식별합니다. 이러한 기능은 클라우드 준비 상태를 개선하는 데 도움이 되는 모범 사례 지침을 제공합니다. AWS CAF는 비즈니스, 사람, 거버넌스, 플랫폼, 보안 및 운영의 6가지 관점에서 기능을 그룹화합니다.

제품 및 가치 흐름을 중심으로 팀 구성

민첩한 방법을 활용하여 빠르게 반복하고 발전

AWS Cloud Adoption Framework(AWS CAF)를 사용하여 비즈니스 및 기술 팀이 고객 가치를 창출하고 전략적 의도를 충족하는 방법을 재구성할 수 있습니다. 민첩한 방법을 활용하여 빠르게 반복하고 발전하는 동시에 제품 및 가치 흐름을 중심으로 팀을 구성하면 대응력과 고객 중심적이 되는 데 도움이 됩니다.

잘못된 옵션:

비용 효율성을 위해 레거시 인프라 활용

기존 제품 및 서비스로 새로운 분석 통찰력 생성

관료적 디자인 원칙에 따라 팀 구성

이 세 가지 옵션은 AWS CAF(AWS Cloud Adoption Framework)에서 고객 문의 및 피드백에 더 잘 응답하기 위해 설명한 작업과 일치하지 않으므로 이러한 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/cloud-adoption-framework/

-> 이것도 답은 맞췃지만 무슨말이야

-------------------------------------------------------------





52. AWS Shield Advanced는 다음 리소스에서 실행되는 웹 애플리케이션에 대해 확장된 DDoS 공격 보호를 제공합니까? (2개 선택)






설명
올바른 옵션:

아마존 루트 53

AWS 글로벌 액셀러레이터

AWS Shield Standard는 기본적으로 모든 AWS 고객에 대해 활성화됩니다. 공격에 대한 더 높은 수준의 보호를 위해 AWS Shield Advanced를 구독할 수 있습니다. Shield Advanced를 사용하면 AWS 리소스에 대한 공격에 대한 광범위한 가시성을 위해 고급 실시간 지표 및 보고서에 독점적으로 액세스할 수 있습니다. DRT(DDoS 대응 팀)의 도움을 받아 AWS Shield Advanced에는 네트워크 계층(계층 3) 및 전송 계층(계층 4) 공격뿐만 아니라 애플리케이션 계층(계층 7) 공격에 대한 지능형 DDoS 공격 탐지 및 완화 기능이 포함되어 있습니다. .

AWS Shield Advanced는 Amazon Elastic Compute Cloud, Elastic Load Balancing(ELB), Amazon CloudFront, Amazon Route 53, AWS Global Accelerator 리소스에서 실행되는 웹 애플리케이션에 대해 확장된 DDoS 공격 보호 기능을 제공합니다.

잘못된 옵션:

Amazon API Gateway - Amazon API Gateway는 개발자가 모든 규모에서 API를 쉽게 생성, 게시, 유지 관리, 모니터링 및 보호할 수 있게 해주는 완전 관리형 서비스입니다. API는 애플리케이션이 백엔드 서비스의 데이터, 비즈니스 로직 또는 기능에 액세스하기 위한 "정문" 역할을 합니다. Amazon Web Application Firewall은 Amazon API Gateway API로 전달되는 HTTP 및 HTTPS 요청을 모니터링하는 데 사용됩니다. AWS Shield Advanced에서는 다루지 않습니다.

AWS CloudFormation - AWS CloudFormation을 사용하면 프로그래밍 언어 또는 간단한 텍스트 파일을 사용하여 자동화되고 안전한 방식으로 모든 지역 및 계정에서 애플리케이션에 필요한 모든 리소스를 모델링하고 프로비저닝할 수 있습니다. CloudFormation은 AWS Shield Advanced에 포함되지 않습니다.

AWS Elastic Beanstalk - AWS Elastic Beanstalk는 다양한 프로그래밍 언어로 개발된 웹 애플리케이션 및 서비스를 배포하고 확장하기 위한 사용하기 쉬운 서비스입니다. 코드를 업로드하기만 하면 Elastic Beanstalk가 용량 프로비저닝, 로드 밸런싱, 자동 확장에서 애플리케이션 상태 모니터링에 이르기까지 배포를 자동으로 처리합니다. Elastic Beanstalk는 AWS Shield Standard에서 다룹니다. 이 서비스에는 고급 보장이 제공되지 않습니다.

참조: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html



--> 이것도 몰랏음 쉴드 다시

----------------------------------------------------



55. AWS에서 처음으로 작업하는 프로젝트 관리자는 AWS에서 크레딧이 사용되는 방식에 대해 혼란스러워합니다. 관리자의 계정에는 두 개의 크레딧이 있습니다. 크레딧 1은 100달러이고 2022년 7월에 만료되며 Amazon S3 또는 Amazon EC2에 사용할 수 있습니다. 크레딧 2는 50달러이고 2022년 12월에 만료되며 Amazon EC2에만 사용할 수 있습니다. 관리자의 AWS 계정에서 Amazon EC2의 경우 $1000, Amazon S3의 경우 $500의 두 가지 요금이 발생했습니다.

크레딧을 사용하면 전체 청구서의 결과는 어떻게 됩니까? (2개 선택)






설명
올바른 옵션:

7월에 만료되는 크레딧 1이 Amazon EC2 요금에 적용되어 $900 Amazon EC2 요금과 $500 Amazon S3 요금이 남습니다.

그런 다음 Amazon EC2 사용량의 나머지 $900에 크레딧 2가 적용됩니다.

크레딧은 다음 순서로 적용됩니다.

가장 빠른 만료

적용 가능한 제품의 최소 수

가장 오래된 신용

주어진 사용 사례에 대해 7월에 만료되는 크레딧 1이 Amazon EC2 요금에 적용되어 $900 Amazon EC2 요금과 $500 Amazon S3 요금이 남습니다. 그런 다음 나머지 $900의 Amazon EC2 사용량에 크레딧 2가 적용됩니다. Amazon EC2의 경우 $850, Amazon S3의 경우 $500를 지불해야 합니다. 이제 모든 크레딧이 소진되었습니다.

잘못된 옵션:

7월에 만료되는 크레딧 1이 Amazon S3 사용에 적용되어 $1000 Amazon EC2 요금과 $400 Amazon S3 요금이 남습니다.

하나의 청구 주기에 하나의 크레딧만 사용할 수 있으며 고객은 사용 가능한 크레딧 중에서 선택할 수 있습니다.

그런 다음 크레딧 2가 Amazon S3 사용량 $500에 적용됩니다.

이 세 가지 옵션은 위에 제공된 설명과 상충되므로 이러한 옵션은 올바르지 않습니다.

참조:

https://www.amazonaws.cn/en/support/faqs/


-> ㅋㅋ 이걸 에라이 봐야함

-----------------------------------------------
62. AWS 공동 책임 모델에 따라 다음 중 AWS와 고객 모두의 공동 책임은 무엇입니까?





설명
올바른 옵션:

구성 관리

보안 및 규정 준수는 AWS와 고객의 공동 책임입니다. 이 공유 모델은 AWS가 호스트 운영 체제 및 가상화 계층에서 서비스가 운영되는 시설의 물리적 보안에 이르기까지 구성 요소를 운영, 관리 및 제어하므로 고객의 운영 부담을 줄이는 데 도움이 될 수 있습니다.

인프라 계층과 고객 계층 모두에 적용되지만 완전히 별개의 컨텍스트 또는 관점에서 적용되는 제어를 공유 제어라고 합니다. 공유 제어에서 AWS는 인프라에 대한 요구 사항을 제공하고 고객은 AWS 서비스 사용 내에서 자체 제어 구현을 제공해야 합니다. 구성 관리는 공유 제어의 일부를 형성합니다. AWS는 인프라 장치의 구성을 유지 관리하지만 고객은 자신의 게스트 운영 체제, 데이터베이스 및 애플리케이션을 구성해야 합니다.

공동 책임 모델 개요:  - https://aws.amazon.com/compliance/shared-responsibility-model/ 을 통해

잘못된 옵션:

Amazon Simple Storage Service(Amazon S3) 스토리지 서버의 인프라 유지 관리 - AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다.

다양한 AWS 고객 간의 데이터 분리 보장 - AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다. 이 인프라는 AWS 클라우드 서비스를 실행하는 하드웨어, 소프트웨어, 네트워킹 및 시설로 구성됩니다.

가용 영역(AZ) 인프라 유지 관리 - AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다.

참조:

https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys


-> 다시 봐야할듯 `고객 간의 데이터 분리 보장 `은 AWS임!!!!!!





