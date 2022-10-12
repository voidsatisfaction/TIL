# Design Classes with a Single Responsibility

## 코드를 쉽게 변화할 수 있도록 디자인한다.

- **어떤 코드를 작성해야 하는가?(TRUE)**
  - Transparent: 변화의 결과가 코드레벨에서 명확하게 알 수 있어야 함. 어디어디에 의존하는지도 쉽게 알 수 있어야 함.
  - Reasonable: 변화의 가치 > 변화의 비용
  - Usable: 새로운, 예측하지 못한 환경에서도 사용할 수 있어야 함
  - Exemplary: 코드 자체가 코드를 변화시키려 하는 사람이 그 퀄리티를 유지할 수 있도록 해야한다.

## 하나의 책임을 가진 클래스들을 만들어라.

Example of bicycles / gears

```rb
# 다음 코드는 하나의 클래스에 많은 역할을 부여했으므로, 부적절하다.
class Gear
  attr_reader :chainring, :cog, :rim, :tire # 애초에 왜 기어가 rim이랑 tire크기를 갖고 있어야 하는걸까?
  def initialize(chainring, cog, rim, tire)
    @chainring = chainring
    @cog = cog
    @rim = rim
    @tire = tire
  end

  def ratio
    chainring / cog.to_f
  end

  def gear_inches
    ratio * (rim + (tire * 2))
  end
end

puts Gear.new(52,11,26,1.5).gear_inches
puts Gear.new(30,27,24,1.25).gear_inches

```

## 하나의 책임을 가진 클래스인지 확인하는 방법

1. 기어씨 당신의 타이어 사이즈 크기가 어떻게 되나요?
2. 클래스를 한 문장으로 묘사해본다(and or가 들어있지 말아야 한다)

**cohension**
**아무것도 하지 않는 것의 미래비용을 생각하라**

## 변화를 수용하는 코드 작성법

### 데이터가 아닌 행위(메소드 추상화)에 의존하라.

1. 인스턴스 변수들을 숨겨라

```rb
# No!
def ratio
  @chainring / @cog.to_f
end

# Good!
attr_reader :chainring, :cog
# def cog
#   @cog
# end
def ratio
  chainring / cog.to_f
end

```

2. 데이터 구조를 숨겨라

**Data structure != Data meaning**

```rb

class RevealingReferences
  attr_reader :wheels
  def initialize(data)
    @wheels = wheelify(data)
  end

  def diameters
    wheels.collect{ |wheel| wheel.rim + (wheel.tire * 2) }
  end

  # 인스턴스 생성시 들어오는 배열의 구조를 wheelify 메소드에 격리시킨다.
  Wheel = Struct.new(:rim, :tire) # 구조체의 틀을 만듬
  def wheelify(data)
    data.collect{ |cell| Wheel.new(cell[0],cell[1]) } # 구조체를 그냥 순서대로 넣었다? 순서가 있는 구조체??
  end
end

```

### 하나의 책임을 코드 전체에 강제하라

1. 메소드들도 반드시 하나의 책임을 가지게 하라.

**작은 메소드를 지향하라**
재사용가능성과 변화에대한 여유.
cf) Functional Programming

```rb

# iterate over this array
def diameters
  wheels.collect{ |wheel| diameter(wheel) }
end

# calculate diameter of ONE wheel
def diameter(wheel)
  wheel.rim + (wheel.tire * 2)
end

```

2. 클래스 안에 있는 여분의 책임들을 격리시켜라.

**결정 대신 결정의 유보를 위한 코드를 써라**

```rb

class Gear
  attr_reader :chainring, :cog, :wheel
  def initialize(chainring, cog, rim, tire)
    @chainring = chainring
    @cog = cog
    @wheel = Wheel.new(rim,tire)
  end

  def ratio
    chainring / cog.to_f
  end

  def gear_inches
    ratio * wheel.diameter
  end

  # 이 곳이 결정의 유보.
  Wheel = Struct.new(:rim, :tire) do
    def diameter
      rim + (tire * 2)
    end
  end
end

```

## The Real Wheel

```rb

class Gear
  attr_reader :chainring, :cog, :wheel

  def initialize(chainring, cog, wheel = nil)
    @chainring = chainring
    @cog = cog
    @wheel = wheel
  end

  def ratio
    chainring / cog.to_f
  end

  def gear_inches
    ratio * wheel.diameter
  end
end

class Wheel
  attr_reader :rim, :tire

  def initialize
    @rim = rim
    @tire = tire
  end

  def diameter
    rim + (tire * 2)
  end

  def circumference
    diameter * Math::PI
  end
end

@wheel = Wheel.new(26, 1.5)
puts @wheel.circumference

puts Gear.new(52, 11, @wheel).gear_inches

puts Gear.new(52, 11).ratio

```
