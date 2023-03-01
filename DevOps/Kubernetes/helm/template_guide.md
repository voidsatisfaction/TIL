# 템플릿 가이드

- 의문
- flow control
  - 화이트스페이스 제어
  - 실제 예시1
  - 실제 예시2
  - 연습 예시1
  - 연습 예시2

## 의문

## flow control

### 화이트스페이스 제어

- `{{- ... -}}`
  - 앞`-`
    - 현재 내용을 앞줄 맨 뒤로 땡긴다
  - 뒤`-`
    - 뒷줄의 내용을 현재줄의 맨 뒤로 땡긴다
  - 양`-`
    - 앞`-` and 뒤`-` 합친것
      - if문에서는 블록을 대체하게 됨

### 실제 예시1

```yaml
{{- if .Values.externalSecret -}}
  {{- if semverCompare ">=1.24-0" .Capabilities.KubeVersion.GitVersion -}}
apiVersion: "external-secrets.io/v1beta1"
  {{- else -}}
apiVersion: "kubernetes-client.io/v1"
  {{- end }}
kind: ExternalSecret
metadata:
```

- `{{- if .Values.externalSecret -}}`
  - 앞-
    - 맨앞이므로 의미가 없음
  - 뒤-
    - 뒷줄을 앞줄로 데려오는 역할
- `{{- if semverCompare ">=1.24-0" .Capabilities.KubeVersion.GitVersion -}}`
  - 앞-
    - 결국 맨앞이므로 의미가 없음
  - 뒤-
    - 뒷줄을 앞줄로 데려오므로, 뒷줄이 맨앞이 됨
- `{{- else -}}`
  - 어차피 앞줄 혹은 뒷줄이 선택될 것이므로, 뒷줄을 앞줄로 추가하는게 바람직
    - 왜냐하면, 앞줄이 선택될 경우, `{{- end }}`블록을 한줄 위로 끌고와야 함
    - 뒷줄이 선택될 경우, `apiVersion: "kubernetes-client.io/v1"`를 맨위로 끌고가야 함
- `{{- end }}`
  - 뒷줄을 앞줄바로 뒤로 끌고가야 하므로

### 실제 예시2

```yaml
- backend:
    service:
    {{- if .Values.nexusProxy.svcName }}
      name: {{ .Values.nexusProxy.svcName }}
    {{- else }}
      name: {{ template "nexus.fullname" . }}
    {{- end }}
      port:
```

- `{{- if .Values.nexusProxy.svcName }}`
  - if의 결과로 나온 줄을 한줄 땡기기
- `{{- else }}`
  - 만약 else 앞줄이 선택될 경우, `{{- end }}`를 바로 뒷줄까지 땡기는 역할을 함
  - 만약 else 뒷줄이 선택될 경우, `name: ... `를 if 바로 뒷줄까지 땡기는 역할을 함
  - 주의
    - 여기서 `{{- else -}}`를 사용하게 되면, else 앞줄이 선택될 경우는 상관없는데, else 뒷줄이 선택될 경우에는 if의 같은줄 뒷쪽에 `name: ...`이 붙어버리는 결과가 나오므로 에러
- ``

### 연습 예시1

```yaml
  food: {{ .Values.favorite.food | upper | quote }}*
**{{- if eq .Values.favorite.drink "coffee" }}
  mug: true*
**{{- end }}
```

- 결과: 원하는 대로 렌더됨
- 위의 예시에서 *가 -에 의해서 삭제되는 whitespace를 나타냄
- 즉, 원하는 대로 food밑에 mug가 들어옴

### 연습 예시2

```yaml
  food: {{ .Values.favorite.food | upper | quote }}*
**{{- if eq .Values.favorite.drink "coffee" -}}*
**mug: true*
**{{- end -}}*
```

- 결과: `food: "PIZZA"mug:true`
  - 오른쪽 -가 그 줄의 뒤의 white space및 다음줄 앞의 whitespace를 다 지워버림
