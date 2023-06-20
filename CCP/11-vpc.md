## CLF 수준의 VPC 

- `CLF 수준에서는 별로 안중요함`


- VPC, 서브넷, 인터넷게이트웨이, NAT 게이트웨이
보안그룹, NACL, vpc 피어링, vpc 엔드포인트, vpc direct connect
transit gateway 중
- 1,2 문제 정도 출제됨

-------------
## AWS VPC
- VPC는 기본적으로 `리전`에 개설됨, 여러 리전에 생성했으면 VPC는 여러개임
- 퍼블릭,프라이빗 서브넷을 생성 할수있고, `AZ`에 종속적임

<br>

`인터넷게이트웨이` <br>
- VPC 전체 에서 인터넷 연결구


<br>

`NAT gateway` <br>
프라이빗 서브넷에 있는 컴퓨터들이 인터넷 하고싶을때 퍼블릭 서브넷에 있는 게이트웨이(`인스턴스임`)


<br>
<br>

-----------------------------
## AWS Network access control list - NACL 네트워크 엑세스 컨트롤

- 서브넷에서 먼저 받고, EC2에 전달함
- 보안그룹은 `Ec2 자체에 새워진 방화벽`임
- NACL은 `서브넷 수준`이고, 보안그룹은 `Ec2 수준`임
- 보안그룹은 `허용만 가능`하고
- NACL은 `허용과 거부를 할 수` 있음
- 보안그룹은 리턴 트래픽이 있어서 stateful하다라고 봄
- NACL은 거부당하면 리턴 트래픽이 없어서 stateless라고 함

<br>
<br>

----------------------------
## AWS VPC flow logs

- 인터페이스를 통과하는 모든 IP 트래픽의 로그
- VPC, 서브넷, 엘라스틱 네트워크 인터페이스 등 EC2인스턴스에 들어오고 나가는 모든 트래픽을 확인가능
- `네트워크에 관련된 문제들을 확인 할 수` 있음
- 로그들은 s3 , 클라우드 워치로 로그 보낼 수 있음

<br>
<br>
<br>

---------------------------
## AWS vpc peering

- vpc 2개를 연결해서 동일한 네트워크처럼 사용 
- 이를 위해 CIDR 이 겹치지 않도록 해야됨 -> `겹치면 연결 못함`
- 피어링은 전이적이지 않음 예) A - B, A - C 연결했으면,  B - C는 통신 안됨

![Alt text](../etc/image/vpc%20%ED%94%BC%EC%96%B4%EB%A7%81.png)

<br>
<br>
<br>

-------------------------------
## AWS VPC EndPoint

- 프라이빗 서브넷에 존재하는 EC2들이 AWS 서비스를 이용하기 위해 사용(비공개 연결)
-  AWS 서비스는 인터넷을 통해 액세스되며, VPC 내에서도 인터넷 게이트웨이나 NAT 게이트웨이를 사용하여 인터넷과 통신할 수 있습니다. 그러나 보안 및 개인 정보 보호 요구 사항이 있는 경우에는 VPC endpoint를 사용하는 것이 좋습니다.
- 왜 씀?  -> 보안
  

<br>

`vpc endpoint gateway`
- 오직 s3와 다이나모DB전용임
- 서브넷에 VPC 엔드포인트용 게이트웨이를 따로 생성함

<br>
<br>

`vpc endpoint interface`
- AWS 서비스 다 쓸 수 있음
- VPC 엔드포인트용 인테넷카드 (ENI)를 통해 통신함

<br>

![Alt text](../etc/image/%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8.png)

<br>
<br>
<br>



----------------------
## AWS site to site VPN
- 하이브리드 클라우드 위함, 내 컴퓨터와 VPC 결합
-  빠르게 구축 가능, 공용 인터넷을 통해 연결되기 때문에.... 대역폭, 보안 문제가 발생 할 수 도 있음
- 결국 `퍼블릭 인터넷`임
- 연결할때는 고객의 IDC에 customer gateway (CGW)가 반드시 필요함
- AWS에서는 VGW(virtual private gateway) 가 꼭 필요함
- 이 두 게이트웨이를 site to site vpn으로 연결 하는 것

<br>
<br>

![Alt text](../etc/image/site-to-site%20vpn.png)

<br>
<br>
<br>

---------------------------
## AWS Direct Connect

- 회사 컴퓨터와 AWS와 전용회선으로 통신함 (사설 네트워크 구축 가능)
- `구축되는 기간 오래걸림(한달)`, 졸 비쌈 (`전용회선 깔아야함`)

<br>
<br>


![Alt text](../etc/image/%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8%EC%BB%A4%EB%84%A5%ED%8A%B8.png)

<br>
<br>
<br>

`site to site VPN 와 AWS Direct Connect CLF 문제 요점`
- 첫 번째는 사설 네트워크인지 이고, 두번째는 빠른 구축이 가능하냐를 물어봄



<br>
<br>
<br>

--------------------------

## AWS Transit gateway

- VPC의 허브 및 스포크 형태로, `수천개의 vpc와 온프레미스 시스템간의 피어링`을 설정

![Alt text](../etc/image/%ED%8A%B8%EB%9E%9C%EC%8B%9D%EA%B2%8C%EC%9D%B4%ED%8A%B8%EC%9B%A8%EC%9D%B4.png)


















