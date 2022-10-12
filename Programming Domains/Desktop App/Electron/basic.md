# Electron basic

## Electron이란

Electron은 데스크탑 애플리케이션을 만들기위한 framework이다. Electron을 이용하여 데스크탑 어플리케이션을 만들 수 있도록 도와주는 기반 기술은 HTML CSS JS와 같은 웹 기술이므로, 개발자들은 오직 애플리케이션의 핵심 가치에 집중할 수 있도록 도와주고, 웹앱 개발자의 저변을 넓혀준다. 복잡한 os와의 커뮤니케이션은 electron이 처리하여 api를 사용하여 다룬다(nodejs api를 사용하는 경우도 있음)

웹 페이지 자체를 GUI로서 제공한다(크로미움 이용)

장점은 다음과 같다.

1. 크로스 플랫폼(Windows, MacOS, Linux)
2. local file system이용가능
3. 자동 업데이트
3. 웹의 거대한 커뮤니티를 등에 업고 있다(Electron은 크로미움 + nodejs로 만들어져 있다)
4. 오픈소스

## Framework Architecture

### Main Process

`package.json`의 `main`스크립트가 **main process**라고 불린다.

웹 페이지를 생성하여 **GUI의 책임을 담당**

### Renderer Process

Chromium의 multi-process architecture이 사용된다. Electron의 각각의 웹 페이지는 각자의 process를 소유하는데, 이를 `renderer process`라 한다.

Electron에서는 Node.js API를 사용할 수 있어서 저레벨의 os와의 상호작용이 가능하다.

### Main Process와 Renderer Process의 차이

Main process

- `BrowserWindow`인스턴스들을 생성하므로써 웹 페이지 생성
- 각각의 `BrowserWindow`인스턴스는 각자의 `renderer process`에서 웹 페이지를 실행
- `BrowserWindow`인스턴스가 파괴되면, 그에 상응하는 `renderer process`역시 사라짐
- 모든 웹페이지들과 각각의 renderer process들을 관리한다.

Renderer Process

- 특정 웹피이지만을 관리

둘의 커뮤니케이션은 `ipcRenderer`과 `ipcMain`모듈을 사용하여 서로 메시지를 RPC방식으로 주고 받을 수 있다.

c.f 페이지간의 데이터 공유는 HTML5의 `Storage API`, `localStorage`, `sessionStorage`, `IndexedDB`를 이용하는 방법이 있다. 또한 IPC시스템을 이용하여, main process에 global variable로 저장하고 renderer들이 필요할 때 마다 이용하는 방식도 있다.
