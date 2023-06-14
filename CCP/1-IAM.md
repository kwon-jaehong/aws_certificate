IAM 왜쓰나?
AWS에서는 각 iam 유저,그룹 등 최소권한만을 부여해 개발하는것을 권장한다.
---------
IAM 정책
json 문서형태고, 유저나 그룹에 적용 할 수 있다.

IAM 정책 JSON 구조



일단 아래 샘플
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

version : 정책의 언어 버젼, 거의 2012-10-17이 고정임 <br>
id (옵션): 정책의 ID <br>
statement (필요) : 설명서? 걍 description이라고 생각하면 될듯, LIST 형식이라 하나, 또는 여러가지 작성 가능함 <br>

<br><br><br>
https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/reference_policies_elements_resource.html

statement의 속성들 <br>
sid (옵션) : statement의 ID, 구별하려고 쓰는것이기에 아무값이나 넣거나 안써도 됨 <br>
Effect (필요) : 설명하는 기능을 허락할지, 금지 시킬지 하는 내용 
Allow,Deny 둘중 하나의 값만 가능 <br>
principal (옵션 또는 ??? 모르것네) : 이 정책이 적용된 계정/사용자/역할. <br>

action (필요) : 이 정책이 허용하거나 거부하는 작업 목록입니다.(API 호출 목록)<br>
Action 요소는 특정 작업의 허용 또는 거부 여부를 지정합니다


Resuorce (필요) : 위 Effect에서 설정한(허락 또는 금지)에 대한 자원 리소스들을 명시한 내용 <br>
condition (옵션) : 이펙트에 대한 컨디션 -> 언제 적용될지 현재 여기는 안배워도 됨


--------------------------------

IAM 암호 정책 password policy
<br><br>

AWS 방어 메커니즘 <br>
1. 강력한 암호 설정이 가능하도록, 마스터가 IAM에서 계정을 발급할때, 옵션을 줄 수 있음 (총 비밀번호는 21자리, 특수키 3개, 대문자 3개, 소문자 3개를 조합해라 -> 설정) <br> 또한 유효기간 비번 설정, 동일한 비번 금지 등 마스터 설정에 따라 구성 가능

![Alt text](../etc/image/%EC%95%94%ED%98%B8%EC%A0%95%EC%B1%851.png)


2. MFA - multi factor authentication 다중 인증 장치를 사용
AWS에서는 가상 MFA 디바이스가 있음 (Authy), 휴대용 저장 장치를 이용한 U2f(universal 2nd factor) security key도 있음
gemalto, surepassid, yubico 등 여러 가지 있음

![Alt text](../etc/image/%EC%95%94%ED%98%B8%EC%A0%95%EC%B1%852.png)







--------------------------------------------------
AWS에 접근하는 방법은 3가지 이다.

1. 웹상의 AWS 메니져 콘솔
2. aws cli (엑세스키, 시크릿키 설정으로 접근 가능)
3. aws sdk (이것도 엑세스키, 시크릿키로 접근 가능) -> python의 boto3 등 코딩을 통해 소프트웨어 속에 심어져 있는 것

엑세스키 = 유저네임
시크릿키 = 패스워드 라고 생각 하면 될듯


----------------------------------
Role

정책은 Iam 유저에 대한 것이고, Role(역할)은 
AWS의 어떠한 서비스에 IAM 권한을 부여한 것이다?
실제 사람이 사용하도록 만들어진 것이 아니고, AWS의 특정 서비스에 의해 사용되도록 만들어졌다.
예를들어 ec2를 만들엇고, s3에 연결하기 위해서는 ec2 인스턴스에 권한을 s3관련 권한을(iam role) 부여해야 한다.

role은 aws가 개체에 짧은 기간동안 자격증명을 허용해서 원하는 작업을 수행 할 수 있게 한다.


자 예를 들어
t3 미디엄 ec2 한대를 띄어놓았고, 접속해서 aws cli를 깔고, aws configure를 설정했다고 치자,
이제부터 이 ec2 인스턴스는 누구든 접속하면 aws configure 정보를 볼 수 있게 된다.

ec2에 역할을 하는 방법은 ec2 선택-> 작업 -> 보안 -> iam 역할 수정 하면된다


--------------
IAM 보안 도구

1. iam credentials report (자격증명 보고서 ) - 계정 레벨
2. IAM access advisor - 유저 레벨
2는 유저를 클릭하고, 액세스 관리자를 클릭하면, 그사람이 마지막으로 사용한 서비스 목록들을 볼 수 있다.

-----------------
root 계정은 되도록 사용하지 마라!


--------------
AWS 공동 책임 모델
AWS는 인프라, 구성과 분석 서비스에 대해 책임

내 책임
키를 자주 교체, MFA 사용, 유저,그룹 역할을 매니징하는 것은 내책임
계정 권한 검토도 내책임



