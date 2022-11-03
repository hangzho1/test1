#!/usr/bin/env bash
deployDir="/mnt/auto_provision_services"
jobId=220
frontApi="http://10.67.119.211:8899/local/api/job/220/"
# host machines to be deployed
deployHost=(
        "name,ansible_host,ip,username,hostname,password"
        "controller,10.67.126.102,10.67.126.102,root,hostname,intel123"
        "node1,10.67.126.81,10.67.126.81,root,hostname,intel123"
)

# kubernetes
kubernetes_deploy="true"
kubernetesInstallMethod="host" # host vm docker
declare -A kubernetesArgs
kubernetesArgs=(
        ["kube_version"]="1.23.5"  #v1.23.5
        ["kube_network_plugin"]=" calico" # cilium, calico, weave or flannel
        ["container_manager"]="docker" #  docker, crio, containerd
        ["dashboard_enabled"]="false" #  true false
        ["helm_enabled"]="false" # true false
        ["registry_enabled"]="false" # true false
        ["ingress_nginx_enabled"]="false" # true false
        ["ingress_nginx_host_network"]="false" # true false
        ["krew_enabled"]="false"
)

# workload args
jenkins="true"
workloadName="Kafka"
jsfRepo="https://github.com/jo5Liu/applications.benchmarking.benchmark.platform-hero-features.git"
commit="7914f4f"
filterCase="pkm"
registry="10.166.44.56:5000"
platforms="ICX"

# software
softwarepackage="false"
softwarepackageArgs=(
        "name,scriptArgs"
)

# system
system_deploy="true"
os_update="false"
os=""                      # ""use system default values        example: ubuntu20.04 / centos8
Kernel_update="false"
kernelVersion="5.8"           # ""use system default values        example: 5.8
kernelArgs_update="false"
kernelArgs='kernelhugepagesz=1G hugepagesz=1G hugepages=16'
# bios args
bios_update="true"
# biosArgs='BIOS_CONFIG: [
#   {"knob":"VTdSupport" , "prompt": "Intel(R) VT for Directed I/O", "value": "0x0"},
#   {"knob":"LlcPrefetchEnable" , "prompt": "LLC Prefetch", "value": "0x0"},
# ]'
biosArgs='BIOS_CONFIG: [

  {"knob": "ProcessorHyperThreadingDisable", "prompt": "Intel(R) Hyper-Threading Tech", "value": "0x01"}

]'
# biosArgs='BIOS_CONFIG: [
#   {"knob":"ProcessorX2apic" , "prompt": "Enable/disable extended APIC support", "value": "0x0"},
#   {"knob":"VTdSupport" , "prompt": "Intel(R) VT for Directed I/O", "value": "0x0"},
#   {"knob": "TurboMode", "prompt": "Intel(R) Turbo Boost Technology", "value": "0x0"},
#   {"knob": "ProcessorHyperThreadingDisable", "prompt": "Intel(R) Hyper-Threading Tech", "value": "0x01"},
#   {"knob": "SncEn", "prompt": "SNC (Sub NUMA)", "value": "0x04"},
#   {"knob": "PcieEnqCmdSupport", "prompt": "PCIe ENQCMD/ENQCMDS", "value": "0x00"}

# ]'

# virtual machine
vm_deploy="false"
vm_docker=""
declare -A vmosArgs
vmosArgs=(
        ["osNumber"]=""
        ["osType"]=""
        ["vmName"]=""
        ["memory"]=""
        ["cpuNumber"]=""
        ["disk"]=""
)

# email
sender="tao2.liu@intel.com"
receivers="tao2.liu@intel.com" #example receivers="renlex.fu@intel.com,owen.zhang@intel.com"
