# python을 이용해서 s3에 정적 사이트 호스팅 하기

- 목차
  - 배경
  - 절차
  - 함정

## 배경

- plotly라는 라이브러리를 이용해서 html파일로 그래프를 생성할 수 있는데, 이 그래프를 정적으로 호스팅해서 웹으로 언제 어디서나 볼 수 있게 하려고 함
- 처음 후보는 github pages에 15분마다 subtree push하는 방법이었으나, 깃허브가 너무 지저분해져서 다른 방법을 찾음
- 그 다음 후보가 aws s3의 정적사이트 호스팅기능을 이용해서 15분마다 그래프 파일(html)을 생성해서 업로드 하는 방식

## 절차

- 그래프 파일 생성 python 스크립트 작성
- s3의 버켓 설정(공개 범위, 정적 호스팅 허가)
- 위의 스크립트를 15분마다 실행하고 aws s3의 앞서 생성한 버켓으로 디플로이 해주는 python 스크립트 작성

## 함정

- 문제1: `boto3`이라는 aws sdk를 사용하는데, `pip3 install boto3`해도 해당 라이브러리를 코드상에서 못 찾는 문제
  - `python -m pip install --user boto3`로 하니까 해결됐다. 근데 왜 이게 해결시키는지는 모름
- 문제2: 정적 호스팅을 위해서는 s3상의 파일의 메타데이터를 `Content-Type text/html`로 수정시키고, 파일을 공개해야 하는데, 이를 코드상으로 어떻게 구현하는가?
  - boto3 client를 바로 이용하지 않고, resources를 이용한다.
  - `data = open('index.html', 'rb')`
  - `html = bucket.put_object(Key='index.html', Body=data, ContentType='text/html')`
  - `x.put(Metadata={'Content-Type': 'text/html'})`
  - `html.Acl().put(ACL='public-read')`
