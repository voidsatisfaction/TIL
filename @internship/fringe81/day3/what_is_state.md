# What is state

## 辞書的定義

事物が、その時にそうなっている、ありさま。特に、外面からでもそれとわかる様子

## Programに置けるstate

Preceding eventsやuser interactionsなど、記憶された情報がstateである（それを記憶しているプログラムはStateful Program）その例としては、variableの活用がある。

プログラミングのパラダイムの視点からは以下の通りである。

- Imperative Programmingの場合、stateにprogrammingのstateを変化させるstatementを加えて、新しいstateを作り出すプログラミング方法である。
- Declarative Programmingの場合、desired resultをそのままプログラムに書くことでstateの明確な変更方法を意識しなくて良い。

## Serial Programmingにおけるstate

Stateful protocolとは、加工される以前のデータの情報(meta data)をどこかにsaveして置いて、現在のデータを加工するために使用する方法論をさす。

Stateless protocolとは、プログラムは加工される以前のinputに対するデータなしに、データを加工することを言う。

## Stateをどう考えるのか

### 参考

- [決定性有限オートマトン](https://ja.wikipedia.org/wiki/%E6%B1%BA%E5%AE%9A%E6%80%A7%E6%9C%89%E9%99%90%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3)
- [有限オートマトン](https://ja.wikipedia.org/wiki/%E6%9C%89%E9%99%90%E3%82%AA%E3%83%BC%E3%83%88%E3%83%9E%E3%83%88%E3%83%B3)

### 結論

stateの抽象度を考えるべきである。Aというアプリが存在するとき、AのDBもAの状態の一部分である。そして、Aをダウンロードした、ユーザーの端末のあなかのAにも状態が存在する(interactionとか、local storageとか)

このような背景の中で、ユーザーはAのサーバーから全ての情報をアプリケーションを起動するたびに持ってくることはしない。なぜなら、AのDBが大きくなると、非常に非効率なやり方であるからだ。なので、Aの端末には全体stateを`S`とした際に、その部分集合の`s1`,`s2`をユーザーごとに持たせる。その抽象化を行う際の軸を考えることが大事である。

自動ドアを「開いた状態」、「閉じた状態」、「半分開いた状態」に分けることもできるし、「開いた状態」、「閉じた状態」、「1/4開いた状態」、「2/4開いた状態」、「3/4開いた状態」に分けることもできる。結局分け方は、自分の軸によって違うものである。(抽象レイヤ基準の決定)

### 自分のプロジェクトに向けて

AsynchStorageのstateと、Redux Storeのstateと、Container componentのstateと、Presentational componentのstateの抽象化をきちんとこなすべき。そのためのエビデンスはDDD Quicklyにあるかもしれないので、探してみる。
