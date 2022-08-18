#!/usr/bin/env bash

# Required_HugePage=$1
# Required_Size=$2

# HugePages_Total=$(grep HugePages_Total /proc/meminfo | awk '{print $2}')
# Hugepagesize=$(grep Hugepagesize /proc/meminfo | awk '{print $2}')
# HugePages_Free=$(grep HugePages_Free /proc/meminfo | awk '{print $2}')
# testTotal=100

# echo $HugePages_Total $Hugepagesize $HugePages_Free $testTotal

# HugePaegs_judge(){

#     if [[ $(expr ${testTotal} \* ${Hugepagesize}) -le $(expr ${Required_HugePage} \* ${Required_Size}) ]]; then
#         echo "Beyond the total memory"
#         return
#     elif [[ ${Hugepagesize} -ne ${Required_Size} ]]; then

#         sudo grubby --update-kernel=DEFAULT --args="hugepages=${Required_Size}" && sudo reboot

#     else [[ ${HugePages_Free} -le ${Required_HugePage} ]];
#         sudo reboot
#     fi

#     echo "The configuration meets the requirements"

# }

# HugePaegs_judge

# if [[ 5 -le 7 ]]; then
#     echo "5"

# echo "The configuration meets the requirements"
# fi

# abd=$(cat /proc/meminfo | grep -E '(?<=\Hugepagesize: +)\d+')
# # abd=$(cat /proc/meminfo |grep '2048')
# echo $abd


###output: /home/sfdev/hangz/shellLearn
DIR="$(cd "$(dirname "$0")" &>/dev/null && pwd)"
echo $DIR
