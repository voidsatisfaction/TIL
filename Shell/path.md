# PATH

## PATH란

어떤 디렉토리에 위치해 있던지 상관 없이 PATH에 지정된 디렉토리에 있는 파일에 접근할 수 있도록 도와준다.

## PATH의 사용

기존에 있던 PATH의 맨 앞에 `/usr/local/go/bin`을 추가하는 경우

```sh
# 관리자 권한이 있는 경우 go path지정
export PATH=/usr/local/go/bin:$PATH

# 관리자 권한이 없는 경우 go path지정
export PATH=$HOME/go/bin:$PATH
```

PATH에서 각 값을 구분하는 것은 콜론(:)이다.

```sh
cho $PATH
```

```sh
/opt/local/bin:/opt/local/sbin:/Users/admin/Library/Enthought/Canopy_64bit/User/bin:/Users/admin/.rvm/gems/ruby-2.3.1/bin:/Users/admin/.rvm/gems/ruby-2.3.1@global/bin:/Users/admin/.rvm/rubies/ruby-2.3.1/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/go/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands:/Applications/Wireshark.app/Contents/MacOS:/Users/admin/.rvm/bin
```
