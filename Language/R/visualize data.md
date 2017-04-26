## 기본통계량과 가시화

### 기본통계량

통계해석의 기본 : 모집단의 확률분포

연속변량 => 정규분포

계산 데이터 => 포아슨분포

위와 같은 경우의 수로 모집단의 확률분포를 가정한다.

확률분포를 결정하는 값 = 모수(parameter)

정규분포의 parameter : 모평균 + 모분산

포아슨분포의 paramter : 모평균, 모분산

통계해석은 표본으로부터 이러한 parameter를 추정하는 것이다.

정규분포의 경우 : 모평균 => 표본평균 / 모분산 => 표본으로부터의 불편분산(不偏分散)

R에서는 모평균의 추정값 => mean() / 모분산의 불편분산 => var()로 구할 수 있다.

### 정규 난수의 발생

```R
# 일괄난수
runif(n=데이터수,min=하한값,max=상한값)
rnorm(n=데이터수,mean=평균,sd=표준편차)
rpois(n=데이터수,lambda=람다값)

# 평균=0 표준편차=1의 정규난수를 1000건 생성하여 평균, 분산, 표준편차를 구한다.
n <- 1000
x <- rnorm(n,mean=0,sd=1)
mean(x) var(x) sd(x) # 평균 분산 표준편차

# summary오브젝트로 기본통계량을 표시한다.
summary(x)
```

### 예제 데이터

```R
# 예제 데이터의 리스트
data()

# 예제 데이터의 개요
help(airquality)

```

### NA값 제외
```R
na.omit(데이터프레임)
데이터프레임이름[complete.cases(데이터프레임이름),]

dt <- na.omit(airquality)
```

### 데이터의 가시화 / 그래프의 작성

단일변수 데이터 분포 : 히스토그램, 箱ひげ図
2변수의 데이터 분포에 : 산포도

이하의 예 : airquality의 오존농도(airquality$Ozone)에 대한 그래프 작성.

#### 1. 히스토그램
```R
dt <- na.omit(airquality)
hist(dt$Ozone)

# 주요 parameter
# main : 표제
# xlab : x축 라벨
# xlim : y축 라벨
# ylim : x축의 범위지정
# col : 색 지정

# parameter를 지정한 히스토그램
hist(dt$Ozone,main="オゾン濃度のヒストグラム",xlab="オゾン濃度(ppm)",ylab="頻度",col="lightblue",xlim=c(0,200),ylim=c(0,40))

# 히스토그램 계급폭의 설정
# e.g 오존농도 150ppm이하의 데이터에 대해서, 계급폭 10ppm으로 표시

Oone150 <- dt$Ozone[dt$Ozone<150]
bk <- seq(0,150,by=10)
hist(Ozone150,breaks=bk,main="オゾン濃度ヒストグラム",xlab="オゾン濃度(ppm)",ylab="頻度",col="lightblue")

```

> mac에서는 그래프 함수를 사용하기 전에 par(family="Osaka") or par(family="HiraKakuProN-W3")과 같이 폰트 지정이 필요하다.
> 또한, utf-8에러가 처음부터 나지 않는지 확인해야한다.

#### 2. 파일 출력
```R
# png
png("출력파일명.png",width=값,height=값,res=300,unit="cm")
par(family="Osaka")
그래프 그리는 함수
dev.off()

# Mac Yosemite에서 버그가발생. 해결방법은 아직 모름. 선생님에게 질문을.
```

#### 3. 箱ひげ図
```R
boxplot(dt$Ozone,main="オゾン濃度の分布",col="lightblue")

# 매월마다의 오존 농도의 箱ひげ図를 표시

dt$Month <- factor(dt$Month) # 연속변수를 이산변수로 변환.
boxplot(dt$Ozone ~ dt$Month, main="月ごとのオゾン濃度の分布",xlab="測定月",ylab="オゾン濃度(ppm)",col="lightblue")
```

#### 4. 산포도

2변수의 관계나 시간순서에 따른 데이터의 표시에 유효

```R
# plot(x축의 변수명, y축의 번수명, 그래프parameter)

# 자주 사용되는 parameter
# type
# "l" : 점을 직선으로 연결
# "b" : 점을 표시하여, 각각을 직선으로 연결
# "n" : 점도 직선도 표시하지 않음
# 디폴트 : 점만 표시

# pch 0 ~ 23

# 간단한 예
temp <- dt$Temp
ozone <- dt$Ozone
plot(temp,ozone)

# 복잡한 예
dt5 <- dt[dt$Month=="5",]
dt9 <- dt[dt$Month=="9",]

dtx <- c(min(dt$Temp),max(dt$Temp))
dty <- c(min(dt$Ozone),max(dt$Ozone))

# 전체 그래프의 묘사(데이터 플롯 x)
plot(
  dt5$Temp,dt5$Ozone,type="n",
  xlim=dtx,ylim=dty,main="5月と9月のオゾン濃度と気温の関係",
  xlab="気温",ylab="オゾン濃度"
)

# 데이터 플롯
points(dt5$Temp,dt5$Ozone,col="red",pch=16)
points(dt9$Temp,dt9$Ozone,col="blue",pch=17)

# 평균값, 표준편차 및 평균값 +- 표준편차의 값의 계산
TempMu <- mean(dt$Temp)
TempSD <- sd(dt$Temp)
OzoneMu <- mean(dt$Ozone)
OzoneSD <- sd(dt$Ozone)
TempR <- TempMu + c(-1,1)*TempSD
OzoneR <- OzoneMu + c(-1,1)*OzoneSD

# 평균값의 위치를 points로 표시
points(TempMu,OzoneMu,pch=4,lwd=2)

# 평균값 - 표준편차, 평균값 + 표준편차 를 직선으로 표시
segments(TempR[1],OzoneMu,TempR[2],OzoneMu,lwd=2)
segments(TempMu,OzoneR[1],TempMu,OzoneR[2],lwd=2)

# 범례의 표시
legend("topleft", legend=c("5月","9月",全体平均),col=c("red","blue","black"),pch=c(16,17,4))

```
