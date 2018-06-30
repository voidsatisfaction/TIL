# 데이터베이스 인덱스와 키

## 인덱스를 지정 하면

- 데이터베이스 내부에 인덱스 트리를 생성
- 삽입할 때 마다, 데이터 베이스의 행 뿐 아니라, 인덱스 트리도 갱신
- 유저의 유스케이스에 맞춰서 지정하는 경우가 많음
  - e.g 북마크 엔트리의 변경 로그를 찾을 경우, `entry_id`와 `createdAt`을 키로 지정함
- 키 지정은 순서가 있음
  - `KEY entry_log (created, entry_id)`
    - 일정 시간동안에서의 다양한 엔트리의 변경 로그를 탐색하고 싶음
  - `KEY entry_log (entry_id, created)`
    - 어떠한 특정 엔트리의 로그를 생성된 순서로 보고 싶을때

## 장점

- 인덱스를 바탕으로 행을 찾을 때 빠르게 할 수 있다.
- 인덱스를 바탕으로 한 정렬도 빨라진다.

## 단점

- 무분별하게 인덱스를 만들어버리면, 삽입, 삭제, 갱신시에 속도가 매우 느려지게 된다.
  - 단순히 데이터베이스 행 뿐 아니라, 인덱스 트리 안의 내용 도 갱신 해야 하므로

```sql
DROP TABLE IF EXISTS `entry_title_log`;
CREATE TABLE `entry_title_log` (
  `id` BIGINT UNSIGNED NOT NULL,
  `entry_id` BIGINT UNSIGNED NOT NULL,
  `user_id` BIGINT UNSIGNED NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `entry_log` (`entry_id`, `created`)
) ENGINE=InnoDB DEFAULT CHARSET=utf9mb4 ROW_FORMAT=DYNAMIC;
```
