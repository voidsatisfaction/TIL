# Functional Programming with GO

## 참고

[Goで関数型プログラミング](http://qiita.com/taksatou@github/items/d721a62158f554b8e399)

## GO의 함수적 패러다임에 관한 한계

```go
// int형 slice의 map
func Map(slice []int, fn func(int) int) {
  result := make([]int, len(slice))
  for i, v := range slice {
    result[i] = fn(v)
  }
  return result
}
```

위에서 보다시피 Map과 같은 함수가 이미 형이 정해져 있기 때문에 모든 type에 관해서 일반화 하기가 힘들다.

하지만 위의 [Goで関数型プログラミング](http://qiita.com/taksatou@github/items/d721a62158f554b8e399)는 `reflect`라는 개념을 이용해서 일반화 하는 예를 보여준다. (하지만, 이러한 프로그래밍 스타일이 Go에서 환영받지 못한다고 한다)
