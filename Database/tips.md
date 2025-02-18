# 데이터 베이스 알아두면 좋은 팁

- MYSQL 문자열 문제
-

## 1. MYSQL 문자열 문제

펄(perl)과 같은 문자열과 숫자의 구분이 애매한 동적 타입 언어와 같은 경우에는, 데이터 베이스를 조작할때 문자면 문자, 숫자면 숫자의 구분을 명확히 할 필요가 있다.

예를들어 펄에서`mysql_client->get_article(article_id)`와 같은 API가 있다고 하면, article_id가 숫자로 해석되어서 인자로 넘겨지면 원하는 대로 동작하나, 만약 문자열로 해석이 되어서 인자로 넘겨지면, MYSQL은 데이터베이스의 모든 article_id행의 값들을 문자열로 변형하고 하나하나 대조한다. 이는 불필요한 자원을 소비하게 만드므로 반드시 `$c->req->positive_int_param`과 같은 데이터 형이 분명하게 정해진 validation이 있는 메서드를 사용하는 것이 바람직하다.

## 2. 배치프로그램에서 Bulk insert를 할 시에 쿼리 패킷 사이즈 문제

- mysql에는 `max_allowed_packet`설정이 있음
  - 서버 클라이언트 둘다 해당 설정을 갖고있음
  - AWS RDS가장 작은 친구는 4MB정도였음
- 만일, 대량의 bulk insert를 하게 된다면 해당 크기의 설정은 매우 부족함
  - 값을 충분히 넓혀줄 필요가 있음
- `show variables where Variable_name LIKE "max_allowed%` 와같이 확인 가능
