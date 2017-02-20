# Flex

## flex : 레이아웃을 좀 더 쉽게 짜기 위해 고안됨. item과 그것을 담을 container가 필요.

컨테이너에 속성에 display:flex;를 하는 것부터 시작
여러 속성들
- flex-basis : 크기 지정
- flex-grow : 아이템들이 컨테이너를 나눠갖는 비율 결정
- flex-shrink : 화면이 작아질 때 줄어드는 비율 결정
- flex-diretion : 컨테이너 방향 결정(row, column)
- flex-wrap : 아이템 크기가 컨테이너 크기보다 크다면 줄바꿈
- align-items : 수직 관련 정렬
- justify-items : 수평 관련 정렬
- align-content : 아이템을 그룹핑해서 정렬
- align-self : 특정 아이템만 크기 다르게
- flex : flex-grow + shrink + basis, order : 아이템의 순서 바꿈.
- holy grail layout : 이런 형태의 레이아웃을 flex를 통해 쉽게 만들 수 있음