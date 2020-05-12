# 윈도우 CMD환경에서 자주 사용하는 커맨드

위는 linux 커맨드 아래는 그에 대응하는 윈도우 커맨드

아래의 첫번째 커맨드: Powershell 커맨드
아래의 두번째 커맨드: Windows CMD

- `ls`
  - `ls`
  - `DIR`
- `cd or pwd`
  - `cd`
  - `CD`
- `cat`
  - `cat`
  - `TYPE`
- `rm -rf (directory name)`
  - ?
  - `RMDIR (directory name) /s /q`
- `rm (filename)`
  - ?
  - `DEL /f (filename)`
- `export VAR1=ABC`
  - ?
  - `SET VAR1=ABC`
- `program &`
  - ?
  - `START /B program`
- `netstat (-ano)`
  - ?
  - `NETSTAT`
- `kill -9 (pid)`
  - ?
  - `TASKKILL /pid (process id)`
- `cp (source file) (destination)`
  - ?
  - `COPY (source file) (destination)`
- `cp -r (source folder) (destination)`
  - ?
  - `XCOPY /e /h /k (source folder) (destination\source folder name)`
- `echo`
  - ?
  - `echo`
- `$환경변수이름`
  - ?
  - `%환경변수이름%`
- 윈도우 서비스(유닉스의 데몬과 유사) 관리 윈도우 띄움
  - ?
  - `services.msc`
