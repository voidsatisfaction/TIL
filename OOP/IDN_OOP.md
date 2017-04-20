## IDN(I Don't Know)시리즈

### super method

상속을 받은 클래스가 어떠한 메소드를 오버라이딩 했을때,
상속처 클래스의 같은 이름의 메소드를 상속 받은 클래스의 같은 메소드에서 실행하기 위한 메소드

super는 **super를 이용해 메소드를 정의한 클래스**의 상속처 클래스의 메소드를 참조한다.

```rb
class A
  def m
    puts "My class name is A"
  end
end

class B < A
  def m
    self.n
    super
  end

  def n
    puts "this is n from B"
  end
end

class C < B
  def n
    puts "this is n from C"
  end
end

c = C.new
c.m # this is n from C    My class name is A
c.n # this is n from C
```

### self

self는 메소드를 실행한 object자기 자신을 말한다.
