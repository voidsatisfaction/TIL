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

### 루비에서 sort할때의 주의

```ruby
# 3가지의 조건으로 num_array를 정렬하고 싶을 때
num_array.sort! do |a,b|
  if a.length < b.length
    return -1
  elsif a.length > b.length
    return 1
  end

  a_sum = a.split('').map{ |e| e.to_i }.reduce(:+)
  b_sum = b.split('').map{ |e| e.to_i }.reduce(:+)
  if a_sum < b_sum
    return -1
  elsif a_sum > b_sum
    return 1
  end

  if a < b
    return -1
  elsif a > b
    return 1
  end
end
```

위의 코드는 언뜻보면 맞는 듯 하지만 사실은 `unexpected return (LocalJumpError)`로 에러가 나온다.

위의 코드를 원하는 방향대로 동작하게 하기 위해서는 `return`을 `next`로 바꿀 필요가 있다.

```ruby
# 3가지의 조건으로 num_array를 정렬하고 싶을 때
num_array.sort! do |a,b|
  if a.length < b.length
    next -1
  elsif a.length > b.length
    next 1
  end

  a_sum = a.split('').map{ |e| e.to_i }.reduce(:+)
  b_sum = b.split('').map{ |e| e.to_i }.reduce(:+)
  if a_sum < b_sum
    next -1
  elsif a_sum > b_sum
    next 1
  end

  if a < b
    next -1
  elsif a > b
    next 1
  end
end
```

이렇게 하면 원하는 대로 동작한다.
