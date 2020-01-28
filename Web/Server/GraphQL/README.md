# GraphQL 기초

- 의문
- 정의
- 쿼리와 변형

## 의문

- 쿼리에 필요한 함수는 서버사이드에 코드로 존재하는 것이겠지?

## 정의

- 정의
  - API를 위한 query language
  - **API layer만 담당**
  - 사용자(서버)가 자신의 데이터에 대해서 정의한 타입 시스템을 사용하여 쿼리를 실행하는 server-side 런타임
- 구성
  - 타입
  - 필드
  - 각각의 타입에 대한 각각의 필드에 대한 함수
- 흐름
  - GraphQL service를 기동
  - GraphQL query를 전송
  - 정의된 타입과 필드만 참조하는지 확인
  - 결과를 얻기 위해 제공된 함수 실행

## 쿼리와 변형(Quries and Mutations)

### Fields

- 쿼리의 형태에 맞는 데이터만 그대로 반환

```
{
  hero {
    name
    # Queries can have comments!
    friends {
      name
    }
  }
}

{
  "data": {
    "hero": {
      "name": "R2-D2",
      "friends": [
        {
          "name": "Luke Skywalker"
        },
        {
          "name": "Han Solo"
        },
        {
          "name": "Leia Organa"
        }
      ]
    }
  }
}
```

### Arguments

- field에 대한 arguments를 넘겨줘서 데이터 필터링 / 변형 가능
- GraphQL 서버는 custom type을 선언할 수 있음

```
{
  human(id: "1002") {
    id
    name
    height(unit: FOOT)
  }
}

{
  "data": {
    "human": {
      "id": "1002",
      "name": "Han Solo",
      "height": 5.905512
    }
  }
}
```

### Aliases

- 같은 필드이름이 겹치는 것을 막기 위해서 alias를 사용해서 쿼리를 할 수 있음

```
{
  empireHero: hero(episode: EMPIRE) {
    name
  }
  jediHero: hero(episode: JEDI) {
    name
  }
}

{
  "data": {
    "empireHero": {
      "name": "Luke Skywalker"
    },
    "jediHero": {
      "name": "R2-D2"
    }
  }
}
```

### Fragments

- 쿼리에서 원하는 구조가 반복되는 경우 원하는 구조의 데이터를 질의할 때 재사용하기 위한 기능
- fragments안에서 변수 사용 가능

```
query HeroComparison($first: Int = 3) {
  leftComparison: hero(episode: EMPIRE) {
    ...comparisonFields
  }
  rightComparison: hero(episode: JEDI) {
    ...comparisonFields
  }
}
​
fragment comparisonFields on Character {
  name
  friendsConnection(first: $first) {
    totalCount
    edges {
      node {
        name
      }
    }
  }
}


{
  "data": {
    "leftComparison": {
      "name": "Luke Skywalker",
      "friendsConnection": {
        "totalCount": 4,
        "edges": [
          {
            "node": {
              "name": "Han Solo"
            }
          },
          {
            "node": {
              "name": "Leia Organa"
            }
          },
          {
            "node": {
              "name": "C-3PO"
            }
          }
        ]
      }
    },
    "rightComparison": {
      "name": "R2-D2",
      "friendsConnection": {
        "totalCount": 3,
        "edges": [
          {
            "node": {
              "name": "Luke Skywalker"
            }
          },
          {
            "node": {
              "name": "Han Solo"
            }
          },
          {
            "node": {
              "name": "Leia Organa"
            }
          }
        ]
      }
    }
  }
}
```

### Operation name

- `query`키워드(operation type - query, mutation, subscription)와 query name을 작성하는 것이 production환경에서 권장됨
  - 디버깅에 용이
- operation type
  - 개요
    - 사용자가 어떠한 동작을 하려고 하는지 묘사
  - 종류
    - query
    - mutation
    - subscription

```
query HeroNameAndFriends {
  hero {
    name
    friends {
      name
    }
  }
}

{
  "data": {
    "hero": {
      "name": "R2-D2",
      "friends": [
        {
          "name": "Luke Skywalker"
        },
        {
          "name": "Han Solo"
        },
        {
          "name": "Leia Organa"
        }
      ]
    }
  }
}
```
