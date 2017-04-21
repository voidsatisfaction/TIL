## IDN(I Don't Know)시리즈 Ruby버전

### Simbol

문자열과 비슷하지만, 심볼은 그 이름마다 object가 1개뿐이다.
`intern`은 그 문자열에 대응하는 심볼을 돌려주는 메소드

### equal?

같은 `오브젝트인가`를 확인해주는 메소드
메모리상의 위치도 같아야한다.

### \&\& 과 \|\|

```ruby
a = false && 4 # false
b = false || 4 # 4
```

### block을 갖는 method

```ruby
def square(a, b)
  for x in a..b
    yield(x, x ** 2)
  end
end

square(1,3){|i, v|
  puts v
}

square(1,3){|i, v|
  puts "#{i}^2 = #{v}"
}
```

### method parameter initialize

```ruby
def m(a, b, c=0, d="default")
```
