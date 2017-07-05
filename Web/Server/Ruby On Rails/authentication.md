# Authentication

## 임시 Session

rails의 session이라는 내장 함수를 이용한다.

### 1. session controller 만듬

### 2. session helper 만듬

```ruby
module SessionsHelper
  def log_in(user)
    # actually session is a method
    session[:user_id] = user.id
  end

  def current_user
    @current_user ||= User.find_by(id: session[:user_id])
  end

  def logged_in?
    !current_user.nil?
  end
end
```

### 3. session controller에 login적용

```ruby
class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user && user.authenticate(params[:session][:password])
      log_in user
      redirect_to user
    else
      flash.now[:danger] = 'Invalid email/password combination'
      render 'new'
    end
  end

  def destroy
  end
end

```

### 4. view에 logged_in? 함수를 이용해서 로그인 여부에 따라서 다른 레이아웃 적용
