# Today I Learned

voidSatisfaction이 오늘 새로 배운 것을 다음의 규칙으로 commit 합니다. [thoughtbot til 참고](https://github.com/thoughtbot/til)

## 기술되는 내용
- 나무보다 숲을 알 수 있는 내용.
- 다른 사람들이 봤을때도 알기 쉽도록 **지나친 추상화는 되도록 피한다.**

## 작성 규칙
- 문서 생성은 [GFM (Github Flavored Markdown)](https://help.github.com/articles/github-flavored-markdown/) 을 사용한다. (확장자 `.md`)
- 언어나 기술명으로 폴더를 만든다. (root에 문서를 만들지 않는다.)
- 파일명은 영어로.

## 로컬에서 띄우기
[gollum](https://github.com/gollum/gollum), [pow](http://pow.cx/) 와 [anvil](http://anvilformac.com/)을 사용한다.

### gollum 설치
```bash
$ [sudo] gem install gollum
```

### pow 설치 및 제거
```bash
$ curl get.pow.cx | sh

$ curl get.pow.cx/uninstall.sh | sh
```
*pow가 global루비 버전을 제대로 인식하지 못할 경우에는 `~/.powconfig`를 이하와 같이 설정해준다.*
```sh
# 루비 위치에 대한 환경 변수 설정 / rbenv에 존재하는 현 루비 버전의 위치(global)
export PATH="/Users/tech-camp-064/.rbenv/versions/2.3.1/bin:$PATH"
```

### 사용법
다음 설정을 하고 브라우저에서 [http://til.wiki.dev/](http://til.wiki.dev/)로 접속한다.

```bash
$ cd ~/.pow
$ ln -s path/to/this_local_repo til.wiki
```

### Anvil 설치
GUI pow 관리툴 Anvil [http://anvilformac.com/](http://anvilformac.com/)

**Special thanks to [milooy](https://github.com/milooy)**
