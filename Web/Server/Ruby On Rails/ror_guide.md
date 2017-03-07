# Ruby On Rails guide

## Model

모델 자체는 단수형. 테이블 이름은 복수형.

## Controller

## View

```rb
  app/views/articles/new.html.erb
  # html은 템플릿의 형식
  # erb는 핸들러(erb, builder, coffee)중 하나.
```

## Router

```rb

resources :articles

# RESTful router설정
Controller#Action
    articles GET    /articles(.:format)          articles#index
             POST   /articles(.:format)          articles#create
 new_article GET    /articles/new(.:format)      articles#new
edit_article GET    /articles/:id/edit(.:format) articles#edit
     article GET    /articles/:id(.:format)      articles#show
             PATCH  /articles/:id(.:format)      articles#update
             PUT    /articles/:id(.:format)      articles#update
             DELETE /articles/:id(.:format)      articles#destroy
        root GET    /                            welcome#index

```

