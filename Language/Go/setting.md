# Go tool Setting

- 참조: [golang - 공식 홈페이지](https://golang.org/doc/code.html#GOPATH)

## 0. 사전 지식

### 개요

- Go 프로그래머들은 모든 Go code를 workspace라는 하나의 공간에 저장한다.
- 한 workspace는 다양한 버전 컨트롤된 repository를 갖는다.
- 각각의 repository는 하나나 그 이상의 packages를 포함한다.
- 각각의 package는 하나나 그 이상의 Go source files를 하나의 디렉토리에 갖는다.
- package directory로의 path는 그 import path를 결정한다.

다른 언어가 각각의 project는 분리된 workspace와 version control을 갖는것과는 매우 대조된다.

### Workspace

하나의 workspace는 다음과 같은 디렉토리 계층을 갖는다.

- `src`: Go source files의 모음
- `pkg`: Package objects의 모음
- `bin`: Executeable commands의 모음

아래는 실제의 예시

```
bin/
    hello                          # command executable
    outyet                         # command executable
pkg/
    linux_amd64/
        github.com/golang/example/
            stringutil.a           # package object
src/
    github.com/golang/example/
        .git/                      # Git repository metadata
	hello/
	    hello.go               # command source
	outyet/
	    main.go                # command source
	    main_test.go           # test source
	stringutil/
	    reverse.go             # package source
	    reverse_test.go        # test source
    golang.org/x/image/
        .git/                      # Git repository metadata
	bmp/
	    reader.go              # package source
	    writer.go              # package source
    ... (many more repositories and packages omitted) ...
```

위의 tree는 두 repositories(example, image)를 포함하는 하나의 workspace를 나타낸다. `example` repo는 두개의 커맨드를 포함한다(`hello`, `outyet`) 그리고 하나의 library(`stringutil`)를 포함한다. `image` repo는 bmp package와 여러 다른 것들을 포함한다.

하나의 workspace에는 많은 소스 많은 packages와 commands를 표함하는 source repos를 포함한다. 대부분의 Go 프로그래머는 모든 Go 소스들과 dependency를 하나의 workspace에 보존한다.

### GOPATH

GOPATH 환경 변수는 workspace의 위치를 특정한다. 초기설정으로는 `$home/go`로 되어있다. 이를 바꾸고 싶으면 `bash_profile`등에 새로 정의한다.

```sh
# 예시 .bash_rc(or .bash_profile)
export GOPATH=$HOME/work/go # working directory를 지정
export PATH=$PATH:$(go env GOPATH)/bin # 편의를 위해 설정
```

### Import paths

import path란 package를 unique하게 식별하는 문자열이다.

standard library의 packages는 `fmt`나 `net/http`와 같이 짧은 import path가 주어진다.

Github와 직접적으로 연동시키지 않는다고 하더라도, `$GOPATH/src/github.com/user`과 같이 놓고 앞으로 publish할것같이 go코드를 작성하는 것이 좋다.

## 1. Install Homebrew

## 2. `brew install go`

## 3. Setup path

```sh
# .bash_rc(or .bash_profile)
export GOPATH=$HOME/work/go # working directory를 지정
export PATH=$PATH:$(go env GOPATH)/bin # 편의를 위해 설정
```

## 4. 명령 도구 설치

```sh
go get golang.org/x/tools/cmd/... # GOPATH에 지정되어있는 workspace에 모든 go명령 도구들을 다운로드한다.
go get golang.org/x/tools/cmd/goimports # GOPATH에 지정되어있는 workspace에 goimports의 도구들을 다운로드 한다.
```

## 5. 간단한 실행(script)

`go run hanoi.go`

이 명령어는 어떠한 디렉토리에서도 작동 가능하다.

## 6. 파일의 설치(install)

`go install github.com/voidsatisfaction/gogo/hanoi`

이후 workspace의 `bin`에 hanoi가 저장된다.

`$GOPATH/bin`에 들어가서 `./hanoi`로 실행 가능하다.

## 7. 각종 도구의 설치

편집기에는 반드시 `gofmt`를 설치 한다.

`goimport`도 설정한다.
