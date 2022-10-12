# Deep learning infra setting

- Initial script
- Docker Setting

## Initial script

```sh
#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# change deb repository to daum
sed -i 's/kr.archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
sed -i 's/us.archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list

apt update
## net-tools: netstat, ifconfig, route ...
## openssh-server: ssh server in ubuntu
## exfat-fuse, exfat-utils: exFAT file system driver, exFAT utils
apt install net-tools openssh-server vim exfat-fuse exfat-utils -y


# install nvidia driver
## add third part apt repository(apt repository is a network server or a local directory containing deb packages)
## PPA(Personal Package Archives) -> service that allows users to upload source packages that are built and published with Launchpad as an apt repository
sudo add-apt-repository ppa:graphics-drivers/ppa -y
sudo apt-get update

## Once the PPA is added to our system, we can install the repository packages
sudo apt install -y nvidia-driver-430

# install docker and etc
apt-get update
## apt-transport-https: allows the use of repositories accessed via the HTTP Secure protocol
## ca-certificates: CA certificates provided by CA
## curl: curl
## software-properties-common: provides an abstraction of the used apt repositories. allows us to easily manage our distribution and independent software vendor software sources
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

## curl
### f: fail silently
### s: silent
### S: show error message if it fails
### L: if server responses with redirection, it will make curl redo with redirection url
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
## apt-key:
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update
sudo apt-get install -y docker-ce

### uname -s: show kernel name e.g) Linux
### uname -m: machine hardware name e.g) x86_64
### curl -o: write output to <file> instead of stdout
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

### apt-key: used to add, delete, list and export public keys used by apt to verify the signature of a release file
### if a public key for a distribution does not exist, then apt will fail to verify the signature of its release file, and issue an error
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
### /etc/os-release or /usr/lib/os-release: operating system identification data
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
### tee: read from stdin and write to stadout and files
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

## usermod: modify user account
### usermod -aG docker yeon => make yeon account to be included as docker group member
usermod -aG docker yeon
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
