# Rails environment

## 종류

1. test
2. development(default)
3. production

## 확인

```ruby
Rails.env # => "development"

Rails.env.development? # => true

Rails.env.test? # => false
```

다른 모드에서 실행

```ruby
rails server --environment production

# production db setting
rails db:migrate RAILS_ENV=production
```
