# Vagrant에서 움직이는 DB를 gui툴로 확인

## 참고

- [vagrant上のmysqlにSequelProで接続する](https://qiita.com/caramelbit/items/7c2eb518d93060fe25a5)
- [SequelProからVagrant内のMySQLへアクセスする](https://qiita.com/ozw_sei/items/1c9c4e8b6c66ccd960d9)

## 방법

Mysql의 SequelPro의 경우

```
MySQL host：127.0.0.1
username：mysqlに追加したユーザー名
password：mysqlに追加したパスワード
port：3306(open to vagrant)

SSH host：127.0.0.1
SSH user：vagrant
SSH password：vagrant
SSH port：2222
```

위와같이 설정한 후 ssh로 연걸하기로 들어감
