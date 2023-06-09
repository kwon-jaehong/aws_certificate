
## 사설 IP, 공용 IP

<br>

- 네트워크는 IPv4,IPv6가 있음
- `IPv6는 주로 사물 인터넷(Iot)`에 쓰임
    - Ipv4 ->  1.2.3.1
    - Ipv6 ->  3ffe:1193:1234:2223:4:203
- `AWS는 Ipv6도 지원함`


<br> 
<br>



public IP( 공용 IP )
- 두 컴퓨터가 같은 공용 IP는 가질 수 없음
- 대중적으로 인터넷(www) 주소로 쓰임

<br>
<br>

private IP (사설 IP )
- 오직 `사설 네트워크 안에서만 식별됨`
- 사설 네트워크 안에서도 두 컴퓨터의 ip는 같을 수 없음
- NAT나 프록시 서버를 이용해 WWW 연결 가능
  - NAT(네트워크 주소 변환 - Network Address Translation, 줄여서 NAT)
  - NAT란. IP 패킷의 TCP/UDP 포트 숫자와 소스 및 목적지의 IP 주소 등을 재기록하면서 라우터를 통해 네트워크 트래픽을 주고 받는 기술을 말합니다.
- 지정된 범위의 IP만 사설 IP로 이용할 수 있음 (192 168 127 )  



-----------------------

## AWS Elastic IPs
- `인터넷용 ipv4`
- 기본적으로 한 계정당 5개만 쓸 수 있음 (서비스 쿼타로 요청해야됨)
- 결론적으로.... `EIP는 사용하지 않는것이 좋습니다` -> 바뀌는 ip를 `DNS`를 써서 운영하는 것이 좋다.
- 로드 밸런서를 사용해 Eip를 전혀 사용 하지 않을 수 있는 패턴이 있다 -> (`AWS에서 취할수 있는 최상의 패턴`)


------------------------------------------------------

## Ec2 Placement Groups (배치 그룹)

- Ec2 인스턴스가 AWS 인프라에 배치되는 방식을 제어할 때 씀
- Ec2 배치 그룹 전략 3가지
  - Cluster (클러스터) - `단일 가용 영역` 내에서(AZ) `지연시간이 짧은` 하드웨어 설정
    - 같은 랙의 장비의(하드웨어) Ec2의 수를 지정해서 예약하는 것. 
    - 10Gbps 네트워크 속도를 자랑함
    - 이 전략은 `높은 성능`을 제공하지만, 위험도 `높다`
    - `빅데이터, 고성능 컴퓨팅(HPC), 낮은 지연시간의 네트워크 성능이 필요할때 씀`



![Alt text](../etc/image2/%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%B0%B0%EC%B9%98.png)


  - Spread (스프레드, 분산배치) - 각 인스턴스가 다른 하드웨어에 분산되어 배치됨
    - 제한사항) 가용 영역별 `최대 7개의` 인스턴스를 가질 수 있음 
    - 동일한 리전의 여러 가용 영역에 적용될 수 있다
    - 따라서, `중요한(크리티컬) 애플리케이션`이 있는경우 이전략을 써야함

![Alt text](../etc/image2/%EC%8A%A4%ED%94%84%EB%A0%88%EB%93%9C%EB%B0%B0%EC%B9%98.png)


- Partition (분할 배치 그룹) - 분산 배치와 비슷함, `Amazon EC2는 각 그룹을 파티션`이라고 하는 논리 세그먼트로 나눔
- 여기서 말하는 `파티션은 = AWS` 랙임
- 그러니까....` 한놈이 죽어도 상관없는 환경을 구축`하는 거임
- Hadoop, Cassandra, Kafka 등 `대규모의 분산 및 복제된 워크로드`에 필요합니다.
- 파티션 배치 그룹은` 동일한 리전의 여러 가용 영역에서` 파티션을 가질 수 있다.
- 제한사항) AZ당 최대 `7개의 파티션(인스턴스 아님!!!)= AWS 랙`
- 파티션에 그룹당 `Ec2 100개 이상` 요청해도 상관없음
- ec2 인스턴스는 내가 어떤 파티션에 있는지 알 수 있음(메타 데이터 서비스 `옵션`을 이용하면 됨)


![Alt text](../etc/image2/%ED%8C%8C%ED%8B%B0%EC%85%98%EB%B0%B0%EC%B9%98.png)



- `ec2 배치그룹`을 만드는것이지, ec2 자체를 배포하는것이 아님


![Alt text](../etc/image2/ec2%EC%83%9D%EC%84%B1%EC%8B%9C%EB%B0%B0%EC%B9%98%EA%B7%B8%EB%A3%B9.png)


참고: <br>
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/placement-groups.html

----------------------


## AWS Elastic Network interfaces (ENI)

- `VPC의 논리적 구성 요소`, 가상 네트워크 카드
- Ec2가 네트워크에 엑세스 할 수 있게 해줌
- ENI는 ec2 인스턴스 `외부에서도 사용됨`
- ENI는 다음과 같은 속성을 가짐
  - 사설(프라이빗) ipv4와, 하나 이상의 `보조 ipv4`를 가질 수 있음 (하나의 ec2에 `보조 ENI`를 얼마든지 추가 해도 됨)
  -  각 ENI는 사설ipv4당, `하나의 Eip를 갖거나, 퍼블릭 IP를 가짐`(둘다 비슷한 말임)
  -  ENI에 `하나 이상의 보안그룹`을 연결 할 수 있음
  -  MAC 주소 및 기타 항목도 연결 가능
  
- ENI는.... Ec2 인스턴스와 `독립적으로 생성 가능`하고, 장애 조치를 위해 Ec2 인스턴스에서 `이동 시킬 수 있음`
- ENI는 특정 가용 영역, 즉 `AZ에 바인딩 됨`(EBS랑 같음, 왜냐? -> ec2 인스턴스와 결합되어 사용되기 때문에 리전이나 글로벌하지 않음)
- 즉 ec2 장애조치를 위해 `사설 IP를 이동/교환/바꿀 수 있음`


------------------------------

## AWS Ec2 Hibernate (절전 모드)

- 인스턴스 중지(stop) : 인스턴스가 다시 시작할떄까지, `EBS 내용은 그대로 유지됨`
- 인스턴스 종료 : EBS 자동 삭제 활성화면 삭제되고, 안걸었으면 그대로 유지


절전모드 
- Ram에 있던 인 메모리 상태는 그대로 보존 (인스턴스를 다시 부팅했을때, 빠름)
- 즉, OS를 스탑(컴퓨터를 껏거나) 재시작 하지 않음
- Ram 상태를 EBS에 기록함 -> 즉, 절전모드를 사용 하려면.... `root EBS 볼륨을 암호화`해야 되고, EBS의 볼륨 용량도 `RAM저장하기에 충분` 해야됨
- 절전모드 + 종료를 섞어 쓰면, 마치, Ec2 인스턴스를 중지한 적이 없는 것처럼 사용 가능함!!!


![Alt text](../etc/image2/%EC%A0%88%EC%A0%84%EB%AA%A8%EB%93%9C.png)


- 사용 케이스
  - 오래 실행되는 프로세스 처리
  - ec2 Ram 상태 저장
  - 부팅을 빠르게 처리 하고 싶을때

- 현재, Ec2 인스턴스의 Ram 최대 크기는 150GB (별로 안중요)
- ec2 (`bare metal instance`)는 적용 할 수 없음
- 리눅스, 윈도우 등의 여러 운영 체제에서 사용 가능
- 오직!!! `루트 볼륨의 유형은` EBS 여야함, 저장이 가능함 
- 온디멘드, 스팟, 예약 인스턴스 모두 사용 가능
- 하지만! 절전 모드는 최대 60일 까지만 사용 가능함 (현재)



`AWS EC2 Bare Metal 인스턴스`
- 가상화된 환경이 아닌 물리적인 서버 환경에서 실행되는 EC2 인스턴스입니다. 이러한 인스턴스는 가상화된 환경을 사용하지 않고 직접적으로 하드웨어에 액세스할 수 있는 기능을 제공하여 고성능 컴퓨팅 워크로드, 메모리 집약적인 애플리케이션, 데이터베이스 또는 하이퍼스케일 아키텍처 등에 적합합니다.


----------------------------------------
## AWS Spot

- 스팟의 기본은, 내가 설정한 최고 구매 가격보다 높아지면 ,`2분의 유예 시간을 줌`
- 실패해도 복구성이 있는 작업에 쓰임
- 최대 온디멘드보다 90% 쌈
- 

스팟 요청 
- 원하는 인스턴스의 개수, 최고 가격, AMI 등 요구되는 사양, `요청의 유효기간`,요청 유형이 필요함
- 요청에는 2가지 타입이 있음
  - one-time 일회성 요청
    - 요청 즉시, 인스턴스가 시작됨
    - 처리되면 요청 문서는 사라짐
    - 스팟 요청이 사라져도 괜찮은 경우 사용
 
  - persistent 지속적 요청
    - valid from(시작) valid until(까지) 유효기간동안 요청을 계속보냄


- 스팟 요청 취소는 스팟이 open, active, disabled 상태여야함
- `스팟 요청`을 취소해도 인스턴스는 종료 안됨 -> 진짜 말 그대로, 스팟 요청만 취소했지, 인스턴스 삭제한건 아님! 
- 또, 스팟 인스턴스만 삭제한다고 되는게 아님, 스팟 요청도 삭제해야됨!!! -> `스팟 인스턴스 삭제하면, 연결된 요청이 다시 스팟 인스턴스를 프로비저닝 함`!!!!

- 즉, '스팟 요청' 삭제 -> 스팟 인스턴스 삭제가 기본 플로우임 

![Alt text](../etc/image2/%EC%8A%A4%ED%8C%9F%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4.png)




Spot Fleets (스팟 집합)

- 한 세트의 스팟 인스턴스에다가 `선택적으로 온디맨드 인스턴스`를 조합해 사용하는 방식
- 정해진 비용 제한내에서 대상 용량을 맞추려 노력함
- `Launch pools`이라는 것을 정의해서 진행함
- 스팟 플릿은 제일 적합한 런치풀을 선택해줌
- 플릿은 정해진 예산 혹은, 원하는 용량에 달한 경우에는 인스턴스 실행을 멈춤?


- `스팟 플릿 - 할당 전략`
  - lowestPrice (최저 가격)
    - 제일 낮은 가격으로 실행해줌, 아주 짧은 워크로드에 적합
  - diversified (모든 풀에서 다각화)
    - 긴 워크로드에 적합하고, `가용성이 뛰어난 옵션`
    - 사용 가능한 모든 풀에서 `스팟 인스턴스를 균등`하게 요청
  - capacity optimized (용량 최적화)
    - 가장 가용성이 높은 풀에서 인스턴스를 요청함
    - 이 전략은 스팟 인스턴스가 `중단될 위험이 가장 낮음`


















