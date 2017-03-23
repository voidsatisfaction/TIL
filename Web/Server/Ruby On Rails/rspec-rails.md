# Rsepc

- about matcher
http://blog.nacyot.com/articles/2014-04-07-rspec-matchers/

- describe:
- context: describe랑 기술적으로 동일하지만 의미론적으로 내용을 다르게 하기 위해서 쓰임
- it: 테스트 케이스를 묘사한다.

```rb
describe StringCalculator do

  describe ".add" do
    context "given an empty string" do
      it "returns zero" do
        expect(StringCalculator.add("")).to eql(0)
      end
    end
  end
end

# add class method: given an empty string, it returns zero.
```

before

```rb

describe RunningWeek do

  describe ".count" do

    context "with 2 logged runs this week and 1 in next" do

      before do
        2.times do
          Run.log(:duration => rand(10),
                  :distance => rand(8),
                  :timestamp => "2015-01-12 20:30")
        end

        Run.log(:duration => rand(10),
                :distance => rand(8),
                :timestamp => "2015-01-19 20:30")
      end

      context "without arguments" do
        it "returns 3" do
          expect(Run.count).to eql(3)
        end
      end

      context "with :week set to this week" do
        it "returns 2" do
          expect(Run.count(:week => "2015-01-12")).to eql(2)
        end
      end
    end
  end
end
```

let: lazy evaluation + repeat

```rb
describe RunningWeek do

  let(:monday_run) do
    Run.new(:duration => 32,
            :distance => 5.2,
            :timestamp => "2015-01-12 20:30")
  end

  let(:wednesday_run) do
    Run.new(:duration => 32,
            :distance => 5.2,
            :timestamp => "2015-01-14 19:50")
  end

  let(:runs) { [monday_run, wednesday_run] }

  let(:running_week) { RunningWeek.new(Date.parse("2015-01-12"), runs) }

  describe "#runs" do

    it "returns all runs in the week" do
      expect(running_week.runs).to eql(runs)
    end
  end

  describe "#first_run" do

    it "returns the first run in the week" do
      expect(running_week.first_run).to eql(monday_run)
    end
  end

  describe "#average_distance" do

    it "returns the average distance of all week's runs" do
      expect(running_week.average_distance).to be_within(0.1).of(5.4)
    end
  end
end
```
# Rspec-rails

레일즈 환경에서 편하게 rspec을 이용하기 위한 gem

- 컨트롤러나 모델을 생성하면 자동적으로 spec파일도 생성해준다.

# FactoryGirls

메소드
- build: 데이터베이스에 저장 없이 오브젝트 생성
- build_stubbed: 데이터베이스에 저장 없이 오브젝트 생성 + 마치 저장된 척

- create: 데이터베이스에 저장 + 오브젝트 생성
- create_list: factory전부를 적용한 오브젝트 생성

```rb
build :article, :unpublished
# (커맨드) (factory종류) (특성)
```

- sequence(데이터 속성): 데이터를 생성할때마다 1부터 순차적으로 n을 증가시켜나감(서로 다른 복수의 데이터 생성)
