# Model

## Structure

![Model_structure](./img/model_structure.png)

## Validation

### 1. Length

```ruby
# 아마 validates는 함수이다.

class Micropost < ApplicationRecord
  belongs_to :user
  validates :content, length: { maximum: 140 }
end

class User < ApplicationRecord
  has_many :microposts
  validates :name, presence: true
  validates :email, presence: true
end

```
