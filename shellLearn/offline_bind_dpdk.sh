#!/bin/bash

if [ ! -e /etc/network_env.conf ]
then
    echo " This machine does not have a /etc/network_env.conf file " && exit
fi

dpdk_port1=$(grep dpdk_port1=0000: /etc/network_env.conf |awk -F "0000:" '{print $NF}')
dpdk_port2=$(grep dpdk_port2=0000: /etc/network_env.conf |awk -F "0000:" '{print $NF}')

echo ${dpdk_port1}  ${dpdk_port2}  $(date) |sudo tee dpdk_port.log

if [ ! -e /opt/intel/dpdk-21.11 ]
then
    sudo mkdir -p /opt/intel/dpdk-21.11
fi


if [ ! -e dpdk-21.11.tar.xz ]
then
    wget -O dpdk-21.11.tar.gz http://fast.dpdk.org/rel/dpdk-21.11.tar.xz

fi
sudo tar -xvf dpdk-21.11.tar.gz

sudo modprobe vfio-pci
cd  /opt/intel/dpdk-21.11/usertools || exit

# set 100GE ports as ifconfig down state
eth_port1=$(./dpdk-devbind.py -s |grep Active |grep ${dpdk_port1} |awk -F "if=" '{print $2}' |awk  '{print $1}')
eth_port2=$(./dpdk-devbind.py -s |grep Active |grep ${dpdk_port2} |awk -F "if=" '{print $2}' |awk  '{print $1}')
ifconfig ${eth_port1} down || echo 1
ifconfig ${eth_port2} down || echo 1

sudo ./dpdk-devbind.py -b vfio-pci ${dpdk_port1}  ${dpdk_port2}
./dpdk-devbind.py -s
