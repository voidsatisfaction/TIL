# Deep learning infra setting

## Initial script

```
#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# change deb repository to daum
sed -i 's/kr.archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
sed -i 's/us.archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list

apt update
apt install net-tools openssh-server vim exfat-fuse exfat-utils -y


# install nvidia driver
sudo add-apt-repository ppa:graphics-drivers/ppa -y
sudo apt-get update

sudo apt install -y nvidia-driver-430

# install docker and etc
apt-get update
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update
sudo apt-get install -y docker-ce

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose


curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

usermod -aG docker vuno
```

다 끝나고 리부팅 필요

## Docker Setting

`/etc/docker/daemon.json` 파일 수정

```sh
{
    # For escaping HOST IP duplication
    "bip": "10.20.0.1/24",
    # For changing the location of docker related files(images, ...)
    "data-root": "/mnt/vuno/docker"
}
```
