# WiX Toolset

- 의문
- 개요
- Getting Started
- 샘플 만들기

## 의문

- *Wix에서 GUID가 겹치면 무슨 일이 일어나는가?*

## 개요

- 윈도우즈 설치 패키지를 XML 코드로부터 빌드할 수 있게 도와주는 툴셋
  - 오픈 소스
  - C#으로 짜여져서, .NET 프레임 워크로 실행
- 배경
  - 윈도우 인스톨러의 관점 변화(imperative description -> declarative)
- 특징
  - declarative
  - Windows Installer 기능으로 불가능한 것이 없음
    - 대신 조금 많이 복잡하긴 함
  - GUI가 아닌, 보다 프로그래밍 적인 접근으로 패키징을 가능하게 함
  - XML 포맷으로, 설치 프로세스의 모든 요소를 기술
  - **메인 애플리케이션 개발과 Wix 패키징을 동시에 Integration한 개발이 가능**
    - **앱이 다 완성된 다음에 패키징 하지말고, 애초에 처음 개발할 때 부터 Wix source에 계속해서 component를 추가하면서 개발하라!**
    - Wix자체가 모듈화 가능
  - MS가 씀

## Getting Started

XML기반

- 가능한 행위(메인)
  - 애플리케이션 설치 프로세스 관리
  - data shortcuts
  - registry
  - .ini 파일 변경
  - 서비스
- helper files
  - dialogs
  - icons
  - 설치 UI를 위한 bitmaps
  - license
  - readme
  - Custom DLL
    - WiX가 할 수 없는 프로그래밍적인 행위

컴파일 구조

- `.wxs(원본)`파일 --(컴파일)-- `.wixobj(중간)`파일 --(컴파일)-- `.msi(패키지)`파일

주의

- **Wix source는 스크립트나 프로그래밍 언어가 아님(그저 기술(description))**
  - Windows Installer가 어떤 행위 해야할지 기술할 뿐(database approach)
    - 베포 하기 위한 `.msi`파일은 setup 애플리케이션이 아니라, Installation database임
    - 실제 조작하기 위한 모든 로직은 Windows Installer속에 있음
  - 따라서, 일반적인 프로그램 처럼 sequential execution이 아님
- **Wix 자체가 하나의 설치 환경이 아님**
  - Windows Installer로 번역될 XML 스타일의 편리한 기술법
    - Windows Installer로 실행될 수 있도록, compiler와 linker가 존재
  - 결국 Windows Installer의 얇은 추상화층

## 샘플 만들기

```xml
<?xml version='1.0' encoding='windows-1252'?>
<Wix xmlns='http://schemas.microsoft.com/wix/2006/wi'>
    <Product Name='Foobar 1.0' Manufacturer='Acme Ltd.'
        Id='YOURGUID-86C7-4D14-AEC0-86416A69ABDE'
        UpgradeCode='YOURGUID-7349-453F-94F6-BCB5110BA4FD'
        Language='1033' Codepage='1252' Version='1.0.0'>
    <Package Id='*' Keywords='Installer' Description="Acme's Foobar 1.0 Installer"
        Comments='Foobar is a registered trademark of Acme Ltd.' Manufacturer='Acme Ltd.'
        InstallerVersion='100' Languages='1033' Compressed='yes' SummaryCodepage='1252' />
```

- GUID
  - 개요
    - Windows가 패키지의 모든 부분을 인식하기 위한 식별자
  - 종류
    - Package GUID
      - 각 생성되는 패키지마다 다름
        - asterisk를 타이핑하므로써 WiX가 Package GUID만 자동 생성하게 함
- 형식
  - Product
    - Name: 마음대로
    - Version: `major.minor.build` format
  - Package
    - Description: 마음대로

## File Inside

- `EmbedCab`
- `Cabinet`
- outermost folder부터 시작, root diretory 폴더(모든 설치)

```xml
<!-- Id should be provided -->
<!-- Id should be unique (cross reference all across the WiX source file) -->
<Directory Id='TARGETDIR' Name='SourceDir'>
  <Directory Id='ProgramFilesFolder' Name='PFiles'>
    <Directory Id='Acme' Name='Acme'>
      <Directory Id='INSTALLDIR' Name='Foobar1.0'>
    </Diredtory>
  </Directory>
</Directory>
```

- Directory
  - `TARGETDIR`
    - source file tree의 가장 root가 되는 디렉토리
    - 여기서부터 모든 디렉터리 구조가 시작
  - `SourceDir`
    - predefined name
  - Shortcuts, desktop icons, user preference같은 친구들은 이미 predefined names를 갖고 있음
    - `ProgramFilesFolder`
    - `ProgramMenuFolder`
    - `DesktopFolder`
    - `INSTALLDIR`

```xml
<Wix>
  <Product>
    <Icon Id="Foobar10.exe" SourceFile="FoobarAppl10.exe" />
    <Component Id='MainExecutable' Guid='YOURGUID-83F1-4F22-985B-FDB3C8ABD471'>
      <File Id='FoobarEXE' Name='FoobarAppl10.exe' DiskId='1' Source='FoobarAppl10.exe' KeyPath='yes'>
        <!-- INSTALLDIR = Program Files\Acme\Foobar 1.0. (위의 코드 참고) -->
        <Shortcut Id="startmenuFoobar10" Directory="ProgramMenuDir" Name="Foobar 1.0" WorkingDirectory='INSTALLDIR' Icon="Foobar10.exe" IconIndex="0" Advertise="yes" />
        <Shortcut Id="desktopFoobar10" Directory="DesktopFolder" Name="Foobar 1.0" WorkingDirectory='INSTALLDIR' Icon="Foobar10.exe" IconIndex="0" Advertise="yes" />
      </File>
    </Component>

    <Component Id='HelperLibrary' Guid='YOURGUID-6BE3-460D-A14F-75658D16550B'>
        <File Id='HelperDLL' Name='Helper.dll' DiskId='1' Source='Helper.dll' KeyPath='yes' />
    </Component>

    <Component Id='Manual' Guid='YOURGUID-574D-4A9A-A266-5B5EC2C022A4'>
        <File Id='Manual' Name='Manual.pdf' DiskId='1' Source='Manual.pdf' KeyPath='yes'>
            <Shortcut Id='startmenuManual' Directory='ProgramMenuDir' Name='Instruction Manual' Advertise='yes' />
        </File>
    </Component>

    <Directory Id="ProgramMenuFolder" Name="Programs">
           <Directory Id="ProgramMenuDir" Name="Foobar 1.0">
               <Component Id="ProgramMenuDir" Guid="YOURGUID-7E98-44CE-B049-C477CC0A2B00">
                   <RemoveFolder Id='ProgramMenuDir' On='uninstall' />
                   <RegistryValue Root='HKCU' Key='Software\[Manufacturer]\[ProductName]' Type='string' Value='' KeyPath='yes' />
               </Component>
           </Directory>
       </Directory>

       <Directory Id="DesktopFolder" Name="Desktop" />
    </Directory>

    <!-- 이거 뭐하는 거임? -->
    <Feature Id='Complete' Level='1'>
        <ComponentRef Id='MainExecutable' />
        <ComponentRef Id='HelperLibrary' />
        <ComponentRef Id='Manual' />
        <ComponentRef Id='ProgramMenuDir' />
    </Feature>
  </Product>
</Wix>
```

- Component
  - 개요
    - 인스톨 될 대상의 최소한의 단위
      - 서로 크게 의존하고 있는 대상들만 포함하고 있어야 함
  - 구성
    - files
    - registry Keys
    - shortcuts
    - 등등
  - 특징
    - component의 설치는 다른 컴포넌트에 영향을 주지 않음
      - 따라서 삭제해도 다른 컴포넌트에 영향을 주지 않음
    - 파일을 공유하지 않음
  - 구현
    - 하나의 컴포넌트는 `Id` 식별자와 GUID를 갖고 있어야 함
    - key path가 필요함
      - Windows Installer가 component가 실제로 설치되었는지 확인할 때 사용
      - Uninstallation
      - repair 기능에 사용
  - 예시
    - file, 두개의 파일을 가르키는 shortcuts
- Features
  - 개요
    - 유저에게 install 할지 안할지 선택지를 주는 애플리케이션의 부분
- File
  - 속성
    - Vital
      - `no`로 설정되면, 인스톨러에게 해당 파일을 설치하는 것은 무조건적인것은 아니라는 것을 의미
      - 일반적으로는 파일을 설치하는 것이 실패하면, installation은 aborted됨
    - ReadOnly
    - Hidden
    - System
- Shortcuts
  - `Directory`
    - shortcut이 놓여지는 장소(Start menu, desktop)
  - `WorkingDirectory`
    - shortcut이 자리키는 장소
    - optional
      - 없는 경우, 파일이 설치되는 곳
  - `Icon`
    - The Icon attribute will allow us to specify the Id of an Icon tag specified somewhere else in the source rather than the actual filename
  - `Advertise`
    - *이거 뭔지 잘 모르겠음*
