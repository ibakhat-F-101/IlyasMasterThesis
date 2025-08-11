# For the moment, the image is built in local, next step is to use it in a pipeline

# The following commands don't work on kali linux.

# Packer doesn't need to be installed on your local pc, it just need to be on the pipeline that will update the box.

# install packer hashicorp

curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install packer

if you can't apt-add-repository do this : sudo apt-get install software-properties-common 

packer plugins install github.com/hashicorp/virtualbox
packer plugins install github.com/hashicorp/vagrant

I follow this link to create the image
https://dev.to/mattdark/a-custom-vagrant-box-with-packer-13ke

# Create the image

use : packer build packer.json

