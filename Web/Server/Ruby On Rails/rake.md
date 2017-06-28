## Rake

Unix의 `make`와 같은 기능을 함.

소스코드에서 실행 가능한 프로그램 생성.

### 레일즈에서의 Rake

`rake db:migrate`

`rake test`

### 주의

Gemfile의 버전에 맞춰서 rake명령어를 실행해야하는 경우

`bundle exec rake db:migrate`

### 취소하기 / 롤백하기

```
rails g controller StaticPages home help
rails d controller Staticpages home help

rails db:migrate
rails db:rollback
rails db:migrate VERSION=0
```
