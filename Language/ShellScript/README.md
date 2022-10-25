# ShellScript

- 의문
- cookbook
  - shell command의 output을 변수에 저장하기
  - 특정 커맨드가 존재하는지 확인
  - 마지막 값 자르기
  - date 비교하기
  - json파싱
  - `:-`, `:=`: fallback
- 예시
  - 1 server health check script

## 의문

## cookbook

### shell command의 output을 변수에 저장하기

`today=$(date +'%Y%m%d')`

### 특정 커맨드가 존재하는지 확인

```sh
if ! [ -x "$(command -v git)" ]; then
  sudo apt update -y
  sudo apt install git
fi
```

### 마지막 값 자르기

```sh
a=123
echo "${a::-1}" # 12
```

### date 비교하기

```sh
today=$(date +%s)
date1=$(date -d 2013-07-18 +%s)
date2=$(date -d 2014-08-19 +%s)

if [[ ${date1} -le ${date2} ]]; then
  echo "date1 < date2"
fi
```

### json파싱

- jq
  - json parsing library

```sh
cat json.txt | jq '.name'
```

### `:-`, `:=`: fallback

```sh
x=
echo ${x:-1} # 1
echo $x #
```

```sh
x=
echo ${x:=1} # 1
echo $x # 1
```

## 예시

### 1. server health check script

`run_health_check.sh`

```sh
#!/bin/bash
function print_usage() {
  echo "Usage: $0"
  echo "  main disk location                         / | /mnt/vuno | /data | ..."
  echo "  license api server container name          vn-m-04-core-dev | fundus-inference | ... | n (no print)"
  echo "  license api server port(inside container)  5034 | 5035 | ... | n (no print)"
}

function print_line() {
  # local variable
  local title=$1

  echo ""
  echo "------------ ${title}"
  echo ""
}

# red text
function print_danger_text() {
  local text=$1

  echo ""
  echo -e "\e[1;31m${text}\e[0m"
  echo ""
}

function print_disk_usage() {
  local disk_location=$1
  local disk_danger_notification_threshold=$2

  # get data from 2 row, 4 column
  local available_disk=$(df -alh ${disk_location} | awk 'FNR == 2 { print $4 }')
  # remove last character from variable
  local available_disk_number=${available_disk::-1}

  if [ ${available_disk_number} -le ${disk_danger_notification_threshold} ]; then
    print_danger_text "Available disk space will go out soon"
  fi

  df -alh ${disk_location}
}

function print_memory_usage() {
  local memory_danger_notification_threshold=$1

  local available_memory=$(free -h | awk 'FNR == 2 { print $7 }')
  local available_memory_number=${available_memory::-1}

  if [ ${available_memory_number} -le ${memory_danger_notification_threshold} ]; then
    print_danger_text "Available memory is too small"
  fi

  free -h
}

function print_license_info() {
  local license_api_server_container_name=$1
  local license_api_server_port=$2
  local license_use_limit_danger_notification_threshold=$3
  local license_expiration_date_danger_notification_threshold=$4

  local license_info=$(docker exec \
    ${license_api_server_container_name} \
    bash -c "curl --silent localhost:${license_api_server_port}/api/license/info")

  if [ -x "$(command -v jq)" ]; then
    local use_limit=$(echo ${license_info} | jq '.use_limit')
    local use_count=$(echo ${license_info} | jq '.use_count')
    local available_count=$((${use_limit} - ${use_count}))

    local exp_date=$(echo ${license_info} | jq '.exp_date | tonumber')
    local date_from_today=$(date +'%Y%m%d' -d '+'${license_expiration_date_danger_notification_threshold}' days')

    if [ ${available_count} -le ${license_use_limit_danger_notification_threshold} ]; then
      print_danger_text "Available license count will go out soon"
    fi

    if [ ${exp_date} -le ${date_from_today} ]; then
      print_danger_text "Available license expiration comes soon"
    fi
  fi

  echo ${license_info}

  echo ""
}

MAIN_DISK_LOCATION=$1
LICENSE_API_SERVER_CONTAINER_NAME=$2
LICENSE_API_SERVER_PORT=$3

# you can configure thresholds here

DISK_DANGER_NOTIFICATION_THRESHOLD=30 # Unit: Gigabyte
MEMORY_DANGER_NOTIFICATION_THRESHOLD=5 # Unit: Gigabyte

LICENSE_USE_LIMIT_DANGER_NOTIFICATION_THRESHOLD=5000 # Unit: Count
LICENSE_EXPIRATION_DATE_DANGER_NOTIFICATION_THRESHOLD=30 # Unit: Day

if [ "$#" -ne 3 ]; then
  print_usage
  exit 1
fi

if ! [ -x "$(command -v jq)" ]; then
  sudo apt update
  sudo apt install -y jq
fi

print_line "Memory Info"
print_memory_usage ${MEMORY_DANGER_NOTIFICATION_THRESHOLD}

print_line "Storage Info"
print_disk_usage ${MAIN_DISK_LOCATION} ${DISK_DANGER_NOTIFICATION_THRESHOLD}

case ${LICENSE_API_SERVER_CONTAINER_NAME} in
  n|N)
    ;;
  *)
    print_line "Vuno License Info"
    print_license_info \
      ${LICENSE_API_SERVER_CONTAINER_NAME} \
      ${LICENSE_API_SERVER_PORT} \
      ${LICENSE_USE_LIMIT_DANGER_NOTIFICATION_THRESHOLD} \
      ${LICENSE_EXPIRATION_DATE_DANGER_NOTIFICATION_THRESHOLD}
    ;;
esac

echo ""
```
