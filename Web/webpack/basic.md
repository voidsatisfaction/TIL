# Webpack

## 참조

- [webpack.js 공식 사이트](https://webpack.js.org/concepts)

## 개념

웹팩은 modern javascript의 module bundler이다.

재귀적으로 어플리케이션의 의존관계를 파악하며 의존 그래프를 작성한 뒤, 많은 의존관계의 파일들을 작은 숫자의 bundlerjs로 변환해준다.

**Entry, Output, Loaders, Plugins**가 핵심 개념

### 1. Entry

의존성이 시작되는 곳을 지정한다(contextual root)

### 2. Output

어디에 번들을 놓을지 지정한다(how to treat bundle code)

### 3. Loaders

웹팩은 자바스크립트 밖에 이해하지 못하기 때문에, Loaders들을 사용해서 다른 타입의 파일들을 의존성 그래프에 넣을 수 있도록 변환시킨다. 두가지 구성으로 되어있다.

1. **어떤 파일**이 loader에 의하여 변환되어야 하는지 지정(test property)
2. 그 파일을 **어떠한 loader**로 변환시켜 의존성 그래프에 추가 될 수 있도록 하는지 지정(use property)

### 4. Plugins

Loaders가 filebase인 반면, Plugins는 compilations / chunk 베이스. 그 말인 즉, 번들된 js파일에 적용되는 변환을 말한다. `require`로 불러올 필요가 있다. `config`내에서 같은 plugin을 재활용 하는 경우도 있으므로, `new`를 사용하여 인스턴스를 생성해준다.

## 예제

```js
// webpack.config.dev.js
var path = require('path')
var webpack = require('webpack')
var HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  devtool: 'cheap-eval-source-map',
  entry: [
    './src/index'
  ],
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    loaders: [{
      test: /\.css$/,
      loaders: ['style-loader', 'css-loader']
    }, {
      test: /\.js$/,
      loaders: ['babel-loader'],
      include: path.join(__dirname, 'src') /* exclude: /node_modules/ */
    }]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({
      template: './src/index.html'
    })
  ],
  devServer: {
    contentBase: './dist',
    hot: true
  }
}
```
