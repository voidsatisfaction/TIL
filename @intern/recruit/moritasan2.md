# 本日学んだこと

## 参考
1. [What is Software Design?](http://web.archive.org/web/20080803072849/www.biwa.ne.jp/~mmura/SoftwareDevelopment/WhatIsSoftwareDesignJ.html)
2. [Manifesto for Agile Software Development](http://agilemanifesto.org/)
3. [データの削除は非推薦](https://www.infoq.com/jp/news/2009/09/Do-Not-Delete-Data)

## 読んだらよい本
1. [Agile Software Development, Principles, Patterns, and Practices](https://www.amazon.com/Software-Development-Principles-Patterns-Practices/dp/0135974445)
2. [パターン、Wiki、XP ~時を超えた創造の原則](https://www.amazon.co.jp/%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%80%81Wiki%E3%80%81XP-~%E6%99%82%E3%82%92%E8%B6%85%E3%81%88%E3%81%9F%E5%89%B5%E9%80%A0%E3%81%AE%E5%8E%9F%E5%89%87-WEB-PRESS-plus%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA/dp/4774138975)

## データの削除はしないほうがいい。

データの完全性に悪影響を及ぼす。
なので、削除でなく、「有効、中止、キャンセル、廃止予定」といった様々なstateを用意すべきである。

## ソフトウェア工学の分類

![software engineering image](./software_engineering_sorts.png)

## Agile開発とは？

### 思想

**Practice より Principle!!!**

1. **個人と相互作用を重視** > 流れとツール
2. **動くソフトウェア** > 文書
3. **顧客とのコラボ** > 契約交渉
4. **変化に対応** > 計画

### Agileの構成員

![agile members](./agile_member.png)

最初にうまくできない人はpair programmingをして、
慣れた後は独立する。

### Agileの導入

- Timebox
  - 一定期間（一週間・二週間のsprint）の間のタスクを見積もって設定。
  - タスクの解決時間は3人で協力して見積もる
- 優先度
  - ROIを考えてやる。
  - 時間と紅葉
- プロセス改善
  - KPT(Keep / Program / Try)
  - Keep : やり続ける
  - Program : 問題を顕著化する。
  - Try : その問題を解決する。

QCD(Quality Cost Delivery）を考慮しながらソフトウェアを作っていくべき。
