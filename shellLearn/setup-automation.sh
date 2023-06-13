#!/bin/bash

logdir="./setup_logs"
mkdir -p $logdir
start_time=$(date +%s)
develop_ip=$(hostname -I | awk '{print $1}')

# 定义函数，将命令输出到指定的日志文件中
function setup-dev() {
  echo "Setup Dev ..."
  bash ./setup-dev.sh &>> $logdir/setup-dev.log
  return $?
}

function setup-sut-native() {
  echo "Setup SUT Native ..."
  bash ./setup-sut-native.sh centos1@10.67.122.9 centos2@10.67.122.133 &>> $logdir/setup-sut-native.log
  return $?
}

function setup-reg() {
  echo "Setup Reg ..."
  bash ./setup-reg.sh sfdev@10.166.31.187 --port 22 --force &>> $logdir/setup-reg.log
  return $?
}

function setup-sut-docker() {
  echo "Setup SUT Docker ..."
  bash ./setup-sut-docker.sh centos1@10.67.122.9 &>> $logdir/setup-sut-docker.log
  return $?
}

function setup-sut-k8s() {
  echo "Setup SUT K8S ..."
  bash ./setup-sut-k8s.sh centos1@10.67.122.9 centos2@10.67.122.133 --reset --nointelcert &>> $logdir/setup-sut-k8s.log
  return $?
}

# 执行上面定义的所有函数，并记录执行状态
set +e
declare -a funcs=("setup-dev" "setup-sut-native" "setup-reg" "setup-sut-docker" "setup-sut-k8s")
# declare -a funcs=("setup-dev" "setup-reg" )
declare -A statuses


for func in "${funcs[@]}"; do
  $func
  status=$?
  echo "Function ${func}: STATUS=${status}"
  statuses[${func}]=$status
done

end_time=$(date +%s)
duration=$((end_time - start_time))

# 显示最终的执行状态
echo "========="
echo "Total test time: ${duration}s."
echo "Summary:"
for func in "${!statuses[@]}"; do
  if [ ${statuses[${func}]} -eq 0 ]; then
    echo "Function '${func}' succeeded."
  else
    echo "Function '${func}' failed with status ${statuses[${func}]}."
  fi
done