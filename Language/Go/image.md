# Go Image Package

Go는 무려 이미지 프로세싱에 관한 패키지도 갖고 있다. 참으로 다재다능한 언어이다.

이번에 image package를 exif문제를 해결하는데에 사용하게 되었다.

## 참고

- [The Go image package - The Go Blog](https://blog.golang.org/go-image-package)
- [JPG파일 EXIF 데이터의 ORIENTATION 값의 뜻](http://www.sy34.net/ko/jpg%ED%8C%8C%EC%9D%BC-exif-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-orientation-%EA%B0%92%EC%9D%98-%EB%9C%BB-2/)
- [imaging - github](https://github.com/disintegration/imaging)

## Go의 Image Package

Go의 이미지 패키지에는 크게 Color와 Rectangle로 나뉘어 있다. 그리고 이 둘을 합친것을 Image라고 생각한다.

## exif의 orientation문제

자세한 것은 참고1의 `JPG파일 EXIF 데이터의 ORIENTATION 값의 뜻`확인

Exif란, jpg사진에 넣는 메타데이터로 `사진기 기종, 날짜, 크기, 노출, 장소, 사진이 찍한 방향(Orientation)`등의 정보를 기록할 수 있는 데이터이다. 이 중에서 Orientation이라는 항목이 있는데, 이는 사진이 찍힌 방향을 의미하며 일반적으로 우리가 스마트폰을 세워서 사진을 찍는 경우 이는 왼쪽으로 누워있게 찍는 것이 된다(왜냐하면 스마트폰은 가로로 찍는 것을 가장 베이스로 한다)

그래서 이를 웹사이트에 단순히 업로드 할 경우 웹앱은 이것을 그냥 왼쪽으로 눕힌채 업로드를 하게 되고 이는 사진 촬영자의 의도에 반하는 사진이 표시되게 한다.

그래서 웹앱은 Exif안의 Orientation을 참고해서 올바른 방향으로 보이게 업로드를 해야한다. 또한 브라우저가 Orientation을 보정하는 경우가 있으므로 사진을 Orientation에 기반하여 보정한 후에는 Exif 데이터를 지워주어야 이용자가 원하는 방향으로 이미지를 보여줄 수 있게 된다.

## 이미지 보정 코드

- 이미지 보정을 위하여 `imaging`이라는 go의 라이브러리를 사용하였다. 프로그래머가 수학을 잘 몰라도 쉽게쉽게 보정할 수 있도록 추상화가 잘 되어있다. 업데이트도 꾸준히 되고 있다.
- 또한 exif정보를 확인하기 위해서 `goexif2`라는 라이브러리도 사용하였다.

가끔가다가 orientation이 음수인 깨진 사진이 등록될 수 있는데, 그런 경우에는 Exif데이터를 지워주기만 한다.

```go
package main

import (
	"fmt"
	"image"
	_ "image/jpeg"
	"log"
	"os"
	"path"

	"github.com/disintegration/imaging"
	"github.com/xor-gate/goexif2/exif"
)

func main() {
	// Get Orientation
	fileNames := []string{
		"up.jpg", "up-mirrored.jpg", "down.jpg", "down-mirrored.jpg",
		"left-mirrored.jpg", "left.jpg", "right-mirrored.jpg", "right.jpg",
	}
	for _, fileName := range fileNames {
		filePath := path.Join("./test-img", fileName)
		f, err := os.Open(filePath)
		if err != nil {
			log.Fatal(err)
		}
		orientation, err := checkFileOrientation(f)
		if err != nil {
			fmt.Errorf("Failed Orientation get")
		}

		// Fix orientation and Delete Exif and Save
		fixOrientation(f, orientation)
	}
}

func checkFileOrientation(f *os.File) (int, error) {
	x, err := exif.Decode(f)
	if err != nil {
		log.Fatal(err)
	}

	tag, err := x.Get(exif.Orientation)
	if err != nil {
		return -1, err
	}

	orientation, err := tag.Int(0)
	if err != nil {
		return -1, err
	}
	return orientation, nil
}

func fixOrientation(f *os.File, orientation int) {
	transFunctions := map[int]func(image.Image) *image.NRGBA{
		-1: imaging.Clone,
		1:  imaging.Clone,
		2:  imaging.FlipH,
		3:  imaging.Rotate180,
		4:  imaging.FlipV,
		5:  imaging.Transpose,
		6:  imaging.Rotate270,
		7:  imaging.Transverse,
		8:  imaging.Rotate90,
	}
	f.Seek(0, 0)
	srcImage, err := imaging.Open(f.Name())
	if err != nil {
		fmt.Errorf("image open error!")
	}

	dstImage := transFunctions[orientation](srcImage)
	if err != nil {
		fmt.Errorf("Cannot make output file")
	}
	dst := fmt.Sprintf("test-img/example_%d.jpg", orientation)
	fmt.Println(dst)
	err = imaging.Save(dstImage, dst)
	if err != nil {
		fmt.Errorf("file save Error occured!")
	}
}
```
