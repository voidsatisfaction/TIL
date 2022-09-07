# Mysql Charset

- 의문
- 개요
  - 유니코드

## 의문

## 개요

### 유니코드

- utf8mb4
  - 개요
    - 1-4바이트 유니코드 인코딩
  - 특징
    - BMP(1-3바이트) + supplementary(4바이트) 서포트
- utf8mb3 = utf8
  - 개요
    - 1-3바이트 유니코드 인코딩
  - 특징
    - BMP만 서포트
- utf16
  - 개요
    - 2,4 바이트로 유니코드 인코딩
    - 빅 인디안
  - 특징
    - BMP(2바이트) + supplementary(4바이트) 서포트
- utf16le
  - 개요
    - utf16이지만 리틀인디안
  - 특징
    - BMP(2바이트) + supplementary(4바이트) 서포트
