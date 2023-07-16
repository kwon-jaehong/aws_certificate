## IAM 왜쓰나?

<br>

-> AWS에서는 각 iam 유저,그룹 등 최소권한만을 부여해 개발하는것을 권장한다.

<br>


---------
## IAM policy

<br>

-> json 문서형태고, 유저나 그룹에 적용 할 수 있다.

<br>


IAM 정책 JSON 구조
``` json
{
    "Version": "2012-10-17",
    "Id": "IAM-READ-Permissionsssssssss"
    "Statement": [
        {
            "Sid" : "몰러",
            "Effect": "Allow",
            "Action": [
                "iam:GenerateCredentialReport",
                "iam:GenerateServiceLastAccessedDetails",
                "iam:Get*",
                "iam:List*",
                "iam:SimulateCustomPolicy",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```
<br>

- version : 정책의 언어 버젼, 거의 2012-10-17이 고정임 <br>
- id (옵션): 정책의 ID <br>
- statement (필요) : 설명서? 걍 description이라고 생각하면 될듯, LIST 형식이라 하나, 또는 여러가지 작성 가능함 <br>

- statement의 속성들 <br>
    - sid (옵션) : statement의 ID, 구별하려고 쓰는것이기에 아무값이나 넣거나 안써도 됨 <br>
    - Effect : 설명하는 기능을 허락할지, 금지 시킬지 하는 내용 
Allow,Deny 둘중 하나의 값만 가능 <br>
    - principal : 이 정책이 적용된 계정/사용자/역할. <br>

    - action : 이 정책이 허용하거나 거부하는 작업 목록입니다.(API 호출 목록)<br>
- Resuorce (필요) : 위 Effect에서 설정한(허락 또는 금지)에 대한 자원 리소스들을 명시한 내용 <br>
- condition (옵션) : 이펙트에 대한 컨디션 -> 언제 적용될지 현재 여기는 안배워도 됨

<br>
<br>
<br>

참고 : https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_elements_resource.html


<br>

--------------------------------


IAM password policy - IAM 암호 정책 

<br><br>

AWS 방어 메커니즘 <br>
1. 강력한 암호 설정이 가능하도록, 마스터가 IAM에서 계정을 발급할때, 옵션을 줄 수 있음 (총 비밀번호는 21자리, 특수키 3개, 대문자 3개, 소문자 3개를 조합해라 -> 설정) <br> 또한 유효기간 비번 설정, 동일한 비번 금지 등 마스터 설정에 따라 구성 가능

![Alt text](../etc/image/%EC%95%94%ED%98%B8%EC%A0%95%EC%B1%851.png)

<br>
<br>
<br>
<br>
<br>
<br>

2. MFA - multi factor authentication 다중 인증 장치를 사용
AWS에서는 가상 MFA 디바이스가 있음 (Authy), 휴대용 저장 장치를 이용한 U2f(universal 2nd factor) security key도 있음
gemalto, surepassid, yubico 등 여러 가지 있음

![Alt text](../etc/image/%EC%95%94%ED%98%B8%EC%A0%95%EC%B1%852.png)




<br>
<br>
<br>

--------------------------------------------------

<br>

## AWS에 접근하는 방법은 3가지 이다.

<br>
<br>

1. 웹상의 AWS 메니져 콘솔
2. aws cli (엑세스키, 시크릿키 설정으로 접근 가능)
3. aws sdk (이것도 엑세스키, 시크릿키로 접근 가능) -> python의 boto3 등 코딩을 통해 소프트웨어 속에 심어져 있는 것

엑세스키 = 유저네임
시크릿키 = 패스워드 라고 생각 하면 될듯


----------------------------------
## IAM Role - IAM 역할

`정책은 Iam 유저에 대한 것이고, Role(역할)은 
AWS의 어떠한 서비스에 IAM 권한을 부여한 것이다
`

<br>

실제 사람이 사용하도록 만들어진 것이 아니고, AWS의 특정 서비스에 의해 사용되도록 만들어졌다.

<br>

예를들어 ec2를 만들엇고, s3에 연결하기 위해서는 ec2 인스턴스에 권한을 s3관련 권한을(iam role) 부여해야 한다. role은 aws가 개체에 짧은 기간동안 자격증명을 허용해서 원하는 작업을 수행 할 수 있게 한다.


자 예를 들어, t3 미디엄 ec2 한대를 띄어놓았고, 접속해서 aws cli를 깔고, aws configure를 설정했다고 치자,
이제부터 이 ec2 인스턴스는 누구든 접속하면 aws configure 정보를 볼 수 있게 된다. ec2에 역할을 하는 방법은 ec2 선택-> 작업 -> 보안 -> iam 역할 수정 하면된다


<br>
<br>
<br>

--------------
## IAM 보안 도구

1. IAM credentials report (자격증명 보고서 ) - 계정 레벨
-> 계정에 언제 접속했는지, 패스워드는 언제바꿧는지, MFA사용여부, 비밀번호 만기 여부 등 마지막 접속 정보


![Alt text](../etc/image/%EC%9E%90%EA%B2%A9%EC%A6%9D%EB%AA%85%EB%B3%B4%EA%B3%A0%EC%84%9C1.png)

![Alt text](../etc/image/%EC%9E%90%EA%B2%A9%EC%A6%9D%EB%AA%85%EB%B3%B4%EA%B3%A0%EC%84%9C2.png)

<br>
<br>
<br>
<br>
<br>

2. IAM access advisor -> 유저 레벨
유저를 클릭하고, 액세스 관리자를 클릭하면, 그사람이 마지막으로 사용한 aws 서비스 목록들을 볼 수 있다.

![Alt text](../etc/image/IAM%EC%9C%A0%EC%A0%80%EC%97%91%EC%84%B8%EC%8A%A4%EA%B4%80%EB%A6%AC%EC%9E%90.png)


<br>
<br>

### 추가
AWS IAM Access Analyzer - IAM 엑세스 분석기
![Alt text](../etc/image/IAM%EC%97%91%EC%84%B8%EC%8A%A4%EB%B6%84%EC%84%9D%EA%B8%B0.png)

IAM Access Analyzer를 사용하면 AWS 계정에서 사용자, 역할, 그룹 등의 엑세스 권한을 검토하고, 잠재적인 보안 위험 요소나 규정 준수 위반 사항을 식별할 수 있습니다. 이를 통해 AWS 리소스에 대한 권한 부여 및 액세스 제어를 강화할 수 있습니다.

<br>
<br>

---------------

## AWS 공동 책임 모델

<br>

- AWS는 인프라, 구성과 분석 서비스에 대해 책임

<br>

고객 책임
- 키를 자주 교체, MFA 사용, 유저,그룹 역할을 매니징하는 것은 내책임
- 계정 권한 검토도 내책임




-----------------

## IAM관련 추가적인 내용

- root 계정은 되도록 사용하지 마라!
- root 사용할꺼면 적어도 MFA는 적용해라

<br>
<br>
