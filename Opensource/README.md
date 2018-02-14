# All of the opensources that I contributed

오픈소스를 이용해서 자라왔던 내가, 오픈소스에 공헌할 수 있다는 것은 크나큰 축복이며 영광이다.

## [Mastodon(5)](https://github.com/tootsuite/mastodon/commits?author=voidsatisfaction)

- Add Korean translation for inner mastodon page
- Fix streaming server url sensitive bug
- Debug Smartphone screen button not showing
- Add report letters validation
- Add new screen for pinned toots

## [Boostnote(4)](https://github.com/BoostIO/Boostnote/commits?author=voidsatisfaction)

- Add Korean translation for debug and developement docs
- Add right click notelist delete
- Enable not focused note right click pin to top and show right context menu
- Add multiselect notes delete and move and pin function(manipulating react state and using promise.all)

## [Golang-spec](https://github.com/golangkorea/golang-spec/commits?author=voidsatisfaction)

Translation

- string-types
- array-types

## [Hatena-Textbook](https://github.com/hatena/Hatena-Textbook/commits?author=voidsatisfaction)

While doing new employee training, I fixed typos and invalid expression of textbook of Hatena

# Opensource Guide

오픈 소스 활동을 처음 시작하는 분들을 위하여

## [네이버 오픈소스 가이드](https://naver.github.io/OpenSourceGuide/book/)

오픈 소스 활동하기 전에 알아두면 좋은 내용들을 담은 책. 무턱대고 기여하려고 하면 어디서부터 어떻게 해야할지 모르기때문에 이 자료를 읽고 시작하는것을 권합니다. 오픈소스에대해서 매우 잘 다루고있는 짧은 분량의 책입니다.

# Opensource Problem solving

Golang-spec에서는 번역에 대한 이슈를 처음에는 `gitbook`, `gitter(채팅방)`, `github issue` 세군데에서 올릴 수 있게 했었다. 풀리퀘스트도 바로바로 머지되어서 만일 번역자가 다른 채널에서 번역에 대한 피드백을 받으면 새로 풀리퀘스트를 다시 만들어야 하는 업무적 중복이 발생했다. 이는 개발자의 반복된 업무로 번역 의욕을 떨어뜨리고 작업 효율도 좋지 못했다.

내가 제안한 방법은 일반적인 opensource의 관리처럼, 리뷰어를 여러 사람 만들어놓고, 리뷰어의 일부(예를들어 두명)이 approve하면 그 때 번역을 merge하도록 하고, 번역에 대한 문제제기는 issue로 관리할 수 있도록 하는 것이었다.

이렇게 하므로써, 번역이 반영되는 phase가 투명해지고, 복수의 리뷰어를 두므로써 리뷰어의 업무량도 경감시킬 수 있고, 번역자는 자신의 번역을 꼼꼼하게 확인하게 된다.

번역 그자체를 하는 것도 중요하지만, 번역을 효율적으로 하는 구조(process)를 만드는 것 역시 중요하다.
