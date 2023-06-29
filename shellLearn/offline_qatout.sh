#!/bin/bash
set -x 

sudo modprobe vfio-pci

if [ ! -e /opt/intel/QAT ]
then 
    sudo mkdir -p /opt/intel/QAT
fi

if [ ! -e QAT20.L.1.0.0-00021.tar.gz ]
then 
    wget -O QAT20.L.1.0.0-00021.tar.gz https://downloadmirror.intel.com/765523/QAT20.L.1.0.0-00021.tar.gz
    
fi

sudo tar -xvzf QAT20.L.1.0.0-00021.tar.gz -C /opt/intel/QAT
cd /opt/intel/QAT || exit
sudo ./configure
sudo make
sudo make install
sudo echo 4096 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
sudo rmmod usdm_drv
sudo insmod /opt/intel/QAT/build/usdm_drv.ko max_huge_pages=4096 max_huge_pages_per_process=224
sudo systemctl stop qat.service
sudo systemctl enable qat.service
sudo systemctl restart qat.service
sudo systemctl status qat.service
