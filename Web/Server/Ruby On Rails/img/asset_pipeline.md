# Asset pipeline

## Asset directories

### 1. app/assets

현재 어플리케이션의 assets

### 2. lib/assets

dev team에서 쓴 assets

### 3. vendor/assets

제삼자 vendors의 assets

## Manifest files

`app/assets/stylesheets/application.css`

```css
/*
 * This is a manifest file that'll be compiled into application.css, which
 * will include all the files listed below.
 *
 * Any CSS and SCSS file within this directory, lib/assets/stylesheets,
 * vendor/assets/stylesheets, or vendor/assets/stylesheets of plugins, if any,
 * can be referenced here using a relative path.
 *
 * You're free to add application-wide styles to this file and they'll appear
 * at the bottom of the compiled file so the styles you add here take
 * precedence over styles defined in any styles defined in the other CSS/SCSS
 * files in this directory. It is generally better to create a new file per
 * style scope.
 *
 *= require_tree .
 *= require_self
 */
```

`require_tree .`가 이 폴더 내부의 모든 css를 import한다.

그리고 마지막에 application.css도 자기자신의 import하여 하나의 큰 css파일을 만든다.

## Preprocessor engines

모든 assets를 조합한 후, rails는 다른 여러 preprocessing engines를 실행하므로써 site template를 구성하는데에 준비한다.

개발자는 `filename extension`을 이용하여 어떠한 processor가 사용하게 되는지 정한다.

process
- Sass(.scss)
- CoffeeScript(.coffee)
- ERb(.erb)

preprocessor engines는 chain될 수 있다.

따라서 다음과 같은 파일은 유효하다.

`foobar.js.erb.coffee`

순서는 오른쪽에서 왼쪽(coffee -> erb -> js)

## Efficiency in production

production app에 맞춰진 최적화.

파일이 하나일때, 더 로딩시간이 적음 + `minify`
