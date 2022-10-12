# 효율적으로 안전하게 Dockerfile을 만들기 위해서

## 참조

- [효율적으로 안전하게 Dockerfile을 만들기 위하여](https://qiita.com/pottava/items/452bf80e334bc1fee69a)

## 내용

1. 베이스가 되는 Docker image를 정한다.
2. `docker run -it <docker-image> /bin/bash`로 컨테이너 내부에서 작업 한다(모든 패키지는 y로 통일되어야 함을 유의)
3. 한 줄 씩실행해 보고 잘 작동하면 메모해둔다.
4. 실패하면 일단 `exit`해서 다시 `docker run`을 해본다(잘 되는 것들은 일단 `docker commit`해두는 것이 중요)
5. 옵션과 함께 `docker run`이 필요한 케이스가 있는데, 그럴때는 `docker run -it -v $(pwd):/tmp/share imageName /bin/bash`와 같이 볼륨을 생성하는것도 좋다.
5. 모두 잘 되면 Dockerfile로 완성한다.
