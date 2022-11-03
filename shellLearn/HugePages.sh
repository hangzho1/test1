#!/usr/bin/env bash

Required_HugePage=$1
Required_Size=$2

HugePages_Total=$(grep HugePages_Total /proc/meminfo | awk '{print $2}')
Hugepagesize=$(grep Hugepagesize /proc/meminfo | awk '{print $2}')
HugePages_Free=$(grep HugePages_Free /proc/meminfo | awk '{print $2}')
# testTotal=10000000
# free=100000000

echo $HugePages_Total $Hugepagesize $HugePages_Free

HugePaegs_judge() {

    # if [[ $(expr ${HugePages_Total} \* ${Hugepagesize}) -le $(expr ${Required_HugePage} \* ${Required_Size}) ]]; then
    #     echo "Beyond the total memory"
    #     return
    # fi

    if [[ ${Hugepagesize} -ne ${Required_Size} || ${HugePages_Total} -lt ${Required_Size} ]]; then

        # sudo grubby --update-kernel=DEFAULT --args="default_hugepagesz=${Required_SiRze}kB" && sudo reboot
        sudo grubby --update-kernel=DEFAULT --args="default_hugepagesz=${Required_Size}kB hugpagesz=${Required_Size}kB hugepages=${Required_HugePage}"
        exit 0

        # sudo grubby --update-kernel=DEFAULT --args="hugepages=${Required_Size}" && sudo reboot

    fi

    if [[ ${HugePages_Free} -lt ${Required_HugePage} ]]; then
        echo "There is not enough free memory to restart"
        # sudo reboot
    fi

    echo "The configuration meets the requirements"

}

HugePaegs_judge
