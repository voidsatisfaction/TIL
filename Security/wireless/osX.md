# osX

## 참조

- [Tcpdump](https://danielmiessler.com/study/tcpdump/#gs.ZkqjbwM)

## 주변 모든 패킷 수집

tcpdump -Ii en0

tshark -Ii en0

**Wireshark + monitoring모드**

p.s 반드시 모니터링모드로 해야한다. 아니면 내 패킷만 보임.

## 802.11 프로토콜의 frame종류

Management frames： APと接続したり切断したり認証したり・・ (0)
Control frames： 他のフレームを運ぶため。ヘッダーしかない (1)
Data frames： 実際にデータを含むパケット (2)

각각 `wlan.fc.type == 0 , 1 , 2`이렇게 필터링 할 수 있다.
