5. 시드니에 기반을 둔 회사는 ap-southeast-2의 Amazon Elastic Compute Cloud(Amazon EC2) 인스턴스에서 애플리케이션을 호스팅합니다. 그들은 eu-south-1에 동일한 Amazon EC2 인스턴스를 배포하려고 합니다. 다음 중 이 사용 사례를 해결할 수 있는 AWS 엔터티는 무엇입니까?

설명
올바른 옵션:

Amazon 머신 이미지(AMI)

Amazon 머신 이미지(AMI)는 인스턴스를 시작하는 데 필요한 정보를 제공합니다. 인스턴스를 시작할 때 Amazon 머신 이미지(AMI)를 지정해야 합니다. 구성이 동일한 여러 인스턴스가 필요한 경우 단일 Amazon 머신 이미지(AMI)에서 여러 인스턴스를 시작할 수 있습니다.

Amazon 머신 이미지(AMI) 사용 방법: - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html 을 통해

잘못된 옵션:

ELB(Elastic Load Balancing) - ELB(Elastic Load Balancing)는 Amazon EC2 인스턴스, 컨테이너, IP 주소 및 Lambda 함수와 같은 여러 대상에 수신 애플리케이션 트래픽을 자동으로 분산합니다. 단일 가용 영역(AZ) 또는 여러 가용 영역(AZ)에서 애플리케이션 트래픽의 다양한 로드를 처리할 수 있습니다. 서로 다른 가용 영역(AZ)에 동일한 EC2 인스턴스를 배포하는 데 사용할 수 없습니다.

AWS Lambda - AWS Lambda를 사용하면 서버를 프로비저닝하거나 관리하지 않고도 코드를 실행할 수 있습니다. 서로 다른 가용 영역(AZ)에 동일한 EC2 인스턴스를 배포하는 데 사용할 수 없습니다.

Amazon EBS 탄력적 볼륨 스냅샷 - Amazon EBS 스냅샷은 Amazon EBS 볼륨의 특정 시점 복사본입니다.` EBS 스냅샷은 AMI의 구성 요소 중 하나이지만, EBS 스냅샷만으로는 여러 가용 영역(AZ)에 동일한 EC2 인스턴스를 배포할 수 없습니다.`

참조:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html

-> 그냥 복사 아니였음? 

-----------------------------------
7. 다음 중 IAM 사용자에게 부여된 권한을 검토할 수 있는 AWS Identity and Access Management(AWS IAM) 보안 도구는 무엇입니까?

설명
올바른 옵션:

AWS Identity and Access Management(IAM) 액세스 고문

IAM 액세스 관리자는 사용자에게 부여된 서비스 권한과 해당 서비스가 마지막으로 액세스된 시간을 보여줍니다. 이 정보를 사용하여 정책을 수정할 수 있습니다. 요약하면 불필요한 권한을 식별하여 그에 따라 IAM 정책을 수정할 수 있습니다.

잘못된 옵션:

IAM 자격 증명 보고서 - 계정의 모든 IAM 사용자와 암호, 액세스 키 및 MFA(다단계 인증) 디바이스를 비롯한 다양한 자격 증명의 상태를 나열하는 자격 증명 보고서를 생성하고 다운로드할 수 있습니다. IAM 사용자에게 부여된 권한을 검토하는 데 사용되지 않습니다.

IAM 정책 - IAM 정책은 작업을 수행하는 데 사용하는 방법에 관계없이 작업에 대한 권한을 정의합니다.

Multi-Factor Authentication(MFA) - Multi-Factor Authentication(MFA)은 사용자 이름과 암호 위에 추가 보호 계층을 추가하는 간단한 모범 사례입니다. Multi-Factor Authentication(MFA)이 활성화된 상태에서 사용자가 AWS Management Console에 로그인하면 사용자 이름과 암호(첫 번째 요소는 알고 있는 것)는 물론 인증 코드를 입력하라는 메시지가 표시됩니다. AWS MFA 디바이스(두 번째 요소—가지고 있는 것). 이러한 여러 요소를 종합하면 AWS 계정 설정 및 리소스에 대한 보안이 강화됩니다. 부여된 권한을 검토하는 데 사용할 수 없습니다.

참조:

https://aws.amazon.com/about-aws/whats-new/2019/06/now-use-iam-access-advisor-with-aws-organizations-to-set-permission-guardrails-confidently/

-> 아... 엑세스 관리자에서 부여된 권한 다 볼수 있음.... 난 awsconfig 처럼... 마지막 로그만 찍히는줄 알았음

---------------------------------------------------------------------------------------------------
8. Amazon EBS 탄력적 볼륨에 관한 다음 설명 중 잘못된 것은 무엇입니까?

설명
올바른 옵션:

Amazon EBS 탄력적 볼륨은 여러 가용 영역(AZ)에 바인딩될 수 있습니다.

Amazon EBS 탄력적 볼륨은 인스턴스에 연결할 수 있는 내구성 있는 블록 수준 스토리지 장치입니다. 볼륨을 인스턴스에 연결한 후에는 물리적 하드 드라이브를 사용하는 것처럼 볼륨을 사용할 수 있습니다.

Amazon EBS 탄력적 볼륨을 사용할 때 볼륨과 인스턴스는 동일한 가용 영역(AZ)에 있어야 합니다.

잘못된 옵션:

Amazon EBS Elastic Volumes는 한 번에 하나의 인스턴스에 탑재할 수 있습니다 . Certified Cloud Practitioner 수준에서 Amazon EBS Elastic Volumes는 한 번에 하나의 인스턴스에 탑재할 수 있습니다. Amazon EBS 탄력적 볼륨이 인스턴스에 마운트되지 않았을 수도 있습니다.

Amazon EBS 탄력적 볼륨은 특정 가용 영역(AZ)에 바인딩됩니다 . `언급한 바와 같이 Amazon EBS 탄력적 볼륨을 사용할 때는 볼륨과 인스턴스가 동일한 가용 영역(AZ)에 있어야 합니다`.

Amazon EBS 탄력적 볼륨은 종료 후에도 데이터를 유지할 수 있습니다 . - Amazon EC2 인스턴스 스토어와 달리 Amazon EBS 탄력적 볼륨은 인스턴스 수명과 독립적으로 유지할 수 있는 인스턴스 외부 스토리지입니다.

참조:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html

-> 어... 잘못된것을 찾는거였음....


--------------------------------------------------------------
9. 회사에서 인프라를 AWS 클라우드로 이전하려고 합니다. 다음 중 총소유비용(TCO) 추정에 포함되어야 하는 것은 무엇입니까? (2개 선택)


설명
올바른 옵션:

서버 관리

전원/냉각

AWS 요금 계산기를 사용하면 AWS 서비스를 탐색하고 AWS에서의 사용 사례 비용을 추정할 수 있습니다. `솔루션을 구축하기 전에 모델링하고 예상 가격과 계산을 살펴보고 필요에 맞는 사용 가능한 인스턴스 유형과 계약 조건을 찾을 수 있습니다`. 이를 통해 AWS 사용에 대해 정보에 입각한 결정을 내릴 수 있습니다. 새로운 인스턴스 및 서비스 세트를 설정하여 AWS 비용 및 사용량을 계획하거나 가격을 책정할 수 있습니다. AWS 요금 계산기는 https://calculator.aws/#/ 에서 액세스할 수 있습니다 .

AWS 가격 계산기는 온프레미스 또는 기존 호스팅 환경의 애플리케이션 비용을 서버, 스토리지, 네트워크 및 IT 노동과 같은 AWS와 비교합니다. 따라서 이러한 비교 지점과 관련된 모든 요소를 ​​포함해야 합니다.

서버 관리는 IT 인건비에 포함됩니다.

전원/냉각은 서버, 스토리지 및 네트워크 비용에 포함됩니다.

잘못된 옵션:

애플리케이션 광고 - 애플리케이션 광고는 총소유비용(TCO) 추정치와 관련이 없습니다.

최종 사용자 수 - 최종 사용자 수는 TCO(총 소유 비용) 추정과 관련이 없습니다.

사무실의 전자 장비 - 사무실의 전자 장비는 총소유비용(TCO) 추정과 관련이 없습니다.

참조:

https://calculator.aws/#/

https://aws.amazon.com/blogs/aws/new-cloud-tco-comparison-calculator-for-web-applications/

-> TCO는 총소유비용을 의미합니다. 데이터 스토리지의 경우, 조직은 IT 인프라를 구매, 설치, 실행 및 유지 관리하는 과정에서 발생하는 모든 비용을 평가해야 합니다. 총소유비용(TCO)에는 하드웨어 및 소프트웨어, 관리 및 실무, 스토리지 용량 및 컴퓨트 리소스 그리고 다운타임 중에 발생하는 모든 기회 비용이 포함될 수 있습니다.
총소유 비용 뜻을 몰랏음


-------------------------------
10. 신생 기업은 기본 인프라를 관리할 필요가 없고 응용 프로그램의 배포 및 관리에 집중하기를 원합니다. 이것은 어떤 유형의 클라우드 컴퓨팅을 의미합니까?


서비스형 플랫폼(PaaS)

클라우드 컴퓨팅은 크게 IaaS(Infrastructure as a Service), PaaS(Platform as a Service), SaaS(Software as a Service)의 세 가지 유형으로 나눌 수 있습니다.

PaaS(Platform as a Service)를 사용하면 기본 인프라(일반적으로 하드웨어 및 운영 체제)를 관리할 필요가 없으며 애플리케이션 배포 및 관리에 집중할 수 있습니다. 리소스 조달, 용량 계획, 소프트웨어 유지 관리, 패치 또는 응용 프로그램 실행과 관련된 기타 획일적인 작업에 대해 걱정할 필요가 없습니다.

클라우드 컴퓨팅 유형에 대한 이 개요를 검토하십시오.  - https://aws.amazon.com/types-of-cloud-computing/

잘못된 옵션:

IaaS(Infrastructure as a Service) - IaaS(Infrastructure as a Service)에는 클라우드 IT의 기본 빌딩 블록이 포함되어 있습니다. 일반적으로 네트워킹 기능, 컴퓨터(가상 또는 전용 하드웨어) 및 데이터 저장 공간에 대한 액세스를 제공합니다. IaaS(Infrastructure as a Service)는 IT 리소스에 대한 최고 수준의 유연성과 관리 제어를 제공합니다.

SaaS(Software as a Service) - SaaS(Software as a Service)는 서비스 공급자가 실행하고 관리하는 완전한 제품을 제공합니다. SaaS(Software as a Service) 오퍼링을 사용하면 서비스 유지 방법이나 기본 인프라 관리 방법에 대해 생각할 필요가 없습니다. 특정 소프트웨어를 사용하는 방법에 대해서만 생각하면 됩니다. Amazon Rekognition은 SaaS 서비스의 한 예입니다.

온프레미스 - 기업이 온프레미스를 선택하면 정교한 하드웨어, 호환 가능한 소프트웨어 및 강력한 서비스에 투자하여 온프레미스 IT 인프라를 생성, 업그레이드 및 확장해야 합니다. 또한 기업은 온프레미스 인프라를 지속적으로 유지, 확장 및 관리하기 위해 전담 IT 직원을 배치해야 합니다.

참조:

https://aws.amazon.com/types-of-cloud-computing/

-> 파스다.... 아 파스 사스 라스 개념 다시 적립

--------------------------------------------------
25. 성장하는 신생 기업은 중요한 `데이터를 대규모로 식별`하고 보호하는 데 어려움을 겪습니다. 이 작업을 지원할 수 있는 AWS 완전관리형 서비스는 무엇입니까?

설명
올바른 옵션:

아마존 매트

Amazon Macie는 기계 학습 및 패턴 일치를 사용하여 AWS에서 중요한 데이터를 검색하고 보호하는` 완전 관리형` 데이터 보안 및 데이터 개인 정보 보호 서비스입니다.

Amazon Macie는 기계 학습 및 패턴 일치를 사용하여 대규모로 중요한 데이터를 비용 효율적으로 검색합니다. Amazon Macie는 이름, 주소, 신용 카드 번호와 같은 개인 식별 정보(PII)를 포함하여 점점 늘어나는 중요한 데이터 유형 목록을 자동으로 감지합니다. 또한 Amazon S3에 저장된 데이터의 데이터 보안 및 데이터 프라이버시에 대한 지속적인 가시성을 제공합니다.

Amazon Macie 작동 방식:  - https://aws.amazon.com/macie/ 를 통해

잘못된 옵션:

AWS Artifact - AWS Artifact는 중요한 규정 준수 관련 정보를 제공하는 중앙 리소스입니다. AWS의 보안 및 규정 준수 보고서에 대한 온디맨드 액세스를 제공하고 온라인 계약을 선택합니다. AWS에서 중요한 데이터를 검색하고 보호하는 데 사용되지 않습니다.

AWS Secrets Manager - AWS Secrets Manager는 애플리케이션, 서비스 및 IT 리소스에 액세스하는 데 필요한 암호를 보호하는 데 도움이 됩니다. 이 서비스를 사용하면 수명 주기 동안 데이터베이스 자격 증명, API 키 및 기타 암호를 쉽게 교체, 관리 및 검색할 수 있습니다. AWS에서 중요한 데이터를 검색하고 보호하는 데 사용되지 않습니다.

AWS Key Management Service(AWS KMS) - AWS Key Management Service(AWS KMS)를 사용하면 손쉽게 키를 생성 및 관리하고 다양한 AWS 서비스 및 애플리케이션에서 암호화 사용을 제어할 수 있습니다. AWS에서 중요한 데이터를 검색하고 보호하는 데 사용되지 않습니다.

참조:

https://aws.amazon.com/macie/


-> 역시... 시크릿 매니저는 데이터 검색에는 사용 안됨


---------------------------------------------------------------

26. 다음 중 AWS 클라우드를 사용할 때의 이점은 무엇입니까? (2개 선택)

설명
올바른 옵션:

속도와 민첩성 향상

용량에 대한 추측 중지

시험 알림:

다음 6가지 Cloud Computing의 장점을 확인하십시오. 기존의 온프레미스 설정과 비교하여 클라우드 컴퓨팅의 이점에 대한 질문을 받게 될 것입니다.

 통해 - https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

잘못된 옵션:

제한된 확장 - 확장은 클라우드에서 제한되지 않습니다. 필요한 만큼의 용량에 액세스할 수 있으며 몇 분 전에 통지하면 필요에 따라 확장 및 축소할 수 있습니다.

AWS는 클라우드의 보안을 책임집니다 . AWS는 클라우드의 보안을 책임집니다. 즉, AWS는 AWS 클라우드에서 제공되는 모든 서비스를 실행하는 인프라를 보호할 책임이 있습니다.

운영 비용을 자본 비용으로 교환 - `클라우드에서는 자본 비용(CAPEX)을 운영 비용(OPEX)으로 교환합니다`. 사용 방법을 알기도 전에 데이터 센터와 서버에 막대한 투자를 하는 대신 컴퓨팅 리소스를 사용할 때만 비용을 지불하고 소비한 양에 대해서만 비용을 지불할 수 있습니다.

참조:

https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html

-> 역시... 영어 번역 오류임

AWS is responsible for security in the cloud 
AWS is responsible for the security OF the cloud,


"AWS is responsible for security in the cloud"와 "AWS is responsible for the security OF the cloud"는 미묘한 차이가 있습니다.

"AWS is responsible for security in the cloud"는 AWS가 클라우드 환경에서의 보안에 책임을 지고 있다는 의미입니다. 즉, AWS는 기밀성, 무결성, 가용성 등의 보안을 유지하기 위한 기본적인 보안 인프라를 구축하고 운영합니다. 이는 AWS 데이터 센터의 물리적 보안, 네트워크 보안, 인프라 보안, 운영 체제 보안 등을 포함합니다. AWS는 클라우드 서비스의 인프라를 보호하여 기본적인 보안을 제공하고, 고객은 이러한 보안 기능을 활용하여 자신의 애플리케이션과 데이터를 안전하게 유지할 수 있습니다.

"AWS is responsible for the security OF the cloud"는 AWS가 제공하는 클라우드 환경 자체의 보안을 말합니다. 이는 AWS의 클라우드 서비스, 리소스, 관리 도구 등에 대한 보안을 의미합니다. AWS는 클라우드 환경에서의 보안을 강화하기 위해 다양한 기능과 서비스를 제공합니다. 예를 들어, AWS Identity and Access Management (IAM)을 사용하여 사용자 액세스 및 권한을 관리하거나, AWS WAF(Web Application Firewall)를 사용하여 웹 애플리케이션을 보호할 수 있습니다. 이러한 보안 기능은 AWS가 제공하는 클라우드 환경 자체의 보안을 강화하고, 사용자는 이를 활용하여 자신의 애플리케이션과 데이터를 보호할 수 있습니다.

요약하면, "AWS is responsible for security in the cloud"는 AWS가 클라우드 환경 전반에 걸친 보안에 책임을 지고 있다는 의미이고, "AWS is responsible for the security OF the cloud"는 AWS가 제공하는 클라우드 환경 자체의 보안에 책임을 지고 있다는 의미입니다.

-------------------------------------------------------------------


43. 한 기업이 온프레미스 데이터 센터에서 AWS로 가장 비용 효율적인 방식으로 50페타바이트(PB)의 데이터를 이동하려고 합니다. 클라우드 실무자로서 다음 중 어떤 솔루션을 선택하시겠습니까?

