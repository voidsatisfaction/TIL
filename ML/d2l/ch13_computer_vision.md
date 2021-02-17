# Ch13 Computer Vision

- 의문
- 13.1. Image Augmentation

## 의문

## 13.1. Image Augmentation

- 배경
  - 성공적인 모델의 학습을 위해서 이미지셋을 늘리는것이 반드시 필요함
- 개요
  - training dataset에 몇가지 random change를 주므로써, 유사 하지만 다른 이미지를 traning example을 생성해서 training dataset의 개수를 늘리는 기술
    - 결국 overfitting을 줄이는 기술
  - 예시
    - image를 다른 위치에서 crop해서, 모델이 object의 position에 대한 dependency를 줄임
    - image의 밝기를 조절해서, 모델이 color sensitivity에 대한 dependency를 줄임
- 대표적인 방법
  - Flipping and Cropping
  - Changing the Color

### 13.1.1. Common Image Augmentation Method

Image augmentation: color change

![](./images/ch13/image_augmentation_color1.png)

```python
# 50% horizontal flipping
torchvision.transforms.RandomHorizontalFlip()

# 50% vertical flipping
torchvision.transforms.RandomVerticalFlip()

shape_aug = torchvision.transforms.RandomResizedCrop(
  (200, 200), scale=(0.1, 1), ratio=(0.5, 2)
)

# changing the color (H, S, V, Contrast)
color_aug = torchvision.transforms.ColorJitter(
  brightness=0.5, contrast=0, saturation=0, hue=0)
)

# multiple image augmentation methods
torchvision.transforms.Compose([
  torchvision.transforms.RandomHorizontalFlip(),
  color_aug,
  shape_aug
])
```

### 13.1.2 Using an Image Augmentation Training Model

```python
def load_cifar10(is_train, augs, batch_size):
    dataset = torchvision.datasets.CIFAR10(root="../data", train=is_train,
                                           transform=augs, download=True)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size,
                    shuffle=is_train, num_workers=d2l.get_dataloader_workers())
    return dataloader
```

- `torch.utils.data.DataLoader`를 사용해서 데이터 로드
  - 그 전에 데이터셋을 image augmentation object를 이용해서 aug된 상태로 등록
