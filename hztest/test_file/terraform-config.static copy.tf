

variable "wl_name" {
  default = ""
}

variable "wl_namespace" {
  default = ""
}

variable "wl_registry_map" {
  default = ""
}

variable "intel_publisher_sut_machine_type" {
  default = "static"
}

variable "intel_publisher_sut_metadata" {
  default = ""
}

variable "worker_profile" {
  default = {
    vm_count = 2
    hosts = {
      "worker-0": {
        "user_name": "raspadmin",
        "public_ip": "10.219.170.236",
        "private_ip": "10.219.170.236",
        "pdu_port": 1,
      },
      "worker-1": {
        "user_name": "raspadmin",
        "public_ip": "10.219.170.13",
        "private_ip": "10.219.170.13",
        "pdu_port": 1,
      },
    }
  }
}

# Note: Make sure to add below two variables in order to execute WL on windows under client profile.
# "winrm_password": "<windows_password>",
# "winrm_port": 5986,

variable "client_profile" {
  default = {
    vm_count = 1
    hosts = {
      "client-0": {
        "user_name": "raspadmin",
        "public_ip": "10.219.170.13",
        "private_ip": "10.219.170.13",
        "ssh_port": 22,
        "pdu_port": 1,
      },
    }
  }
}

variable "controller_profile" {
  default = {
    vm_count = 1
    hosts = {
      "controller-0": {
        "user_name": "raspadmin",
        "public_ip": "10.219.170.13",
        "private_ip": "10.219.170.13",
        "ssh_port": 22,
      }
    }
  }
}

output "instances" {
  value = merge({
    for i in range(var.worker_profile.vm_count) : 
      "worker-${i}" => var.worker_profile.hosts["worker-${i}"]
  }, {
    for i in range(var.client_profile.vm_count) :
      "client-${i}" => var.client_profile.hosts["client-${i}"]
  }, {
    for i in range(var.controller_profile.vm_count) :
      "controller-${i}" => var.controller_profile.hosts["controller-${i}"]
  })
}

output "options" {
  value = { 
    wl_name : var.wl_name,
    wl_registry_map : var.wl_registry_map,
    wl_namespace : var.wl_namespace,
    intel_publisher_sut_machine_type: var.intel_publisher_sut_machine_type,
    intel_publisher_sut_metadata: var.intel_publisher_sut_metadata,

    # Enable k8s registry only in the DDCW use case. See doc/user-guide/preparing-infrastructure/setup-wsf.md
    k8s_enable_registry: false,
  }
}

