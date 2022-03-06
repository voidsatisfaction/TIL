# Spring Coroutine

- 의문
- 개요

## 의문

## 개요

```kotlin
@RestController
class CoroutinesRestController(client: WebClient, banner: Banner) {

    @GetMapping("/suspend")
    suspend fun suspendingEndpoint(): Banner {
        delay(10)
        return banner
    }

    @GetMapping("/flow")
    fun flowEndpoint() = flow {
        delay(10)
        emit(banner)
        delay(10)
        emit(banner)
    }

    @GetMapping("/deferred")
    fun deferredEndpoint() = GlobalScope.async {
        delay(10)
        banner
    }

    @GetMapping("/sequential")
    suspend fun sequential(): List<Banner> {
        val banner1 = client
                .get()
                .uri("/suspend")
                .accept(MediaType.APPLICATION_JSON)
                .awaitExchange()
                .awaitBody<Banner>()
        val banner2 = client
                .get()
                .uri("/suspend")
                .accept(MediaType.APPLICATION_JSON)
                .awaitExchange()
                .awaitBody<Banner>()
        return listOf(banner1, banner2)
    }

    @GetMapping("/parallel")
    suspend fun parallel(): List<Banner> = coroutineScope {
        val deferredBanner1: Deferred<Banner> = async {
            client
                    .get()
                    .uri("/suspend")
                    .accept(MediaType.APPLICATION_JSON)
                    .awaitExchange()
                    .awaitBody<Banner>()
        }
        val deferredBanner2: Deferred<Banner> = async {
            client
                    .get()
                    .uri("/suspend")
                    .accept(MediaType.APPLICATION_JSON)
                    .awaitExchange()
                    .awaitBody<Banner>()
        }
        listOf(deferredBanner1.await(), deferredBanner2.await())
    }

    @GetMapping("/error")
    suspend fun error() {
        throw IllegalStateException()
    }

    @GetMapping("/cancel")
    suspend fun cancel() {
        throw CancellationException()
    }

}
```

- Spring Framework에서 제공하는 코루틴 서포트
  - Spring WebFlux의 `@Controller`어노테이션이 달린 곳에서의 `Deferred`, `Flow` 반환값
  - Spring WebFlux의 `@Controller`어노테이션이 달린 곳에서의 suspending function 서포트
  - WebFlux client, server API
  - *WebFlux.fn `coRouter{}` DSL*
    - 그냥 router를 만들때 사용되는 DSL인듯
