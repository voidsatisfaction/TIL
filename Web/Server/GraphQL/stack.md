# GraphQL Tech stack

- graphql-yoga
- GraphQL Nexus
- Prisma
  - 개요
  - How does Prisma work

## graphql-yoga

- 개요
  - GraphQL Server
- 특징
  - 서버 실행이 쉬움
  - Subscription 기능 포함
  - 다양한 client(Apollo, Relay, ...) 호환 가능성
- 역할
  - gql client의 query를 receive
  - gql query parse
  - gql query validation
  - resolver execution
  - response serialization

```ts
import { GraphQLServer } from 'graphql-yoga'
// ... or using `require()`
// const { GraphQLServer } = require('graphql-yoga')

const typeDefs = `
  type Query {
    hello(name: String): String!
  }
`

const resolvers = {
  Query: {
    hello: (_, { name }) => `Hello ${name || 'World'}`,
  },
}

const server = new GraphQLServer({ typeDefs, resolvers })
server.start(() => console.log('Server is running on localhost:4000'))
```

## GraphQL Nexus

- 개요
  - *GraphQL을 위한 type definition(schema)*
    - *???*

## Prisma(2)

Prisma ver2의 docs를 기반으로 작성.

ver1의 경우에는 prisma server라는 jvm위에 돌아가는 db와 application layer사이의 추상 레이어가 존재(2에서 삭제).

- 개요
  - 정의
  - 구성
- How does Prisma work

### 개요

#### 정의

- 데이터베이스 툴킷
  - 기존의 ORM과 유사 개념
  - application layer와 db layer를 이어주는 추상 레이어
    - js의 plain object <-> db record / table

#### 구성

- Prisma Client
  - Auto-generated, type-safe query builder for Node.js & TypeScript
  - 어떤 백엔드던(standalone, serverless 등), REST API, GraphQL API, gRPC API 등 데이터 베이스를 필요로 하는 모든 곳에서 사용 가능
- Prisma Migrate
  - Declarative data modeling & migration system
- Prisma Studio
  - GUI to view and edit data in your database

### How does Prisma work

- Prisma schema
- Prisma data model

```
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
generator client {
  provider = "prisma-client-js"
}
model Post {
  id        Int     @id @default(autoincrement())
  title     String
  content   String?
  published Boolean @default(false)
  author    User?   @relation(fields:  [authorId], references: [id])
  authorId  Int?
}
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}
```

- Prisma schema
  - 개요
    - Prisma toolkit을 사용하는 경우, 가장 먼저의 시작 포인트(Application model 작성)
  - 구성
    - Data source
      - db connection
    - Generator
      - prisma client 지정
        - *클라이언트를 복수개 만들 수 있다는 것인가?*
        - *다양한 라이브러리 선택이 가능해보임?*
    - Data model
      - application model 정의
- Prisma data model
  - 개요
    - 데이터베이스의 테이블을 나타냄
    - Prisma Client API에서의 쿼리 foundation 제공
  - **Getting a data model**
    - DB를 검사해서 자동적으로 생성
    - data model을 직접 작성하고, Prisma Migrate 모듈을 이용해서 데이터베이스에 매핑함
  - Data model이 정의된 다음에, Prisma Client를 생성할 수 있고, 그 클라이언트로 CRUD등의 쿼리를 행할 수 있음
    - TS를 사용하는 경우, type-safe한 쿼리를 날릴 수 있음
- Accessing your database with Prisma Client
  - Generating Prisma Client
    - `npm install @prisma/client`
    - `prisma generate`
      - Prisma schema를 읽고 Prisma Client code를 생성(코드는 `node_modules/@prisma/client`에 위치)
      - 데이터 모델을 변경하고 수동적으로 호출해줘야 함
    - `@prisma/client` 노드 모듈은 `.prisma/client`라는 폴더를 참조함
