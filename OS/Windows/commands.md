# 윈도우 CMD환경에서 자주 사용하는 커맨드

위는 Windows cmd커맨드 아래는 그에 대응하는 linux 커맨드

- `DIR`
  - `ls`
- `CD`
  - `cd or pwd`
- `TYPE`
  - `cat`
- `RMDIR (directory name) /s /q`
  - `rm -rf (directory name)`
- `DEL /f (filename)`
  - `rm (filename)`
- `SET VAR1=ABC`
  - `export VAR1=ABC`
- `START /B program`
  - `program &`
- `NETSTAT`
  - `netstat (-ano)`
- `TASKKILL /pid (process id)`
  - `kill -9 (pid)`
- `COPY (source file) (destination)`
  - `cp (source file) (destination)`
- `XCOPY /e /h /k (source folder) (destination\source folder name)`
  - `cp -r (source folder) (destination)`
- `echo`
  - `echo`
- `%환경변수이름%`
  - `$환경변수이름`
- `services.msc`
  - 윈도우 서비스(유닉스의 데몬과 유사) 관리 윈도우 띄움
