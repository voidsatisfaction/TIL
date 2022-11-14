# Helm

- 의문
- 개요
  - 주요 개념
  - 기본 명령어
- 차트
- 템플릿

## 의문

## 개요

### 주요 개념

- 차트
  - 헬름 패키지
    - 쿠버네티스 클러스터 내에서 애플리케이션, 도구, 서비스를 구동하는데 필요한 모든 리소스가 정의 되어있음
    - c.f) Homebrew의 포뮬러, apt dpkg, yum rpm 파일과 유사
- 저장소
  - 차트를 모아두고 공유하는 장소
  - c.f) purl의 CPAN 아카이브, 페도라 패키지 데이터베이스와 유사
- 릴리스
  - 클러스터에서 구동되는 차트의 인스턴스
    - 하나의 차트는 동일한 클러스터내에 여러번 설치될 수 있음

헬름은 쿠버네티스 내부에 차트를 설치하고, 각 설치에 대해 새로운 release를 생성
새로운 차트를 찾기 위해 헬름 차트 리포지토리를 검색할 수 있다

### 기본 명령어

- 차트 관련
  - `helm create PATH`
    - PATH에 helm 차트를 생성
  - 차트 템플릿 확인
    - `helm get manifest RELEASE_NAME [flags]`
      - 서버에 어떤 템플릿들이 설치되어 있는지 알아볼 수 있는 커맨드
    - `helm install --dry-run --debug`
      - 무엇이 생성되는지 확인할때 사용
  - `helm search [hub|repo] [package name]`
    - `helm search hub`
      - 여러 저장소들에 있는 헬름 차트들을 포괄하는 헬름 허브를 검색
    - `helm search repo`
      - 로컬 헬름 클라이언트에 추가된 저장소들을 검색
        - 퍼블릭 네트워크 접속 필요없음
  - `helm show values [CHART] [flags]`
    - 차트에 가능한 구성 옵션을 보기
    - e.g)
      - `helm show values`
- 차트 릴리스 설치 관련
  - `helm install [NAME] [CHART] [flags]`
    - e.g)
      - `helm install happy-panda stable/mariadb`
    - 설치 방식
      - 차트 저장소
      - 로컬 차트 압축파일(`helm install foo foo-0.0.1.tgz`)
      - 압축해제된 차트 디렉터리(`helm install foo path/to/foo`)
      - 완전한 URL(`helm install foo https://example.com/charts/foo-1.2.3.tgz`)
  - `helm upgrade [RELEASE] [CHART] [flags]`
    - 새로운 버전의 차트가 릴리스되었을때, 또는, 릴리스의 구성을 변경하고자 할 때 사용하는 명령어
    - e.g)
      - `helm upgrade --install gryphon-${PROJECT} vcnc/app-common -f deploy/charts/tada/${PROJECT}/values-${STAGE}.yaml --namespace ${NAMESPACE} --version ${VERSION} --debug`
  - `helm rollback <RELEASE> [REVISION] [flags]`
    - 이전 릴리스로 롤백
    - e.g)
      - `helm rollback prometheus-rules 5 -n monitoring`
  - `helm uninstall RELEASE_NAME [...] [flags]`
    - 릴리스 삭제
      - 릴리스 버전 및 관련 리소스 전부 삭제됨
    - e.g)
      - `helm uninstall happy-panda --keep-history`
        - 릴리스 히스토리는 살린채로 릴리스 제거
- 릴리스 관련
  - `helm history RELEASE_NAME [flags]`
    - 릴리스의 히스토리 조회
    - e.g)
      - `helm history prometheus-rules -n monitoring`
  - `helm status RELEASE_NAME [flags]`
    - 릴리스의 상태 추적 및 구성 정보 확인
  - `helm get values RELEASE_NAME [flags]`
- 저장소
  - 추가
    - `helm repo add [NAME] [URL] [flags]`
      - e.g)
        - `helm repo add dev https://example.com/dev-charts`
  - 조회
    - `helm repo ls`
  - 삭제
    - `helm repo remove`

## 차트

차트란

![](./images/helm/chart1.png)

차트 파일 구조

```yaml
wordpress/
  Chart.yaml          # 차트에 대한 정보를 가진 YAML 파일
  LICENSE             # (옵션) 차트의 라이센스 정보를 가진 텍스트 파일
  README.md           # (옵션) README 파일
  values.yaml         # 차트에 대한 기본 환경설정 값들
  values.schema.json  # (옵션) values.yaml 파일의 구조를 제약하는 JSON 파일
  charts/             # 이 차트에 종속된 차트들을 포함하는 디렉터리
  crds/               # 커스텀 자원에 대한 정의
  templates/          # values와 결합될 때, 유효한 쿠버네티스 manifest 파일들이 생성될 템플릿들의 디렉터리
  templates/NOTES.txt # 옵션: 간단한 사용법을 포함하는 텍스트 파일
```

Chart.yaml 파일 내부

```yaml
# Chart.yaml
apiVersion: 차트 API 버전 (필수)
name: 차트명 (필수)
version: SemVer 2 버전 (필수)
kubeVersion: 호환되는 쿠버네티스 버전의 SemVer 범위 (선택)
description: 이 프로젝트에 대한 간략한 설명 (선택)
type: 차트 타입 (선택)
keywords:
  - 이 프로젝트에 대한 키워드 리스트 (선택)
home: 프로젝트 홈페이지의 URL (선택)
sources:
  - 이 프로젝트의 소스코드 URL 리스트 (선택)
dependencies: # 차트 필요조건들의 리스트 (optional)
  - name: 차트명 (nginx)
    version: 차트의 버전 ("1.2.3")
    repository: 저장소 URL ("https://example.com/charts") 또는 ("@repo-name")
    condition: (선택) 차트들의 활성/비활성을 결정하는 boolean 값을 만드는 yaml 경로 (예시: subchart1.enabled)
    tags: # (선택)
      - 활성화 / 비활성을 함께하기 위해 차트들을 그룹화 할 수 있는 태그들
    enabled: (선택) 차트가 로드될수 있는지 결정하는 boolean
    import-values: # (선택)
      - ImportValues 는 가져올 상위 키에 대한 소스 값의 맵핑을 보유한다. 각 항목은 문자열이거나 하위 / 상위 하위 목록 항목 쌍일 수 있다.
    alias: (선택) 차트에 대한 별명으로 사용된다. 같은 차트를 여러번 추가해야할때 유용하다.
maintainers: # (선택)
  - name: maintainer들의 이름 (각 maintainer마다 필수)
    email: maintainer들의 email (각 maintainer마다 선택)
    url: maintainer에 대한 URL (각 maintainer마다 선택)
icon: 아이콘으로 사용될 SVG나 PNG 이미지 URL (선택)
appVersion: 이 앱의 버전 (선택). SemVer인 필요는 없다.
deprecated: 차트의 deprecated 여부 (선택, boolean)
annotations:
  example: 키로 매핑된 주석들의 리스트 (선택).
```

- 개요
  - 쿠버네티스 패키지 매니저
  - 쿠버네티스의 오브젝트 yaml파일을 템플릿으로 만들고 메타정보파일 등을 압축한 파일
    - 특정한 디렉터리 구조 속 파일들의 컬렉션으로 구성됨
    - e.g) `wordpress/`
      - `Chart.yaml`
      - `values.yaml`
      - `templates/`
- 저장소
  - artifacthub(~ dockerhub)
- 명령어
  - `helm install [이름] [경로]`
    - 차트를 k8s로 배포

## 템플릿

### 템플릿 함수

- [Sprig 함수들](https://masterminds.github.io/sprig/)
  - `trim`
  - `b64enc`
  - ...
- `include`
  - 템플릿을 가져오고, 결과를 다른 템플릿 함수로 넘겨줌
