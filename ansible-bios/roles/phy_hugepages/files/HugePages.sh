#!/usr/bin/env bash


Required_HugePage=$1
Required_Size=$2

HugePages_Total=$(grep HugePages_Total /proc/meminfo | awk '{print $2}')
Hugepagesize=$(grep Hugepagesize /proc/meminfo | awk '{print $2}')
HugePages_Free=$(grep HugePages_Free /proc/meminfo | awk '{print $2}')


echo $HugePages_Total $Hugepagesize $HugePages_Free 

HugePaegs_judge(){

    if [[ ${Hugepagesize} -ne ${Required_Size} || ${HugePages_Total} -lt ${Required_HugePage } ]]; then

        sudo grubby --update-kernel=DEFAULT --args="default_hugepagesz=${Required_Size}kB hugpagesz=${Required_Size}kB hugepages=${Required_HugePage}" && sudo reboot
        # exit 0

    fi

    if [[ ${HugePages_Free} -lt ${Required_HugePage} ]]; then
        echo "There is not enough free memory to restart"
        sudo reboot
    fi
    
    echo "The configuration meets the requirements"


}

HugePaegs_judge


