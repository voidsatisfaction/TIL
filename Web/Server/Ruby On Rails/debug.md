# Debug

## 디버그 편하게 하기

```erb
<%= debug(params) if Rails.env.development? %>
```

위의 함수를 넣는것으로, 현재 페이지에 대한 데이터(어떠한 파라미터가 있는지)에 대한 정보를 쉽게 알 수 있다.

controller와 action도 알 수 있음.
