
## AWS KMS (Key Management service)

- 클라우드트레일을 통해 키사용 API 호출 다 볼 수 있음
- KMS도 교차계정 접근 지원함

- KMS는 키 캐싱이 되므로, 자주 암호화 하면... 같은키를 사용한다
  - LocalCryptoMaterialsCache를 사용하여, 캐싱 시간을 정할 수 있다.


-----------

## AWS KMS 봉투 암호화

- 왜씀? -> KMS 암호화는 데이터를 암호화 하는데 `4KB 용량 제한이 있음` 
- `GeneratedataKey API를 씀`
- `데이터 키, 암호화된 데이터 키 2가지를 받고`, 클라이언트 측에서 큰 데이터 암호화를 함
- 복호화는 암호화된 데이터를 먼저하고, 클라이언트에서 데이터키로 컨텐츠 복호화 함

![Alt text](../etc/image3/kms_%EC%95%94%ED%98%B8%ED%99%941.png)

![Alt text](../etc/image3/kms_%EC%95%94%ED%98%B8%ED%99%942.png)


-------------------------

## AWS KMS 제한

- AWS 소유 & 관리키를 사용하지 않으면 KMS 초당 API 콜 제한이 있음
  - API콜 초과를 하면 `ThrottlingExption` 에러 발생
  - 지수 백오프 전략을 사용해서 완하 할 수 있음
- `암호화 / 복호화 API콜 횟수 할당량을 함께 씀`
- 

















































































































