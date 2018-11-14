# binary file processing

- 문제
- 설명
- 언어별 프로세싱 방식

## 문제

`fp` 확장자를 갖는 바이너리 파일을 주어주고 코딩테스트를 하는 기업이 있었다. 당시 나는 바이너리 파일을 다뤄보지 않았으므로 매우 당황했으나 결국은 어떻게 프로세싱하는지 하나하나 찾아봐서 알게 되었다.

## 설명

언어마다 다양한 바이너리파일 파싱을 지원한다. 다만, 그것을 단순 버퍼로 제공하는지 아니면 구조체와 같은 형식으로 파싱가능한지는 별개. 그리고 데이터를 빅엔디안으로 파싱하는지 빅 엔디안으로 파싱하는지는 데이터가 어떻게 저장되었는지에 따라 다르다.

1바이트씩을 저장하는 배열에 보통 저장이 됨(버퍼)

## 언어별 프로세싱 방식

### nodejs

```js
function parseBinaryFile(filePath) {
  const fileName = filePath.split('/')[filePath.split('/').length - 1]
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, (err, buffer) => {
      if (err) {
        reject(err)
        return
      }

      const binaryStrings = []

      buffer // 여기서는 바이너리 데이터가 됨
      buffer[0] // 바이너리 데이터의 가장 첫 1바이트 참조, 이렇게 바이너리 데이터를 배열처럼 쉽게 접근 가능, reverse와 같은 api도 사용가능
      // 리틀엔디안으로 되어있으므로, 데이터 chunk마다 읽는 순서가 중요.
      // e.g 32비트 정수를 읽을 때는 수의 경계 오른쪽끝 에서부터 왼쪽 4개를 순서대로 읽어야 함

      resolve({ ... })
    })
  })
}
```

- 버퍼를 이진수로 바꿀 때는, `.toString(2)` 이런 식으로 변환 가능

### golang

```go

type DocData struct {
	Version [16]byte
	NumCode byte
	Codes   []uint32
}

func main() {
	path := "./dataset/test_data/21_test.fp"

	file, err := os.Open(path)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	docData := DocData{}

	err = binary.Read(file, binary.LittleEndian, &docData.Version) // 16바이트 Version로 파싱
	err = binary.Read(file, binary.LittleEndian, &docData.NumCode) // 1바이트 NumCode로 파싱
	temp := make([]uint32, 0, int(docData.NumCode))
	for i := 0; i < int(docData.NumCode); i++ {
		var num uint32
		binary.Read(file, binary.LittleEndian, &num) // byte를 uint32로 파싱
		temp = append(temp, num)
	}
	docData.Codes = temp

	fmt.Printf("%+v %d\n", docData)
}
```
