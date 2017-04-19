## R Lecture basics

**R은 함수 지향형 언어이다.**

### sapply

일반 언어의 map과 같은 역할.
벡터의 원소를 훑고 지나가면서 lambda함수에 나타난 대로 각각의 요소를 변화시킴.

```R
x <- c(9.66,12.06,2.24,9.53,11.95,11.70,4.40,1.97,13.69,13.61)
n <- length(x)
u <- 1/n * sum(x) # 母平均
x_var <- (1/(n-1)) * ((sum(sapply(x, function(x){x^2}))) - (sum(x))^2/n) # 母分散

u # 9.081
mean(x) # 9.081
x_var # 20.61485
var(x) # 20.61485
```

### Vectorize

vector를 필터링할때 사용 가능.
아래의 func의 조건에 따라서 원소들을 솎아주고 그것으로 구성된 새로운 벡터를 생성.

```R
# assignment2

x <- runif(9999,0,1)
y <- runif(9999,0,1)
x_2 <- sapply(x, function(x){x^2})
y_2 <- sapply(y, function(y){y^2})
z <- 0
func <- function(x){ x < 1 }
k <- x_2 + y_2
z <- length((x_2+y_2)[Vectorize(func)(k)])
pi <- z * 4 / 9999
pi # 3.140714
```
