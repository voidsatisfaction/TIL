# psql

- 의문
- 꿀 쿼리

## 의문

## 꿀 쿼리

- `psql -h postgres -U postgres`
  - postgre db에 host가 postgre, user가 postgres인 계정으로 접속
- `\l`
  - 모든 데이터베이스를 리스트 업
- `\connect database_name`
  - database_name 데이터베이스에 연결
- `\dt+`
  - 접속한 database의 table을 listup(size포함)
- `0 0 * * 0 pg_dump -U postgres dbname > ~/postgres/backups/dbname.bak`
  - 백업파일을 생성하는 쉘 스크립트 크론탭 설정
  - 더 발전된 설정
    - TODAY=`date +"%Y%m%d"`
    - docker exec dental_web_postgres_1 pg_dump -U postgres > ~/dental_clinical.${TODAY}.bak
      - 오늘 날짜로 백업 파일을 생성
- `\x on`
  - 데이터를 1레코드마다 더 이쁘게 출력(알아보기 쉬움)
