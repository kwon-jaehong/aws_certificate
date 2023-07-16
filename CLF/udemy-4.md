4. AWS 공동 책임 모델에 따라 보안 및 규정 준수는 AWS와 고객 간의 공동 책임입니다. 다음 보안 서비스/유틸리티 중 AWS 공유 책임 모델에 따라 AWS의 범위에 속하는 것은 무엇입니까?

설명
올바른 옵션:

AWS 실드 표준

AWS Shield는 AWS에서 실행되는 애플리케이션에 대한 DDoS(Distributed Denial of Service) 공격으로부터 보호하는 관리형 서비스입니다. AWS Shield Standard는 모든 AWS 고객이 추가 비용 없이 사용할 수 있습니다. AWS Shield Standard는 가장 일반적이고 자주 발생하는 DDoS 공격으로부터 AWS에서 실행되는 웹 애플리케이션을 자동으로 보호합니다. AWS에서 DDoS 복원력의 모범 사례를 따르면 AWS Shield Standard의 모든 이점을 얻을 수 있습니다. AWS Shield Standard는 사용자 지정 옵션 없이 모든 AWS 고객에 대해 자동으로 활성화되므로 AWS에서 이 서비스의 유지 관리 및 구성을 관리해야 합니다. 따라서 이 서비스는 AWS의 범위에 속합니다.

잘못된 옵션:

AWS 웹 애플리케이션 방화벽(AWS WAF) - AWS 웹 애플리케이션 방화벽(AWS WAF)은 Amazon API Gateway API, Amazon CloudFront 또는 Application Load Balancer로 전달되는 HTTP 및 HTTPS 요청을 모니터링할 수 있는 웹 애플리케이션 방화벽입니다. AWS 웹 애플리케이션 방화벽(AWS WAF)을 사용하면 콘텐츠에 대한 액세스를 제어할 수도 있습니다.` AWS 웹 애플리케이션 방화벽(AWS WAF)은 고객이 활성화`해야 하며 고객의 책임입니다.

AWS Shield Advanced - 공격에 대한 더 높은 수준의 보호를 위해 AWS Shield Advanced를 구독할 수 있습니다. AWS Shield Advanced 고객은 DDoS 공격 중에 연중무휴 24시간 DDoS 대응 팀(DRT)에 연락하여 지원을 받을 수 있습니다. 또한 AWS 리소스에 대한 공격에 대한 광범위한 가시성을 위해 고급 실시간 지표 및 보고서에 독점적으로 액세스할 수 있습니다. `고객은 AWS Shield Advanced에 가입해야 하며 이 서비스에 대한 비용`을 지불해야 합니다. 이는 AWS 공동 책임 모델에 따라 고객의 책임입니다.

보안 그룹 - 보안 그룹은 Amazon EC2 인스턴스에 대한 가상 방화벽 역할을 하여 들어오고 나가는 트래픽을 제어합니다. 인바운드 규칙은 인스턴스로 들어오는 트래픽을 제어하고 아웃바운드 규칙은 인스턴스에서 나가는 트래픽을 제어합니다. 보안 그룹은 고객의 책임입니다.

참조:

https://aws.amazon.com/compliance/shared-responsibility-model/


-> 몰라서 일부러 틀림, 실드 표준은 무료고, 기본으로 활성화 됐기 때문에 AWS 책임임


-------------------------------

17. IT 회사의 DevOps 팀은 소프트웨어 인벤토리를 수집하고, 명령을 실행하고, 규모에 맞게 서버를 구성 및 패치할 수 있도록 온프레미스 데이터 센터뿐만 아니라 AWS 클라우드에서 서버를 중앙 집중식으로 관리하려고 합니다. 클라우드 실무자로서 이 사용 사례에 대해 어떤 AWS 서비스를 추천하시겠습니까?


설명
올바른 옵션:

AWS 시스템 관리자

AWS Systems Manager는 AWS의 인프라에 대한 가시성과 제어를 제공합니다. Systems Manager는 통합 사용자 인터페이스를 제공하므로 여러 AWS 서비스의 운영 데이터를 볼 수 있으며 소프트웨어 인벤토리 수집, 명령 실행, 패치 관리, AWS 클라우드 및 온프레미스 인프라에서 서버 구성과 같은 운영 작업을 자동화할 수 있습니다.

AWS Systems Manager는 https://aws.amazon.com/systems-manager/faq/ 를 통해 명령 실행, 패치 관리 및 구성 규정 준수를 위한 유틸리티를 제공합니다.

 경유 - https://aws.amazon.com/systems-manager/

잘못된 옵션:

AWS OpsWorks - AWS OpsWorks는 Chef 및 Puppet의 관리형 인스턴스를 제공하는 구성 관리 서비스입니다. AWS OpsWorks를 사용하면 Chef 및 Puppet을 사용하여 Amazon EC2 인스턴스 또는 온프레미스 컴퓨팅 환경에서 서버를 구성, 배포 및 관리하는 방법을 자동화할 수 있습니다.` 소프트웨어 인벤토리를 수집하고 여러 AWS 서비스에서 운영 데이터를 보는 데 AWS OpsWorks를 사용할 수 없습니다.`

AWS CloudFormation - AWS CloudFormation을 사용하면 프로그래밍 언어 또는 간단한 텍스트 파일을 사용하여 자동화되고 안전한 방식으로 모든 리전 및 계정에서 애플리케이션에 필요한 모든 리소스를 모델링하고 프로비저닝할 수 있습니다. 인프라를 코드로 생각하십시오. AWS CloudFormation을 생각하십시오. 서버에서 명령을 실행하거나 패치를 관리하는 데 AWS CloudFormation을 사용할 수 없습니다.

AWS Config - AWS Config는 AWS 리소스의 구성을 평가, 감사 및 평가할 수 있는 서비스입니다. AWS Config는 AWS 리소스 구성을 지속적으로 모니터링하고 기록하며 원하는 구성에 대해 기록된 구성 평가를 자동화할 수 있습니다. 서버에서 명령을 실행하거나 패치를 관리하는 데 AWS Config를 사용할 수 없습니다.

참조:

https://aws.amazon.com/systems-manager/

https://aws.amazon.com/systems-manager/faq/

-> 옵스웍스는 걍 구성 배포, 관리는 할 수 있는데, 소프트웨어 인벤토리를 보는데는 사용할 수 없음

---------------------------------------------------------

20. Bob과 Susan은 각각 AWS Organizations에 AWS 계정을 가지고 있습니다. Susan에게는 동일한 유형의 예약 인스턴스(RI)가 5개 있고 Bob에게는 없습니다. 특정 시간 동안 Susan은 3개의 인스턴스를 사용하고 Bob은 6개를 사용하여 조직의 통합 청구서에서 총 9개의 인스턴스를 사용합니다.

다음 중 AWS Organizations의 통합 결제에 대한 설명으로 옳은 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

Bob은 Susan이 예약 인스턴스를 구입한 동일한 가용 영역(AZ)에서 인스턴스를 시작하는 경우에만 Susan의 예약 인스턴스(RI)에서 비용 이점을 얻습니다.

Bob은 Susan이 예약 인스턴스를 구입한 동일한 가용 영역(AZ)에서 인스턴스를 시작하는 경우에만 Susan의 예약 인스턴스(RI)에서 비용 이점을 받습니다. 예를 들어 Susan이 예약 인스턴스를 구매할 때 us-west-2a를 지정했다면 Bob은 인스턴스를 시작할 때 us-west-2a를 지정해야 조직의 통합 청구서에서 비용 이점을 얻을 수 있습니다. 그러나 AZ(가용 영역)의 실제 위치는 계정 간에 독립적입니다. 예를 들어 Bob 계정의 us-west-2a 가용 영역(AZ)은 Susan 계정의 위치와 다른 위치에 있을 수 있습니다.

AWS는 5개의 인스턴스를 예약 인스턴스로 청구하고 나머지 4개의 인스턴스는 일반 인스턴스로 청구합니다.

Susan에게는 5개의 예약 인스턴스(RI)가 있으므로 AWS는 5개의 인스턴스를 예약 인스턴스로 청구하고 나머지 4개의 인스턴스를 일반 인스턴스로 청구합니다.

잘못된 옵션:

AWS는 3개의 인스턴스를 예약 인스턴스(RI)로 청구하고 나머지 6개의 인스턴스를 일반 인스턴스로 청구합니다. - 이 옵션은 위에 제공된 설명과 모순되므로 올바르지 않습니다.

Bob은 예약 인스턴스(RI)를 구매하지 않았기 때문에 비용 이점을 받지 못합니다. 그의 계정에 하나의 RI가 있는 경우 Susan 계정의 비용-편익도 그의 계정에 추가됩니다 . 결제 목적으로 AWS Organizations의 통합 결제 기능은 조직의 모든 계정을 하나의 계정으로 취급합니다. 이는 조직의 모든 계정이 다른 계정에서 구입한 예약 인스턴스(RI)의 시간당 비용 이점을 받을 수 있음을 의미합니다.

Bob은 Susan이 예약 인스턴스(RI)를 구입한 동일한 AWS 리전에서 인스턴스를 시작한 경우에만 Susan의 예약 인스턴스(RI)로부터 비용-이점을 받습니다. 위에서 논의한 바와 같이 이 설명은 올바르지 않습니다 . Bob은 Susan이 예약 인스턴스(RI)를 구입한 동일한 가용 영역(AZ)에서 자신의 인스턴스를 시작한 경우에만 Susan의 예약 인스턴스로부터 비용 이점을 받습니다.

참조:

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-other.html

-> AWS 오거니 제이션에서.... 아냐 이건 내가 맞는듯 참조 사이트 보면 내말이 맞음



---------------------------------

28. 다음 중 Amazon Relational Database Service(Amazon RDS) 서비스에 대한 설명으로 옳은 것은 무엇입니까?


`향상된 읽기 성능과 재해 복구 모두를 위해 읽기 전용 복제본`을 사용할 수 있습니다.

Amazon Relational Database Service(Amazon RDS)를 사용하면 클라우드에서 관계형 데이터베이스를 쉽게 설정, 운영 및 확장할 수 있습니다. 읽기 복제본을 사용하면 마스터 데이터베이스와 동기화되는 읽기 전용 복사본을 만들 수 있습니다. 읽기 전용 복제본은 향상된 읽기 성능을 위해 사용됩니다. 성능 향상을 위해 읽기 전용 복제본을 사용자와 더 가까운 다른 AWS 리전에 배치할 수도 있습니다. 리전 간 읽기 복제본을 사용하면 재해 발생 시 리전 가용성 문제가 발생하는 경우 백업 및 실행을 보장하는 데 도움이 될 수 있습니다. 읽기 전용 복제본은 리소스의 수평 확장의 예입니다.

읽기 복제본 개요:  - https://aws.amazon.com/rds/features/multi-az/ 를 통해

Amazon RDS 다중 AZ 배포는 RDS 데이터베이스(DB) 인스턴스에 향상된 가용성과 내구성을 제공하므로 프로덕션 데이터베이스 워크로드에 적합합니다. Amazon RDS 다중 AZ DB 인스턴스를 프로비저닝하면 Amazon RDS가 기본 DB 인스턴스를 자동으로 생성하고 데이터를 다른 가용 영역(AZ)의 대기 인스턴스에 동기식으로 복제합니다. Amazon RDS는 장애 조치가 완료되는 즉시 데이터베이스 작업을 재개할 수 있도록 대기로 자동 장애 조치를 수행합니다. DB 인스턴스의 엔드포인트는 장애 조치 후에도 동일하게 유지되므로 애플리케이션은 수동 관리 개입 없이 데이터베이스 작업을 재개할 수 있습니다. 다중 AZ 배포를 시스템의 가용성과 안정성을 향상시키는 것으로 생각하십시오.

다중 AZ 배포 작동 방식: https://aws.amazon.com/rds/features/multi-az/ 를 통해

Amazon Relational Database Service(Amazon RDS) 재해 복구 기능을 더 자세히 이해하려면 다음 AWS 블로그를 참조하십시오. https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy -with-amazon-rds/

잘못된 옵션:

향상된 읽기 성능을 위해 읽기 복제본을 사용하고 재해 복구를 위해 다중 AZ 배포를 사용할 수 있습니다.

향상된 읽기 성능을 위해 읽기 전용 복제본과 다중 AZ 배포를 모두 사용할 수 있습니다.

향상된 읽기 성능을 위해 재해 복구 및 다중 AZ 배포에 읽기 전용 복제본을 사용할 수 있습니다.

이 세 가지 옵션은 설명의 앞부분에서 제공된 세부 정보와 상충되므로 이러한 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/

https://aws.amazon.com/rds/features/multi-az/


-> 음... 이건 말장난임
-> 복구와 읽기 향상은 둘다 다됨, 성능향상이 읽기복제본은 제외라서그렇지

--------------------------------------------------------------------
31. 화물 운송 회사는 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스에서 서버 플릿을 실행합니다. 이러한 인스턴스 중 일부는 연중무휴로 액세스할 수 있어야 하는 CRM(Customer Relationship Management) 애플리케이션을 호스팅합니다. 이러한 응용 프로그램은 미션 크리티컬하지 않습니다. 재해가 발생하는 경우 이러한 애플리케이션은 얼마 동안 더 적은 수의 인스턴스에서 관리할 수 있습니다.

이 요구 사항에 적합하고 비용 효율적인 재해 복구 전략은 무엇입니까?

설명
올바른 옵션:

웜 스탠바이 전략

DR(재해 복구) 전략을 선택할 때 낮은 RTO(복구 시간 목표) 및 RPO(복구 지점 목표)의 이점과 전략 구현 및 운영 비용을 비교해야 합니다. 파일럿 라이트 및 웜 대기 전략은 모두 이점과 비용의 적절한 균형을 제공합니다.

이 전략은 기본 리전의 데이터를 Amazon Relational Database Service(Amazon RDS) DB 인스턴스 또는 Amazon DynamoDB 테이블과 같은 복구 리전의 데이터 리소스로 복제합니다. 이러한 데이터 리소스는 요청을 처리할 준비가 되었습니다. 복제 외에도 이 전략에서는 복구 지역에 연속 백업을 생성해야 합니다. 이는 "인간 행동" 유형의 재해가 발생하면 데이터가 삭제되거나 손상될 수 있으며 복제가 잘못된 데이터를 복제하기 때문입니다. 마지막으로 알려진 정상 상태로 돌아가려면 백업이 필요합니다.

웜 대기 전략은 기능적 스택을 배포하지만 용량은 줄어듭니다. DR 엔드포인트는 요청을 처리할 수 있지만 프로덕션 수준의 트래픽은 처리할 수 없습니다. 더 많을 수도 있지만 비용 절감을 위해 항상 전체 생산 배포보다 적습니다. 그러나 수동 스택이 전체 용량으로 복구 지역에 배포되는 경우 이 전략을 "상시 대기"라고 합니다. 웜 대기는 기능 스택을 복구 지역에 배포하기 때문에 가상 트랜잭션을 사용하여 지역 준비 상태를 더 쉽게 테스트할 수 있습니다.

재해 복구(DR) 전략: https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/ 를 통해

잘못된 옵션:

다중 사이트 활성-활성 전략 - 이 전략은 AWS 리전을 활성 사이트로 사용하여 다중 리전 활성/활성 아키텍처를 생성합니다. 일반적으로 두 개의 리전이 사용됩니다. 각 리전은 가용성이 높은 다중 가용 영역(AZ) 워크로드 스택을 호스팅합니다. 각 리전에서 데이터는 데이터 저장소 간에 실시간으로 복제되고 백업됩니다. 이것은 데이터 백업이 마지막으로 알려진 양호한 상태로 복원될 수 있기 때문에 데이터 삭제 또는 손상을 포함하는 재해로부터 보호합니다. 각 지역 스택은 프로덕션 트래픽을 효과적으로 처리합니다. 그러나 이 전략은 비용이 많이 들고 `미션 크리티컬 애플리케이션`에만 사용해야 합니다.

파일럿 라이트 전략 - 파일럿 라이트는 웜 대기 전략과 마찬가지로 기본 리전의 데이터를 Amazon Relational Database Service(Amazon RDS) DB 인스턴스 또는 Amazon DynamoDB 테이블과 같은 복구 리전의 데이터 리소스로 복제합니다. 그러나 파일럿 라이트 전략(웜 대기와 달리)의 DR 지역은 추가 단계를 수행할 때까지 요청을 처리할 수 없습니다. 가정용 화로의 표시등은 가정에 열을 공급하지 않습니다. 그것은 열을 제공하는 용광로 버너에 불을 붙이는 빠른 방법을 제공합니다.

웜 스탠바이는 감소된 수준의 트래픽을 즉시 처리할 수 있습니다. 파일럿 라이트에서는 워크로드가 요청을 처리하기 전에 먼저 인프라를 배포한 다음 리소스를 확장해야 합니다.

백업 및 복원 전략 - 백업 및 복원은 더 높은 RTO(복구 시간 목표) 및 RPO(복구 지점 목표)와 관련이 있습니다. 이로 인해 재해 이벤트가 발생한 시점과 복구 시점 사이에 중단 시간이 길어지고 데이터 손실이 커집니다. 그러나 백업 및 복원은 구현하기 가장 쉽고 비용이 적게 드는 전략이기 때문에 여전히 워크로드에 적합한 전략일 수 있습니다.

참조:

https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/

-> 이거는.. CLF문제 아닌듯....

-> 백업 및 복원 -> 파일럿라이트 -> 웜 스탠바이 -> 사이트투사이트
-> 1시간 -> 10분 -> 1분 -> 리얼타임 복구



-----------------------------

37. 다음 중 `브라우저 기반 클라이언트`를 통해 Mac OS, Windows 또는 Linux 기반 컴퓨터에서 Amazon Elastic Compute Cloud(Amazon EC2) 서버에 연결하는 데 사용할 수 있는 엔터티는 무엇입니까?

Amazon EC2 인스턴스 연결

Amazon EC2 Instance Connect는 SSH(Secure Shell)를 사용하여 인스턴스에 간단하고 안전하게 연결할 수 있는 방법을 제공합니다. Amazon EC2 Instance Connect에서는 AWS Identity and Access Management(AWS IAM) 정책 및 보안 주체를 사용하여 인스턴스에 대한 SSH 액세스를 제어하므로 SSH 키를 공유하고 관리할 필요가 없습니다. Amazon EC2 Instance Connect를 사용하는 모든 연결 요청은 연결 요청을 감사할 수 있도록 AWS CloudTrail에 기록됩니다.

Amazon EC2 Instance Connect를 사용하여 브라우저 기반 클라이언트, Amazon EC2 Instance Connect CLI 또는 선택한 SSH 클라이언트를 통해 Linux 인스턴스에 연결할 수 있습니다. Amazon EC2 Instance Connect를 사용하여 Mac OS, Windows 또는 Linux 기반 컴퓨터에서 EC2 인스턴스에 연결할 수 있습니다.

잘못된 옵션:

SSH - SSH는 Mac OS, Windows 또는 Linux 기반 컴퓨터에서 사용할 수 있지만 `브라우저 기반 클라이언트`는 아닙니다.

Putty - Putty는 Windows 기반 컴퓨터에서만 사용할 수 있습니다.

AWS Direct Connect - AWS Direct Connect는 온프레미스에서 AWS로 전용 네트워크 연결을 쉽게 설정할 수 있는 클라우드 서비스 솔루션입니다. AWS Direct Connect를 사용하여 온프레미스 네트워크에서 Amazon VPC로 직접 프라이빗 가상 인터페이스를 설정할 수 있습니다. 이 비공개 연결은 완료하는 데 최소 한 달이 걸립니다. AWS Direct Connect는 Mac OS, Windows 또는 Linux 기반 컴퓨터에서 Amazon EC2 인스턴스에 연결하는 데 사용할 수 없습니다.

참조:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html

-> ?? 문제를 못읽음.....

--------------------

44. 다음 중 AWS Global Accelerator에 대한 올바른 설명은 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS Global Accelerator는 글로벌 사용자에게 제공하는 애플리케이션의 가용성과 성능을 개선하는 데 도움이 되는 네트워킹 서비스입니다. Global Accelerator는 하나 이상의 AWS 리전에서 실행되는 애플리케이션에 대해 에지의 패킷을 프록시하여 TCP 또는 UDP를 통해 광범위한 애플리케이션의 성능을 개선합니다.

AWS Global Accelerator 작동 방식: https://aws.amazon.com/global-accelerator/ 를 통해

AWS Global Accelerator는 비 HTTP 사용 사례에 적합합니다.

AWS Global Accelerator는 게임(UDP), IoT(MQTT) 또는 VoIP와 같은 비HTTP 사용 사례와 특히 정적 IP 주소 또는 결정적이며 빠른 지역 장애 조치가 필요한 HTTP 사용 사례에 적합합니다. .

AWS Global Accelerator는 애플리케이션에 대한 고정 진입점 역할을 하는 정적 IP 주소를 제공합니다.

애플리케이션에 대한 고정 진입점을 제공하고 다양한 AWS 리전 및 가용 영역(AZ)에 대한 특정 IP 주소를 관리하는 복잡성을 제거하는 정적 IP 주소를 제공합니다.

잘못된 옵션:

AWS Global Accelerator는 AWS 글로벌 네트워크와 엣지 로케이션을 사용합니다. 그러나 Global Accelerator에서 사용하는 엣지 로케이션은 Amazon CloudFront 엣지 로케이션과 다릅니다 . AWS Global Accelerator와 Amazon CloudFront는 동일한 엣지 로케이션을 사용합니다.

AWS Global Accelerator는 ELB(Elastic Load Balancer)로 구성할 수 없습니다 . `리전 ELB 로드 밸런서는 AWS Global Accelerator의 이상적인 대상`입니다. AWS Global Accelerator는 이러한 기능을 단일 AWS 리전 이상으로 확장하여 ELB를 보완하므로 여러 리전에서 애플리케이션에 글로벌 인터페이스를 제공할 수 있습니다.

AWS Global Accelerator는 정적 웹사이트를 호스팅하는 데 사용할 수 있습니다 . Amazon S3는 정적 웹사이트를 호스팅할 수 있습니다. 따라서 이 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/global-accelerator/

-> 글로벌 악세레이터 이해 부족


---------------------------------------------


51. 다음 중 Amazon Simple Storage Service(Amazon S3)(2개 선택)에 대한 설명으로 옳은 것은 무엇입니까?


설명
올바른 옵션:

Amazon Simple Storage Service(Amazon S3)는 키 값 기반 객체 스토리지 서비스입니다.

Amazon Simple Storage Service(Amazon S3)는 평평한 비계층 구조에 데이터를 저장합니다.

Amazon Simple Storage Service(Amazon S3)는 업계 최고의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스입니다. Amazon Simple Storage Service(Amazon S3)는 플랫한 비계층 구조에 데이터를 저장합니다. 모든 객체는 Amazon S3 버킷에 저장되며 접두사라는 공유 이름으로 구성할 수 있습니다. 또한 각 객체에 Amazon S3 객체 태그라고 하는 최대 10개의 키-값 페어를 추가할 수 있습니다. 이 페어는 객체의 수명 주기 전체에서 생성, 업데이트 및 삭제할 수 있습니다.

잘못된 옵션:

Amazon Simple Storage Service(Amazon S3)는 광범위한 워크로드를 위해 설계된 블록 스토리지 서비스입니다. 블록 스토리지 서비스는 Amazon Elastic Block Store(Amazon EBS)에서 제공하여 Amazon EC2 인스턴스와 함께 사용할 영구 블록 수준 스토리지 볼륨을 제공합니다. Amazon S3는 객체 스토리지 서비스입니다.

Amazon Simple Storage Service(Amazon S3)는 데이터베이스 백업으로 사용되는 완전 관리형 `탄력적 파일 시스템 스토리지` 서비스입니다. Amazon Elastic File System(Amazon EFS)은 AWS 클라우드 서비스 및 온프레미스 리소스. Amazon S3는 객체 스토리지 서비스입니다.

Amazon Simple Storage Service(Amazon S3)에 데이터베이스를 설치할 수 있습니다 . Amazon S3는 객체 스토리지 서비스입니다. Amazon S3에는 데이터베이스를 설치할 수 없습니다.

참조:

https://aws.amazon.com/s3/features/


-> 아... 탄력적... 문제 좀 잘 읽어 보자


--------------------------------------

63. Amazon Virtual Private Cloud(Amazon VPC)를 Amazon Simple Queue Service(Amazon SQS) 대기열에 비공개로 연결할 수 있는 AWS 엔터티는 무엇입니까?

설명
올바른 옵션:

VPC 인터페이스 엔드포인트

인터페이스 엔드포인트는 지원되는 서비스로 향하는 트래픽의 진입점 역할을 하는 서브넷의 IP 주소 범위에 있는 사설 IP 주소가 있는 탄력적 네트워크 인터페이스(ENI)입니다. 인터페이스 엔드포인트는 프라이빗 IP 주소를 사용하여 비공개로 서비스에 액세스할 수 있는 기술인 AWS PrivateLink로 구동됩니다. AWS PrivateLink는 VPC와 서비스 간의 모든 네트워크 트래픽을 Amazon 네트워크로 제한합니다. 인터넷 게이트웨이, NAT(Network Address Translation) 장치 또는 가상 프라이빗 게이트웨이가 필요하지 않습니다.

시험 알림:

시험에서 이 개념에 대한 질문을 볼 수 있습니다. Amazon S3 및 Amazon DynamoDB만 VPC 게이트웨이 엔드포인트를 지원한다는 점을 기억하십시오. VPC 엔드포인트를 지원하는 다른 모든 서비스는 VPC 인터페이스 엔드포인트를 사용합니다(Amazon S3도 VPC 인터페이스 엔드포인트를 지원함).

잘못된 옵션:

VPC 게이트웨이 엔드포인트 - 게이트웨이 엔드포인트는 지원되는 AWS 서비스로 향하는 트래픽에 대한 라우팅 테이블의 경로에 대한 대상으로 지정하는 게이트웨이입니다. 지원되는 AWS 서비스는 Amazon S3, DynamoDB입니다. VPC 게이트웨이 엔드포인트를 사용하여 VPC를 Amazon SQS 대기열에 비공개로 연결할 수 없습니다.

AWS Direct Connect - AWS Direct Connect는 온프레미스에서 AWS로 전용 네트워크 연결을 쉽게 설정할 수 있는 클라우드 서비스 솔루션입니다. AWS Direct Connect를 사용하여 온프레미스 네트워크에서 Amazon VPC로 직접 프라이빗 가상 인터페이스를 설정할 수 있습니다. 이 비공개 연결은 완료하는 데 최소 한 달이 걸립니다. AWS Direct Connect를 사용하여 VPC를 Amazon SQS 대기열에 비공개로 연결할 수 없습니다.

인터넷 게이트웨이 - 인터넷 게이트웨이는 VPC와 인터넷 간의 통신을 허용하는 수평 확장, 중복 및 고가용성 VPC 구성 요소입니다. 인터넷 게이트웨이는 두 가지 용도로 사용됩니다. 즉, 인터넷 라우팅 가능 트래픽에 대해 VPC 라우팅 테이블에 대상을 제공하고 퍼블릭 IPv4 주소가 할당된 인스턴스에 대해 네트워크 주소 변환(NAT)을 수행하는 것입니다. 인터넷 게이트웨이를 사용하여 VPC를 Amazon SQS 대기열에 비공개로 연결할 수 없습니다.

참조:

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html


-> 아!!!!!!!!! 인터페이스, 게이트웨이 엔드포인트 차이점 !!!!!


--------------------------------








