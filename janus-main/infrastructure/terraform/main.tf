########################################
# This code is using a template who is already create
########################################
terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = ">=2.8.0"
    }
  }
}

provider "proxmox" {
  pm_api_url = "https://81.164.62.96:1234/api2/json"
  pm_user    = "terraform-prov@pve"
  pm_password = "testtest"
}

# The vmid need to be change for each creation
resource "proxmox_vm_qemu" "example_vm" {
  name       = "vm-template"
  target_node = "proxLabo"
  vmid       = 301
  clone       = "debian-vm"
}


########################################
# This code is creating a vm with a iso
########################################
# terraform {
#   required_providers {
#     proxmox = {
#       source  = "telmate/proxmox"
#     }
#   }
# }

# provider "proxmox" {
#   pm_api_url = "https://81.164.62.96:1234/api2/json"
#   pm_user    = "terraform-prov@pve"
#   pm_password = "testtest"
# }

# resource "proxmox_vm_qemu" "example_vm" {
#   name = "debian-vm"
#   target_node = "proxLabo"
#   vmid = 300
#   memory = 2048
#   sockets = 1
#   cores = 2
#   network {
#     model = "virtio"
#     bridge = "vmbr0"
#   }
#   iso = "local:iso/debian.iso"

#   disk {
#     type = "scsi"
#     storage = "local-lvm"
#     size = "20G"
#   }

# SCSI controller configuration
#   scsihw = "virtio-scsi-pci"
# }