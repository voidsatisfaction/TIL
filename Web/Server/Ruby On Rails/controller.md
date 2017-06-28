# Controller

## Structure

![controller_structure](./img/controller_structure.png)

## Byebug

```ruby
class UsersController < ApplicationController

  def show
    @user = User.find(params[:id])
    debugger
  end

  def new
  end
end
```

이렇게 설정하면, debugger에서 서버 process가 멈춘다.

그리고 commandline에서 `@user` 와 같은 커맨드를 입력해서 그 당시의 값을 디버깅 할 수있다.
