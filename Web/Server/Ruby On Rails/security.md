# Security

## SSL 적용

```ruby
# config/environments/production.rb
# heroku는 이대로 배포하면 ssl적용. 다른 경우에는 자기자신이 증명서를 사야한다.
Rails.application.configure do
  .
  .
  .
  # Force all access to the app over SSL, use Strict-Transport-Security,
  # and use secure cookies.
  config.force_ssl = true
  .
  .
  .
end
```
