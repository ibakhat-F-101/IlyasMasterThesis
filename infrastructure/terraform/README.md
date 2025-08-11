# Explanation

The first part of the code allows for the creation of the virtual machine by connecting to the Proxmox server and then creating it using a previously created template.

The commented section of the code is precisely where we create the virtual machine from an ISO image located on the Proxmox server:
We connect to Proxmox, configure the virtual machine with the desired resources, specify the path of the ISO, and add a disk and a controller.

----------------------------------------

# Terraform command

```
terraform init 
```
This will initialize Terraform and download the necessary plugins.

----------------------------------------

```
terraform validate
```
Checks the syntax of your Terraform configuration.

----------------------------------------

```
terraform plan
```
See what Terraform will do

----------------------------------------

```
terraform apply
```
Terraform will apply the changes

----------------------------------------

