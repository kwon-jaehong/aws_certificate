5. 한 조직이 온프레미스 데이터 센터에서 AWS 클라우드로 인프라를 이동할 계획입니다. Cloud Practioner로서 조직이 AWS 클라우드에서 솔루션을 구축하기 위해 올바른 AWS 서비스를 식별할 수 있도록 권장하는 옵션은 무엇입니까(2개 선택)?


AWS Service Catalog - AWS Service Catalog를 사용하면 조직에서 AWS에서 사용하도록 승인된 IT 서비스의 카탈로그를 만들고 관리할 수 있습니다. 이러한 IT 서비스에는 가상 머신 이미지, 서버, 소프트웨어 및 데이터베이스에서 완전한 다중 계층 애플리케이션 아키텍처에 이르는 모든 것이 포함될 수 있습니다.

AWS 파트너 네트워크(APN) - 조직은 AWS 파트너 네트워크(APN)의 도움을 받아 AWS 클라우드에서 솔루션을 구축하는 데 적합한 AWS 서비스를 식별할 수 있습니다. AWS 파트너 네트워크(APN)는 Amazon Web Services를 활용하여 고객을 위한 솔루션 및 서비스를 구축하는 기술 및 컨설팅 비즈니스를 위한 글로벌 파트너 프로그램입니다.

잘못된 옵션:

AWS Organizations - AWS Organizations는 AWS에서 워크로드를 확장하고 확장함에 따라 환경을 중앙에서 관리하는 데 도움이 됩니다. AWS Organizations는 결제를 중앙에서 관리하는 데 도움이 됩니다. 액세스, 규정 준수 및 보안 제어 AWS 계정 간에 리소스를 공유합니다. AWS Organizations는 AWS 클라우드에서 솔루션을 구축하는 데 적합한 AWS 서비스를 식별하는 데 도움을 줄 수 없습니다.

Amazon CloudWatch - Amazon CloudWatch는 DevOps 엔지니어, 개발자, 사이트 안정성 엔지니어(SRE) 및 IT 관리자를 위해 구축된 모니터링 및 관찰 가능성 서비스입니다. CloudWatch는 애플리케이션을 모니터링하고, 시스템 전반의 성능 변화에 대응하고, 리소스 활용을 최적화하고, 운영 상태에 대한 통합 보기를 얻을 수 있는 데이터 및 실행 가능한 통찰력을 제공합니다. 리소스 성능 모니터링, 이벤트 및 경고를 생각하십시오. CloudWatch를 생각하십시오. CloudWatch는 AWS 클라우드에서 솔루션을 구축하는 데 적합한 AWS 서비스를 식별하는 데 도움이 되지 않습니다.

AWS CloudTrail - AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는 서비스입니다. CloudTrail을 사용하면 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록하고 지속적으로 모니터링하고 유지할 수 있습니다. 계정별 활동 및 감사를 생각합니다. CloudTrail을 생각하십시오. CloudTrail은 AWS 클라우드에서 솔루션을 구축하기 위해 올바른 AWS 서비스를 식별하는 데 도움이 될 수 없습니다.

참조:

https://aws.amazon.com/servicecatalog/

https://aws.amazon.com/partners/

-> 왜 서비스 카탈로그이지? `솔루션을 구축하기 위해 올바른`말을 끝까지... 좀 봐라


----------------------------------

7. AWS Compute Optimizer는 다음 AWS 리소스에 대한 권장 사항을 제공합니까? (2개 선택)

Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스, Amazon EC2 Auto Scaling 그룹

Amazon Elastic Block Store(Amazon EBS), AWS Lambda 함수

AWS Compute Optimizer는 기계 학습을 사용하여 사용률 기록 지표를 분석하여 Amazon EC2 인스턴스 유형, Amazon EBS 볼륨 구성 및 AWS Lambda 함수 메모리 크기와 같은 최적의 AWS 리소스 구성을 식별하는 데 도움이 됩니다. AWS Compute Optimizer는 선택한 유형의 EC2 인스턴스, EC2 Auto Scaling 그룹, Amazon EBS 볼륨 및 AWS Lambda 함수에 대한 권장 사항을 제공합니다.

AWS Compute Optimizer는 CPU, 메모리, EBS 처리량, EBS IOPS, 디스크 처리량, 디스크 처리량, 네트워크 처리량 및 PPS(초당 네트워크 패킷 수)를 포함하여 권장 인스턴스의 각 리소스 차원에 대한 개별 성능 위험 점수를 계산합니다.

AWS Compute Optimizer는 그룹 크기가 고정된 EC2 Auto Scaling 그룹에 대한 EC2 인스턴스 유형 및 크기 권장 사항을 제공합니다.

AWS Compute Optimizer는 범용(SSD)(gp3) 볼륨에 대한 IOPS 및 처리량 권장 사항과 프로비저닝된 IOPS(io1 및 io2) 볼륨에 대한 IOPS 권장 사항을 지원합니다.

AWS Compute Optimizer는 Lambda 함수의 두 범주를 최적화하는 데 도움이 됩니다. 첫 번째 범주에는 메모리 크기가 과도하게 프로비저닝될 수 있는 Lambda 함수가 포함됩니다. 두 번째 범주에는 추가 CPU 성능을 활용할 수 있는 컴퓨팅 집약적 Lambda 함수가 포함됩니다.

잘못된 옵션:

Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스, Amazon Elastic File System(Amazon EFS)

Amazon Elastic File System(Amazon EFS), AWS Lambda 함수

AWS Lambda 함수, Amazon Simple Storage Service(Amazon S3)

AWS Compute Optimizer는 S3 및 EFS에 대한 최적화 권장 사항을 제공하지 않으므로 이러한 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/compute-optimizer/faqs/

-> 요건 몰랏음


--------------------------------------------------

9. AWS 공유 책임 모델에 따라 다음 중 보안 및 규정 준수 관점에서 AWS의 책임은 무엇입니까?

설명
올바른 옵션:

엣지 로케이션 관리

보안 및 규정 준수는 AWS와 고객의 공동 책임입니다. AWS 공유 책임 모델은 AWS가 호스트 운영 체제 및 가상화 계층에서 서비스가 운영되는 시설의 물리적 보안에 이르기까지 구성 요소를 운영, 관리 및 제어하므로 고객의 운영 부담을 덜어줄 수 있습니다.

AWS는 클라우드 "의" 보안을 책임집니다. 여기에는 리전, 가용 영역(AZ) 및 엣지 로케이션을 비롯한 글로벌 인프라 요소가 포함됩니다.

잘못된 옵션:

고객 데이터

ID 및 액세스 관리

서버측 암호화(SSE)

고객은 클라우드 "내"의 보안을 책임집니다. 고객은 조직 요구 사항에 따라 적절한 액세스 제어 정책을 구현하기 위해 암호화 옵션을 포함하여 데이터를 관리하고 ID 및 액세스 관리 도구를 사용할 책임이 있습니다. Amazon S3 및 Amazon DynamoDB와 같은 추상화된 서비스의 경우 AWS가 인프라 계층, 운영 체제 및 플랫폼을 운영하고 고객은 엔드포인트에 액세스하여 데이터를 저장하고 검색합니다. 따라서 이 세 가지 옵션은 AWS 공유 책임 모델에 따라 고객의 책임에 속합니다.

시험 알림:

https://aws.amazon.com/compliance/shared-responsibility-model/

-> 이건 햇갈렷음.... 서버측 암호화도 (정확히는 설정도) 내가 했어야함

--------------------------------------------------------------------------------

15. 개발자는 PHP로 간단한 웹 애플리케이션을 작성했으며 자신의 코드를 AWS 클라우드에 업로드하고 AWS가 배포를 자동으로 처리하도록 하려고 하지만 추가 개선을 위해 여전히 기본 운영 체제에 액세스하기를 원합니다. Cloud Practioner로서 이 사용 사례에 대해 다음 중 어떤 AWS 서비스를 추천하시겠습니까?


설명
올바른 옵션:

AWS Elastic Beanstalk

AWS Elastic Beanstalk는 Apache, Nginx, Passenger와 같은 친숙한 서버에서 Java, .NET, PHP, Node.js, Python, Ruby, Go 및 Docker로 개발된 웹 애플리케이션 및 서비스를 배포하고 확장하기 위한 사용하기 쉬운 서비스입니다. , 및 IIS. 코드를 업로드하기만 하면 AWS Elastic Beanstalk가 용량 프로비저닝, 로드 밸런싱, 자동 확장에서 애플리케이션 상태 모니터링에 이르기까지 배포를 자동으로 처리합니다. 동시에 애플리케이션을 지원하는 AWS 리소스에 대한 완전한 제어권을 유지하고 언제든지 기본 리소스에 액세스할 수 있습니다. AWS Elastic Beanstalk에 대한 추가 비용은 없습니다. 애플리케이션을 저장하고 실행하는 데 필요한 AWS 리소스에 대해서만 비용을 지불하면 됩니다.

AWS Elastic Beanstalk의 주요 이점: - https://aws.amazon.com/elasticbeanstalk/ 를 통해

잘못된 옵션:

AWS CloudFormation - AWS CloudFormation을 사용하면 프로그래밍 언어 또는 간단한 텍스트 파일(YAML 또는 JSON 형식)을 사용하여 자동화되고 안전한 방식으로 모든 리전 및 계정에서 애플리케이션에 필요한 모든 리소스를 모델링하고 프로비저닝할 수 있습니다. 인프라를 코드로 생각하십시오. CloudFormation을 생각하십시오. 이는 애플리케이션 코드를 업로드하기만 하면 Beanstalk가 해당 애플리케이션을 배포하는 데 필요한 리소스를 자동으로 파악하는 Beanstalk와 매우 다릅니다. AWS CloudFormation에서는 프로비저닝할 리소스를 명시적으로 지정해야 합니다.

Amazon Elastic Compute Cloud(Amazon EC2) - Amazon Elastic Compute Cloud(Amazon EC2)는 클라우드에서 안전하고 크기 조정 가능한 컴퓨팅 용량, 초당 청구 및 기본 OS에 대한 액세스를 제공하는 웹 서비스입니다. 개발자가 웹 규모의 클라우드 컴퓨팅을 보다 쉽게 ​​수행할 수 있도록 설계되었습니다. 서버 및 해당 소프트웨어 유지 관리는 고객이 수행해야 합니다. EC2는 애플리케이션 배포를 자동으로 처리할 수 없으므로 이 옵션은 올바르지 않습니다.

Amazon Elastic Container Service(Amazon ECS) - Amazon Elastic Container Service(Amazon ECS)는 확장성이 뛰어나고 빠른 컨테이너 관리 서비스로 클러스터에서 Docker 컨테이너를 쉽게 실행, 중지 및 관리할 수 있습니다. Amazon Elastic Container Service(Amazon ECS)는 애플리케이션 배포를 자동으로 처리할 수 없으므로 이 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/elasticbeanstalk/


-> 아.... ` 자신의 코드를 AWS 클라우드에 업로드하고 AWS가 배포를 자동`를 봣어야 햇음.... ec2로 정답을 냇음.....


------------------------------------------------------------------

24. 다음 AWS 서비스 중 AWS Cloud의 Well-Architected 프레임워크의 안정성 기반에 대한 AWS Foundation 서비스의 일부인 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS 신뢰할 수 있는 조언자

Service Quotas

기초는 AWS Well-Architected 프레임워크의 안정성 기둥의 일부입니다. AWS는 시스템을 설계하기 전에 안정성에 영향을 미치는 기본 요구 사항이 마련되어 있어야 한다고 말합니다. 기반의 일부인 서비스는 Amazon VPC, AWS Trusted Advisor, AWS Service Quotas(이전에는 AWS Service Limits라고 함)입니다.

AWS Trusted Advisor는 비용 최적화, 보안, 내결함성, 서비스 제한 및 성능 개선에 대한 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공하는 온라인 도구입니다. 새로운 워크플로 설정, 애플리케이션 개발 또는 지속적인 개선의 일환으로 Trusted Advisor에서 제공하는 권장 사항은 솔루션을 최적으로 프로비저닝하는 데 정기적으로 도움이 됩니다.

Service Quotas를 사용하면 중앙 위치에서 AWS 서비스에 대한 할당량을 보고 관리할 수 있습니다. AWS에서 제한이라고도 하는 할당량은 AWS 계정의 리소스, 작업 및 항목에 대한 최대값입니다. 각 AWS 서비스는 할당량을 정의하고 해당 할당량의 기본값을 설정합니다.

잘못된 옵션:

AWS CloudTrail - AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는 서비스입니다. CloudTrail을 사용하면 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록하고 지속적으로 모니터링하고 유지할 수 있습니다. CloudTrail은 AWS Management Console, AWS SDK, 명령줄 도구 및 기타 AWS 서비스를 통해 수행된 작업을 포함하여 AWS 계정 활동의 이벤트 기록을 제공합니다. 계정별 활동 및 감사를 생각합니다. CloudTrail을 생각하십시오.

AWS CloudFormation - AWS CloudFormation은 클라우드 환경에서 AWS 및 타사 애플리케이션 리소스를 모델링하고 프로비저닝하기 위한 공통 언어를 제공합니다. AWS CloudFormation을 사용하면 프로그래밍 언어 또는 간단한 텍스트 파일을 사용하여 자동화되고 안전한 방식으로 모든 리전 및 계정에서 애플리케이션에 필요한 모든 리소스를 모델링하고 프로비저닝할 수 있습니다. 인프라를 코드로 생각하십시오. CloudFormation을 생각하십시오.

Amazon CloudWatch - Amazon CloudWatch는 DevOps 엔지니어, 개발자, 사이트 안정성 엔지니어(SRE) 및 IT 관리자를 위해 구축된 모니터링 및 관찰 가능성 서비스입니다. CloudWatch는 애플리케이션을 모니터링하고, 시스템 전체의 성능 변화에 대응하고, 리소스 활용을 최적화하고, 운영 상태에 대한 통합 보기를 얻기 위한 데이터 및 실행 가능한 통찰력을 제공합니다. `이것은 탄력적 시스템 구축을 위한 훌륭한 서비스`입니다. 리소스 성능 모니터링, 이벤트 및 경고를 생각하십시오. CloudWatch를 생각하십시오.

참조:

https://wa.aws.amazon.com/wat.pillar.reliability.en.html

다음 AWS 서비스 중 AWS Cloud의 Well-Architected 프레임워크의 안정성 기반에 대한 AWS Foundation 서비스의 일부인 것은 무엇입니까? (2개 선택)

a. Service Quotas
b. AWS Trusted Advisor
c. AWS CloudTrail
d. AWS CloudFormation 
e. Amazon CloudWatch

-> ㅋㅋㅋ 챗 gpt에 물어보면  b. AWS Trusted Advisor와 c. AWS CloudTrail

-----------------------------------------------------

30. 사진 공유 웹 애플리케이션은 사용자가 업로드한 이미지의 썸네일을 Amazon Simple Storage Service(Amazon S3)에 저장하려고 합니다. 썸네일은 거의 사용되지 않지만 웹 애플리케이션에서 즉시 액세스할 수 있어야 합니다. 썸네일은 손실된 경우 쉽게 재생성할 수 있습니다. Amazon Simple Storage Service(Amazon S3)에 이러한 썸네일을 저장하는 가장 비용 효율적인 방법은 무엇입니까?

설명
올바른 옵션:

Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)를 사용하여 썸네일 저장

Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 자주 액세스하지 않지만 필요할 때 빠르게 액세스해야 하는 데이터용입니다. 최소 3개의 가용 영역(AZ)에 데이터를 저장하는 다른 S3 스토리지 클래스와 달리 Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 단일 가용 영역(AZ)에 데이터를 저장하고 Amazon보다 20% 저렴한 비용으로 S3 Standard-Infrequent Access(S3 Standard-IA). Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 낮은 GB당 스토리지 가격과 GB당 검색 요금으로 S3 Standard와 동일한 높은 내구성, 높은 처리량 및 짧은 지연 시간을 제공합니다. Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 S3 Standard보다 가용성이 낮지만 썸네일을 쉽게 재생성할 수 있으므로 주어진 사용 사례에 문제가 되지 않습니다.

썸네일은 거의 사용되지 않지만 필요할 때 빠르게 액세스해야 하므로 Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)가 이 사용 사례에 가장 적합합니다.

시험 알림:

https://aws.amazon.com/s3/storage-classes/ 를 통해 S3의 이 측면에 대한 몇 가지 질문을 예상할 수 있으므로 S3 스토리지 클래스에 대한 이 자세한 비교를 검토하십시오.

잘못된 옵션:

Amazon S3 Standard-Infrequent Access(S3 Standard-IA)를 사용하여 썸네일 저장 - Amazon S3 Standard-Infrequent Access(S3 Standard-IA) 스토리지 클래스는 덜 자주 액세스하지만 필요할 때 빠른 액세스가 필요한 데이터용입니다. Amazon S3 Standard-Infrequent Access(S3 Standard-IA)는 S3 Standard의 높은 내구성, 높은 처리량 및 짧은 지연 시간에 필적하며 GB당 스토리지 가격과 GB당 검색 요금이 낮습니다. Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 Amazon S3 Standard-Infrequent Access(S3 Standard-IA)보다 20% 저렴하므로 이 옵션은 올바르지 않습니다.

Amazon S3 Standard를 사용하여 썸네일 저장 - Amazon S3 Standard는 자주 액세스하는 데이터에 대해 높은 내구성, 가용성 및 성능 객체 스토리지를 제공합니다. 위에서 설명한 것처럼 Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)는 Amazon S3 Standard보다 더 적합하므로 주어진 사용 사례에서 Amazon S3 표준을 사용하는 것은 제외됩니다.

Amazon S3 Glacier Flexible Retrieval을 사용하여 썸네일 저장 - Amazon S3 Glacier Flexible Retrieval은 데이터 아카이빙을 위한 안전하고 내구성이 있으며 저렴한 스토리지 클래스입니다. Amazon S3 Glacier Flexible Retrieval은 Amazon S3 One Zone-Infrequent Access(S3 One Zone-IA)보다 저렴하지만 검색 시간 범위가 1분에서 몇 시간까지이므로 이 옵션도 주어진 사용 사례에서 제외됩니다.

참조:

https://aws.amazon.com/s3/storage-classes/

-> IA one zone이 더쌈.... `가장 비용 효율적인 방법`을 봣어야함


--------------------------------------------------
41. 게임 회사는 다양한 위치의 최종 사용자에게 훌륭한 사용자 경험을 보장하기 위해 지연 시간이 짧은 게임 플레이를 일관되게 제공할 수 있는 기술/서비스를 찾고 있습니다.

최종 사용자에게 필요한 짧은 지연 시간 액세스를 제공하는 AWS 기술/서비스는 무엇입니까?


AWS 로컬 영역

AWS 로컬 영역을 사용하면 컴퓨팅 및 스토리지 서비스와 같은 엄선된 AWS 서비스를 더 많은 최종 사용자와 더 가깝게 사용할 수 있으므로 로컬에서 실행되는 애플리케이션에 매우 짧은 지연 시간으로 액세스할 수 있습니다. AWS 로컬 영역은 또한 Amazon의 중복 및 매우 높은 대역폭 사설 네트워크를 통해 상위 지역에 연결되어 AWS 로컬 영역에서 실행되는 애플리케이션이 나머지 AWS 서비스에 빠르고 안전하며 원활하게 액세스할 수 있도록 합니다.

지연 시간이 짧은 요구 사항을 위해 최종 사용자에게 더 가까운 워크로드를 배포하려면 AWS 로컬 영역을 사용해야 합니다. AWS 로컬 영역은 인터넷에 연결되어 있고 AWS Direct Connect를 지원하므로 로컬 영역에서 생성된 리소스는 지연 시간이 매우 짧은 통신으로 로컬 최종 사용자에게 서비스를 제공할 수 있습니다.

Amazon Elastic Compute Cloud(EC2), Amazon Virtual Private Cloud(VPC), Amazon Elastic Block Store(EBS), Amazon FSx, Amazon Elastic Load Balancing, Amazon EMR, Amazon ElastiCache 및 Amazon Relational Database Service(RDS)와 같은 다양한 AWS 서비스 )는 AWS 로컬 영역에서 로컬로 사용할 수 있습니다. Amazon EC2 Auto Scaling, Amazon EKS 클러스터, Amazon ECS 클러스터, Amazon EC2 Systems Manager, Amazon CloudWatch, AWS CloudTrail 및 AWS CloudFormation과 같은 로컬 서비스를 오케스트레이션하거나 함께 작동하는 서비스를 사용할 수도 있습니다. AWS 로컬 영역은 또한 AWS 리전에 대한 고대역폭 보안 연결을 제공하므로 동일한 API 및 도구 세트를 통해 AWS 리전의 모든 서비스에 원활하게 연결할 수 있습니다.

잘못된 옵션:

AWS 엣지 로케이션 - AWS 엣지 로케이션은 CloudFront가 모든 위치의 사용자에게 더 빠르게 전달하기 위해 콘텐츠 사본을 캐시하는 데 사용하는 사이트입니다.

AWS Wavelength - AWS Wavelength는 AWS 클라우드를 5G 엣지 로케이션의 글로벌 네트워크로 확장하여 개발자가 초저지연 시간이 필요한 완전히 새로운 종류의 애플리케이션을 혁신하고 구축할 수 있도록 합니다. Wavelength Zone은 상위 AWS 리전에 대한 고대역폭 보안 연결을 제공하여 개발자가 동일한 API 및 도구 세트를 통해 AWS 리전의 모든 서비스에 원활하게 연결할 수 있도록 합니다.

AWS Direct Connect - AWS Direct Connect는 네트워크를 AWS에 직접 연결하여 인터넷을 우회하여 보다 일관되고 지연 시간이 짧은 성능을 제공하는 클라우드 서비스입니다. 새 연결을 생성할 때 AWS Direct Connect 제공 파트너가 제공하는 호스팅 연결을 선택하거나 AWS의 전용 연결을 선택하고 전 세계 100개 이상의 AWS Direct Connect 위치에 배포할 수 있습니다. AWS Direct Connect는 지속적으로 높은 대역폭, 낮은 지연 시간 액세스를 제공하며 일반적으로 온프레미스 데이터 센터와 AWS 네트워크 간에 사용됩니다. Direct Connect는 주어진 요구 사항에 대해 과잉입니다.

참조:

https://aws.amazon.com/about-aws/global-infrastructure/localzones/

->  AWS 엣지 로케이션은 CloudFront가 모든 위치의 사용자에게 더 빠르게 전달하기 위해 콘텐츠 사본을 캐시하는 데 사용하는 사이트입니다....
다운 받는 캐쉬 사이트가 아님!!!

----------------------------------------------------------------

42. 운영 관점에서 AWS CAF(AWS Cloud Adoption Framework)의 일부인 기본 기능은 무엇입니까?


설명
올바른 옵션:

성능 및 용량 관리

AWS Cloud Adoption Framework(AWS CAF)는 AWS 경험과 모범 사례를 활용하여 AWS를 혁신적으로 사용하여 비즈니스 성과를 디지털 방식으로 전환하고 가속화하도록 지원합니다. AWS CAF를 사용하여 변환 기회를 식별하고 우선 순위를 지정하고, 클라우드 준비 상태를 평가 및 개선하고, 변환 로드맵을 반복적으로 발전시키십시오.

AWS CAF는 비즈니스, 사람, 거버넌스, 플랫폼, 보안 및 운영의 6가지 관점에서 기능을 그룹화합니다. 각 관점은 클라우드 혁신 과정에서 기능적으로 관련된 이해 관계자가 소유하거나 관리하는 일련의 기능으로 구성됩니다.

운영 관점은 클라우드 서비스가 비즈니스 요구 사항을 충족하는 수준으로 제공되도록 보장합니다. 운영 관점에서의 성능 및 용량 관리는 AWS Cloud Adoption Framework(AWS CAF)의 일부입니다.

AWS 클라우드 채택 프레임워크(AWS CAF) - 기본 기능: https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html 을 통해

잘못된 옵션:

취약성 관리 - 취약성 관리는 AWS CAF(AWS Cloud Adoption Framework)의 보안 관점에서 기본 기능입니다.

Platfrom 엔지니어링 - Platfrom 엔지니어링은 AWS Cloud Adoption Framework(AWS CAF)의 플랫폼 관점에서 기본 기능입니다.

애플리케이션 포트폴리오 관리 - 애플리케이션 포트폴리오 관리는 AWS CAF(AWS Cloud Adoption Framework)에 대한 거버넌스 관점의 기본 기능입니다.

참조:

https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html







