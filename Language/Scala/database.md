# 스칼라로 데이터베이스 프로그래밍 하기

## Scala(Java)에서 RDBMS를 사용하기: JDBC

- 자바에서 데이터베이스 관리 시스템에 접속하는 가장 기본적인 모듈
- JDBC
  - 자바와 관계 데이터베이스의 접속을 위한 API(자바의 기본 SDK내장 모듈)
  - 각 DBMS용의 JDBC드라이버를 준비해야 함
  - 드라이버로, RDBMS의 차이를 흡수하는 통일적 인터페이스를 제공
  - MySQL, PostgreSQL, H2, ...

## JDBC를 이용하기

- JDBC로 RDBMS와 주고받기 하는 가장 소박한 방법
  - 플레이스홀더 기능(placeholder)
  - 프리페어드 스테이트먼트 기능(prepared statement)

```scala
package example

import java.sql.{Connection, ResultSet, Statement, PreparedStatement, DriverManager}

object Main {
  def main(args: Array[String]): Unit = {
    Class.forName("com.mysql.jdbc.Driver")
    val conn: Connection = DriverManager.getConnection("jdbc:mysql://localhost:13306/vocaloid", "root", "root")

    val st: PreparedStatement = conn.prepareStatement("SELECT * FROM artist WHERE birthday < ? ORDER BY birthday ASC")
    st.setString(1, "2008-01-01")
    val rs: ResultSet = st.executeQuery()

    while (rs.next()) {
      println(s"""${rs.getInt("id")}, ${rs.getString("name")}, ${rs.getString("birthday")}""")
    }
    rs.close()
    st.close()
    conn.close()
  }
}
```

## 보다 편리한 모듈

- Slick
  - Functional Relational Mapping Library(FRM)
    - 오브젝트 모델과 데이터베이스 모델 사이의 갭을 줄여줌
    - 데이터 베이스 모델을 스칼라로 가져옴
      - 인메모리 데이터를 다루는 것 처럼 데이터베이스를 다룸
      - 마치 스칼라 자체의 컬렉션을 이용하는 듯한 느낌을 줌
    - ORM보다 더 사전 최적화가 잘 되어있음
    - 타입 안정성이 높음(테이블 칼럼을 잘못 입력해도 잡아줌)
  - Reactive
    - 샘플코드에서는 간단하기 때문에 Reactive한 코드는 쓰지 않음
  - Plain SQL
- HikariCP
  - Connection Pooling

```scala
package example

import scala.concurrent.{Future, Await}
import scala.concurrent.duration.Duration
import scala.concurrent.ExecutionContext.Implicits.global
import slick.driver.MySQLDriver.api._

object Main {
  def main(args: Array[String]): Unit = {
    val db = Database.forURL("jdbc:mysql://localhost:13306/vocaloid", driver="com.mysql.jdbc.Driver", user="root", password="root")

    val name = "sdfs"

    Await.result(
      db.run(
        sql"""SELECT * FROM artist WHERE name = ${name} LIMIT 1""".as[(Int, String, String)]
      ).map(println),
      Duration.Inf
    )
  }
}
```

## 얻은 데이터를 Case Class로 변환하기

- 대응하는 레코드를 표시하는 Case Class의 인스턴스로 변환하면 편리
- 예
  - artist테이블에 대응하는 Artist케이스 클래스
  - album테이블에 대응하는 Album케이스 클래스

```scala
package example

import scala.concurrent.{Future, Await}
import scala.concurrent.duration.Duration
import scala.concurrent.ExecutionContext.Implicits.global
import slick.driver.MySQLDriver.api._
import org.joda.time.LocalDate
import slick.jdbc.GetResult
import com.github.tototoshi.slick.MySQLJodaSupport._

case class Artist(id: Long, name: String, birthday: LocalDate)

object Main {
  implicit val userGetResult = GetResult(r => Artist(r.<<, r.<<, r.<<))
  def main(args: Array[String]): Unit = {
    val db = Database.forURL("jdbc:mysql://localhost:13306/vocaloid", driver="com.mysql.jdbc.Driver", user="root", password="root")

    val name = "sdfs"

    Await.result(
      db.run(
        sql"""SELECT * FROM artist WHERE name = ${name} LIMIT 1""".as[Artist]
      ).map{ artists => println(artists(0).name) },
      Duration.Inf
    )
  }
}
```

## Slick + 독자 확장

- `Future`를 사용한 코드를 작성하는 것은 귀찮음
- 이번에는 SQL에 집중하기 위해서 동기적으로 사용하기 위해서 랩퍼(wrapper)를 사용

```scala
def find(userId: Long)(implicit ctx: Context): Option[User] = run(
  sql"""SELECT * FROM user WHERE id = $userId LIMIT 1""".as[User].map(_.headOption)
  )
```

## Slick에 의한 SQL발행

- 여기서부터 설명하는 방법으로 쿼리를 발행하자

### 조건에 맞는 하나의 행을 취득 `sql`

```scala
val name = "abc"
val artist: Option[Artist] = run(
  sql"""SELECT * FROM artist
          WHERE name = ${name}
          LIMIT 1""".as[Artist]
).headOption

println artist
```

### 조건에 맞는 복수의 행을 취득 `sql`

### 행의 삽입 `sqlu`

### 행의 갱신 `sqlu`

### 행의 삭제 `sqlu`

### 보안

- 데이터베이스의 취약성에 치명적
- 데이터의 누수, 손실
- 조심 합시다

#### 나쁜 예

```scala
val name = "..." // 유저의 입력

val st: PreparedStatement = conn.prepareStatement(
  s"SELECT * FROM artist WHERE name = $name",
)
...
```

#### 조심해야 할 점

- **유저의 입력은 안전하지 않음**
- 혹시 이름에 `''; DROP TABLE artist`가 입력된다면..?
- 대책으로 반드시 플레이스홀더(placeholder)를 사용하기

## 실천편

### 데이터 베이스의 설계

### 프로그램의 설계

- 어디에 무엇을 작성하면 좋은가?
  - DB접근
  - 얻은 데이터를 모음
  - 데이터 표시
- 적절히 분할하는 것으로 품질이 높은 소프트웨어가 됨

### 레이어 아키텍처

- 프로그램을 책임마다 레이어를 나눠서 설계
- 상위의 층이 하위의 층을 이용하는 형태로 프로그램을 작성, 알기 쉬움
- 예시
  - 인터페이스 층
    - 유저나 외부 프로그램과 상호작용하는 층
  - **애플리케이션 층**
    - 도메인층의 기능을 조합하는 층
  - **도메인 층**
    - 인프라층의 기능을 사용하여 프로그램에 도움이 되는 기능을 만드는 층
  - 인프라 층
    - DB나 네트워크등 프로그램의 외부기능과 주고받는 층
  - **Q) 도메인층과 애플리케이션층의 분리 기준?**
  - 작은 애플리케이션은 애플리케이션층을 만들지 않는 경우도 있음

#### 서비스와 모델

- 도메인 층을 정리하기 위한 설계 방법
  - 모델: 모델을 추상화한 단순 오브젝트(알기 쉬움)
  - 서비스: 모델에 포함시키는 것이 불가능한 인프라층과의 상호작용을 구현하는 모듈
    - 리포지토리(repository)를 사용해서 애플리케이션의 코어 로직을 구현

#### 모델

```scala
package internbookmark.model

import org.joda.time.DateTime

case class User(id: Long, name: String, createdAt: DateTime, updatedAt: DateTime)
```

#### 서비스

```scala
package internbookmark.service

import internbookmark.model.{Bookmark, User}
import internbookmark.repository

class BookmarkApp(currentUserName: String) {
  def currentUser(implicit ctx: Context): User = {
    repository.Users.findOrCreateByName(currentUserName)
  }

  val entriesRepository: repository.Entries = repository.Entries

  def find(bookmarkId: Long)(implicit ctx: Context): Option[Bookmark] = {
    repository.Bookmarks.find(bookmarkId)
  }

  def add(url: String, comment: String)(implicit ctx: Context): Either[Error, Bookmark] = {
    val entry = entriesRepository.findOrCreateByUrl(url)
    val user = currentUser
    repository.Bookmarks.createOrUpdate(user, entry, comment)
    repository.Bookmarks.findByEntry(user, entry).toRight(BookmarkNotFoundError)
  }

  def edit(bookmarkId: Long, comment: String)(implicit ctx: Context): Either[Error, Bookmark] = {
    for {
      bookmark <- repository.Bookmarks.find(bookmarkId).toRight(BookmarkNotFoundError).right
      _ <- Right(repository.Bookmarks.createOrUpdate(currentUser, bookmark.entry, comment)).right
      editedBookmark <- repository.Bookmarks.find(bookmarkId).toRight(BookmarkNotFoundError).right
    } yield editedBookmark
  }

  def list()(implicit ctx: Context): List[Bookmark] =
    repository.Bookmarks.listAll(currentUser).toList

  def listPaged(page: Int, limit: Int)(implicit ctx: Context): List[Bookmark] = {
    require( page > 0 )
    require( limit > 0 )
    repository.Bookmarks.listPaged(currentUser, page, limit).toList
  }

  def delete(bookmarkId: Long)(implicit ctx: Context): Either[Error, Unit] = ctx.withTransaction {
    for {
      bookmark <- repository.Bookmarks.find(bookmarkId).toRight(BookmarkNotFoundError).right
    } yield repository.Bookmarks.delete(bookmark)
  }

  def deleteByUrl(url: String)(implicit ctx: Context): Either[Error, Unit] = ctx.withTransaction {
    for {
      entry <- repository.Entries.findByUrl(url).toRight(EntryNotFoundError).right
      bookmark <- repository.Bookmarks.findByEntry(currentUser, entry).toRight(BookmarkNotFoundError).right
    } yield repository.Bookmarks.delete(bookmark)
  }
}
```

#### 리포지토리 구현

- 데이터베이스 등과 데이터를 주고 받는 인프라층에 속하는 모듈
  - SQL을 실행하는 것은 리포지토리층만
  - 리포지토리의 메서드는 필요에 의해서 모델 오브젝트를 반환

```scala
package internbookmark.repository

import internbookmark.repository
import internbookmark.model.{Entry, Bookmark, User}
import scala.concurrent.ExecutionContext.Implicits.global
import org.joda.time.LocalDateTime
import slick.driver.MySQLDriver.api._
import slick.jdbc.GetResult
import com.github.tototoshi.slick.MySQLJodaSupport._

object Bookmarks {

  private case class BookmarkRow(id: Long, userId: Long, entryId: Long, comment: String, createdAt: LocalDateTime, updatedAt: LocalDateTime) {
    def toBookmark(user: User, entry: Entry): Bookmark =
      Bookmark(id, user, entry, comment, createdAt, updatedAt)
  }

  private implicit val getBookmarkRowResult = GetResult(r => BookmarkRow(r.<<, r.<<, r.<<, r.<<, r.<<, r.<<))

  def createOrUpdate(user: User, entry: Entry, comment: String)(implicit ctx: Context): Unit =
   findByEntry(user, entry) match {
     case Some(bookmarkRow) =>
       val updatedAt = new LocalDateTime()
       run(sqlu"""
         UPDATE bookmark
           SET
             comment = $comment,
             updated_at = $updatedAt
           WHERE
             id = ${bookmarkRow.id}
       """.map(_ => ()))
     case None => {
       val id = Identifier.generate
       val bookmark: Bookmark = Bookmark(id, user, entry, comment, new LocalDateTime(), new LocalDateTime())
       run(sqlu"""
         INSERT INTO bookmark
           (id, user_id, entry_id, comment, created_at, updated_at)
           VALUES
           (
             ${bookmark.id},
             ${bookmark.user.id},
             ${bookmark.entry.id},
             ${bookmark.comment},
             ${bookmark.createdAt},
             ${bookmark.updatedAt}
           )
       """.map(_ => ()))
     }
   }

  def delete(bookmark: Bookmark)(implicit ctx: Context): Unit = {
    val _: Int = run(sqlu"""DELETE FROM bookmark WHERE id = ${bookmark.id} """)
  }

  def findByEntry(user: User, entry: Entry)(implicit ctx: Context): Option[Bookmark] = run(
    sql"""
      SELECT * FROM bookmark
        WHERE user_id = ${user.id} AND entry_id = ${entry.id} LIMIT 1
    """.as[BookmarkRow].map(_.headOption.map(_.toBookmark(user, entry)))
  )

  def find(bookmarkId: Long)(implicit ctx: Context): Option[Bookmark] = for {
    bookmarkRow <- run(sql"""
      SELECT * FROM bookmark
        WHERE id = $bookmarkId LIMIT 1
    """.as[BookmarkRow].map(_.headOption))
    entry <- repository.Entries.find(bookmarkRow.entryId)
    user <- repository.Users.find(bookmarkRow.userId)
  } yield bookmarkRow.toBookmark(user, entry)

  ...
}
```

- 처음부터 다 구현하려면 어렵다?
  - 대안1: 일단 테스트부터 작성해본다
  - 대안2: 일단 가장 밖(추상화된 부분)을 작성해본다
- REPL에서 실행해보면서 조금씩 만들어본다

### 프로그램의 설계 요약

- 레이어 아키텍처를 의식
- `레포지토리`에는 DB에의 접근을 작성
  - 모델로부터 DB에 접근하지 않음
- 모델은 테이블의 행을 표현
- 서비스에서 애플리케이션의 코어 로직을 구현
- `scala-Intern-Bookmark`를 잘 읽어보자

## 테스트

- 작성한 프로그램은 잘 동작하는가?
  - 소규모는 그냥 동작을 보고 유추 가능
    - 대규모 시스템에서는 무리
  - 코드의 변경 영향을 완전히 파악하는 것은 무리
    - 의도하지 않은 다른 기능에 장애를 야기하지 않는가(리액션)
  - 타인의 코드의 의도를 파악하기 힘듬
    - 옛날의 자기자신도 타인임(보통 하룻밤 지나면 타인이 됨)

### 테스트 해야하는 것들

- 올바른 조건에서 올바르게 동작할 것
- 이상한 조건에서 올바르게 동작할 것
  - 에러를 내는 등
- 경계 조건에서 올바르게 동작할 것

### 테스트용 패키지를 작성해두면 편리함

- 모든 테스트용 스크립트로부터 임포트함
- 사전 조건을 설정하는 유틸리티 작성(유저를 만듬, 엔트리를 준비함 등)
- HTTP 접근 없는 플래그를 세움 등등

### 마음가짐: 테스트는 안심해서 실행 할 수 있도록

- 진짜 서비스의 DB에 접근하지 않도록 함
  - 테스트 전용의 DB를 준비하여, 테스트에서는 반드시 그것을 사용하도록 함
  - `test.conf`
- 외부와의 통신을 발생시키지 않음
  - 테스트의 고속화 / 자동화에 이어짐
