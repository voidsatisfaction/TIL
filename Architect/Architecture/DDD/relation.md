# 관계의 정의

"어떠한 것"을 리포지토리에 의해서 가져오는 것은 가능합니다만, 그것만으로는 단순히 "어떠한 것"이 있는것을 나타내는 것에 지나지 않습니다. 실제의 "어떠한 것"은 다른 "어떠한 것"과 서로 관계를 갖고 있습니다. 도메인 모델을 제대로 표현하기 위해서는, 이 "어떠한 것"사이의 관계도 코드로 표현 해야만 합니다.

예를들면, 복수의 북마크의 URL을 취득하는 다음과 같은 코드를 생각해봅시다.

```scala
val bookmarks: Seq[BookmarkEntity] = ...
val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  bookmarks.flatMap { b =>
    locationLoader.find(b.id.locationId).map((b, _.url))
  }
```

만일 위의 코드가 도메인의 밖, 예를들어 애플리케이션 서비스의 코드라고 하면, 그다지 좋지 못한 코드가 됩니다. 가장 큰 문제는, "북마크의 URL이란, 공통하는 로케이션ID를 갖는 로케이션 URL필드 이다"라는, 북마크와 로케이션의 두 모델이 관계하는 것에 의하여 정의되는 모델상의 개념이, 애플리케이션층에 유출되어 버리는 것 입니다. 원래는, 북마크와 로케이션 및 로케이션의 URL이 어떻게 관계하고 있는가 아는 것은, 도메인층 만으로, 애플리케이션층 에서는 "북마크에 대응하는 URL을 알고싶다"고 도메인층에 문의하는 것 만으로 끝나도록 해야 합니다.

이 코드에는 또 하나 간과할 수 없는 문제가 있습니다. `locationLoader.find()`을 `bookmarks.map()`안에서 매번 호출하고 있으므로, 인프라 층에서는 북마크의 개수만큼 SQL의 `SELECT`가 발행되어 버리는 것 입니다. 원래는, `locationLoader.findAll()`로 모든 북마크의 대응하는 로케이션을 모아서 취득하면 `SELECT`는 1번으로 끝나는데 말이죠.

이러한 포인트를 염두에 두어, "어떠한 것"과 "어떠한 것"의 관계를 도메인층에서 어떻게 잘 추상화하여, 효율 좋은 구현으로 만들어가는가를 봅시다.

- 이제까지의 문제
  - N+1쿼리 문제
  - 비대화한 모델
- 해결책
  - 해결의 대상의 타입을 한정함
  - 관계 해결의 확장 메서드
- 구현
  - 관계하는 "어떠한 것"을 취득함
  - 관계하는 "어떠한 것"을 이어줌
    - 짝으로 이어줌
    - 필드를 확장함
  - 관계하는 "어떠한 것"이 반드시 있는 경우

## 이제까지의 문제

이제까지도 "어떠한 것"(모델)사이의 관계를 추상적으로 정의한 시도는 많이 있었습니다. 예를들면, Ruby on Rails의 Active Record에는 어소시에이션의 기능이 있습니다. 사내에서는 과거 이용되어온 `DBIx::MoCo`에 닮은 기능이 있습니다. 이러한 방법들은 모델의 관계를 손쉽게 다루는 수단을 제공하고 있습니다만, 몇가지 문제를 갖고 있었습니다.

### N+1 쿼리 문제

관계형 데이터베이스를 사용하여 관계를 해결하는 경우에 공통하는 문제로서 "N+1쿼리 문제"라고 불리는 것이 있습니다. 앞서 말한 예에 있었던 필요 없는 `SELECT`가 발행되어 버리는, 문제가 바로 그것입니다.

앞서의 예에서, 발행되는 SQL의 쿼리를 작성해 봅시다.

```scala
val bookmarks: Seq[BookmarkEntity] = ...
// SELECT * FROM bookmark WHERE ...

val bookmarksWithUrl: Seq[(BookmarkEntity, URL)] =
  bookmarks.flatMap { b =>
    locationLoader.find(b.id.locationId).map((b, _.url))
    // SELECT * FROM location WHERE location_id = $locationId (x N)
  }
```

가장 먼저 북마크의 리스트 취득을 위해서 1회 쿼리가 발행되어, 그 위에 로케이션을 가져오고 있습니다만, 이는 `bookmarks.map()`안에서 실행되는 것이므로 `bookmarks`의 사이즈 N횟수 만큼 반복되어, 결국 쿼리의 발행횟수는 N+1이 됩니다.

로케이션을 가져오는 부분은 원래 다음의 쿼리로 전부 가져올 수 있었으므로, 전체 쿼리의 발행수는 2번으로 끝났어야 합니다

```sql
SELECT * FROM location WHERE location_id IN ($locationIds)
```

RoR의 Active Record나 `DBIx::MoCo`등과 같은 높은 레이어의 OR맵퍼를 사용하면, 실제 쿼리가 너무나도 은폐되어 버려서 이러한 문제를 발견하기 힘들게 됩니다. 특히, 모델에 대한 메서드가 루프 속에서 호출되어 되는지 안되는지, 겉으로 봐서는 구별이 불가능하게 됩니다.

### 비대화 하는 모델

`DBIx::MoCo`등의 이제까지의 방법으로는, 관계의 해결을 위한 메서드를 모델 자신이 갖게 됩니다. 이는 "어떤 관계인지 아는 것은 도메인층"이라는 사상에는 맞습니다만, 그와 동시에 모델으로부터 리포지토리에의 직접 접근을 허용하는 것으로되어, 적어도 두가지의 문제를 낳을 위험이 있습니다.

- 원래 서비스가 행해야 할 역할을 모델이 짊어지게 되는 것에 대한 방지책이 없어짐
- 모델이 상태나 부작용을 갖으며 단독 테스트가 힘들어짐

모델로부터 리포지토리에의(읽기/쓰기) 접근이 가능하게 되면, 그 모델을 인자로 둔 도메인 서비스, 애플리케이션 서비스의 메서드로 구현 해야만 하는 처리를 무엇이든 모델의 메서드로서 구현해버리는 것이 가능하게 됩니다. 이를 방지하기 위해서는, 무엇인가 모델의 메서드가 되어야만 하고, 무엇인가 도메인 서비스나 애플리케이션 서비스의 메서드야 하거나 항상 주의 하여, 잘못된 추상화를 피하지 못하면 리뷰에서 지적할 필요가 있습니다. 그러나 모델은 원래부터 리포지토리 접근을 동반하고 있으므로, 모델이 해도 되는 조작의 구분은 애매하게 되어, 애매한 기준으로 우연히 리뷰를 통과해버려서, 그 뒤의 개발이 파탄나 버리게 됩니다.

- (예시) 매우 거대하게 된 모델
  - 무려 4404줄......

또한, 모델 그 자체가 읽고 쓰기 둘다 조작을 하게 되면, 단독 테스트가 매우 어렵게 됩니다. 예를들면, 어떤 서비스 A의 메서드의 안에 다른 서비스 B에 모델을 넘겨줄 때, A의 단독 테스트를 할 때 B의 안에서 모들의 상태가 변화할 수 있는지 어떤지 주의를 할 필요가 있게 되어버립니다. 혹은, 어떠한 모델을 테스트하기 위해서 테스트 데이터를 넣어두고 싶은경우, 그 모델의 메서드로부터 줄줄이 소세지 식으로 참조될 가능성이 있는 다른 여러가지 모델을 위해서 데이터도 넣어둘 필요가 생겨버려, 대체 어디까지의 범위의 데이터를 준비해 두어야 제대로 테스트가 가능한지 파악하는 것이 곤란하게 됩니다.

- (예시) 광범위한 데이터를 고려로 둔다

하테나 에픽 이후의 프로젝트 에서는, 이러한 문제를 해결하기 위해서 모델을 단순한 불변 오브젝트로서 다루는 수법을 채용 했습니다. 이 프로젝트에서의 엔티티나 값 오브젝트도 이 발상에 따르고 있다고 말할 수 있습니다. 그렇다고는 하나, 모델을 단순한 불변 오브젝트로 하는 것 만으로는, 모델 사이의 관계등 원래 도메인 모델로서 추상화 되어야 하는 것을 방치해버리는 것으로 됩니다.

## 해결책

이 프로젝트에서는 위의 문제들을 대처하기 위해서 두가지 수법을 조합하여 모델 관계의 정의에 이용하고 있습니다.

- 해결 대상의 타입을 한정함
- 확장 메서드에 의한 구현