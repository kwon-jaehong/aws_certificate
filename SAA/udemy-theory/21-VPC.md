## CIDR - IPv4 (Classless inter-domain routing)



- CIDR는 Ip주소를 할당하는 방법
  - `베이스 IP / 서브넷 마스크`  -> 10.2.3.4/32
  - /8이면, 255.0.0.0 
  - /16, 255.255.0.0

------------------------------------
## AWS VPC
- VPC는 기본적으로 `리전`에 생성됨
- 한 리전에 여러 VPC 생성 가능 (`리전당 5개` -> 서비스 요청으로 늘릴 수 있음)
  - vpc에서 최소 서브넷마스크 크기는 `28` => `IP 16개 할당 가능`
  - vpc에서 최대 서브넷마스크 크기는 `16` => `IP 65536개 할당 가능`
- `사설 IP 대역만 개설 가능`
  - 10.0.0.0 ~ 10.255.255.255 (10.0.0.0/8) -> 
  - 172.16.0.0 ~ 172.31.255.255 (10.0.0.0/12)
  - 192.168.0.0 ~ 192.168.255.255 (10.0.0.0/16)

- VPC에서 수정도 가능 (`CIDR 추가 5개 까지 가능`)




--------------------

## AWS SubNet
- 공용, 사설 서브넷 존재
- 각 서브넷마다 `AWS 공식적으로 주소를 5개` 예약함
  - 서브넷에서 CIDR 블럭을 10.0.0.0/24를 예약했다면
    - 10.0.0.0 - Network address 네트워크 주소
    - 10.0.0.1 - VPC router 주소
    - 10.0.0.2 - DNS 주소
    - 10.0.0.3 - AWS 미정 (예약은 했지만, 아직 안씀)
    - 10.0.0.255 - VPC 브로드캐스트 주소 (AWS에서 브로드 캐스트를 지원하진않음 -> `예약은 되지만, 사용은 못함`)
- `하나의 서브넷은 하나의 AZ에 소속됨`

- CIDR은 IP/`32` 일때 1개 선택
  - 32비트를 잘 생각해야됨
  - 
![Alt text](../../etc/image2/%EC%84%9C%EB%B8%8C%EB%84%B7.png)

<br><br><br><br>

----------------------------------------------
## AWS Internet Gateway

- VPC에 붙여 인터넷을 가능하게 하는 문
- VPC는 `하나의 IGW에만 연결 가능`
- IGW는 인터넷 자체를 허용하지 않음 -> 라우팅 테이블이 담당함


---------------------------------------------------
## AWS Bastion Host

- 퍼블릭 서브넷에서 프라이빗 서브넷 Ec2에 접속하기 위한 `Ec2 인스턴스`
  - 베스쳔 호스트 `AWS 서비스 이름이 아님!!!` -> ec2 인스턴스의 사용방법/기법임
- `베스쳔 보안그룹`을 따로 지정해줌
- 기업의 CIDR 엑세스 허용, `SSH로만 통신 (22포트)`

![Alt text](../../etc/image2/%EB%B2%A0%EC%8A%A4%EC%B3%94%ED%98%B8%EC%8A%A4%ED%8A%B8.png)


---------------------------------------------
## AWS NAT (Network address Translation 네트워크 주소 변환)

- 프라이빗 서브넷에 있는 Ec2인스턴스 인터넷 연결 통로
  - 왜씀? -> 베스쳔 호스트는 SSH연결만 해주기 위함이고, 프라이빗 Ec2는 인터넷 여전히 안됨
- 오직 `Ipv4에서만 작동`

- NAT에는 2종류가 있다
  - NAT Instance (구식)
    - 프라이빗과 퍼블릭의 중계용 Ec2 인스턴스
    - EIP로 연결 되어있어야함
    - 베스쳔 호스트처럼 Ec2 생성하고, 라우팅 테이블 설정, 보안그룹 , 일일이 해줘야함
    - 프라이빗 Ec2가 요청한 패킷을 `대신 받아서 전달 해줌`
    - `NAT 인스턴스용 AMI 지원은 20년에` 종료됬음 (생성은 할 수있지만, 업데이트 안됨)
    - 저가용성, ASG설정등 관리가 복잡함
      - 저사양 인스턴스는 네트워크 대역폭이 작아, 감당 못함
    - Nat 인스턴스 설정을 네트워크->`소스/목적지 체크`를 중단 해야됨
  - NAT Gateway
    - `AWS 관리형 Nat인스턴스`
    - Eip필요하고, Az에 생성됨
    - 고가용성을 지향하려면, 멀티 AZ에 생성하는것이 좋음

----------------------------------
## AWS NACL & 보안그룹

- NACL은 서브넷에 적용,보안그룹은 인스턴스에 적용
- NACL은 stateless, 보안그룹은 stateful 이다 (기록을 남기냐, 안남기냐 차이)
- NACL은 규칙이 있고, 번호는 1~32766까지 있다, `번호가 낮을수록 규칙 검사 우선순위가 높음`
  - 예)
    - NACL 규칙 100번 10.0.0.10/32 거부
    - NACL 규칙 200번 규칙 10.0.0.10/32 허용
    - `NACL 규칙 100번 규칙이 숫자가 낮으므로, 10.0.0.10은 거부당함`
  - 규칙을 100씩 증가시키는것을 추천 -> 그사이에 규칙을 작성하기 좋음
  - 번호에 `*`인 것이 있는데, 일치하지 않으면, 거부를 위한것 (조건에 안맞으면, 거부 기본값이라고 생각)
  - NACL은 `기본적으로 모두 거부함`

- 서버와 클라이언트가 통신할때, 클라이언트는 `Ephemeral Port(임시포트)`를 만들어서 통신한다. 통신이 유지되는 동안 열려있음
  - 윈도우는 49152 - 65535
  - 리눅스는 32768 - 60999

![Alt text](../../etc/image2/%EC%84%9C%EB%B2%84%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8%EC%9E%84%EC%8B%9C%ED%8F%AC%ED%8A%B8.png)



- Stateful(상태 보존):
  - 보안그룹은 상태 보존(stateful) 기능을 가지고 있습니다. 이는 허용한 트래픽에 대한 응답 트래픽을 자동으로 허용한다는 의미입니다. 즉, `보안그룹에 허용 규칙을 추가하면 해당 트래픽의 응답은 자동으로 허용`됩니다. 예를 들어, HTTP 트래픽을 허용하는 규칙을 추가하면, HTTP 응답도 자동으로 허용됩니다. 따라서 `보안그룹에서 인바운드 규칙을 설정하면, 관련된 아웃바운드 규칙을 별도로 설정할 필요가 없습니다`.
  - 인바운드,아웃바운드 허용 하나만 설정하면, 둘다 허용됨


- Stateless(상태 비보존):
- NACL은 상태 비보존(stateless) 기능을 가지고 있습니다. 이는 `트래픽에 대한 요청 및 응답을 개별적으로 처리`한다는 의미입니다. 예를 들어, `특정 포트로 들어오는 트래픽을 허용하는 인바운드 규칙을 추가한 경우, 해당 포트에서 나가는 트래픽은 자동으로 허용되지 않습니다`. 따라서 NACL에서 인바운드 규칙을 설정한 후, 관련된 아웃바운드 규칙도 별도로 설정해야 합니다



- 물건을 보낼 때, 택배 상자에 상태를 유지하는(stateful) 방식과 상태를 유지하지 않는(stateless) 방식을 생각해볼 수 있습니다.

- 상태를 유지하는(stateful) 방식:
  - 택배 상자에 물건을 넣고 주소를 붙이면, 택배 회사는 이 정보를 유지합니다. 이후에 물건을 배송하거나 문의가 있을 때, 택배 회사는 상자에 붙은 주소 정보를 참조하여 처리합니다. 이는 `상자와 주소 간의 상태를 유지하는 방식`입니다. 예를 들어, 택배 회사가 물건을 배송하는 도중 문제가 발생하면, 상태 정보를 확인하고 문제를 해결할 수 있습니다.

- 상태를 유지하지 않는(stateless) 방식:
  - 상태를 유지하지 않는 방식에서는 택배 상자에 물건을 넣고 주소를 붙이는 것으로 끝입니다. `택배 회사는 상자에 대한 어떠한 정보도 기억하지 않습니다`. 따라서 물건이 배송되거나 문의가 있을 때, 상자에 대한 정보가 없으므로 주소 정보를 기반으로 처리합니다. 이 방식에서는 상자의 상태를 따로 유지하지 않고, `주어진 정보를 기반으로 처리하는 것`입니다.

- 이와 비슷하게, 네트워크에서도 상태를 유지하는(stateful) 방식과 상태를 유지하지 않는(stateless) 방식을 사용할 수 있습니다. `상태를 유지하는 프로토콜이나 장치는 통신의 시작부터 끝까지 연결 정보를 기억하고 유지합니다. 반면에 상태를 유지하지 않는 프로토콜이나 장치는 각각의 통신이 독립적이며`, 통신에 대한 추가 정보를 기억하지 않습니다.

- 간단히 말해, 상태를 유지하는(stateful) 방식은 정보를 계속 유지하고 참조하여 처리하는 반면, 상태를 유지하지 않는(stateless) 방식은 정보를 한 번 사용하고 나면 버리는 것입니다.

-----------------------------------------------------

## VPC Peering

- VPC끼리 네트워크 연결
- `다른 리전, 다른 계정도 연결 가능`
- 단, CIDR가 안 겹쳐야함
- 연결된 `VPC(2개) 서브넷의 라우트 테이블을 업데이트` 해서, Ec2간 충돌을 막아야 한다
- 연결되면, 보안그룹 참조 가능항(`같은 리전`)


---------------------------------------
## VPC endpoint (VPC PrivateLink)
- `AWS PrivateLink` 라고도 부름
- AWS 내부 트래픽처리를 위해 엔드포인트 씀
- 종류는 2가지 있음
  - `VPC Endpoint interface`
    - `ENI`를 할당해서 연결
    - 보안그룹 적용해야함
  - VPC Endpoint Gateway
    - `라우팅 테이블만 수정해야됨 (보안그룹 X)`
    - `S3,다이나모 DB`만 지원 가능
    - `무료`
- S3, 다이나모는 거의 게이트웨이를 이용하는 것이 좋음
  - 하지만, VPN이나, 온프레미스에서 엑세스해야될 워크로드면 인터페이스 써야함

- 엔드포인트가 생성되면, 정책 연결 해야됨

![Alt text](../../etc/image2/%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B81.png)

![Alt text](../../etc/image2/%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B82.jpg)

<br><br><br><br>

------------------------------------
## VPC Flow Logs

- 인터페이스로 향하는 IP 트래픽 정보를 로그남기는 서비스
  - 타입은
    - `VPC Flow logs`
      - 로그 분석 최선의 방법은, S3에 저장해서 아테나로 분석 하는것
    - `subnet flow logs`
      - 서브넷 선택해서 이 서브넷따로 로그 남길수 있ㅇ므
    - `ENI flow logs`
      - ENI 선택해서 따로 로그 남기기 가능
  - 



- VPC flow 로그를 읽는방법
  - 전송/목적지 IP, port 패킷, 통신 시간, 인터페이스 ID
![Alt text](../../etc/image2/VPC%ED%94%8C%EB%A1%9C%EC%9A%B0%EB%A1%9C%EA%B7%B8.png)


------------------------------------------
## AWS Site-to-Site VPN

## AWS site to site VPN
- 하이브리드 클라우드 위함, 내 컴퓨터와 VPC 결합
- 빠르게 구축 가능, 공용 인터넷을 통해 연결되기 때문에.... 대역폭, 보안 문제가 발생 할 수 도 있음
- 결국 `퍼블릭 인터넷`임
- 연결할때는 고객의 IDC에 customer gateway (`CGW`)가 반드시 필요함
  - 어쨋든 `퍼블릭 IP`꼭 있어야함 
- AWS에서는 VGW(`virtual private gateway`) 가 꼭 필요함




![Alt text](../../etc/image2/site-to-siteVPN.png)



- 서브넷의 VPC에서 `라우트 전파를 꼭 활성화` 시켜야 작동됨




![Alt text](../../etc/image2/site-to-siteVPN%EB%9D%BC%EC%9A%B0%ED%8C%85%EC%A0%84%ED%8C%8C.png)


-------------------------------------------
## AWS CloudHub

- 한 VPC에, 회사의 여러 데이터센터의 VPN 연결을 함
- `제품명이 아님` 걍 site-to-site VPN을 한 VPC에서, 여러개 만들면 됨
- `데이터 센터끼리 통신도 가능`

![Alt text](../../etc/image2/site-to-siteVPN%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%ED%97%88%EB%B8%8C.png)



<br>
<br>
<br>



-----------------------------------------
## AWS Direct Connect

- 기업 데이터 센터와 AWS AZ간에 `전용 연결선`을 생성
- `DX`라고도 부름
- VPC에 `VGW 설치해야됨`, `프라이빗 연결`
- 하이브리드 구성 가능 (온프레미스,클라우드)
- IPv4와 IPv6 지원 가능
- 설치에 `한달정도 걸릴수` 있음 -> 안빠름
  - 예)
    - 기업 데이터 센터에서 큰 네트워크 대역폭 (큰 데이터셋)을 필요로 할때 


![Alt text](../../etc/image2/DX.png)

- Direct Connect Gateway
  - 리전에(다른 리전 포함) `여러 VPC와 다이렉트로 연결`하고 싶을때 사용

![Alt text](../../etc/image2/DX%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4.png)



- Direct Connect 연결 타입
  - Dedicated connections (전용 연결)
    - 1, 10, 100 Gbps 대역폭 가능
    - AWS에서 `전용 회선을 깔아줌`
  - Hosted Connections (호스팅된 연결)
    - 50Mbps, 500Mbps, 1,2,5,10 ~ 100Gbps 대역폭 가능 
    - 필요하면 언제든 제거 해달라고 하면되고, 전용 회선보다는 유연함
  

- Hosted Connections:
  - Hosted Connections은 `공유 인프라`를 사용하여 AWS Direct Connect 서비스를 제공합니다. `AWS는 여러 고객이 공유하는 물리적 링크를 유지하고 관리`합니다. 이 연결 유형은 여러 고객이 같은 물리적 인프라를 공유하기 때문에 비용이 저렴합니다. 하지만 이는 `가용성과 대역폭 효율성에 일부 제약`이 있을 수 있습니다.

- Dedicated Connections:
  - Dedicated Connections는 `고객에게 전용 물리적 연결을 제공`합니다. 각 고객은 자체 물리적 링크를 보유하며, `이 연결은 고객 전용`입니다. Dedicated Connections은 고객이 전체 대역폭을 사용하고 최고의 성능과 가용성을 제공할 수 있도록 합니다. 이러한 연결은 고객이 고유한 물리적 경로를 갖게 되므로 보안과 성능에 대한 추가 제어를 제공합니다.

- 요약하면,`Hosted Connections는 공유 인프라를 사용하여 비용을 절감`하면서 연결을 설정하는 데 사용되며, `Dedicated Connections는 고객에게 전용 물리적 연결`을 제공하여 최고의 성능과 가용성을 보장합니다. 선택은 고객의 요구 사항과 예산에 따라 달라집니다.



- Direct Connect `암호화 기능이 없음` -> 어짜피 프라이빗 통신이기 때문에
  - 만약 암호화를 원한다면, VPN에서 제공하는 IPsec을 통해 암호화 가능


- Direct Connect - Resiliency (복원력)
  - 복원력을 높이기 위해, 여러 Direct Connect를 설치하는것이 좋다
  - 복원력을 최대로 올릴려면, Direct Connect 이중화 필수

![Alt text](../../etc/image2/DX%EB%B3%B5%EC%9B%90%EB%A0%A5.png)


--------------------------
## AWS Direct Connect + Site to Site VPN

- Direct Connect 2개 쓰면 좋겠지만, `비용이 많이듬`
- 그래서 `백업으로 Site to Site VPN`을 연결 아키텍쳐에 적합

![Alt text](../../etc/image2/DX+site.png)



-----------------------------------------------------
## AWS Transit GateWay

- 수천개의 `VPC 피어링, Site to Site VPN, Direct Connect`를 hub-and-spoke(star)별형 연결
- 연결에는 `VPC 피어링 할 필요가 없고`, `전이적으로 연결 가능`
- 즉, 이 서비스 이용하면, 모든 VPC에 접근 가능함
- 기본은 리전 리소스이며, `리전 안에서 작동`
  - 설정하면, `리전간 피어링도 가능`
- 다른 계정에서 AWS 리소스를 사용하려면, `Resuorce Access Manager(RAM)을 사용`
- Transit GateWay에 `자체 라우팅 테이블을 설정, VPC끼리 통신제어를 함`
- AWS 서비스중 유일하게, `IP Multicast` 기능 제공
  - `IP Multicast`는 IP 네트워크에서 `한 송신자가 여러 수신자에게 데이터를 전송하는 방법`입니다. 일반적으로 유니캐스트(Unicast)는 한 송신자가 한 수신자에게 데이터를 보내는 방식이며, 브로드캐스트(Broadcast)는 한 송신자가 모든 수신자에게 데이터를 보내는 방식입니다. 그러나 IP Multicast는 그 중간에 위치한 방식으로, 한 송신자가 관심 있는 그룹의 여러 수신자에게 데이터를 전송합니다.


- 사례)
  - Site-to-Site VPN 연결 대역폭을 `ECMP`를 사용해 늘림
    - `Site-to-Site VPN를 많이 생성해서, 패킷의 분산 통신 정도라고 생각`
    - ECMP는 Equal-Cost Multipath Routing(`다중 경로 라우팅`)의 약어입니다. ECMP는 네트워크에서 데이터 패킷이 여러 경로를 통해 전송되도록 하는 라우팅 알고리즘입니다. 이를 통해 네트워크 대역폭을 확장하고 링크의 부하를 균형있게 분산시킬 수 있습니다.


    - Site-to-Site VPN을 AWS Transit Gateway에 연결하면 기본적으로 `2개`의 VPN 터널이 생성됩니다. 이는 일반적으로 `고가용성을 위해 사용`되며, 각각의 터널은 별도의` IPsec 연결로 암호화되어 데이터를 전송`합니다.

    - 두 개의 VPN 터널은 동시에 사용되지만, 주로 하나의 터널이 활성화되고 `다른 하나는 대기 상태`로 유지됩니다. 터널 중 하나가 실패하거나 문제가 발생하면 다른 터널이 자동으로 활성화되어 연결을 유지합니다. 이를 통해 VPN 연결의 가용성과 내결함성이 향상됩니다.

    - 터널 하나당 `1.25Gbps`처리
    - Transit GateWay를 사용하면, 2터널이 뚫리므로, 2.5Gbps(ECMP)처리 가능


    - ![Alt text](../../etc/image2/%ED%8A%B8%EB%9E%9C%EC%A7%93%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4.png)

    - 만약, 2개의 Site-to-Site VPN을 생성하면? -> `터널 4개 생성`

    - ![Alt text](../../etc/image2/%ED%8A%B8%EB%9E%9C%EC%A7%93%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B42.png)
    - 터널 추가 밑, 기본 VGW
    - ![Alt text](../../etc/image2/%ED%8A%B8%EB%9E%9C%EC%A7%93%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B43.png)

    - 하지만... `돈이 비쌈`
  - Direct connect Gateway랑도 연동 가능

  - ![Alt text](../../etc/image2/%ED%8A%B8%EB%9E%9C%EC%A7%93%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B44.png)


------------------------------------------
## AWS VPC Traffic mirroring

- VPC에서 트래픽을 수집하고, 검사하되 `AWS 리소스가 방해되지 않는방식`
- ENI의 `source,target`을 정해 트래픽을 전체,필터링 해서 트래픽 분석 워크로드에 전송 할 수 있음
- `동일한 VPC 리소스`나 `다른 VPC 리소스도` 가능(피어링 되어있으면)
- 사례)
  - 콘텐츠 검사, 위협 모니터링 등

![Alt text](../../etc/image2/VPC%ED%8A%B8%EB%9E%98%ED%94%BD%EB%AF%B8%EB%9F%AC%EB%A7%81.png)



-----------------------------------------
## AWS VPC용 IPv6

- IPv4는 43억개 주소를 가짐 (부족)
- IPv6는 3.4 * 10^38 주소 제공
- IPv6에는 `사설 범위가 없음`, 다 퍼블릭임
- 형식은 8자리, 16진수 사용
  - 예) 
    - 2001:db8:3333:4444:5555:6666:7777:8888

- VPC와 서브넷에서 `IPv4는 비활성이 불가능함`
- IPv6는 활성화 가능하고, `활성화` 하면, Ec2인스턴스를 생성하면 -> `사설 IPv4 하나와, 공용 IPv6 하나를 얻음` (ipv6 ipv4 dual stack)
- `IPv6 IPv4 Dual Stack` 모드는 네트워크 장치나 시스템이 동시에 IPv6 및 IPv4 주소 체계를 지원하는 모드를 말합니다. 이 모드에서는 IPv6과 IPv4 주소 체계가 병렬로 동작하며, `네트워크 장치 및 시스템은 두 가지 IP 버전을 동시에 처리`할 수 있습니다.

- SAA문제) IPv6가 활성화된 VPC에서 Ec2를 생성했는데, 서브넷에서 Ec2를 실행 할 수 없다고 나오면? -> `Ec2가 Ipv6를 받지 못해서가 아님(Ipv6 주소는 너무 많기 때문에), 원인은 서브넷에 이용가능한 IPv4가 없기 때문임`


<br><br><br><br>

-------------------------------------
## AWS Egress-only internet GateWay - 송신 전용 게이트웨이


<br><br>

- `프라이빗 서브넷에 있는 Ec2 ipv6의 인터넷 아웃바운드` <-> 인터넷이랑 연결
- Nat Gateway랑 비슷하지만, `Ipv6트래픽만 사용됨`
- VPC에서 IPv6의 `아웃바운드를 연결`을 허용, `인바운드 아님!`
- `라우팅 테이블 업데이트 해야됨`



![Alt text](../../etc/image2/%EC%9D%B4%EA%B7%B8%EB%9E%98%EC%8A%A4%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B42.png)


![Alt text](../../etc/image2/%EC%9D%B4%EA%B7%B8%EB%A0%88%EC%8A%A4%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4.png)

<br><br><br><br>


---------------------------------------
## AWS 네트워크 비용

<br><br>

- 같은 AZ Ec2가 사설(private IP)로 통신할 시 `무료`
- 같은 리전, 다른 AZ 퍼블릭 IP 통신 0.02달러
- 같은 리전, 다른 AZ 프라이빗 IP 통신 0.01달러

![Alt text](../../etc/image2/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%B9%84%EC%9A%A91.png)


- `S3와 클라우드 프론트사이에서 데이터를 주고받는건 무료`


![Alt text](../../etc/image2/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%B9%84%EC%9A%A92.png)

- VPC 엔드포인트 이용해라, GB당, 0.01달러

![Alt text](../../etc/image2/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%B9%84%EC%9A%A93.png)

<br><br><br><br>

------------------------------------------
## AWS Network Firewall

<br><br>

- VPC를 보호를 위한 방화벽
- 3계층에서 7계층까지 보호
- `모든 방향(인,아웃), 모든 트래픽을 검사, 필터링`
- `여러 계정 or 여러 VPC에 적용 가능`
- 수천개의 규칙, 수만 IP나 Port를 필터링 가능
- `트래픽 허용,차단, 알림을 설정 할 수 있음`


![Alt text](../../etc/image2/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%B0%A9%ED%99%94%EB%B2%BD.png)

<br><br><br><br>

--------------------------------
## AWS PrivateLink

<br><br>

- AWS PrivateLink는 Virtual Private Cloud(VPC)와 지원되는 `AWS 서비스`,` 다른 AWS 계정에서 호스팅하는 서비스 및 지원되는 AWS Marketplace 서비스 간에 프라이빗 연결을 설정`
- 일종의 `VPC 인터페이스 엔드포인트` + `VPC 피어링` 등 상위버젼
- https://docs.aws.amazon.com/ko_kr/vpc/latest/userguide/endpoint-services-overview.html

![Alt text](../../etc/image2/VPC%ED%94%84%EB%9D%BC%EC%9D%B4%EB%B9%97%EB%A7%81%ED%81%AC.png)

<br><br><br><br>
