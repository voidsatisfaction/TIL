# All about routes

## resources

```ruby

Rails.application.routes.draw do
  resources :users
  root 'application#hello'
end

```

Result

|URL|	Action|	Purpose|
|---|--------|--------|
|users|index|page to list all users|
|users/1|	show|page to show user with id 1|
|users/new|new|page to make a new user|
|users/1/edit|edit|page to edit user with id 1|

## router and variable

```ruby
# routes.rb

get '/help', to: 'static_pages#help'

=begin
  help_path -> '/help'
  help_url -> 'http://www.example.com/help'
=end

```
