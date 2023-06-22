1. AWS 버짓(3개 선택)에서 생성할 수 있는 예산 유형은 무엇입니까?

설명
올바른 옵션:

AWS 예산을 사용하면 서비스 사용량, 서비스 비용 및 인스턴스 예약을 계획할 수 있습니다. AWS 예산 정보는 하루에 최대 3번 업데이트됩니다. 업데이트는 일반적으로 이전 업데이트 후 8~12시간 사이에 발생합니다. 예산은 일반 비용, 구독, 환불 및 RI를 추적합니다. AWS 예산에서 생성할 수 있는 예산 유형에는 비용 예산, 사용 예산, 예약 예산 및 저축 계획 예산의 네 가지가 있습니다.

비용 예산 - 서비스에 지출할 금액을 계획하는 데 도움이 됩니다.

사용 예산 - 하나 이상의 서비스를 얼마나 사용할 것인지 계획하는 데 도움이 됩니다.

예약 예산 - 예약 인스턴스(RI)의 사용량을 추적하는 데 도움이 됩니다. 이를 수행하는 두 가지 방법 - 예약 인스턴스(RI) 사용 예산(예약 인스턴스(RI)이 사용되지 않았는지 또는 충분히 활용되지 않았는지 확인할 수 있음), 예약 인스턴스(RI) 적용 예산(인스턴스 사용량을 확인할 수 있음) 사용량은 예약에 포함됩니다).

잘못된 옵션:

리소스 예산 - 구성 옵션이며 선택 항목으로 추가되었습니다.

소프트웨어 예산 - 구성 옵션이며 선택 항목으로 추가되었습니다.

하드웨어 예산 - 구성 옵션이며 선택 항목으로 추가되었습니다.

참조:

이것은 구성 옵션이며 선택 항목으로 추가되었습니다.

-> 이건 몰랏음.... 


----------------------------------------
3. 읽기 전용 복제본 구성에서 Amazon Relational Database Service(Amazon RDS) 데이터베이스를 배포할 때의 주요 이점은 무엇입니까?


설명
올바른 옵션:

읽기 전용 복제본으로 데이터베이스 확장성 향상

Amazon Relational Database Service(Amazon RDS)를 사용하면 클라우드에서 관계형 데이터베이스를 쉽게 설정, 운영 및 확장할 수 있습니다. 읽기 전용 복제본을 사용하면 마스터 데이터베이스와 동기화되는 읽기 전용 복사본을 만들 수 있습니다. 읽기 전용 복제본은 향상된 읽기 성능을 위해 사용됩니다. 성능 향상을 위해 읽기 전용 복제본을 사용자와 더 가까운 다른 AWS 리전에 배치할 수도 있습니다. 읽기 전용 복제본은 리소스의 수평 확장의 예입니다.

읽기 복제본 개요: https://aws.amazon.com/rds/features/multi-az/ 를 통해

시험 알림:

https://aws.amazon.com/rds/features/multi-az/ 를 통해 Amazon RDS 다중 AZ, 다중 리전 및 RDS용 읽기 전용 복제본 배포 간의 차이점을 검토하십시오.

잘못된 옵션:

읽기 전용 복제본으로 데이터베이스 가용성 향상 - Amazon RDS 다중 AZ 배포는 RDS 데이터베이스(DB) 인스턴스에 향상된 가용성과 내구성을 제공하므로 프로덕션 데이터베이스 워크로드에 적합합니다. 다중 AZ DB 인스턴스를 프로비저닝하면 Amazon RDS가 기본 DB 인스턴스를 자동으로 생성하고 데이터를 다른 가용 영역(AZ)의 대기 인스턴스에 동기식으로 복제합니다. 읽기 전용 복제본은 데이터베이스 가용성을 향상시킬 수 없습니다.

읽기 전용 복제본은 지역 장애로부터 데이터베이스를 보호합니다 . 지역 장애로부터 보호하려면 다중 지역 배포 구성에서 RDS를 사용해야 합니다. 읽기 전용 복제본은 지역 장애로부터 보호할 수 없습니다.

읽기 전용 복제본으로 데이터베이스 사용 비용 절감 - 읽기 전용 복제본이 포함된 Amazon Relational Database Service(Amazon RDS)는 표준 배포에 비해 데이터베이스 비용을 증가시킵니다. 따라서 이 옵션은 올바르지 않습니다.

참조:

-> 아... 읽기 복제본은 확장성 확장이고, 멀티 복제가 가용성 확장이다!


-------------------------------------------------------------------

7 조직은 부서별로 별도의 Amazon Virtual Private Cloud(Amazon VPC)를 유지 관리합니다. 비즈니스가 확장됨에 따라 이제 조직은 더 나은 부서 협업을 위해 모든 Amazon Virtual Private Cloud(Amazon VPC)를 연결하려고 합니다. 조직이 문제를 효과적으로 해결하는 데 도움이 되는 AWS 서비스는 무엇입니까?


설명
올바른 옵션:

AWS 전송 게이트웨이

AWS Transit Gateway는 중앙 허브를 통해 Amazon Virtual Private Cloud(Amazon VPC)와 온프레미스 네트워크를 연결합니다. 이것은 네트워크를 단순화하고 복잡한 피어링 관계를 종식시킵니다. 클라우드 라우터 역할을 합니다. 새로운 각 연결은 한 번만 이루어집니다. 전 세계로 확장함에 따라 리전 간 피어링은 AWS 글로벌 네트워크를 사용하여 AWS Transit Gateway를 연결합니다. 귀하의 데이터는 자동으로 암호화되며 공용 인터넷을 통해 이동하지 않습니다.

AWS Transit Gateway가 네트워크를 단순화하는 방법: https://aws.amazon.com/transit-gateway/ 를 통해

잘못된 옵션:

VPC 피어링 연결 - VPC 피어링 연결은 두 Amazon Virtual Private Cloud(Amazon VPC) 간에 비공개로 트래픽을 라우팅할 수 있는 네트워킹 연결입니다. VPC 피어링 연결은 전이적이지 않으므로 서로 통신해야 하는 두 VPC 간에 별도의 VPC 피어링 연결을 만들어야 합니다. VPC가 증가하면 관리하기가 어려워집니다.

전환 VPC 피어링 연결은 다음을 통해 허용되지 않습니다.  - https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html

AWS Direct Connect - AWS Direct Connect는 원격 네트워크에서 VPC로의 전용 프라이빗 연결을 생성합니다. 이것은 개인 연결이며 공용 인터넷을 사용하지 않습니다. 이 연결을 설정하는 데 최소 한 달이 걸립니다. AWS Direct Connect는 VPC를 상호 연결하는 데 사용할 수 없습니다.

AWS Site-to-Site VPN - AWS Site-to-Site VPN은 데이터 센터 또는 지사와 AWS 클라우드 리소스 간에 보안 연결을 생성합니다. 이 연결은 공용 인터넷을 통해 이루어집니다. AWS Site-to-Site VPN은 VPC를 상호 연결하는 데 사용할 수 없습니다.

참조:

https://aws.amazon.com/transit-gateway/


-> 문제... 똑바로 안읽음


-----------------------------

8. 다음 중 AWS Billing의 비용 할당 태그에 대한 설명으로 옳은 것은 무엇입니까? (2개 선택)

설명
올바른 옵션:

각 리소스에 대해 각 태그 키는 고유해야 하며 각 태그 키는 하나의 값만 가질 수 있습니다.

비용 탐색기 또는 비용 할당 보고서에 표시되려면 AWS 생성 태그와 사용자 정의 태그를 별도로 활성화해야 합니다.

비용 할당 태그는 귀하 또는 AWS가 AWS 리소스에 할당하는 레이블입니다. 각 태그는 키와 값으로 구성됩니다. 각 리소스에 대해 각 태그 키는 고유해야 하며 각 태그 키는 하나의 값만 가질 수 있습니다. 태그를 사용하여 리소스를 구성하고 비용 할당 태그를 사용하여 자세한 수준에서 AWS 비용을 추적할 수 있습니다.

AWS는 두 가지 유형의 비용 할당 태그인 AWS 생성 태그와 사용자 정의 태그를 제공합니다. AWS는 귀하를 위해 AWS 생성 태그를 정의, 생성 및 적용하고 귀하는 사용자 정의 태그를 정의, 생성 및 적용합니다. 비용 탐색기 또는 비용 할당 보고서에 표시되려면 두 유형의 태그를 개별적으로 활성화해야 합니다.

AWS 비용 할당 태그 개요: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html 을 통해

잘못된 옵션:

태그는 리소스를 구성하는 데 도움이 되며 보고서를 실행하기 위한 필수 구성 항목입니다. - 태그는 조직의 요구 사항에 따라 리소스를 구성하는 데 확실히 도움이 됩니다. `하지만 필수는 아닙니다.`

각 리소스에 대해 각 태그 키는 고유해야 하지만 여러 값을 가질 수 있음 - 각 리소스에 대해 각 태그 키는 고유해야 하며 각 태그 키는 하나의 값만 가질 수 있습니다.

비용 탐색기 또는 비용 할당 보고서에 표시되려면 `사용자 정의 태그만` 활성화해야 합니다. `위에서 설명한 대로 두 종류의 태그(사용자 정의 및 AWS 생성)는 보고서에 표시되기 전에 별도로 활성화해야 합니다.` 세대.

참조:

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html




-> 비용 할당 태그에 관해 좀더 자료 조사

-------------------------------------------------------
10. AWS Trusted Advisor는 AWS 환경을 분석하고 다음 범주 중 모범 사례 권장 사항을 제공합니다. (2개 선택)

설명
올바른 옵션:

비용 최적화

서비스 제한

AWS Trusted Advisor는 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공하는 온라인 도구입니다. 새로운 워크플로를 설정하든, 애플리케이션을 개발하든, 아니면 지속적인 개선의 일환으로 Trusted Advisor가 정기적으로 제공하는 권장 사항은 솔루션을 최적으로 프로비저닝하는 데 도움이 됩니다. AWS Trusted Advisor는 AWS 환경을 분석하고 비용 최적화, 성능, 보안, 내결함성, 서비스 제한의 5가지 범주에서 모범 사례 권장 사항을 제공합니다.

Trusted Advisor의 작동 방식:  - https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ 를 통해

AWS Trusted Advisor 권장 사항:  - https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ 를 통해

잘못된 옵션:

탄력

선적 서류 비치

변경 관리

이 세 가지 옵션은 구성되어 있으며 AWS Trusted Advisor의 맥락에서 중요하지 않습니다.

참조:

https://aws.amazon.com/premiumsupport/technology/trusted-advisor/


-> Trusted Advisor 5가지 다시 외우기

---------------------------------------------------------

12. 다음 중 Amazon Rekognition이 바로 사용할 수 있는 기능으로 제공하는 기능은 무엇입니까? 
설명
올바른 옵션:

사진에서 개체 식별

Amazon Rekognition을 사용하면 이미지와 동영상에서 객체, 사람, 텍스트, 장면, 활동을 식별하고 부적절한 콘텐츠를 감지할 수 있습니다. Amazon Rekognition은 또한 매우 정확한 얼굴 분석 및 얼굴 검색 기능을 제공하여 다양한 사용자 확인, 사람 수 계산 및 공공 안전 사용 사례에서 얼굴을 감지, 분석 및 비교하는 데 사용할 수 있습니다.

Amazon Rekognition 사용 사례:

 - https://aws.amazon.com/rekognition/ 을 통해

 - https://aws.amazon.com/rekognition/ 을 통해

잘못된 옵션:

이미지를 그레이스케일로 변환

빠르게 이미지 크기 조정

`인간 포즈 감지` <- 안됨

Amazon Rekognition은 이미지를 회색조로 변환하거나 이미지 크기 조정과 같은 이미지 처리 작업을 수행하지 않습니다. 사람의 자세 감지는 Amazon Rekognition에서 사용할 수 없습니다.

참조:

-> 문제 잘못 해석

-----------------------------------------------------------
13. 다음 중 AWS 공동 책임 모델에 대한 올바른 설명은 무엇입니까? (2개 선택)

설명
올바른 옵션:

보안 및 규정 준수는 AWS와 고객의 공동 책임입니다. 이 공유 모델은 AWS가 호스트 운영 체제 및 가상화 계층에서 서비스가 운영되는 시설의 물리적 보안에 이르기까지 구성 요소를 운영, 관리 및 제어하므로 고객의 운영 부담을 줄이는 데 도움이 될 수 있습니다.

AWS는 클라우드 '의' 보안을 담당합니다.

AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다. 이 인프라는 AWS 클라우드 서비스를 실행하는 하드웨어, 소프트웨어, 네트워킹 및 시설로 구성됩니다.

Amazon S3와 같은 추상화된 서비스의 경우 AWS가 인프라 계층, 운영 체제 및 플랫폼을 운영합니다.

Amazon S3 및 Amazon DynamoDB와 같은 추상화된 서비스의 경우 AWS가 인프라 계층, 운영 체제 및 플랫폼을 운영하고 고객은 엔드포인트에 액세스하여 데이터를 저장하고 검색합니다.

AWS 공동 책임 모델 개요: https://aws.amazon.com/compliance/shared-responsibility-model/ 을 통해

잘못된 옵션:

Amazon EC2와 같이 Infrastructure as a Service에 해당하는 서비스의 경우 AWS에서 게스트 운영 체제 유지 관리를 담당합니다. - Amazon Elastic Compute Cloud(Amazon EC2)와 같은 서비스는 IaaS(Infrastructure as a Service)로 분류되며 이와 같이 , 고객은 필요한 모든 보안 구성 및 관리 작업을 수행해야 합니다. 고객은 게스트 운영 체제(업데이트 및 보안 패치 포함), 고객이 인스턴스에 설치한 모든 애플리케이션 소프트웨어 또는 유틸리티, 각 인스턴스에서 AWS 제공 방화벽(보안 그룹이라고 함)의 구성을 관리할 책임이 있습니다. .

구성 관리는 고객의 책임입니다 . 구성 관리는 공동 책임입니다. AWS는 인프라 장치의 구성을 유지하지만 고객은 자신의 게스트 운영 체제, 데이터베이스 및 애플리케이션을 구성할 책임이 있습니다.

AWS는 AWS 제품 및 서비스에 대해 AWS 및 고객 직원을 교육할 책임이 있습니다 . `인식 및 교육도 공동 책임입니다`. AWS는 AWS 직원을 교육하지만 고객은 자신의 직원을 교육해야 합니다.

참조:

https://aws.amazon.com/compliance/shared-responsibility-model/

-> 이걸왜 틀렷을까....


-----------------------------------------------------

17. 한 IT 회사는 비용 최적화에 열중하고 있으며 활용도가 낮은 모든 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스를 식별하려고 합니다. `수동 구성 없이` 이 사용 사례를 해결하기 위해 기성품으로 사용할 수 있는 AWS 서비스는 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS 신뢰할 수 있는 조언자

AWS Trusted Advisor는 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공하는 온라인 도구입니다. 새로운 워크플로 설정, 애플리케이션 개발 또는 지속적인 개선의 일환으로 Trusted Advisor에서 제공하는 권장 사항은 솔루션을 최적으로 프로비저닝하는 데 정기적으로 도움이 됩니다. AWS Trusted Advisor는 AWS 환경을 분석하고 비용 최적화, 성능, 보안, 내결함성, 서비스 제한의 5가지 범주에서 모범 사례 권장 사항을 제공합니다.

AWS Trusted Advisor는 지난 14일 동안 언제든지 실행 중이던 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스를 확인하고 일일 CPU 사용률이 10% 이하이고 네트워크 I/O가 5MB 이하인 경우 경고합니다. 또는 더 많은 일.

AWS Trusted Advisor 작동 방식:  - https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ 를 통해

AWS Trusted Advisor가 사용률이 낮은 Amazon EC2 인스턴스를 식별하는 방법: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/#Cost_Optimization 을 통해

AWS 비용 탐색기

AWS Cost Explorer에는 시간 경과에 따른 AWS 비용 및 사용량을 시각화, 이해 및 관리할 수 있는 사용하기 쉬운 인터페이스가 있습니다. AWS Cost Explorer에는 비용 발생 상위 5개 AWS 서비스와 관련된 비용 및 사용량을 시각화하는 데 도움이 되는 기본 보고서가 포함되어 있으며 테이블 보기에서 모든 서비스에 대한 자세한 분석을 제공합니다. 보고서를 사용하면 시간 범위를 조정하여 최대 12개월까지의 기록 데이터를 보고 비용 추세를 이해할 수 있습니다.

AWS Cost Explorer의 크기 조정 권장 사항 기능은 Amazon EC2 인스턴스를 축소하거나 종료하여 비용 절감 기회를 식별하는 데 도움이 됩니다. 사용률이 낮은 모든 Amazon EC2 인스턴스를 멤버 계정 전체에서 단일 보기로 확인하여 얼마나 절약할 수 있는지 즉시 확인할 수 있습니다.

잘못된 옵션:

AWS 비용 및 사용 보고서(AWS CUR) - AWS 비용 및 사용 보고서(AWS CUR)에는 사용 가능한 가장 포괄적인 비용 및 사용 데이터 세트가 포함되어 있습니다. AWS 비용 및 사용 보고서(AWS CUR)를 사용하여 소유하고 있는 Amazon Simple Storage Service(Amazon S3) 버킷에 AWS 결제 보고서를 게시할 수 있습니다. 시간 또는 월, 제품 또는 제품 리소스 또는 직접 정의한 태그별로 비용을 분석한 보고서를 받을 수 있습니다. AWS 비용 및 사용 보고서(AWS CUR)는 활용도가 낮은 Amazon EC2 인스턴스를 식별하는 데 사용할 수 없습니다.

Amazon CloudWatch - Amazon CloudWatch를 사용하여 예상 요금을 모니터링하는 경보를 생성할 수 있습니다. AWS 계정에 대한 예상 요금 모니터링을 활성화하면 예상 요금이 계산되어 지표 데이터로 CloudWatch에 매일 여러 번 전송됩니다. 요금이 특정 임계값을 초과하면 이메일로 알림을 받도록 선택할 수 있습니다. 리소스 성능 모니터링, 이벤트 및 경고를 생각하십시오. CloudWatch를 생각하십시오. Amazon CloudWatch는 Amazon EC2 사용률을 추적하기 위해 적절한 임계값으로 경보를 `수동으로 구성하지 않고` 사용률이 낮은 Amazon EC2 인스턴스를 식별하는 데 사용할 수 없으므로 이 옵션은 올바르지 않습니다.

AWS Budgets - AWS Budgets는 비용 또는 사용량이 예산 금액을 초과(또는 초과할 것으로 예상)될 때 알려주는 사용자 지정 예산을 설정할 수 있는 기능을 제공합니다. 또한 AWS 예산을 사용하여 예약 사용률 또는 적용 범위 목표를 설정하고 사용률이 정의한 임계값 아래로 떨어지면 알림을 받을 수 있습니다. AWS 예산은 월별, 분기별 또는 연간 수준에서 생성할 수 있으며 시작 날짜와 종료 날짜를 사용자 지정할 수 있습니다. 예산을 더 세분화하여 AWS 서비스, 연결된 계정, 태그 등과 같은 여러 차원과 관련된 비용을 추적할 수 있습니다. 적용 범위 대상을 수동으로 구성하지 않고는 활용률이 낮은 EC2 인스턴스를 식별하는 데 AWS 예산을 사용할 수 없으므로 이 옵션은 올바르지 않습니다.

참조:

https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/#Cost_Optimization

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html


-> 신뢰 조언자 역활 다시보기


---------------------------------------------------------

18. 전자 상거래 회사는 AWS 클라우드를 사용하며 개발 및 생산 환경에 대한 별도의 송장을 받고자 합니다. Cloud Practioner로서 이 사용 사례에 대해 다음 중 어떤 솔루션을 추천하시겠습니까?


설명
올바른 옵션:

별도의 인보이스를 받으려면 개발 및 프로덕션 환경에 대해 별도의 AWS 계정을 생성하십시오.

모든 AWS 계정은 자체 송장을 월말에 제공합니다. 각 환경에 대해 별도의 AWS 계정을 설정하여 개발 및 프로덕션 환경에 대해 별도의 인보이스를 받을 수 있습니다.

잘못된 옵션:

AWS Organizations를 사용하여 개발 및 프로덕션 환경에 대한 별도의 인보이스 생성 - AWS Organizations는 결제를 중앙에서 관리하는 데 도움이 됩니다. 액세스, 규정 준수 및 보안 제어 AWS 계정 간에 리소스를 공유합니다. AWS Organizations를 사용하면 계정 생성을 자동화하고, 비즈니스 요구 사항을 반영하는 계정 그룹을 생성하고, 거버넌스를 위해 이러한 그룹에 대한 정책을 적용할 수 있습니다. 모든 AWS 계정에 단일 결제 방법을 설정하여 결제를 간소화할 수도 있습니다. AWS Organizations는 모든 AWS 고객이 추가 비용 없이 사용할 수 있습니다.

AWS Organizations는 개발 및 프로덕션 환경에 대해 `별도의 인보이스를 생성할 수 없으며` 대신 AWS Organizations는 결제를 중앙에서 관리하는 데 도움이 됩니다.

AWS 계정의 모든 리소스에 또는 로 태그를 지정 development합니다 production. 그런 다음 태그를 사용하여 별도의 인보이스를 생성합니다 .` 태그를 기반으로 별도의 인보이스를 생성할 수 없습니다`.

AWS Cost Explorer를 사용하여 개발 및 생산 환경에 대한 별도의 인보이스 생성 - AWS Cost Explorer를 사용하면 상위 수준 및 세부 분석 수준 모두에서 AWS 비용 및 사용량을 탐색하고 여러 필터링 차원(예: , AWS 서비스, 리전, 연결된 계정). AWS Cost Explorer는 개발 및 프로덕션 환경에 대해 별도의 인보이스를 생성할 수 없습니다.

참조:

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html

-> 별도의 세금계산서를 받으려면, 무조건 별개의 계정 생성해라....


---------------------------------------------------------------------------

22. 다국적 기업은 지역별 규정 준수 규칙으로 구성된 다양한 국가의 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스에 비즈니스 크리티컬 데이터를 저장하고 있습니다. 규정 준수를 입증하기 위해 회사는 정기적으로 `과거 구성`을 제출해야 합니다. 이 요구 사항에 가장 적합한 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

AWS 구성

AWS Config는 AWS 계정의 AWS 리소스 구성에 대한 자세한 보기를 제공합니다. 여기에는 리소스가 서로 관련되어 있는 방식과 과거에 리소스가 구성되었던 방식이 포함되므로 `구성 및 관계가 시간 경과에 따라 어떻게 변경`되는지 확인할 수 있습니다. AWS Config는 리소스 관리, 감사 및 규정 준수, 구성 변경 관리 및 문제 해결, 보안 분석 시나리오에서 애플리케이션 리소스를 감독하는 데 도움이 되도록 설계되었습니다.

AWS Config 작동 방식:  - https://aws.amazon.com/config/ 를 통해

잘못된 옵션:

Amazon Macie - Amazon Macie는 기계 학습 및 패턴 일치를 사용하여 AWS에서 중요한 데이터를 검색하고 보호하는 완전 관리형 데이터 보안 및 데이터 개인 정보 보호 서비스입니다. Amazon Macie는 PII(개인 식별 정보)와 같은 민감한 데이터를 식별하고 경고하는 데 도움이 됩니다. 이 서비스는 데이터 프라이버시를 위한 추가 보안 기능으로 현재 요구 사항에 가장 적합하지 않습니다.

AWS CloudTrail - AWS CloudTrail은 AWS 계정의 거버넌스, 규정 준수, 운영 감사 및 위험 감사를 지원하는 서비스입니다. AWS CloudTrail을 사용하면 AWS 인프라 전체에서 작업과 관련된 계정 활동을 기록하고 지속적으로 모니터링하고 유지할 수 있습니다. AWS CloudTrail은 AWS Management Console, AWS SDK, 명령줄 도구 및 기타 AWS 서비스를 통해 수행된 작업을 포함하여 AWS 계정 활동의 이벤트 기록을 제공합니다.

AWS Config는 리소스가 어떻게 변경되었는지에 대한 자세한 스냅샷과 함께 AWS 리소스 및 보고서의 구성에 중점을 둡니다. AWS CloudTrail은 이러한 변경을 주도하는 이벤트 또는 API 호출에 중점을 둡니다. 시스템에서 수행되는 사용자, 애플리케이션 및 활동에 중점을 둡니다.

Amazon GuardDuty - Amazon GuardDuty는 AWS 계정을 보호하기 위해 악의적인 활동 및 무단 동작을 모니터링하는 위협 탐지 서비스입니다. Amazon GuardDuty는 AWS CloudTrail, Amazon VPC 흐름 로그 및 DNS 로그에서 AWS 계정 전체에 걸쳐 수십억 개의 이벤트를 분석합니다. 구성 관리 및 추적 서비스가 아닌 위협 탐지 서비스입니다.

참조:

https://aws.amazon.com/config/

https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html

-> 문제 제대로 못읽음.... 과거 구성을 제출해야됨 -> 컨피규임


------------------------------------------------------------------------------
24. 고객이 애플리케이션을 호스팅하는 Amazon EC2 인스턴스와 함께 사용되는 Amazon EFS 및 Amazon Elastic Block Store(Amazon EBS)의 요금 모델에 대한 비교 연구를 실행하고 있습니다. 이 사용 사례에 대한 다음 설명 중 올바른 것은 무엇입니까? (2개 선택)


설명
올바른 옵션:

Amazon Elastic File System(Amazon EFS) - Infrequent Access 스토리지 클래스에 저장된 데이터를 읽거나 쓸 때마다 요금을 지불합니다.

Amazon Elastic File System(Amazon EFS) - Infrequent Access 스토리지 클래스는 자주 액세스하지 않는 파일에 대해 비용 최적화되어 있습니다. Amazon Elastic File System(Amazon EFS)에 저장된 데이터 - Infrequent Access 스토리지 클래스 비용은 Standard보다 저렴하며 파일을 읽거나 쓸 때마다 요금을 지불합니다.

Amazon Elastic Block Store(Amazon EBS) `스냅샷은 점진적으로 저장되므로 저장된 변경된 블록에 대해서만 비용이 청구됩니다.`

Amazon EBS 스냅샷은 블록 데이터의 특정 시점 복사본입니다. 볼륨의 첫 번째 스냅샷을 위해 Amazon EBS는 데이터의 전체 복사본을 Amazon S3에 저장합니다. Amazon EBS 스냅샷은 증분식으로 저장되므로 저장된 변경된 블록에 대해서만 요금이 청구됩니다.

잘못된 옵션:

Amazon Elastic Compute Cloud(Amazon EC2) 데이터 전송 요금은 스냅샷용 모든 Amazon Elastic Block Store(Amazon EBS) 다이렉트 API에 적용됩니다. - 스냅샷용 Amazon EBS 다이렉트 API를 사용하는 경우 추가 Amazon EC2 데이터 전송 요금은 외부 또는 지역 간 데이터 전송.

Amazon Elastic Block Store(Amazon EBS) 스냅샷 스토리지 요금은 데이터가 Amazon Elastic Block Store(Amazon EBS)에서 소비하는 공간의 양을 기반으로 합니다. - `스냅샷 스토리지는 데이터가 Amazon S3에서 소비하는 공간의 양`을 기반으로 합니다. Amazon EBS는 빈 블록을 저장하지 않기 때문에 스냅샷 크기가 볼륨 크기보다 상당히 작을 가능성이 있습니다. Amazon EBS 스냅샷 복사는 리전 간에 전송된 데이터에 대해 요금이 부과됩니다. 스냅샷이 복사된 후 대상 리전의 스토리지에 대해 표준 Amazon EBS 스냅샷 요금이 적용됩니다.

AWS Backup을 사용하면 한 달 동안 사용한 Amazon Elastic File System(Amazon EFS) 백업 스토리지의 양에 대해서만 비용을 지불하면 이 데이터 복원 비용을 지불할 필요가 없습니다. Amazon EFS 파일 데이터를 백업하려면 AWS Backup을 사용할 수 있습니다. AWS 서비스 전체에서 데이터 백업을 쉽게 중앙 집중화하고 자동화할 수 있는 완전 관리형 백업 서비스입니다.AWS Backup에서는 `사용한 백업 스토리지 양과 해당 월에 복원한 백업 데이터 양`에 대해서만 비용을 지불합니다. 최소 비용이 없으며 설정 비용이 없습니다.

참조:

https://aws.amazon.com/efs/pricing/

https://aws.amazon.com/ebs/pricing/

-> 이건 몰랏음 AWS Backup 비용, EFS ia 비용, ebs 스냅샷 방식


--------------------------------------

30. 다음 중 AWS 글로벌 인프라의 일부는 무엇입니까?

설명
올바른 옵션:

AWS 리전

AWS 리전은 AWS가 데이터 센터를 구축하는 전 세계의 물리적 위치입니다. 논리적 데이터 센터의 각 그룹을 가용 영역(AZ)이라고 합니다. 각 AWS 리전은 지리적 영역 내에서 격리되고 물리적으로 분리된 여러 AZ로 구성됩니다.

미국의 AWS 리전에 대한 이 그림을 참조하십시오.  - https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

잘못된 옵션:

Virtual Private Cloud(VPC) - Amazon Virtual Private Cloud(Amazon VPC)는 정의한 가상 네트워크에서 AWS 리소스를 시작할 수 있는 논리적으로 격리된 AWS 클라우드 섹션입니다. IP 주소 범위 선택, 서브넷 생성, 경로 테이블 및 네트워크 게이트웨이 구성을 포함하여 가상 네트워킹 환경을 완벽하게 제어할 수 있습니다. VPC는 리전의 모든 가용 영역에 걸쳐 있습니다.

VPN(가상 사설망) - AWS 가상 사설망(AWS VPN)을 사용하면 온프레미스 네트워크에서 AWS 글로벌 네트워크로 암호화된 안전한 프라이빗 터널을 설정할 수 있습니다. AWS VPN은 AWS Site-to-Site VPN과 AWS Client VPN의 두 가지 서비스로 구성됩니다.

서브넷 - 서브넷은 VPC 내의 IP 주소 범위입니다. 서브넷은 리전에서 하나의 가용 영역에만 걸쳐 있습니다.

이 세 가지 옵션은 AWS 글로벌 인프라의 일부가 아닙니다.

참조:

https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

-> VPN이 아니였음.... 리전이 글로벌 인프라 일부임 -> 리전의 일부는 vpc,서브넷

---------------------------------------------------------------------------

42. 다음 중 데이터 암호화가 자동으로 활성화된 AWS 서비스는 무엇입니까? (2개 선택)?

설명
올바른 옵션:

Amazon Simple Storage Service(Amazon S3)

모든 Amazon S3 버킷에는 기본적으로 암호화가 구성되어 있으며 객체는 `Amazon S3 관리형 키(SSE-S3)로 서버 측 암호화를` 사용하여 자동으로 암호화됩니다. 이 암호화 설정은 Amazon S3 버킷의 모든 객체에 적용됩니다.

AWS 스토리지 게이트웨이

AWS Storage Gateway는 사실상 무제한의 클라우드 스토리지에 대한 온프레미스 액세스를 제공하는 하이브리드 클라우드 스토리지 서비스입니다. 게이트웨이와 AWS 스토리지 간에 전송되는 모든 데이터는 SSL을 사용하여 암호화됩니다(파일, 볼륨 및 테이프 게이트웨이의 세 가지 게이트웨이 유형 모두에 대해).

잘못된 옵션:

Amazon Elastic Block Store(Amazon EBS) - Amazon Elastic Block Store(Amazon EBS) 볼륨은 기본적으로 암호화되지 않습니다. 생성한 새 EBS 볼륨 및 스냅샷 복사본의 암호화를 적용하도록 AWS 계정을 구성할 수 있습니다.

Amazon Redshift - 암호화는 Amazon Redshift의 선택적 설정입니다. 클러스터에 대한 암호화를 활성화하면 데이터 블록 및 시스템 메타데이터가 클러스터 및 해당 스냅샷에 대해 암호화됩니다.

Amazon Elastic File System(Amazon EFS) - 암호화는 기본 설정이 아니라 Amazon EFS 드라이브에 대한 선택적 구성입니다. Amazon EFS는 파일 시스템에 대해 전송 데이터 암호화와 유휴 데이터 암호화라는 두 가지 형태의 암호화를 지원합니다.

참조:

https://aws.amazon.com/storagegateway/faqs/

https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

-> 아... 그러니까 `s3는 KSM 생성키` 말고도, 아에 기본적으로 s3키로 서버측 암호화를 함, 나머지는 안함
->  암호화는 Amazon Redshift의 선택적 설정입니다. 클러스터에 대한 암호화를 활성화하면 데이터 블록 및 시스템 메타데이터가 클러스터 및 해당 스냅샷에 대해 암호화됩니다.

----------------------------------------

45. 금융 서비스 기업은 직원을 위해 MFA(Multi-Factor Authentication)를 활성화할 계획입니다. 여행의 편의를 위해 물리적 장치를 사용하여 MFA(Multi-Factor Authentication)를 구현하는 것을 선호하지 않습니다. 다음 중 이 사용 사례에 가장 적합한 옵션은 무엇입니까?

가상 멀티 팩터 인증(MFA) 장치

전화 또는 기타 장치에서 실행되고 물리적 장치를 에뮬레이트하는 소프트웨어 앱입니다. 이 장치는 시간 동기화된 일회용 암호 알고리즘을 기반으로 6자리 숫자 코드를 생성합니다. 사용자는 로그인하는 동안 장치의 유효한 코드를 두 번째 웹 페이지에 입력해야 합니다. 사용자에게 할당된 각 가상 Multi-Factor Authentication(MFA) 장치는 고유해야 합니다. 사용자는 인증을 위해 다른 사용자의 가상 Multi-Factor Authentication(MFA) 장치에서 코드를 입력할 수 없습니다.

Google Authenticator는 가상 MFA(Multi-Factor Authentication) 장치의 예입니다. 

잘못된 옵션:

U2F 보안 키 - 컴퓨터의 USB 포트에 연결하는 장치입니다. U2F는 FIDO Alliance에서 호스팅하는 개방형 인증 표준입니다. U2F 보안 키를 활성화하면 코드를 수동으로 입력하는 대신 자격 증명을 입력한 다음 장치를 눌러 로그인합니다.

하드웨어 Multi-Factor Authentication(MFA) 장치 - 시간 동기화된 일회용 암호 알고리즘을 기반으로 6자리 숫자 코드를 생성하는 하드웨어 장치입니다. 사용자는 로그인하는 동안 장치의 유효한 코드를 두 번째 웹 페이지에 입력해야 합니다. 사용자에게 할당된 각 Multi-Factor Authentication(MFA) 장치는 고유해야 합니다. 사용자는 인증을 위해 다른 사용자의 장치에서 코드를 입력할 수 없습니다.

Soft Token Multi-Factor Authentication(MFA) 장치 - 구성된 옵션이며 선택 항목으로 추가되었습니다.


-> `Soft Token Multi-Factor는` 없는말임....

-----------------------------------------------------

50. 다음 중 리전 범위에 해당하는 AWS 서비스는 무엇입니까? (2개 선택)

설명
올바른 옵션:

AWS가 제공하는 대부분의 서비스는 리전별로 다릅니다. 그러나 제공하는 기본 서비스 때문에 정의상 글로벌 범위에 있어야 하는 서비스는 거의 없습니다. AWS Identity and Access Management(AWS IAM), Amazon CloudFront, Amazon Route 53 및 AWS 웹 애플리케이션 방화벽(AWS WAF)은 일부 글로벌 서비스입니다.

AWS 람다

AWS Lambda는 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있는 컴퓨팅 서비스입니다. AWS Lambda는 필요할 때만 코드를 실행하고 하루에 몇 건의 요청에서 초당 수천 건까지 자동으로 확장됩니다. AWS Lambda는 지역 서비스입니다.

아마존 인식

Amazon Rekognition을 사용하면 이미지와 동영상에서 객체, 사람, 텍스트, 장면, 활동을 식별하고 부적절한 콘텐츠를 감지할 수 있습니다. Amazon Rekognition은 또한 매우 정확한 얼굴 분석 및 얼굴 검색 기능을 제공하여 다양한 사용자 확인, 사람 수 계산 및 공공 안전 사용 사례에서 얼굴을 감지, 분석 및 비교하는 데 사용할 수 있습니다. Amazon Rekognition은 지역 서비스입니다.

잘못된 옵션:

AWS Identity and Access Management(AWS IAM) - AWS Identity and Access Management(AWS IAM)를 사용하면 AWS 서비스 및 리소스에 대한 액세스를 안전하게 관리할 수 있습니다. AWS Identity and Access Management(AWS IAM)를 사용하여 IAM 사용자 및 IAM 사용자 그룹을 생성 및 관리하고 권한을 사용하여 AWS 리소스에 대한 액세스를 허용 및 거부할 수 있습니다.

Amazon CloudFront - Amazon CloudFront는 개발자 친화적인 환경 내에서 짧은 지연 시간, 높은 전송 속도로 데이터, 비디오, 애플리케이션 및 API를 전 세계 고객에게 안전하게 전달하는 빠른 콘텐츠 전송 네트워크(CDN) 서비스입니다.

AWS 웹 애플리케이션 방화벽(AWS WAF) - AWS 웹 애플리케이션 방화벽(AWS WAF)을 사용하면 요청 서명을 기반으로 요청을 필터링하고 차단하도록 CloudFront 배포 또는 Application Load Balancer에서 웹 액세스 제어 목록(웹 ACL)을 구성할 수 있습니다.

앞서 언급한 바와 같이 이 세 가지 서비스는 전 세계적으로 적용됩니다.

시험 알림:

Amazon S3 - Amazon S3는 글로벌 네임스페이스를 따르지만 버킷은 지역적이라는 점에서 고유한 서비스입니다. Amazon S3 버킷을 생성할 때 AWS 리전을 지정합니다. 지역별 서비스입니다.


-> 문제 이해 잘못.
-> `WAF는 글로벌 임`
-> rekognition, 람다 서비스 범위 알기


------------------------------

54. 다음 중 블록 수준 스토리지를 제공하는 AWS 서비스는 무엇입니까? (2개 선택)

설명
올바른 옵션:

Amazon Elastic Block Store(Amazon EBS) - Amazon Elastic Block Store(Amazon EBS)는 Amazon Elastic Compute Cloud(Amazon EC2)와 함께 사용하도록 설계된 사용하기 쉬운 고성능 블록 스토리지 서비스로, 모든 규모. 관계형 및 비관계형 데이터베이스, 엔터프라이즈 애플리케이션, 컨테이너화된 애플리케이션, 빅 데이터 분석 엔진, 파일 시스템 및 미디어 워크플로와 같은 광범위한 워크로드가 Amazon EBS에 광범위하게 배포됩니다.

인스턴스 스토어 - 인스턴스 스토어는 EC2 인스턴스에 대한 임시 블록 수준 스토리지를 제공합니다. 이 저장소는 호스트 컴퓨터에 물리적으로 연결된 디스크에 있습니다. 인스턴스 스토어는 버퍼, 캐시, 스크래치 데이터 및 기타 임시 콘텐츠와 같이 자주 변경되는 정보의 임시 스토리지 또는 로드 밸런싱된 웹 서버 풀과 같은 인스턴스 집합 전체에 복제되는 데이터에 이상적입니다. . 인스턴스 스토리지는 일시적이며 인스턴스에 장애가 발생하거나 종료되면 데이터가 손실됩니다. Amazon EC2 인스턴스 스토어는 인스턴스 간 파일 공유에 사용할 수 없습니다.

잘못된 옵션:

Amazon Elastic File System(Amazon EFS) - Amazon Elastic File System(Amazon EFS)은 간단하고 확장 가능하며 완전히 관리되는 탄력적인 NFS 파일 시스템을 제공합니다. 애플리케이션을 중단하지 않고 온디맨드 방식으로 페타바이트까지 확장할 수 있도록 구축되었으며, 파일을 추가 및 제거함에 따라 자동으로 확장 및 축소되므로 성장을 수용하기 위해 용량을 프로비저닝하고 관리할 필요가 없습니다. Amazon EFS는 수천 개의 Amazon EC2 인스턴스에 대한 대규모 병렬 공유 액세스를 제공하도록 설계되어 애플리케이션이 지속적으로 낮은 지연 시간으로 높은 수준의 집계 처리량과 IOPS를 달성할 수 있도록 합니다.

Amazon Simple Storage Service(Amazon S3) - Amazon Simple Storage Service(Amazon S3)는 업계 최고의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스입니다. 즉, 모든 규모와 업종의 고객이 웹 사이트, 모바일 애플리케이션, 백업 및 복원, 아카이브, 엔터프라이즈 애플리케이션, IoT 장치 및 빅 데이터 분석과 같은 다양한 사용 사례에 대해 모든 양의 데이터를 저장하고 보호하는 데 사용할 수 있습니다.

Amazon Elastic Container Service(Amazon ECS) - Amazon Elastic Container Service(Amazon ECS)는 Docker 컨테이너를 지원하고 Amazon EC2 인스턴스의 관리형 클러스터에서 애플리케이션을 쉽게 실행할 수 있는 확장성이 뛰어난 고성능 컨테이너 관리 서비스입니다. 이것은 스토리지 서비스가 아니며 산만함으로 추가되었습니다.

참조:

https://aws.amazon.com/ebs/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html

-> 블록 수준을 몰랐음....  `인스턴스 스토어는 EC2 인스턴스에 대한 임시 블록 수준 스토리지를 제공합니다.`

-------------------------------------
62. AWS Lambda 요금은 다음 기준에 따라 결정됩니까? (2개 선택)

설명
올바른 옵션:

AWS Lambda 함수에 대한 요청 수

람다 함수가 실행되는 데 걸리는 시간

AWS Lambda를 사용하면 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있습니다. AWS Lambda를 사용하면 관리 없이 거의 모든 유형의 애플리케이션 또는 백엔드 서비스에 대한 코드를 실행할 수 있습니다. 코드를 업로드하기만 하면 Lambda가 고가용성으로 코드를 실행하고 확장하는 데 필요한 모든 것을 처리합니다.

AWS Lambda에서는 사용한 만큼만 비용을 지불합니다. 함수에 대한 요청 수와 기간, 코드를 실행하는 데 걸리는 시간에 따라 요금이 부과됩니다. AWS Lambda는 콘솔의 테스트 호출을 포함하여 이벤트 알림 또는 호출 호출에 대한 응답으로 실행을 시작할 때마다 요청을 계산합니다. 기간은 코드가 실행되기 시작한 시간부터 코드가 반환되거나 종료될 때까지 계산되며 가장 가까운 100ms로 반올림됩니다.

잘못된 옵션:

AWS Lambda 함수의 언어 런타임 - AWS Lambda는 NodeJS, Python, Go, C# 등과 같은 많은 프로그래밍 언어 런타임을 지원합니다. AWS Lambda 함수의 가격은 함수의 언어 런타임에 따라 달라지지 않습니다.

AWS Lambda 함수의 코드 줄 수 - AWS Lambda 함수의 요금은 함수의 코드 줄 수에 따라 달라지지 않습니다.

AWS Lambda 함수의 배포 패키지 크기 - AWS Lambda 함수의 가격은 함수의 배포 패키지 크기에 따라 달라지지 않습니다.

참조:

https://aws.amazon.com/lambda/pricing/



-> 캥.... `함수의 언어 런타임`을 몰랐음 `함수의 언어 런타임에 따라 달라지지 않습니다.`





