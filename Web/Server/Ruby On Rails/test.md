# Test

## 테스트의 기본

내가 테스트를 하고 싶은 부분을 하나의 system으로 생각한다.

```
Input(given) => 테스트 대상(System) => Output(expected)
```

테스트에서는 주어진 input에 대하여 예측된 output을 내는지 확인하는 것이 필요하다.

이러한 측면에서 보면, functional programming은 테스트하기에 참 적절하다고 할 것이다(프로그래밍의 스타일이 부작용이 적고 애초에 function이 하나의 system이라고 볼 수 있음)

## 테스트를 도와주는 gems

- RSpec
- byebug
  - controller에 놓음으로써, 그 부분에 있어서의 app의 상태를 출력해준다.
- Factory Girl
  - fixture. 테스트하는 데에 필요한 기본적인 데이터를 생성해준다.

fxture는 테스트에 필요한 기본 dataset을 지칭한다.

## 테스트 종류

### 1. controller

```ruby
require 'test_helper'

class SessionsControllerTest < ActionDispatch::IntegrationTest
  test "should get new" do
    get login_path
    assert_response :success
  end
end
```

위와 같이 클라이언트의 request에 대하여 서버는 예측된 response를 돌려주는 지에 대한 테스트.

### 2. integration

```ruby
require 'test_helper'

class UsersLoginTest < ActionDispatch::IntegrationTest
  test "login with invalid information" do
    get login_path
    assert_template 'sessions/new'
    post login_path, params: { session: { email: "", password: "" } }
    assert_template 'sessions/new'
    assert_not flash.empty?
    get root_path
    assert flash.empty?
  end
end
```

위와 같이 일련의 클라이언트의 `행동`에 대해서 어플리케이션의 전반적인 반응이 적절한지 확인.

(BDD같은 느낌이 물씬)

### 3. model

```ruby
class UserTest < ActiveSupport::TestCase
  def setup
    @user = User.new(
      name: "Example User",
      email: "user@example.com",
      password: "foobar",
      password_confirmation: "foobar"
    )
  end

  test "the truth" do
    assert @user.valid?
  end

  test "name should be present" do
    @user.name = "      "
    assert_not @user.valid?
  end
end
```

위와 같이 controller로부터의 input과 예상된 output(validation등)이 일치하는지 확인

### 4. helper

```ruby
require 'test_helper'

class ApplicationHelperTest < ActionView::TestCase
  test "full title helper" do
    assert_equal full_title, "Ruby on Rails Tutorial Sample App"
    assert_equal full_title("Help"), "Help | Ruby on Rails Tutorial Sample App"
  end
end
```

위와 같이 특정 헬퍼(메소드)가 input에 대하여 output을 제대로 내는지 확인.

### 5. mailer
