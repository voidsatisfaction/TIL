# Eslint & Prettier

- 의문
- Eslint
  - 설정 파일 (.eslintrc)
- Prettier
  - 설정 파일 (.prettierrc.json)

## 의문

## Eslint

참고: https://www.daleseo.com/eslint-config/

- 개요
  - 코드에 문제가 있는지 체크하는 툴

### 설정 파일 (.eslintrc)

.eslintrc.json 설정 파일의 예시

```json
{
  "root": true,
  "env": {
    "browser": true,
    "commonjs": true,
    "es6": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jsx-a11y/strict",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:@typescript-eslint/recommended",
    "plugin:testing-library/react",
    "prettier"
  ],
  "plugins": [
    "react",
    "react-hooks",
    "jsx-a11y",
    "import",
    "@typescript-eslint"
  ],
  "settings": {
    "import/resolver": {
      "typescript": {
        "alwaysTryTypes": true
      }
    },
    "react": {
      "version": "detect"
    }
  },
  "rules": {
    "no-console": "error",
    "import/prefer-default-export": "off"
  },
  "overrides": [
    {
      "files": "**/*.+(ts|tsx)",
      "parser": "@typescript-eslint/parser",
      "plugins": ["@typescript-eslint"],
      "extends": ["plugin:@typescript-eslint/recommended"]
    },
    {
      "files": ["**/__tests__/**/*", "**/*.{spec,test}.*"],
      "env": {
        "jest/globals": true
      },
      "plugins": ["jest", "jest-dom", "testing-library"],
      "extends": [
        "plugin:jest/recommended",
        "plugin:jest-dom/recommended",
        "plugin:testing-library/react"
      ]
    }
  ]
}
```

- 형식
  - `.eslintrc`를 파일 이름에 반드시 포함해야 함
    - e.g) `.eslintrc.json`, `.eslintrc.yaml`
  - `package.json`파일의 `eslintConfig` 속성을 통해서 eslint 설정도 가능
- 옵션
  - root
    - true인 경우, 상위 폴더의 eslint 파일을 참조하지 않음
  - plugins
    - 기본 rule 이외에 추가적인 rule을 사용할 수 있도록 함
      - rule자체를 추가 가능하게 한것임(custom rule도 생성가능하다는 뜻!)
      - e.g) "plugins": ["import", "react"]
    - npm
      - `eslint-plugin-*`
        - e.g) `eslint-plugin-import`, `eslint-plugin-react`
  - extends
    - 기업이나 다른 사람이 공개해놓은 rule에 대한 설정(warn, error, off)을 그대로 가져와서 base 설정으로 활용하기
      - e.g) "extends": ["airbnb"]
    - 대부분의 eslint 플러그인은 추천 설정을 제공함
      - e.g) "extends": ["plugin:import/recommended", "plugin:react/recommended"]
    - npm
      - `eslint-config-*`
  - rules
    - rule 하나 하나를 세세하게 제어하고, extends를 override함
  - env
    - runtime에서 기본적으로 제공되는 전역 객체에 대해서 설정을 통해 알려줌
      - e.g) eslint로 lint할 코드가 자바스크립트 브라우저에서 실행될 수 있고, nodejs에서도 실행될 수 있는경우
      - `"env": { "browser": true, "node": true }`
  - parser, parserOptions
    - 타입스크립트, JSX와 같이 자바스크립트의 확장문법으로 개발하거나, Babel과 같은 transpiler를 통해 최신 문법을 통해 개발하는 경우, eslint는 순수 자바스크립트만 이해 가능하므로, js parser가 있어야 제대로 lint가능함
  - settings
    - eslint plugin의 추가적인 설정이 가능하게 함
    - e.g) `react`플러그인이 프로젝트에 설치된 리액트 버전을 자동탐지 가능하게 함
  - ignorePatterns
    - `node_modules`폴더나, `.`로 시작하는 설정 파일 이외의 다른 파일이나 폴더를 무시하는 방법
    - e.g) `"ignorePatterns": ["build", "dist", "public"]`
    - `.eslintignore`파일을 생성해도 됨
  - overrides
    - 프로젝트 내에서 일부 파일에 대해서만 살짝 다른 설정을 적용하고 싶을 때 사용함
    - e.g)
      - js파일과 ts파일이 공존할 경우, js파일은 js기준 설정, ts파일은 parser plugin과 다른 설정을 적용

## Prettier

- 개요
  - 코드를 자동으로 포맷팅 해주는 툴
- 주의
  - eslint와 설정이 충돌되지 않도록, eslint의 extends 옵션에 `eslint-config-prettier`를 npm install --save-dev 이후 설정해줘야 함

### 설정 파일 (.prettierrc.json)

```json
{
  "tabWidth": 2,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": false,
  "bracketSpacing": true
}
```