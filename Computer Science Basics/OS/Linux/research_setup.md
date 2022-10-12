# 研究室サーバーようセッティング

## 0. Prolog

- Super key : windowsキー
- ターミナル起動 : Ctrl + Alt + T

## 1. Apparmorを消す

これは、権限による面倒なことがなくなるようにするためです。

ターミナルで

~~`sudo /etc/init.d/apparmor stop` # これは、apparmorをストップさせる~~

`sudo update-rc.d -f apparmor remove` # これは、ブートしてもapparmorが動かないようにする。

## 2. IPの固定

`ifconfig`やさまざまな命令語で、現在のipを

`sudo nano /etc/network/interfaces`で、固定IPとする。

## 3. アカウントの発行

各々のユーザを生成してからsudoerにする。

## 4. Docker管理
