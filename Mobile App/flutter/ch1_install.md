# CH1. 개발 환경 세팅

## 0. 기본 설치

- MAC
  - Iterm2 설치하기

## 1.1 설치

- [설치](https://flutter.dev/docs/get-started/install)
  - 각자 컴퓨터에 맞는 OS를 선택

### MAC

- 1 Get the Flutter SDK에 있는 `flutter_macos_...-stable.zip`를 바탕화면에 클릭해서 다운로드
- 2 binary file Path 추가
  - 이 부분은 안중요하므로, 그냥 따라하라고 하거나, 직접 해주기
- 3 `flutter doctor`를 터미널에서 실행하기
  - Android studio
  - XCode
  - VSCode

## 2. 첫 예시

### Flutter

- Material app
  - 모바일과 웹의 표준 디자인 언어(스펙같은 느낌)
- Flutter는 Material 다양한 widget의 집합을 제공

### Stateful Widget

- `StatefulWidget` class
  - immutable and can be thrown away and regenerated
- `State` class
  - persists over the lifetime of the widget

### Simple example code

```dart
import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

// pubspec.yaml
// // publication spec definition

// one line function or method uses =>
void main() => runApp(MyApp());

// extends StatelessWidget -> makes app itself a widget
// In flutter, almost everything is a widget(e.g alignment, padding, layout)
// Stateless widgets are immutable
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Startup Name Generator',
      home: RandomWords(),
    );
  }
}

// App
// -- Stateless Widget
// -- -- MaterialApp
// -- -- -- title
// -- -- -- home
// -- -- -- -- appBar
// -- -- -- -- -- title
// -- -- -- -- body
// -- -- -- -- -- child

// enforce privacy
// generic State class specialized for use with RandomWords
class _RandomWordsState extends State<RandomWords> {
  final _suggestions = <WordPair>[];
  final _biggerFont = TextStyle(fontSize: 18.0);

  Widget _buildSuggestions() {
    return ListView.builder(
      padding: EdgeInsets.all(16.0),
      // callback
      // called once per suggested word pairing
      itemBuilder: /*1*/ (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;
        if (index >= _suggestions.length) {
          _suggestions.addAll(generateWordPairs().take(10));
        }

        return _buildRow(_suggestions[index]);
      },
    );
  }

  Widget _buildRow(WordPair pair) {
    return ListTile(title: Text(pair.asPascalCase, style: _biggerFont));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Startup Name Generator'),
        ),
        body: _buildSuggestions());
  }
}

class RandomWords extends StatefulWidget {
  @override
  State<RandomWords> createState() => _RandomWordsState();
}

```
