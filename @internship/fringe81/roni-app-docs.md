# Why?

## 企画

## Modeling / 設計

### なんでReduxなのか？

今までのMVCは、Modelが変わると、Viewも変わったり、Viewが変わると他のModelが変わってMVC間の相互作用がわかりにくかった。現在、Frontendサイドの課題の一つが、Mutationとasynchrocityを管理することだが、その問題を解決するために、全体設計にある制約(rule)を加えたのがReduxである。結局「Client side app」のInteractionの流れの「明瞭化」が目的である。

その原則は三つある。

1. Single state of truth
2. State is read-only
3. Changes are made with pure functions.

**他のケースだと。。(mobx)**

### Redux Sagaを使う理由？

Redux thunkは実際、様々が人が使われていて、使うルール自体が簡単。しかし、コードが直感的ではない。また、thunkの中で様々なActionの呼び出しがあると、そのActionの流れがわかりにくくなる。

そこで、Redux Sagaを使う。Generatorという概念を使って、非同期処理をまるで同期のように扱うことができる。なお、Action flow上の副作用を含めた相互作用をきちんと見えるかできる。

また、現在、Redux thunkは開発者による、アップデートがされていない（1年以上）がそれに対して、Redux Sagaは最新のコミットが半月となっていて継続的にアップデートされているので、きちんと、開発者による管理がされていると考える。

**本当にSagaって難しいの？**　を確実にする。

### なんでAtomic Designなのか？

Reactのコア思想の一つは、UIのComponent化である。つまり、UIを宣言的にComponentとして再利用することを目指している。Atomic Designは、自然現象の分子にComponentを例えることで、Layerを分け、コンポーネントを融合させ、新しいものを作り出す。こうすることで、非常に再利用しやすいコンポーネントを作り出すことができる。

もちろん、今の段階ではそこまで分ける必要がないかもしれない。しかし、これからのアプリケーションの成長性を考えると、Atomic Designの効用は期待できる。

### なんでContainer / Presentational Componentなのか？

多くのコンポーネントがstateを持つようになると、どのコンポーネントがどのようなstateを持っていたのかをトラッキングしにくくなる。それは、将来の生産性に大きな問題を起こりうる上に、重複的なコードを書く可能性が増えるため、Containerコンポーネント(上でstateを管理するコンポーネント)とPresentationalコンポーネントにわけることが望ましい。

具体的に言うと、アプリケーション・Screenレベルのstateはcontainerコンポーネントが管理し、単純なUIのところはPresentationalコンポーネントが管理すると、よりわかりやすい。

### なんでHOCを利用するのか？

applicationレベルの情報を「見える化」することで、どのような情報やactionがこれから使われるかをわかるようになる。なお、routerによる画面転換のactionも一目でわかりやすくすることができる。

## デプロイ

### なんでCode pushを利用するのか？

簡単なコード修正は、App storeなどを通じて行うには、時間的な非効率性が大きいため、そのコストを下げるために、実装する。

## なんでGoogle Analyticsを取り入れるのか

ユーザーのデータを収集する。どのような画面に主にいたのか、再訪問率や、国別情報んなどを把握することができる。これらの情報はこれからマーケティングの展開や新機能追加に非常に大きなタネになる。
