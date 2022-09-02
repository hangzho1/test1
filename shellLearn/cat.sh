#!/bin/bash

pwd 
hostname


Required_HugePage=$1
Required_Size=$2

HugePages_Total=$(grep HugePages_Total /proc/meminfo | awk '{print $2}')
Hugepagesize=$(grep Hugepagesize /proc/meminfo | awk '{print $2}')
HugePages_Free=$(grep HugePages_Free /proc/meminfo | awk '{print $2}')


echo $HugePages_Total $Hugepagesize $HugePages_Free 

echo $Required_HugePage $Required_Size


