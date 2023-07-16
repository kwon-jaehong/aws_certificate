8. 다음 중 AWS 리전 및 가용 영역(AZ)에 대한 설명으로 옳은 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

각 AWS 리전은 지리적 영역 내에서 여러 개의 격리되고 물리적으로 분리된 가용 영역(AZ)으로 구성됩니다.

AWS에는 데이터 센터를 클러스터링하는 전 세계의 물리적 위치인 리전이라는 개념이 있습니다. AWS는 논리적 데이터 센터의 각 그룹을 가용 영역(AZ)이라고 부릅니다. 각 AWS 리전은 지리적 영역 내에서 여러 개의 격리되고 물리적으로 분리된 가용 영역(AZ)으로 구성됩니다.

각 가용 영역(AZ)은 독립적인 전원, 냉각 및 물리적 보안을 갖추고 있으며 지연 시간이 매우 짧은 중복 네트워크를 통해 연결됩니다. 고가용성에 중점을 둔 AWS 고객은 애플리케이션이 여러 가용 영역(AZ)에서 실행되도록 설계하여 더 큰 내결함성을 달성할 수 있습니다. AWS 인프라 리전은 최고 수준의 보안, 규정 준수 및 데이터 보호를 충족합니다.

`가용성 영역(AZ) 간의 모든 트래픽은 암호화됩니다.`

AWS 리전의 모든 가용 영역(AZ)은 가용 영역(AZ) 간에 높은 처리량, 짧은 지연 시간 네트워킹을 제공하는 완전히 중복된 전용 메트로 파이버를 통해 고대역폭, 짧은 지연 시간 네트워킹으로 상호 연결됩니다. 가용성 영역(AZ) 간의 모든 트래픽은 암호화됩니다.

잘못된 옵션:

가용 영역(AZ) 간의 트래픽은 기본적으로 암호화되지 않지만 AWS 콘솔에서 구성할 수 있습니다. `가용 영역(AZ) 간의 모든 트래픽은 암호화됩니다.`

가용 영역(AZ)은 AWS가 데이터 센터를 클러스터링하는 물리적 위치입니다 . AWS에는 AWS가 데이터 센터를 클러스터링하는 전 세계의 물리적 위치인 리전 개념이 있습니다.

AWS는 논리적 데이터 센터의 각 그룹을 AWS 리전이라고 부릅니다 . AWS에는 AWS가 데이터 센터를 클러스터링하는 전 세계의 물리적 위치인 리전 개념이 있습니다. `AWS는 논리적 데이터 센터의 각 그룹을 AZ(가용 영역)`라고 부릅니다.

참조:

https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

-> AZ간... 암호화를 내가 어케암.... 
-> 영어 해석도 이상함

------------------------------

9. 금융 컨설팅 회사는 AWS 클라우드에서 금융 솔루션을 배포하는 프로세스를 가속화할 자동화된 참조 배포를 찾고 있습니다. 참조 배포는 대부분의 잘 알려진 금융 서비스 기능을 배포할 수 있어야 하며 필요한 경우 사용자 지정을 위한 공간을 남겨 둘 수 있어야 합니다.

이 요구 사항을 달성하는 데 도움이 되는 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

AWS 파트너 솔루션(이전의 Quick Starts)

AWS 파트너 솔루션은 AWS 클라우드의 주요 워크로드에 대한 자동화된 참조 배포입니다. `각 파트너 솔루션은 보안 및 가용성에 대한 AWS 모범 사례를 사용하여 AWS에서 특정 워크로드를 배포하는 데 필요한 AWS 컴퓨팅, 네트워크, 스토리지 및 기타 서비스를 시작, 구성 및 실행합니다.`

파트너 솔루션은 수백 가지 수동 절차를 단 몇 단계로 압축하는 액셀러레이터입니다. 사용자 정의가 가능하고 생산용으로 설계되었습니다.

파트너 솔루션에는 다음이 포함됩니다. 1. 배포를 위한 참조 아키텍처 2. 배포를 자동화하고 구성하는 AWS CloudFormation 템플릿(JSON 또는 YAML 스크립트) 3. 아키텍처 및 구현에 대해 자세히 설명하고 다음을 사용자 지정하기 위한 지침을 제공하는 배포 가이드 전개

파트너 솔루션에는 고객 관계 관리(CRM), 인력 최적화(WFO), 분석, 통합 커뮤니케이션(UC), 다른 사용 사례.

잘못된 옵션:

AWS CloudFormation - AWS CloudFormation은 인프라를 코드로 취급하여 관련 AWS 및 타사 리소스 모음을 모델링하고 빠르고 일관되게 프로비저닝하며 전체 수명 주기 동안 관리할 수 있는 쉬운 방법을 제공합니다. CloudFormation 템플릿은 원하는 리소스와 해당 종속성을 설명하므로 스택으로 함께 시작하고 구성할 수 있습니다.

AWS Elastic Beanstalk - AWS Elastic Beanstalk는 Apache와 같은 친숙한 서버에서 Java, .NET, PHP, Node.js, Python, Ruby, Go 및 Docker로 개발된 웹 애플리케이션 및 서비스를 배포하고 확장하기 위한 사용하기 쉬운 서비스입니다. , Nginx, 승객 및 IIS. 코드를 업로드하기만 하면 Elastic Beanstalk가 용량 프로비저닝, 로드 밸런싱, 자동 확장에서 애플리케이션 상태 모니터링에 이르기까지 배포를 자동으로 처리합니다. 동시에 애플리케이션을 지원하는 AWS 리소스에 대한 완전한 제어권을 유지하고 언제든지 기본 리소스에 액세스할 수 있습니다.

Amazon Quicksight - Amazon QuickSight는 클라우드용으로 구축된 확장 가능하고 서버리스 내장형 기계 학습 기반 비즈니스 인텔리전스(BI) 서비스입니다. QuickSight를 사용하면 기계 학습 기반 통찰력을 포함하는 대화형 BI 대시보드를 쉽게 만들고 게시할 수 있습니다. QuickSight를 사용하면 대화형 대시보드를 애플리케이션, 웹 사이트 및 포털에 신속하게 포함할 수 있습니다.

참조:

https://aws.amazon.com/solutions/partners/faq/

-> 아니 이건좀... 안가르켜준거임


------------------------------------------------------------------

17. 온라인 소매 의류 매장은 3D 장면을 쉽게 생성하고 기존 웹 페이지에 포함하여 사용자 경험을 향상하고 판매를 개선할 수 있는 서비스/도구를 찾고 있습니다. 이러한 3D 시각적 개체를 생성하는 데 도움이 되는 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

아마존 수메르어

Amazon Sumerian은 3D, 증강 현실(AR) 및 가상 현실(VR) 애플리케이션을 생성하고 실행할 수 있는 관리형 서비스입니다. AR 및 VR, 모바일 장치 및 웹 브라우저에서 실행되는 몰입형 대화형 장면을 구축할 수 있습니다. 기술 지식이 없거나, 웹 또는 모바일 개발자이거나, 수년간의 3D 개발 경험이 있더라도 Sumerian을 쉽게 시작할 수 있습니다. 브라우저에서 직접 장면을 디자인할 수 있으며 Sumerian은 웹 기반 애플리케이션이기 때문에 장면의 연결을 기존 AWS 서비스에 빠르게 추가할 수 있습니다.

Amazon Sumerian은 AWS의 기능을 활용하여 더 스마트하고 매력적인 프런트 엔드 경험을 만듭니다. Amazon Lex를 사용하여 장면에 대화형 인터페이스를 쉽게 포함하고 AWS Amplify를 사용하여 웹 애플리케이션에 장면을 포함합니다. Amazon Sumerian은 최신 WebGL 및 WebXR 표준을 채택하여 웹 브라우저에서 직접 몰입형 경험을 만들고 간단한 URL을 통해 몇 초 만에 액세스할 수 있으며 AR/VR용 주요 하드웨어 플랫폼에서 실행할 수 있습니다. 장면을 한 번 빌드하고 어디에나 배포하십시오.

잘못된 옵션:

Amazon SageMaker - Amazon SageMaker는 모든 개발자와 데이터 과학자에게 기계 학습(ML) 모델을 신속하게 구축, 교육 및 배포할 수 있는 기능을 제공하는 완전관리형 서비스입니다. SageMaker는 기계 학습 프로세스의 각 단계에서 어려운 작업을 제거하여 고품질 모델을 더 쉽게 개발할 수 있도록 합니다. Amazon SageMaker는 ML 모델 아티팩트 및 기타 시스템 아티팩트가 전송 및 유휴 상태에서 암호화되도록 합니다.

Amazon Comprehend - Amazon Comprehend는 기계 학습을 사용하여 텍스트에서 의미와 통찰력을 찾는 자연어 처리(NLP) 서비스입니다. Amazon Comprehend를 사용하여 텍스트의 언어를 식별하고, 핵심 문구, 장소, 사람, 브랜드 또는 이벤트를 추출하고, 제품 또는 서비스에 대한 감정을 이해하고, 문서 라이브러리에서 주요 주제를 식별할 수 있습니다. 이 텍스트의 출처는 웹 페이지, 소셜 미디어 피드, 이메일 또는 기사일 수 있습니다.

Amazon Polly - Amazon Polly는 텍스트를 생생한 음성으로 변환하는 서비스로, 말하는 애플리케이션을 만들고 완전히 새로운 범주의 음성 지원 제품을 만들 수 있습니다. Polly의 TTS(텍스트 음성 변환) 서비스는 고급 딥 러닝 기술을 사용하여 자연스러운 사람의 음성을 합성합니다. 광범위한 언어 세트에 걸쳐 수십 개의 실제와 같은 음성을 사용하여 다양한 국가에서 작동하는 음성 지원 애플리케이션을 구축할 수 있습니다.

참조:

https://aws.amazon.com/sumerian/

-> 일부러 틀림, 폴리와 햇갈렷음 


-------------------------------------------------------------------------------------------------

18. 전자 상거래 회사는 여러 애플리케이션에서 병렬로 액세스하는 `NFS` 파일 시스템에 온프레미스 데이터 저장소를 가지고 있습니다. 이 회사는 애플리케이션과 데이터 저장소를 AWS 클라우드로 이전하는 방법을 모색하고 있습니다.

애플리케이션이 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스에서 호스팅되는 경우 회사에서 파일을 AWS 클라우드로 원활하게 이동하려면 어떤 스토리지 서비스를 사용해야 합니까?

설명
올바른 옵션:

Amazon 탄력적 파일 시스템(Amazon EFS)

Amazon Elastic File System(Amazon EFS)은 AWS 클라우드 서비스 및 온프레미스 리소스와 함께 사용할 수 있는 간단하고 확장 가능하며 완벽하게 관리되는 탄력적 NFS 파일 시스템을 제공합니다. 애플리케이션을 중단하지 않고 온디맨드 방식으로 페타바이트까지 확장할 수 있도록 구축되었으며, 파일을 추가 및 제거함에 따라 자동으로 확장 및 축소되므로 성장을 수용하기 위해 용량을 프로비저닝하고 관리할 필요가 없습니다.

Amazon EFS는 수천 개의 Amazon EC2 인스턴스에 대한 대규모 병렬 공유 액세스를 제공하도록 설계되어 애플리케이션이 지속적으로 낮은 지연 시간으로 높은 수준의 집계 처리량과 초당 입출력 작업(IOPS)을 달성할 수 있도록 합니다.

Amazon EFS는 홈 디렉터리에서 비즈니스 크리티컬 애플리케이션에 이르기까지 광범위한 사용 사례를 지원하는 데 매우 적합합니다. 고객은 EFS를 사용하여 기존 엔터프라이즈 애플리케이션을 AWS 클라우드로 리프트 앤 시프트할 수 있습니다. 다른 사용 사례로는 빅 데이터 분석, 웹 서비스 및 콘텐츠 관리, 애플리케이션 개발 및 테스트, 미디어 및 엔터테인먼트 워크플로우, 데이터베이스 백업 및 컨테이너 스토리지가 있습니다.

Amazon EFS는 Standard 스토리지 클래스와 Infrequent Access 스토리지 클래스(EFS IA)라는 두 가지 스토리지 클래스를 제공합니다. EFS IA는 매일 액세스하지 않는 파일에 대해 비용 최적화된 가격 대비 성능을 제공합니다. 파일 시스템에서 EFS 수명 주기 관리를 활성화하기만 하면 선택한 수명 주기 정책에 따라 액세스되지 않은 파일이 자동으로 투명하게 EFS IA로 이동됩니다.

Amazon EFS 작동 방식:  - https://aws.amazon.com/efs/ 를 통해

잘못된 옵션:

Amazon Elastic Block Store(Amazon EBS) - Amazon Elastic Block Store(Amazon EBS)는 처리량과 트랜잭션 모두를 위해 Amazon Elastic Compute Cloud(EC2)와 함께 사용하도록 설계된 사용하기 쉬운 고성능 블록 스토리지 서비스입니다. 모든 규모의 집약적 워크로드. 관계형 및 비관계형 데이터베이스, 엔터프라이즈 애플리케이션, 컨테이너화된 애플리케이션, 빅 데이터 분석 엔진, 파일 시스템 및 미디어 워크플로와 같은 광범위한 워크로드가 Amazon EBS에 광범위하게 배포됩니다. EBS는 블록 스토리지 서비스이며 EFS와 같은 파일 스토리지 서비스가 아닙니다.

Amazon Simple Storage Service(Amazon S3) - Amazon Simple Storage Service(Amazon S3)는 업계 최고의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스입니다. 즉, 모든 규모와 산업의 고객이 데이터 레이크, 웹 사이트, 모바일 애플리케이션, 백업 및 복원, 아카이브, 엔터프라이즈 애플리케이션, IoT 장치 및 빅 데이터와 같은 다양한 사용 사례에 대해 모든 양의 데이터를 저장하고 보호하는 데 사용할 수 있습니다. 데이터 분석. NFS 파일 시스템의 병렬 액세스는 Amazon S3에서 가능한 기능이 아니므로 여기에서 EFS가 올바른 선택입니다.

AWS Storage Gateway - AWS Storage Gateway는 사실상 무제한의 클라우드 스토리지에 온프레미스 액세스를 제공하는` 하이브리드 클라우드 스토리지 서비스`입니다. 고객은 Storage Gateway를 사용하여 스토리지 관리를 단순화하고 주요 하이브리드 클라우드 스토리지 사용 사례의 비용을 절감합니다. 여기에는 백업을 클라우드로 이동하고, 클라우드 스토리지에서 지원하는 온프레미스 파일 공유를 사용하고, 온프레미스 애플리케이션을 위해 AWS의 데이터에 대한 지연 시간이 짧은 액세스를 제공하는 것이 포함됩니다.

참조:

https://aws.amazon.com/efs/

-> 왜 스토리지 게이트웨이 아니지? `NFS` 나오면 무조건 EFS 찍어야됨


-------------------------------------------------------------------------------------------

21. 다음 중 AWS Elastic Beanstalk에서 지원하는 상태 모니터링 및 보고 기능에 대한 설명이 올바른 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS Elastic Beanstalk 상태 모니터링은 환경의 Auto Scaling 그룹이 사용 가능하고 최소 하나 이상의 인스턴스가 있는지 확인할 수 있습니다.

`Elastic Load Balancing 상태 확인 외에도 AWS Elastic Beanstalk는 환경의 리소스를 모니터링하고 배포에 실패하거나 올바르게 구성되지 않았거나 사용할 수 없게 되면 상태를 빨간색으로 변경합니다.` 이러한 검사는 다음을 확인합니다. 1. 환경의 Auto Scaling 그룹이 사용 가능하고 최소 하나 이상의 인스턴스가 있습니다. 2. 환경의 보안 그룹을 사용할 수 있으며 포트 80에서 들어오는 트래픽을 허용하도록 구성됩니다. 3. 환경 CNAME이 존재하고 올바른 로드 밸런서를 가리키고 있습니다. 4. 작업자 환경에서 Amazon Simple Queue Service(Amazon SQS) 대기열은 최소 3분마다 한 번씩 폴링됩니다.

`기본 상태 보고를 통해 AWS Elastic Beanstalk 서비스는 Amazon CloudWatch에 지표를 게시하지 않습니다.`

기본 상태 보고를 통해 AWS Elastic Beanstalk 서비스는 Amazon CloudWatch에 지표를 게시하지 않습니다. 환경 콘솔의 모니터링 페이지에서 그래프를 생성하는 데 사용되는 CloudWatch 지표는 환경의 리소스에 의해 게시됩니다.

잘못된 옵션:

AWS Elastic Beanstalk는 기본 상태 보고 시스템만 제공합니다. ELB(Elastic Load Balancing)와 결합하여 고급 상태 확인 기능을 제공합니다. `이 옵션은 선택 항목으로 추가되었습니다.`

단일 인스턴스 환경에서 AWS Elastic Beanstalk는 Elastic Load Balancing(ELB) 상태 설정을 모니터링하여 인스턴스의 상태를 결정합니다. - 단일 인스턴스 또는 작업자 계층 환경에서 AWS Elastic Beanstalk는 Amazon EC2 인스턴스 상태를 모니터링하여 인스턴스의 상태를 결정합니다. HTTP 상태 확인 URL을 포함한 Elastic Load Balancing 상태 설정은 이러한 환경 유형에서 사용할 수 없습니다.

AWS Elastic Beanstalk 환경의 인스턴스 상태에 대한 정보를 제공하는 기본 상태 보고 시스템은 Elastic Load Balancing(ELB)에서 수행하는 상태 확인을 사용하지 않습니다. - 기본 상태 보고 시스템은 AWS Elastic Beanstalk의 인스턴스 상태에 대한 정보를 제공합니다. 로드 밸런싱된 환경의 경우 Elastic Load Balancing에서 수행하는 상태 확인 또는 단일 인스턴스 환경의 경우 Amazon Elastic Compute Cloud(Amazon EC2)에서 수행하는 상태 확인을 기반으로 하는 환경.

참조:

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.healthstatus.html#monitoring-basic-additionalchecks

-> 빈스텍 모니터링 숙지

---------------------------------------------------------------------
23. 다음 중 AWS Key Management Service(KMS)를 사용하여 AWS 계정에서만 AWS 서비스용 데이터를 암호화하는 가장 쉬운 방법은 무엇입니까?

설명
올바른 옵션:

각 서비스에 대해 계정에 자동으로 생성되는 AWS 관리형 마스터 키 사용

`AWS KMS 키(KMS 키)는 AWS KMS의 기본 리소스입니다`. KMS 키를 사용하여 데이터를 암호화, 해독 및 재암호화할 수 있습니다. 또한 AWS KMS 외부에서 사용할 수 있는 데이터 키를 생성할 수도 있습니다. AWS KMS는 고객 마스터 키(CMK)라는 용어를 AWS KMS 키 및 KMS 키로 대체합니다.

`AWS 관리형 CMK`는 AWS KMS와 통합된 AWS 서비스에서 사용자 대신 생성, 관리 및 사용하는 계정의 CMK입니다. 일부 AWS 서비스는 AWS 관리형 CMK만 지원합니다. 다른 사람들은 AWS 소유 CMK를 사용하거나 CMK 선택권을 제공합니다. AWS 관리형 CMK는 AWS 계정에만 사용할 수 있습니다.

계정에서 AWS 관리형 CMK를 보고, 키 정책을 보고, AWS CloudTrail 로그에서 사용을 감사할 수 있습니다. 그러나 이러한 CMK를 관리하거나 교체하거나 키 정책을 변경할 수 없습니다. 또한 암호화 작업에서 직접 AWS 관리형 CMK를 사용할 수 없습니다. 그것들을 생성하는 서비스는 당신을 대신하여 그것들을 사용합니다.

AWS 관리형 CMK는 AWS KMS용 AWS Management 콘솔의 AWS 관리형 키 페이지에 나타납니다. 또한 aws/redshift와 같은 aws/service-name 형식의 별칭으로 대부분의 AWS 관리형 CMK를 식별할 수 있습니다.

AWS 관리형 CMK에 대해 월별 요금을 지불하지 않습니다. 프리 티어를 초과하여 사용하는 경우 요금이 부과될 수 있지만 일부 AWS 서비스는 이러한 비용을 부담합니다.

잘못된 옵션:

AWS KMS에서 자체 고객 관리형 키(CMK) 생성 - 생성하는 AWS KMS 키는 고객 관리형 키입니다. 고객 관리형 키는 귀하가 생성, 소유 및 관리하는 AWS 계정의 KMS 키입니다. 키 정책, IAM 정책 및 권한 부여 설정 및 유지 관리, 활성화 및 비활성화, 암호화 자료 교체, 태그 추가, KMS 키를 참조하는 별칭 생성, KMS 키 예약을 포함하여 이러한 KMS 키를 완전히 제어할 수 있습니다. 삭제를 위해.

고객 관리형 키(CMK)는 월 사용료와 프리 티어를 초과하는 사용료가 발생합니다. 계정에 대한 AWS KMS 할당량에 대해 계산됩니다.

AWS KMS API를 사용하여 AWS 암호화 SDK를 사용하여 자체 애플리케이션 내의 데이터를 암호화합니다. AWS KMS API는 프로그래밍 방식 액세스를 위해 AWS KMS Command Line Interface 또는 AWS SDK를 통해 직접 액세스할 수도 있습니다. AWS KMS API는 AWS 암호화 SDK를 사용하여 자체 애플리케이션 내의 데이터를 암호화하는 데 간접적으로 사용할 수도 있습니다. 이를 위해서는 코드 변경이 필요하며 암호화를 달성하는 가장 쉬운 방법은 아닙니다.

암호화를 사용하려는 서비스에서 AWS 소유 CMK 사용 - AWS 소유 CMK는 AWS 서비스가 여러 AWS 계정에서 사용하기 위해 소유하고 관리하는 CMK 모음입니다. AWS 소유 CMK가 AWS 계정에 없지만 AWS 서비스는 AWS 소유 CMK를 사용하여 계정의 리소스를 보호할 수 있습니다. AWS 소유 CMK는 여러 AWS 계정에 사용할 수 있습니다.

AWS 소유 CMK를 생성하거나 관리할 필요가 없습니다. 그러나 이를 보거나 사용하거나 추적하거나 감사할 수는 없습니다. AWS 소유 CMK에 대한 월별 요금 또는 사용 요금은 청구되지 않으며 계정의 AWS KMS 할당량에 포함되지 않습니다.

참조:

https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys

-> KSM 실습 필요....

-----------------------------------------------

26. 다음 중 AWS 공동 책임 모델에 대한 설명으로 옳은 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS는 인프라 내의 결함 패치 및 수정을 담당하지만 고객은 게스트 운영 체제 및 애플리케이션 패치를 담당합니다.

AWS는 AWS 직원을 교육하지만 고객은 자신의 직원을 교육해야 합니다.

"클라우드의 보안"은 AWS의 책임입니다. AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다. 이 인프라는 AWS 클라우드 서비스를 실행하는 하드웨어, 소프트웨어, 네트워킹 및 시설로 구성됩니다. AWS 공유 책임 모델의 공유 제어 책임인 패치 관리의 일환으로 AWS는 인프라 내의 결함 패치 및 수정을 담당하지만 고객은 게스트 OS 및 애플리케이션 패치를 담당합니다.

"클라우드 보안"은 고객의 책임입니다. 고객 책임은 고객이 선택한 AWS 클라우드 서비스에 따라 결정됩니다. 이는 고객이 보안 책임의 일부로 수행해야 하는 구성 작업의 양을 결정합니다.

AWS 공유 책임 모델의 공유 제어 책임인 인식 및 교육의 일환으로 AWS는 AWS 직원을 교육하지만 고객은 자신의 직원을 교육해야 합니다.

AWS 공유 책임 모델: https://aws.amazon.com/compliance/shared-responsibility-model/ 을 통해

잘못된 옵션:

AWS는 인프라 장치의 구성을 유지 관리하고 게스트 운영 체제, 데이터베이스 및 애플리케이션 구성을 담당합니다. AWS 공유 책임 모델의 공유 제어 책임인 구성 관리의 일부로 AWS는 인프라 장치의 구성을 유지 관리하지만 고객은 자신의 게스트 운영 체제, 데이터베이스 및 애플리케이션을 구성할 책임이 있습니다.

Amazon Elastic Compute Cloud(Amazon EC2)는 IaaS(Infrastructure as a Service)로 분류되므로 AWS는 필요한 모든 보안 구성 및 관리 작업을 수행합니다. Amazon Elastic Compute Cloud(Amazon EC2)와 같은 서비스는 다음과 같은 인프라로 분류됩니다. 서비스(IaaS)이므로 고객은 필요한 모든 보안 구성 및 관리 작업을 수행해야 합니다. Amazon EC2 인스턴스를 배포하는 고객은 게스트 운영 체제(업데이트 및 보안 패치 포함), 고객이 인스턴스에 설치한 모든 애플리케이션 소프트웨어 또는 유틸리티, AWS에서 제공하는 방화벽( 보안 그룹)이 각 인스턴스에 있습니다.

Amazon S3와 같은 추상화된 서비스의 경우 AWS가 인프라 계층, 운영 체제, 플랫폼, 암호화 옵션 및 S3 리소스에 액세스하기 위한 적절한 권한을 운영합니다. - Amazon S3 및 Amazon DynamoDB와 같은 추상화된 서비스의 경우 AWS가 인프라 계층을 운영합니다 . , 운영 체제 및 플랫폼과 고객은 끝점에 액세스하여 데이터를 저장하고 검색합니다. `고객은 데이터 관리(암호화 옵션 포함)`, 자산 분류 및 IAM 도구를 사용하여 적절한 권한을 적용할 책임이 있습니다.

참조:

https://aws.amazon.com/ko/compliance/shared-responsibility-model/

-> ? aws에서 고객을 교육해야되는거 아니엿음? ` AWS는 AWS 직원을 교육하고, 고객은 자사의 직원을 교육해야 합니다.`잇네...
-> 일부러 틀리긴 함.


----------------------------------
30. AWS Control Tower 및 서비스 제어 정책에 관한 다음 설명 중 올바른 것은 무엇입니까? (2개 선택)



올바른 옵션:

AWS Control Tower는 고객이 새 AWS 계정에 대한 랜딩 존을 구현하는 데 도움이 되는 사전 정의된 청사진 및 가드레일 세트를 제공하는 AWS 기본 서비스입니다.

AWS Control Tower는 고객이 새 AWS 계정에 대한 랜딩 존을 구현하는 데 도움이 되는 사전 정의된 청사진 및 가드레일 세트를 제공하는 AWS 기본 서비스입니다.

AWS Control Tower는 쉬운 셀프 서비스 설정 환경과 가드레일을 통한 지속적인 거버넌스를 위한 대화형 사용자 인터페이스를 제공하도록 설계되었습니다. Control Tower는 미리 구성된 청사진(예: 디렉터리 및 액세스를 위한 AWS IAM Identity Center)을 사용하여 새로운 랜딩 존 생성을 자동화하는 반면, AWS Landing Zone 솔루션은 맞춤형 추가 기능을 통해 풍부한 사용자 지정 옵션으로 구성 가능한 랜딩 존 설정을 제공합니다. (예: Active Directory, Okta Directory) 및 코드 배포 및 구성 파이프라인을 통한 지속적인 수정.

AWS Control Tower 작동 방식:  - https://aws.amazon.com/controltower/ 를 통해

서비스 제어 정책(SCP)은 조직에서 권한을 관리하는 데 사용할 수 있는 조직 정책 유형입니다.

서비스 제어 정책(SCP)은 조직에서 권한을 관리하는 데 사용할 수 있는 조직 정책 유형입니다. 서비스 제어 정책(SCP)은 조직의 모든 계정에 대해 사용 가능한 최대 권한에 대한 중앙 제어를 제공합니다. 서비스 제어 정책(SCP)은 계정이 조직의 액세스 제어 지침을 준수하도록 하는 데 도움이 됩니다. SCP는 모든 기능이 활성화된 조직에서만 사용할 수 있습니다. 조직에서 통합 결제 기능만 활성화한 경우 SCP를 사용할 수 없습니다.

잘못된 옵션:

AWS Control Tower는 다중 계정 AWS 환경을 배포하고 일상적인 알림 및 권장 사항으로 운영할 수 있도록 지원합니다. AWS Control Tower는 모범 사례를 기반으로 다중 계정 AWS 환경을 배포하는 데 도움을 주지만 여전히 고객은 일상적인 운영 및 규정 준수 상태 확인. 클라우드에서 규제된 인프라를 운영하는 데 도움이 필요한 기업은 인증된 MSP 파트너 또는 AWS 관리형 서비스(AMS)를 고려해야 합니다.

서비스 제어 정책(SCP)은 조직의 계정에 권한을 부여하는 데 도움이 될 수 있습니다 . `SCP만으로는 조직의 계정에 권한을 부여하기에 충분하지 않습니다`. SCP는 권한을 부여하지 않습니다. SCP는 계정 관리자가 영향을 받는 계정의 IAM 사용자 및 역할에 위임할 수 있는 작업에 대한 `가드레일을 정의하거나 제한`을 설정합니다. 관리자는 실제로 권한을 부여하기 위해 자격 증명 기반 또는 리소스 기반 정책을 IAM 사용자나 역할 또는 계정의 리소스에 연결해야 합니다. 유효 권한은 SCP에서 허용하는 것과 IAM 및 리소스 기반 정책에서 허용하는 것 사이의 논리적 교차점입니다.

서비스 제어 정책(SCP)은 기본적으로 AWS Organization의 모든 사용자에게 영향을 미칩니다. 필요한 경우 회원 계정에만 영향을 미치도록 구성해야 합니다 . SCP는 마스터 계정의 사용자 또는 역할에 영향을 미치지 않습니다. 조직의 멤버 계정에만 영향을 미칩니다.

참조:

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

https://aws.amazon.com/controltower/faqs/


-> 아... scp만으로는 조직의 계정에 관한 권한은 도움이 안되네... `IAM까지 해야됨`

---------------------------------------------
35. 제조 회사는 대기 시간이 짧은 애플리케이션을 실행하기 위해 온프레미스 데이터 센터에 AWS 인프라, AWS 서비스, API 및 도구를 제공할 수 있는 서비스를 찾고 있습니다.

다음 중 주어진 요구 사항에 가장 적합한 서비스/도구는 무엇입니까?


올바른 옵션:

AWS 전초기지

AWS Outposts는 진정으로 일관된 하이브리드 경험을 위해 거의 모든 데이터 센터, 코로케이션 공간 또는 온프레미스 시설에 동일한 AWS 인프라, AWS 서비스, API 및 도구를 제공하는 완전 관리형 서비스입니다. AWS Outposts는 온프레미스 시스템에 대한 짧은 대기 시간 액세스, 로컬 데이터 처리, 데이터 레지던시 및 로컬 시스템 상호 종속성이 있는 애플리케이션 마이그레이션이 필요한 워크로드에 이상적입니다.

AWS 컴퓨팅, 스토리지, 데이터베이스 및 기타 서비스는 Outposts에서 로컬로 실행되며 리전에서 사용 가능한 모든 AWS 서비스에 액세스하여 친숙한 AWS 서비스 및 도구를 사용하여 온프레미스 애플리케이션을 구축, 관리 및 확장할 수 있습니다.

AWS Outposts를 사용하여 지연 시간이 짧거나 로컬 데이터 처리 요구 사항이 있는 애플리케이션을 지원할 수 있습니다. 이러한 애플리케이션은 최종 사용자 애플리케이션에 대한 거의 실시간 응답을 생성하거나 다른 온프레미스 시스템과 통신하거나 현장 장비를 제어해야 할 수 있습니다. 여기에는 제조, 실시간 환자 진단 또는 의료 영상, 콘텐츠 및 미디어 스트리밍의 자동화된 작업을 위해 공장 현장에서 실행되는 워크로드가 포함될 수 있습니다. Outposts를 사용하여 온프레미스 또는 AWS 리전이 없는 국가에 유지해야 하는 고객 데이터를 안전하게 저장하고 처리할 수 있습니다. 데이터를 클라우드로 전송하는 것이 비용이 많이 들고 낭비적일 때 데이터 분석, 백업 및 복원을 더 잘 제어하기 위해 Outposts에서 데이터 집약적인 워크로드를 실행하고 로컬에서 데이터를 처리할 수 있습니다.

AWS Outposts 작동 방식:  - https://aws.amazon.com/outposts/ 를 통해

잘못된 옵션:

AWS Snow 패밀리 - AWS Snow 패밀리는 네트워크에 의존하지 않고 클라우드 안팎으로 대량의 데이터를 마이그레이션하는 데 도움이 되는 물리적 장치 모음입니다. 이를 통해 분석, 파일 시스템 및 아카이브를 위한 다양한 AWS 서비스를 데이터에 적용할 수 있습니다. 위치에서 데이터 전송 및 간헐적인 사전 처리를 위해 AWS Snow Family 서비스를 사용할 수 있습니다. 일부 대규모 데이터 전송의 예로는 클라우드 마이그레이션, 재해 복구, 데이터 센터 재배치 및/또는 원격 데이터 수집 프로젝트가 있습니다. 이러한 프로젝트에서는 일반적으로 가장 짧고 가장 비용 효율적인 시간 내에 많은 양의 데이터를 마이그레이션해야 합니다.

AWS Wavelength - AWS Wavelength는 모바일 엣지 컴퓨팅 애플리케이션에 최적화된 AWS 인프라 제품입니다. Wavelength Zone은 5G 네트워크 가장자리에 있는 CSP(통신 서비스 제공업체) 데이터 센터 내에 AWS 컴퓨팅 및 스토리지 서비스를 포함하는 AWS 인프라 배포로, 5G 장치의 애플리케이션 트래픽이 통신 네트워크를 벗어나지 않고 Wavelength Zone에서 실행되는 애플리케이션 서버에 도달할 수 있습니다. .

AWS 로컬 영역 - AWS 로컬 영역은 대규모 인구, 산업 및 IT 센터에 가까운 AWS 컴퓨팅, 스토리지, 데이터베이스 및 기타 선별된 서비스를 배치하는 AWS 인프라 배포 유형입니다. AWS 로컬 영역을 사용하면 특정 지역의 최종 사용자에게 더 가까운 한 자릿수 밀리초의 지연 시간이 필요한 애플리케이션을 쉽게 실행할 수 있습니다. AWS 로컬 영역은 미디어 및 엔터테인먼트 콘텐츠 생성, 실시간 게임, 라이브 비디오 스트리밍, 기계 학습 추론과 같은 사용 사례에 이상적입니다.

참조:

https://aws.amazon.com/outposts/

-> 아웃풋츠 생각 못햇슴....


-----------------------------------------------------

36. 전자 상거래 애플리케이션은 주문이 생성될 때마다 다운스트림 애플리케이션에 메시지를 보냅니다. 다운스트림 애플리케이션은 메시지를 처리하고 자체 시스템을 업데이트합니다. 현재 두 애플리케이션은 서로 직접 통신합니다.

두 시스템 간의 통신 손실 없이 이 아키텍처를 분리하는 데 사용할 서비스는 무엇입니까?


올바른 옵션:

Amazon 단순 대기열 서비스(SQS)

Amazon Simple Queue Service(SQS)는 마이크로서비스, 분산 시스템 및 서버리스 애플리케이션을 분리하고 확장할 수 있는 완전관리형 메시지 대기열 서비스입니다. SQS는 메시지 지향 미들웨어 관리 및 운영과 관련된 복잡성과 오버헤드를 제거하고 개발자가 차별화 작업에 집중할 수 있도록 합니다. SQS를 사용하면 메시지 손실이나 다른 서비스를 사용할 필요 없이 모든 볼륨에서 소프트웨어 구성 요소 간에 메시지를 전송, 저장 및 수신할 수 있습니다. 선택한 AWS 콘솔, 명령줄 인터페이스 또는 SDK와 세 가지 간단한 명령을 사용하여 몇 분 만에 SQS를 시작하십시오.

Amazon SQS는 풀 메커니즘을 사용합니다. 즉, 등록된 프로세스가 메시지를 풀링하여 처리할 때까지 대기열의 메시지를 사용할 수 있습니다. 이는 두 번째 애플리케이션이 애플리케이션 1에서 오는 메시지를 처리하기 위해 항상 사용 가능할 필요가 없기 때문에 아키텍처를 분리합니다.

잘못된 옵션:

Amazon Simple Notification Service(Amazon SNS) - Amazon Simple Notification Service(Amazon SNS)는 A2A(애플리케이션 간) 및 A2P(애플리케이션 간) 통신을 위한 완전관리형 메시징 서비스입니다. A2A 게시/구독 기능은 분산 시스템, 마이크로서비스 및 이벤트 기반 서버리스 애플리케이션 간의 높은 처리량, 푸시 기반, 다대다 메시징에 대한 주제를 제공합니다. Amazon SNS를 사용하면 애플리케이션이 "푸시" 메커니즘을 통해 시간이 중요한 메시지를 여러 구독자에게 보낼 수 있습니다. 즉, 메시지를 수신하려면 수신 애플리케이션이 존재하고 실행 중이어야 합니다. SNS에는 메시지 손실 범위가 있으므로 SQS는 이 사용 사례에 적합한 선택입니다.

Amazon Kinesis 데이터 스트림 - Amazon Kinesis Data Streams를 사용하면 특별한 요구에 맞게 스트리밍 데이터를 처리하거나 분석하는 사용자 지정 애플리케이션을 구축할 수 있습니다. 클릭스트림, 애플리케이션 로그, 소셜 미디어와 같은 다양한 유형의 데이터를 수십만 소스의 Amazon Kinesis 데이터 스트림에 지속적으로 추가할 수 있습니다. 몇 초 안에 Amazon Kinesis 애플리케이션이 스트림에서 데이터를 읽고 처리할 수 있습니다. Kinesis Data Streams는 스트리밍 빅 데이터의 실시간 처리를 위한 것이기 때문에 Kinesis Data Streams는 이 사용 사례에 과잉입니다.

AWS Lambda - AWS Lambda는 서버 프로비저닝 또는 관리, 워크로드 인식 클러스터 확장 논리 생성, 이벤트 통합 유지 또는 런타임 관리 없이 코드를 실행할 수 있는 서버리스 컴퓨팅 서비스입니다. Lambda를 사용하면 관리 없이 거의 모든 유형의 애플리케이션 또는 백엔드 서비스에 대한 코드를 실행할 수 있습니다. 코드를 ZIP 파일 또는 컨테이너 이미지로 업로드하기만 하면 Lambda가 컴퓨팅 실행 능력을 자동으로 정확하게 할당하고 모든 규모의 트래픽에 대해 들어오는 요청 또는 이벤트를 기반으로 코드를 실행합니다. Lambda 함수는 자체 호출할 수 없으며 호출해야 합니다. 또한 Lambda 함수는 나중에 처리하기 위해 데이터를 저장할 수 없습니다.

참조:

https://aws.amazon.com/sqs/

-> 아니... 다운스트림에 뿌려주는게 아니엿네.... 아오

------------------------------------------------

40. 다음 중 필요한 AWS 리소스 수를 유지하기 위해 Auto Scaling 그룹(ASG)의 `예측 조정`을 효과적으로 사용할 수 있는 올바른 시나리오를 나타내는 것은 무엇입니까?

올바른 옵션:

특정 요일 또는 시간에 따라 반복되는 부하 패턴을 나타내는 워크로드를 관리하려면

예측 조정은 기계 학습을 사용하여 CloudWatch의 기록 데이터를 기반으로 용량 요구 사항을 예측합니다. 기계 학습 알고리즘은 사용 가능한 과거 데이터를 소비하고 과거 부하 패턴에 가장 적합한 용량을 계산한 다음 새로운 데이터를 기반으로 지속적으로 학습하여 향후 예측을 더 정확하게 만듭니다.

예측 조정은 다음과 같은 상황에 매우 적합합니다.

정규 업무 시간에는 리소스 사용량이 많고 저녁 및 주말에는 리소스 사용량이 적은 순환 트래픽

일괄 처리, 테스트 또는 주기적인 데이터 분석과 같은 반복적인 온/오프 워크로드 패턴

초기화하는 데 오랜 시간이 걸리는 애플리케이션으로 확장 이벤트 중에 애플리케이션 성능에 눈에 띄는 대기 시간 영향을 줍니다.

잘못된 옵션:

Auto Scaling 그룹의 평균 집계 CPU 사용률을 40%로 유지하도록 조정 정책을 구성하려면 대상 추적 조정 정책이 이 사용 사례에 가장 적합합니다. 대상 추적 조정 정책을 사용하여 조정 지표를 선택하고 대상 값을 설정합니다. Amazon EC2 Auto Scaling은 조정 정책을 트리거하고 지표 및 대상 값을 기반으로 조정 조정을 계산하는 CloudWatch 경보를 생성 및 관리합니다. 조정 정책은 메트릭을 지정된 목표 값 또는 그에 근접하게 유지하는 데 필요한 만큼 용량을 추가하거나 제거합니다.

ApproximateNumberOfMessagesVisible지표 값에 따라 그룹을 조정하는 것과 같이 CloudWatch Amazon Simple Queue Service(Amazon SQS) 지표를 구성하는 데 도움이 되도록 대상 추적 조정 정책이 이 backlog per instance metric사용 사례에 가장 적합합니다. SQS 대기열의 메시지 수가 필요한 인스턴스 수를 단독으로 정의하지 않기 때문입니다. Auto Scaling 그룹의 인스턴스 수는 메시지를 처리하는 데 걸리는 시간과 허용되는 지연 시간(대기열 지연)을 비롯한 여러 요인에 의해 좌우될 수 있습니다.

Auto Scaling 그룹에서 고정된 수의 리소스를 관리하려면 - 현재 인스턴스 수준을 항상 고정된 수로 유지하는 것이 ASG를 구성하는 기본적인 방법입니다. 고정된 수의 리소스를 유지하기 위해 Predictive Scaling이 필요하지 않습니다.

참조:

https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling_plan.html

-> `예측`조정이라는 말...


---------------------------------------------------------

47. 다음 중 Amazon Detective에서 이벤트를 분석하고 잠재적인 보안 문제를 식별하는 데 사용하는 데이터 소스는 무엇입니까?


올바른 옵션:

AWS CloudTrail 로그, Amazon VPC 흐름 로그 및 Amazon GuardDuty 결과

Amazon Detective는 Virtual Private Cloud(VPC) Flow Logs, AWS CloudTrail 및 Amazon GuardDuty와 같은 여러 데이터 소스에서 수조 건의 이벤트를 분석하고 리소스, 사용자 및 시간 경과에 따른 상호 작용에 대한 통합된 대화형 보기를 자동으로 생성할 수 있습니다. .

Amazon Detective는 데이터 보호에 대한 규정 및 지침을 포함하는 AWS 공유 책임 모델을 준수합니다. 활성화되면 Amazon Detective는 활성화된 모든 계정에 대한 `AWS CloudTrail 로그, VPC 흐름 로그 및 Amazon GuardDuty` 조사 결과의 데이터를 처리합니다.

Amazon Detective를 사용하려면 해당 계정에서 Detective를 활성화하기 전에 최소 48시간 동안 해당 계정에서 Amazon GuardDuty를 활성화해야 합니다. 그러나 Detective를 사용하여 GuardDuty 결과 이상을 조사할 수 있습니다. Amazon Detective는 AWS 계정, EC2 인스턴스, AWS 사용자, 역할 및 IP 주소 간의 동작 및 상호 작용에 대한 자세한 요약, 분석 및 시각화를 제공합니다. 이 정보는 보안 문제 또는 운영 계정 활동을 이해하는 데 매우 유용할 수 있습니다.

Amazon Detective의 작동 방식:  - https://aws.amazon.com/detective/ 를 통해

잘못된 옵션:

Amazon CloudWatch Logs, Amazon VPC 흐름 로그 및 Amazon GuardDuty 결과

Amazon CloudWatch Logs, AWS CloudTrail 로그 및 Amazon Simple Storage Service(Amazon S3) 액세스 로그

Amazon CloudWatch Logs, AWS CloudTrail 로그 및 Amazon Inspector 로그

이 세 가지 옵션은 위에 제공된 설명과 상충되므로 이러한 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/detective/

-> 아... vpc 플로우 듀티구나...

---------------------------------------------
49. 의료 회사는 연속 복제 기반 재해 복구 메커니즘을 구현하고 물리적, 가상 및 클라우드 기반 서버를 AWS 클라우드로 빠르고 안정적으로 복구하고자 합니다. 다음 중 이 사용 사례에 가장 적합한 솔루션은 무엇입니까?


설명
올바른 옵션:

CloudEndure 재해 복구 (견디다)

AWS Marketplace에서 제공되는 CloudEndure Disaster Recovery는 기본 서버의 블록 수준 복제를 사용하여 모든 소스의 서버 호스팅 애플리케이션 및 서버 호스팅 데이터베이스를 AWS로 지속적으로 복제합니다. CloudEndure Disaster Recovery를 사용하면 AWS 클라우드를 온프레미스 워크로드 및 해당 환경의 재해 복구 리전으로 사용할 수 있습니다. 또한 EC2(예: RDS 아님)에서 호스팅되는 애플리케이션 및 데이터베이스로만 구성된 경우 AWS 호스팅 워크로드의 재해 복구에도 사용할 수 있습니다.

CloudEndure Disaster Recovery의 기능:

연속 복제: CloudEndure Disaster Recovery는 소스 머신을 스테이징 영역으로 연속 비동기식 블록 수준 복제를 제공합니다. 재해가 발생하면 최신 애플리케이션이 항상 AWS에서 가동될 준비가 되어 있으므로 1초 미만의 RPO(복구 지점 목표)를 달성할 수 있습니다.

저비용 스테이징 영역: 데이터는 대상 AWS 리전의 경량 스테이징 영역에서 지속적으로 동기화됩니다. 스테이징 영역에는 CloudEndure Disaster Recovery에서 자동으로 프로비저닝하고 관리하는 저비용 리소스가 포함되어 있습니다. 이렇게 하면 중복 리소스가 필요하지 않으며 재해 복구 총 소유 비용(TCO)이 크게 줄어듭니다.

자동화된 머신 변환 및 오케스트레이션: 재해 또는 드릴이 발생하는 경우 CloudEndure Disaster Recovery는 고도로 자동화된 머신 변환 프로세스와 확장 가능한 오케스트레이션 엔진을 트리거하여 대상 AWS 리전에 있는 수천 대의 머신을 병렬로 신속하게 가동합니다. 이를 통해 몇 분의 RTO(복구 시간 목표)를 달성할 수 있습니다. 애플리케이션 수준 솔루션과 달리 CloudEndure Disaster Recovery는 OS, 시스템 상태 구성, 시스템 디스크, 데이터베이스, 애플리케이션 및 파일을 포함한 전체 시스템을 복제합니다.

지정 시간 복구: 세분화된 지정 시간 복구를 사용하면 우발적인 시스템 변경, 랜섬웨어 또는 기타 악의적인 공격으로 인해 손상된 애플리케이션 및 IT 환경을 복구할 수 있습니다. 이러한 경우 가장 최신 상태로 애플리케이션을 시작하는 대신 이전의 일관된 시점에서 애플리케이션을 시작할 수 있습니다. 복구 중에 특정 시점 목록에서 최신 상태 또는 이전 상태를 선택할 수 있습니다.

손쉬운 무중단 훈련: CloudEndure Disaster Recovery를 사용하면 소스 환경을 중단하거나 데이터 손실 위험 없이 재해 복구 훈련을 수행할 수 있습니다. 훈련 중에 CloudEndure Disaster Recovery는 네트워크 충돌 및 성능 영향을 방지하기 위해 완전히 격리된 상태에서 대상 AWS 리전의 시스템을 가동합니다.

광범위한 애플리케이션 및 인프라 지원: CloudEndure Disaster Recovery는 블록 수준에서 데이터를 복제하므로 지원되는 버전의 Windows 및 Linux OS에서 실행되는 모든 애플리케이션 및 데이터베이스에 사용할 수 있습니다.

CloudEndure 재해 복구:  - https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html 을 통해

잘못된 옵션:

AWS Snowball Edge - AWS Snowball Edge는 일부 AWS 기능을 위한 온보드 스토리지 및 컴퓨팅 성능을 갖춘 Snowball 디바이스 유형입니다. Snowball Edge는 로컬 환경과 AWS 클라우드 간에 데이터를 전송하는 것 외에도 로컬 처리 및 엣지 컴퓨팅 워크로드를 수행할 수 있습니다. AWS Snowball Edge는 모바일 네트워크를 통한 연결을 최적화하는 데 사용할 수 없습니다. 연속 복제 기반 재해 복구에는 사용할 수 없습니다.

AWS Storage Gateway - AWS Storage Gateway는 사실상 무제한의 클라우드 스토리지에 온프레미스 액세스를 제공하는 하이브리드 클라우드 스토리지 서비스입니다. Storage Gateway는 iSCSI, SMB 및 NFS와 같은 표준 스토리지 프로토콜 세트를 제공하므로 기존 애플리케이션을 다시 작성하지 않고도 AWS 스토리지를 사용할 수 있습니다. Amazon EBS 스냅샷 형식으로 볼륨 게이트웨이 볼륨의 특정 시점 스냅샷을 생성할 수 있습니다. 이 접근 방식을 사용하면 데이터 처리를 위한 온디맨드 컴퓨팅 용량이 추가로 필요하거나 재해 복구를 위한 교체 용량이 필요한 경우 온프레미스 애플리케이션의 데이터를 Amazon EC2에서 실행되는 애플리케이션으로 쉽게 공급할 수 있습니다. 그러나 Storage Gateway는 연속 복제 기반 재해 복구에 사용할 수 없습니다.

CloudCover 재해 복구 - 이것은 구성된 옵션이며 선택 항목으로 추가되었습니다.

참조:

https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html


-> 이거 안가르쳐줌

---------------------------------------

50. Amazon API Gateway에 대한 다음 설명 중 올바른 것은 무엇입니까? (2개 선택)

Amazon API Gateway는 AWS Lambda 함수를 호출하여 서버리스 애플리케이션의 정문을 생성할 수 있습니다.

Amazon API Gateway는 모든 규모에서 REST, HTTP 및 WebSocket API를 생성, 게시, 유지 관리, 모니터링 및 보호하기 위한 AWS 서비스입니다. API 개발자는 AWS 클라우드에 저장된 데이터뿐만 아니라 AWS 또는 기타 웹 서비스에 액세스하는 API를 생성할 수 있습니다.

API Gateway는 애플리케이션이 Amazon Elastic Compute Cloud(Amazon EC2)에서 실행되는 워크로드, AWS Lambda에서 실행되는 코드, 모든 웹 애플리케이션 또는 실시간 통신 응용 프로그램.

데이터를 Amazon Kinesis Data Stream으로 직접 보내도록 Amazon API Gateway를 구성할 수 있습니다.

Amazon API Gateway는 계정에서 AWS Lambda 함수를 실행하거나, AWS Step Functions 상태 시스템을 시작하거나, AWS Elastic Beanstalk, Amazon EC2에서 호스팅되는 HTTP 엔드포인트를 호출할 수 있으며, 공용 인터넷을 통해 액세스할 수 있는 비 AWS 호스팅 HTTP 기반 작업도 호출할 수 있습니다.API 또한 Gateway를 사용하면 반환할 정적 콘텐츠를 생성하는 매핑 템플릿을 지정할 수 있으므로 백엔드가 준비되기 전에 API를 모의하는 데 도움이 됩니다. API Gateway를 다른 AWS 서비스와 직접 통합할 수도 있습니다. 예를 들어 API Gateway에서 데이터를 Amazon Kinesis로 직접 보내는 API 메서드를 노출할 수 있습니다.

Amazon API Gateway 작동 방식: - https://aws.amazon.com/api-gateway/ 를 통해

잘못된 옵션:

Amazon API Gateway는 RESTful API를 생성하고 Storage Gateway는 WebSocket API를 생성합니다 . Amazon API Gateway는 REST, HTTP 및 WebSocket API를 생성, 게시, 유지 관리, 모니터링 및 보호하기 위한 AWS 서비스입니다. AWS Storage Gateway는 AWS에서 제공하는 하이브리드 스토리지 솔루션입니다.

Amazon API Gateway는 아직 API 결과 캐싱을 지원하지 않습니다. - API Gateway는 결과 캐싱을 지원합니다. API Gateway 캐시를 프로비저닝하고 크기를 기가바이트 단위로 지정하여 API 호출에 캐싱을 추가할 수 있습니다.

API 응답이 캐시된 데이터에 의해 제공되는 경우 청구 목적의 API 호출로 간주되지 않습니다. API 호출은 응답이 백엔드 작업 또는 Amazon API Gateway 캐싱 작업에 의해 처리되는지 여부에 관계없이 청구 목적에 대해 동일하게 계산됩니다.

참조:

https://aws.amazon.com/api-gateway/

https://aws.amazon.com/api-gateway/faqs/

-> API 게이트웨이 다시 보기


-----------------------------------------------
53. 다음 서비스 중 AWS WAF(AWS 웹 애플리케이션 방화벽)를 배포할 수 있습니까?


`Amazon CloudFront, 애플리케이션 로드 밸런서, Amazon API Gateway, AWS AppSync`

AWS 웹 애플리케이션 방화벽(AWS WAF)은 가용성에 영향을 미치거나 보안을 손상시키거나 과도한 리소스를 소비할 수 있는 일반적인 웹 익스플로잇으로부터 웹 애플리케이션 또는 API를 보호하는 데 도움이 되는 웹 애플리케이션 방화벽입니다. AWS WAF는 SQL 삽입 또는 사이트 간 스크립팅과 같은 일반적인 공격 패턴을 차단하는 보안 규칙과 정의한 특정 트래픽 패턴을 필터링하는 규칙을 생성할 수 있도록 하여 트래픽이 애플리케이션에 도달하는 방식을 제어할 수 있습니다.

CDN 솔루션의 일부로 Amazon CloudFront에 AWS WAF, EC2에서 실행되는 웹 서버 또는 오리진 서버 앞에 있는 Application Load Balancer, REST API용 Amazon API Gateway 또는 GraphQL API용 AWS AppSync를 배포할 수 있습니다.

AWS WAF는 Amazon CloudFront, Application Load Balancer, Amazon API Gateway 및 AWS AppSync(AWS 고객이 일반적으로 웹 사이트 및 애플리케이션용 콘텐츠를 제공하는 데 사용하는 서비스)와 긴밀하게 통합됩니다. Amazon CloudFront에서 AWS WAF를 사용하면 최종 사용자와 가까운 전 세계에 위치한 모든 AWS 엣지 로케이션에서 규칙이 실행됩니다. 이것은 보안이 성능을 희생시키지 않는다는 것을 의미합니다. 차단된 요청은 웹 서버에 도달하기 전에 중지됩니다. Application Load Balancer, Amazon API Gateway 및 AWS AppSync와 같은 리전 서비스에서 AWS WAF를 사용하면 규칙이 리전에서 실행되며 인터넷 연결 리소스와 내부 리소스를 보호하는 데 사용할 수 있습니다.

AWS WAF 작동 방식:  - https://aws.amazon.com/waf/ 를 통해

잘못된 옵션:

Amazon CloudFront, Amazon Elastic Compute Cloud(Amazon EC2), Amazon API Gateway, Application Load Balancer

애플리케이션 로드 밸런서, Amazon Elastic Compute Cloud(Amazon EC2), Amazon API Gateway

AWS AppSync, Amazon CloudFront, Application Load Balancer, Amazon Elastic Compute Cloud(Amazon EC2)

AWS WAF는 Amazon `EC2 인스턴스에 직접 배포할 수 없으므로` 이 세 가지 옵션은 올바르지 않습니다. AWS WAF를 배포하려면 `EC2 인스턴스 앞에 Application Load Balancer`를 구성해야 합니다.

참조:

https://aws.amazon.com/waf/

-> 아.... WAF도 봐야할듯


---------------------------------------
54. 역사적으로 IT 부서는 최고 수요에 대비해 과잉 공급해야 했습니다. IT 전문가는 클라우드 인프라를 구축할 때 리소스 과잉 프로비저닝과 불필요한 비용을 초래하는 이러한 레거시 사고방식을 테이블에 가져올 수 있습니다. 클라우드 기능을 최적으로 사용하면서 인프라 비용을 줄이려면 적절한 리소스 크기 조정이 필요합니다.

AWS 클라우드의 어떤 기능이 리소스의 적절한 크기 조정을 의미합니까?



탄력

대부분의 사람들은 클라우드 컴퓨팅을 생각할 때 필요할 때 리소스를 쉽게 조달할 수 있다고 생각합니다. 이것은 탄력성의 한 측면일 뿐입니다. 다른 측면은 더 이상 자원이 필요하지 않을 때 계약하는 것입니다. 스케일 아웃 및 스케일 인. 스케일 업 및 스케일 다운.

필요할 때 리소스를 획득하고 더 이상 필요하지 않을 때 리소스를 해제하는 기능. 클라우드에서는 이 작업을 자동으로 수행하려고 합니다.

일부 AWS 서비스는 Amazon Simple Storage Service(Amazon S3), Amazon Simple Queue Service(Amazon SQS), Amazon Simple Notification Service(Amazon SNS), Amazon Simple Email Service(Amazon SES), Amazon Aurora와 같은 일부 AWS 서비스에서 이 작업을 서비스의 일부로 수행합니다. 등 일부는 Amazon Relational Database Service(Amazon RDS)와 같은 수직 확장이 필요합니다. 기타는 Amazon EC2, Amazon ECS, AWS Fargate, Amazon EKS 및 Amazon DynamoDB와 같은 AWS Auto Scaling과 통합됩니다. Amazon Aurora Serverless 및 Amazon Athena도 탄력적입니다.

잘못된 옵션:

신뢰성 - 예상할 때 의도한 기능을 정확하고 일관되게 수행하는 워크로드의 능력입니다. 여기에는 전체 수명 주기 동안 워크로드를 작동하고 테스트하는 기능이 포함됩니다.

복원력 - 인프라 또는 서비스 중단에서 복구하고, 컴퓨팅 리소스를 동적으로 획득하여 수요를 충족하고, 구성 오류 또는 일시적인 네트워크 문제와 같은 중단을 완화하는 워크로드의 기능입니다.

수평적 확장 - "수평적으로 확장 가능한" 시스템은 시스템에 더 많은 컴퓨터를 추가하여 용량을 늘릴 수 있습니다. 이는 한 대의 컴퓨터에서만 프로세스를 실행하도록 제한되는 "수직 확장 가능" 시스템과 대조됩니다. 이러한 시스템에서 성능을 향상시키는 유일한 방법은 더 빠른(또는 더 많은) CPU, 메모리 또는 스토리지의 형태로 더 많은 리소스를 하나의 컴퓨터에 추가하는 것입니다.

참조:

https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.elasticity.en.html

https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concepts.wa-concepts.en.html

-> 탄력 = (수평,수직확장) , 문제에서는 `어떤 기능이 리소스의 적절한 크기 조정을`이니까 탄력이 맞음


-------------------------------------------------------------
61. AWS Support는 고객을 위해 5가지 지원 계획을 제공합니다. 다음 중 AWS Basic Support 플랜의 일부로 포함되는 기능은 무엇입니까? (2개 선택)



올바른 옵션:

계정 및 청구 질문에 대한 일대일 응답

서비스 상태 확인

AWS Support는 기본 지원 플랜, AWS 개발자 지원 플랜, AWS 비즈니스 지원 플랜, AWS Enterprise-On-Ramp 지원 플랜 및 AWS Enterprise Support 플랜의 5가지 지원 플랜을 제공합니다.

기본 계획은 계정 및 청구 질문과 서비스 할당량 증가에 대한 지원을 제공합니다. 다른 계획은 장기 계약 없이 월 단위로 지불하는 다양한 기술 지원 사례를 제공합니다. 모든 AWS 고객은 자동으로 기본 지원 플랜의 다음 기능에 연중무휴 액세스할 수 있습니다. 1. 계정 및 청구 질문에 대한 일대일 응답 2. 지원 포럼 3. 서비스 상태 확인 4. 문서, 기술 문서 및 모범 사례 가이드

 - https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html 을 통해

잘못된 옵션:

클라이언트측 진단 도구 - Developer, Business, Enterprise-On-Ramp, Enterprise 지원 플랜을 보유한 고객은 클라이언트측 진단 도구에 액세스할 수 있습니다.

사용 사례 지침 – 특정 요구 사항을 가장 잘 지원하기 위해 사용할 AWS 제품, 기능 및 서비스 - Business, Enterprise-On-Ramp, Enterprise 지원 플랜을 보유한 고객은 사용 사례 지침에 액세스할 수 있습니다.

인프라 이벤트 관리 - AWS Enterprise-On-Ramp 또는 Enterprise 지원 플랜을 보유한 고객은 고객 사용 사례를 심층적으로 이해할 수 있도록 AWS Support와 단기적으로 계약하는 인프라 이벤트 관리에 액세스할 수 있습니다. `분석 후 AWS는 이벤트에 대한 아키텍처 및 확장 지침을 제공`합니다.

참조:

https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html

https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html

-> 아... 비지니스로 착각함

------------------------------------------------------------------------




























