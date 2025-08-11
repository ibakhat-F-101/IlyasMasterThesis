#!/bin/bash

# Function to gracefully power off a VM
power_off_vm() {
    vm_name=$1
    echo "Attempting to gracefully power off VM: $vm_name"
    VBoxManage controlvm "$vm_name" poweroff
}

# List all running VMs
running_vms=$(VBoxManage list runningvms | awk -F\" '{print $2}')

# If there are running VMs, attempt to power them off gracefully
if [ -n "$running_vms" ]; then
    echo "Found running VMs: $running_vms"
    for vm in $running_vms; do
        power_off_vm "$vm"
    done
fi

# List all VMs
all_vms=$(VBoxManage list vms | awk -F\" '{print $2}')

# Loop through VMs and delete each one
if [ -n "$all_vms" ]; then
    echo "Found VMs: $all_vms"
    for vm in $all_vms; do
        VBoxManage unregistervm "$vm" --delete
    done
else
    echo "No VMs found."
fi

