# rbenv

- general

`brew install rbenv`

`rbenv install 2.3.3`

`rbenv global 2.3.3`

- bash_profile & zshrc

```rb

$ vim ~/.bash_profile
# 以下の二行を貼り付けて保存
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"

```


# rvm