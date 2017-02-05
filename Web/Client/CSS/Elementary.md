## display
- block : 새 줄에서 시작해서 가장자리까지 최대한 늘어난다(p, form, header, footer, section)
- inline : 해당 단락의 흐름을 방해하지 않는 상태로 텍스트를 감쌀 수 있음(a, span)
- none : 마치 없는것 처럼 보이게 함(cf visibility: hidden)
- inline-block
- flex

## margin: auto;

```css
#main {
  max-width: 600px;
  margin: 0 auto;
}
```
width설정 : 컨테이너 좌우 가장자리로 늘어나지 않게
margin auto : 좌우 마진에 균등한 값을 주어서 해당 엘리먼트를 정 중앙에 배치할 수 있다.

## box-sizing

```css
.simple {
  width: 500px;
  margin: 20px auto;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}

.fancy {
  width: 500px;
  margin: 20px auto;
  padding: 50px;
  border: solid blue 10px;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}

/* 개별지정 or 전체에 적용 */

* {
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
}

```

이런식으로 box-sizing을 지정하면, padding과 border를 집어넣어도 크기가 같아진다.

## position

- static : 기본값
- relative : top / right / bottom / left 등의 프로퍼티를 지정하면 기본 위치와는 다르게 조정된다.
- fixed : 페이지가 스크롤 되더라도 늘 같은위치 top / right / bottom / left 사용
- absolute : static이 아닌 가장 가까운 조상 엘리먼트에 대하여 상대적인 위치 결정. 만약 조상 엘리먼트가 없으면 document body를 기준으로 삼는다.

```css
/* example */

/* 기본위치에 대해서 변화 정도를 나타낸다. */
.relative {
  position: relative;
  top: -20px;
  left: 20px;
  background-color: white;
  width: 500px;
}

.fixed {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 200vw;
  background-color: white;
}

/* absolute를 나타내기 위한 relative */
.relative {
  position: relative;
  width: 600px;
  height: 400px;
}
.absolute {
  position: absolute;
  top: 120px;
  right: 0;
  width: 300px;
  height: 200px;
}
```

## Nav container

### position을 사용한 경우
```css
.container {
  position: relative;
}

nav {
  position: absolute;
  left: 0;
  width: 200px;
}

section {
  margin-left: 200px;
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  height: 70px;
  background-color: white;
  width: 100%;
}

body {
  margin-bottom: 120px;
}
```