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

설명
올바른 옵션:

AWS 스노우모빌

AWS Snowmobile은 매우 많은 양의 데이터를 AWS로 이동하는 데 사용되는 엑사바이트 규모의 데이터 전송 서비스입니다. 세미 트레일러 트럭으로 견인되는 45피트 길이의 견고한 운송 컨테이너인 Snowmobile당 최대 100PB를 전송할 수 있습니다. AWS Snowmobile을 사용하면 비디오 라이브러리, 이미지 리포지토리 또는 전체 데이터 센터 마이그레이션을 포함하여 대량의 데이터를 클라우드로 쉽게 이동할 수 있습니다. Snowmobile을 통한 데이터 전송은 보다 안전하고 빠르며 비용 효율적입니다.

잘못된 옵션:

AWS Snowball Edge - AWS Snowball Edge는 AWS Snowball 서비스에서 제공하는 엣지 컴퓨팅 및 데이터 전송 장치입니다. 엣지 로케이션에서 사용할 엄선된 AWS 서비스를 제공하는 온보드 스토리지 및 컴퓨팅 성능을 갖추고 있습니다. 그러나 하나의 AWS Snowball Edge는 최대 100TB의 용량만 제공합니다. 따라서 50PB를 전송하려면 AWS Snowball Edge가 가장 비용 효율적인 옵션이 아닙니다.

AWS Snowball - AWS Snowball은 보안 어플라이언스를 사용하여 AWS 안팎으로 대량의 데이터를 전송하는 페타바이트 규모의 데이터 전송 솔루션입니다. Snowball을 사용하면 높은 네트워크 비용, 긴 전송 시간, 보안 문제 등 대규모 데이터 전송의 일반적인 문제를 해결할 수 있습니다. AWS Snowball을 사용한 데이터 전송은 간단하고 빠르고 안전하며 고속 인터넷 비용의 1/5에 불과합니다. 그러나 하나의 Snowball은 최대 80TB의 용량만 제공합니다. 따라서 50PB를 전송하려면 AWS Snowball이 가장 비용 효율적인 옵션이 아닙니다.

AWS Storage Gateway - AWS Storage Gateway는 온프레미스 애플리케이션이 AWS 클라우드 스토리지를 원활하게 사용할 수 있도록 지원하는 하이브리드 스토리지 서비스입니다. 백업 및 아카이빙, 재해 복구, 클라우드 데이터 처리, 스토리지 계층화 및 마이그레이션에 서비스를 사용할 수 있습니다. 그러나 AWS Storage Gateway를 통한 데이터 전송은 대역폭이 크더라도 더 오래 걸립니다. 또한 50PB의 데이터를 전송하는 것은 AWS Snowmobile을 사용하는 것보다 더 비쌉니다.

참조:

https://aws.amazon.com/snowmobile/

-> 스노우 패밀리 최대크기 다시 보기


-----------------------------------------------------

47. 다음 중 Amazon Route 53에서 제공하는 서비스는 무엇입니까? (2개 선택)

설명
올바른 옵션:

도메인 등록

상태 확인 및 모니터링

Amazon Route 53은 가용성과 확장성이 뛰어난 클라우드 도메인 이름 시스템(DNS) 웹 서비스입니다. www.example.com과 같은 이름을 컴퓨터가 서로 연결하는 데 사용하는 192.0.2.1과 같은 숫자 IP 주소로 변환하여 최종 사용자를 인터넷 애플리케이션으로 라우팅하는 매우 안정적이고 비용 효율적인 방법을 개발자와 기업에 제공하도록 설계되었습니다.

Amazon Route 53은 사용 가능한 도메인 이름을 검색 및 등록하거나 Route 53에서 관리할 기존 도메인 이름을 이전할 수 있는 도메인 이름 등록 서비스를 제공합니다.

Amazon Route 53은 `애플리케이션과 웹 서버 및 기타 리소스의 상태와 성능을 모니터링`할 수 있습니다.

잘못된 옵션:

IP 라우팅 - `이름에도 불구하고 Amazon Route 53은 IP 라우팅을 제공하지 않습니다`. 그러나 라우팅 정책을 사용하여 엔드포인트 상태, 지리적 위치 및 대기 시간과 같은 여러 기준에 따라 트래픽을 라우팅할 수 있습니다.

로드 밸런싱 - 이는 Amazon Route 53이 아닌 ELB(Elastic Load Balancing)의 기능입니다. ELB(Elastic Load Balancing)는 Amazon EC2 인스턴스, 컨테이너, IP 주소 및 Lambda 함수와 같은 여러 대상에 수신 애플리케이션 트래픽을 자동으로 분산합니다. 단일 가용 영역(AZ) 또는 여러 가용 영역(AZ)에서 애플리케이션 트래픽의 다양한 로드를 처리할 수 있습니다.

Transfer Acceleration - Transfer Acceleration은 Amazon의 단순 스토리지 서비스(Amazon S3)의 기능입니다. Amazon S3 Transfer Acceleration(Amazon S3TA)은 더 큰 객체의 장거리 전송을 위해 Amazon S3와의 콘텐츠 전송 속도를 50~500%까지 높일 수 있습니다.

참조:

https://aws.amazon.com/route53/


-> 아... 라우트53은.. ip 라우팅을 지원하지 않는구나..... 모니터링도 가능하다는거 암기해야됨


-----------------------------

51. 기업은 여러 AWS 계정에 대한 액세스 관리를 단순화하고 AWS 계정에 대한 AWS Single Sign-On(AWS SSO) 액세스를 용이하게 하고자 합니다. 클라우드 실무자로서 이 작업에 어떤 AWS 서비스를 사용하시겠습니까?

설명
올바른 옵션:

AWS IAM 자격 증명 센터

AWS IAM Identity Center는 AWS Single Sign-On(AWS SSO)의 후속 제품입니다. AWS Identity and Access Management(IAM) 위에 구축되어 여러 AWS 계정, AWS 애플리케이션 및 기타 SAML 지원 클라우드 애플리케이션에 대한 액세스 관리를 간소화합니다. IAM Identity Center에서는 AWS 전체에서 사용할 인력 사용자를 생성하거나 연결합니다. AWS 계정, 클라우드 애플리케이션 또는 둘 모두에 대한 액세스를 관리하도록 선택할 수 있습니다.

IAM Identity Center에서 직접 사용자를 생성하거나 기존 인력 디렉터리에서 가져올 수 있습니다. IAM Identity Center를 사용하면 세분화된 액세스를 정의, 사용자 지정 및 할당할 수 있는 통합 관리 환경을 얻을 수 있습니다. 직원 사용자는 할당된 AWS 계정 또는 클라우드 애플리케이션에 액세스할 수 있는 사용자 포털을 얻습니다.

IAM Identity Center를 사용하여 여러 AWS 계정, SAML 지원 클라우드 애플리케이션(Salesforce, Microsoft 365, Box 등), 맞춤형 사내 애플리케이션에 대한 직원의 액세스 권한을 쉽고 빠르게 할당하고 관리할 수 있습니다. 중앙 장소.

AWS IAM Identity Center 작동 방식: - https://aws.amazon.com/iam/identity-center/ 를 통해

잘못된 옵션:

AWS Cognito - Amazon Cognito를 사용하면 웹 및 모바일 앱에 사용자 가입, 로그인 및 액세스 제어를 쉽고 빠르게 추가할 수 있습니다. Amazon Cognito를 사용하면 Facebook, Twitter 또는 Amazon과 같은 소셜 자격 증명 공급자를 통해 SAML 자격 증명 솔루션을 사용하거나 자체 자격 증명 시스템을 사용하여 사용자를 인증할 수도 있습니다. 고객을 위해 B2C 또는 B2B 앱을 구축하는 고객/개발자를 위한 ID 관리 솔루션입니다.

AWS Identity and Access Management(AWS IAM) - AWS Identity and Access Management(AWS IAM)를 사용하면 사용자의 AWS 서비스 및 리소스에 대한 액세스를 안전하게 제어할 수 있습니다. AWS IAM을 사용하여 AWS 사용자 및 그룹을 생성 및 관리하고 권한을 사용하여 AWS 리소스에 대한 액세스를 허용 및 거부할 수 있습니다. 로그인이 아니라 사용자 및 역할을 관리하는 데 사용됩니다.

AWS 명령줄 인터페이스(CLI) - AWS 명령줄 인터페이스(CLI)는 AWS 서비스를 관리하기 위한 통합 도구입니다. 하나의 도구만 다운로드하고 구성하면 명령줄에서 여러 AWS 서비스를 제어하고 스크립트를 통해 자동화할 수 있습니다. 중앙 사용자 포털이 아닙니다.

참조:

https://aws.amazon.com/iam/identity-center/


-> 이건 몰랏음
-> 코그니토에 대한 복습 다시

------------------------------------------------------------------------------------------------
53. 클라우드 실무자는 해당 리소스를 사용하는 애플리케이션에 영향을 미칠 수 있는 문제를 신속하게 식별하기 위해 해당 리소스에 대한 운영 통찰력을 얻고자 합니다. 이 작업에 도움이 되는 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

AWS 시스템 관리자

AWS Systems Manager를 사용하면 여러 AWS 서비스의 운영 데이터를 중앙 집중화하고 AWS 리소스 전체에서 작업을 자동화할 수 있습니다. 애플리케이션, 애플리케이션 스택의 다른 계층 또는 프로덕션 대 개발 환경과 같은 리소스의 논리적 그룹을 생성할 수 있습니다.

AWS Systems Manager를 사용하면 리소스 그룹을 선택하고 최근 API 활동, 리소스 구성 변경, 관련 알림, 운영 알림, 소프트웨어 인벤토리 및 패치 규정 준수 상태를 볼 수 있습니다. 운영상의 필요에 따라 각 리소스 그룹에 조치를 취할 수도 있습니다. AWS Systems Manager는 AWS 리소스를 보고 관리할 수 있는 중앙 위치를 제공하므로 작업을 완벽하게 파악하고 제어할 수 있습니다.

AWS Systems Manager 작동 방식: https://aws.amazon.com/systems-manager/ 를 통해

잘못된 옵션:

Amazon Inspector - Amazon Inspector는 AWS에 배포된 애플리케이션의 보안 및 규정 준수를 개선하는 데 도움이 되는 자동화된 보안 평가 서비스입니다. `AWS 리소스`의 운영 통찰력을 얻는 데 사용되지 않습니다.

AWS 상태 대시보드 - 귀하의 계정 상태 - AWS 상태 대시보드 - 귀하의 계정 상태는 AWS에서 귀하에게 영향을 미칠 수 있는 이벤트가 발생할 때 알림 및 해결 지침을 제공합니다. AWS 리소스의 운영 통찰력을 얻는 데 사용되지 않습니다.

AWS Trusted Advisor - AWS Trusted Advisor는 AWS 환경을 최적화하여 비용 절감, 성능 향상 및 보안 향상에 도움이 되는 온라인 리소스입니다. AWS Trusted Advisor는 AWS 모범 사례에 따라 리소스를 프로비저닝하는 데 도움이 되는 실시간 지침을 제공합니다. AWS 리소스의 운영 통찰력을 얻는 데 사용되지 않습니다.

참조:

https://aws.amazon.com/systems-manager/


-> 아... 문제좀 잘 읽지... aws 인스펙터는 ec2, ecr만 해줌..... 그리고 인스펙터는 평가지, `운영 통찰력을 얻는 데` 사용되지 않습니다.

------------------------

54. AWS 클라우드를 처음 접하는 엔지니어링 팀이 저렴한 월별 요금으로 개발/테스트 환경을 시작하려고 합니다. 이 사용 사례를 해결할 수 있는 AWS 서비스는 무엇입니까?

설명
올바른 옵션:

아마존 라이트세일

Amazon Lightsail은 AWS에서 가상 사설 서버(VPS)를 시작하고 관리하는 가장 쉬운 방법으로 설계되었습니다. Amazon Lightsail 요금제에는 가상 머신, SSD 기반 스토리지, 데이터 전송, DNS(도메인 이름 시스템) 관리, 고정 IP 주소 등 프로젝트를 바로 시작하는 데 필요한 모든 것이 포함되어 있으며 저렴하고 예측 가능한 가격입니다.

`클라우드 경험이 거의 없는 사람들이 즉시 사용할 수 있는 인기 있는 IT 솔루션을 신속하게 출시하는 것이 좋습니다.`

잘못된 옵션:

AWS CloudFormation - AWS CloudFormation은 개발자와 시스템 관리자가 관련 AWS 리소스 모음을 생성 및 관리하고 질서 정연하고 예측 가능한 방식으로 프로비저닝 및 업데이트할 수 있는 쉬운 방법을 제공합니다. AWS CloudFormation을 사용하려면 Virtual Private Cloud(VPC) 내에 리소스가 배포되므로 경험이 필요합니다.

Amazon Elastic Compute Cloud(Amazon EC2) - Amazon Elastic Compute Cloud(Amazon EC2)는 클라우드에서 안전하고 크기 조정 가능한 컴퓨팅 용량을 제공하는 웹 서비스입니다. 개발자가 웹 규모 컴퓨팅을 보다 쉽게 ​​수행할 수 있도록 설계되었습니다. Amazon EC2를 사용하여 개발/테스트 환경을 배포하려면` 가상 사설 클라우드(VPC) 내에 인스턴스를 배포하므로 경험이 필요`합니다.

Amazon Elastic Container Service(Amazon ECS) - Amazon Elastic Container Service(Amazon ECS)는 Docker 컨테이너를 지원하고 AWS에서 컨테이너화된 애플리케이션을 쉽게 실행하고 확장할 수 있게 해주는 확장성이 뛰어난 고성능 컨테이너 오케스트레이션 서비스입니다. Amazon ECS를 사용하면 자체 컨테이너 오케스트레이션 소프트웨어를 설치 및 운영하거나, 가상 머신 클러스터를 관리 및 확장하거나, 해당 가상 머신에서 컨테이너를 예약할 필요가 없습니다. Amazon ECS를 사용하려면 경험이 필요합니다.

참조:

https://aws.amazon.com/lightsail/

-> 아... 이건좀... `쉬운거, 처음접해본 사람` 리소스 추천은 무조건... 라이트 세일

------------------------------------------
59. 전자 상거래 회사는 자연어 이해(NLU)를 사용하여 고객 서비스용 챗봇을 구축하려고 합니다. 클라우드 실무자로서 어떤 AWS 서비스를 사용하시겠습니까?


설명
올바른 옵션:

아마존 렉스

Amazon Lex는 `음성 및 텍스트를 사용하여 대화형 인터페이스`를 구축하기 위한 서비스입니다. Amazon Alexa와 동일한 대화 엔진으로 구동되는 Amazon Lex는 고품질 음성 인식 및 언어 이해 기능을 제공하여 신규 및 기존 애플리케이션에 정교한 자연어 '챗봇'을 추가할 수 있습니다.

Amazon Lex 사용 사례:

 - https://aws.amazon.com/lex/ 를 통해

잘못된 옵션:

Amazon Rekognition - Amazon Rekognition을 사용하면 이미지와 비디오에서 객체, 사람, 텍스트, 장면 및 활동을 식별하고 부적절한 콘텐츠도 탐지할 수 있습니다. Amazon Rekognition은 또한 매우 정확한 얼굴 분석 및 얼굴 검색 기능을 제공하여 다양한 사용자 확인, 사람 수 계산 및 공공 안전 사용 사례에서 얼굴을 감지, 분석 및 비교하는 데 사용할 수 있습니다.

Amazon SageMaker - Amazon SageMaker는 개발자와 데이터 과학자가 모든 규모의 기계 학습 모델을 쉽고 빠르게 구축, 교육 및 배포할 수 있도록 하는 완전 관리형 플랫폼입니다. Amazon SageMaker는 일반적으로 기계 학습을 사용하려는 개발자의 속도를 늦추는 모든 장벽을 제거합니다.

Amazon Comprehend - Amazon Comprehend는 기계 학습을 사용하여 텍스트에서 의미와 통찰력을 찾는 자연어 처리(NLP) 서비스입니다. 자연어 처리(NLP)는 컴퓨터가 스마트하고 유용한 방식으로 텍스트 정보를 분석, 이해하고 의미를 도출하는 방법입니다. NLP(Natural Language Processing)를 활용하여 중요한 문구, 감정, 구문, 브랜드, 날짜, 위치, 사람 등의 핵심 엔터티와 텍스트의 언어를 추출할 수 있습니다.

참조:

https://aws.amazon.com/lex/

-> 아... 컴프리핸드는 챗봇이 아님, Amazon Lex는 `음성 및 텍스트를 사용하여 대화형 인터페이스`를 구축하기 위한 서비스입니다

---------------------------------------------------------

60. 신생 기업은 AWS에서 인`기 있는 기술을 신속하게 배포`하려고 합니다. 클라우드 실무자로서 이 작업에 어떤 AWS 도구를 사용하시겠습니까?


설명
올바른 옵션:

AWS 파트너 솔루션(이전의 Quick Starts)

AWS 파트너 솔루션은 AWS(Amazon Web Services) 솔루션 설계자와 AWS 파트너가 구축한 자동화된 참조 배포입니다. 파트너 솔루션은 AWS 모범 사례에 따라 널리 사용되는 기술을 AWS에 배포하는 데 도움이 됩니다. 수백 가지 수동 절차를 몇 단계로 줄이고 몇 분 안에 환경 사용을 시작할 수 있습니다.

AWS 파트너 솔루션은 AWS 클라우드의 주요 워크로드에 대한 자동화된 참조 배포입니다. 각 파트너 솔루션은 보안 및 가용성에 대한 AWS 모범 사례를 사용하여 AWS에서 특정 워크로드를 배포하는 데 필요한 AWS 컴퓨팅, 네트워크, 스토리지 및 기타 서비스를 시작, 구성 및 실행합니다.

잘못된 옵션:

AWS 포럼 - AWS 포럼은 사람들이 서로 도울 수 있는 AWS 커뮤니티 플랫폼입니다. AWS에서 기술을 배포하는 데 사용되지 않습니다.

AWS CodeDeploy - AWS CodeDeploy는 Amazon EC2 인스턴스 및 온프레미스에서 실행되는 인스턴스를 포함하여 모든 인스턴스에 대한 코드 배포를 자동화하는 서비스입니다. 즉시 사용할 준비가 된 AWS에 널리 사용되는 기술을 신속하게 배포하는 데는 적합하지 않습니다.

AWS 백서 - AWS 백서는 클라우드에 대한 지식을 확장하기 위해 AWS와 AWS 커뮤니티에서 작성한 기술 콘텐츠입니다. 여기에는 기술 백서, 기술 가이드, 참조 자료 및 참조 아키텍처 다이어그램이 포함됩니다. 배포에 유용한 콘텐츠를 찾을 수 있지만 `기술을 배포하는 서비스`는 아닙니다.

참조:

https://aws.amazon.com/quickstart/

-> aws parameter solution을 안배웟음




















