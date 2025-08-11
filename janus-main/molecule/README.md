## Molecule Test

I followed this [link](https://ansible.readthedocs.io/projects/molecule/installation/) to install molecule. Python package installer (pip) can be used to install molecule on the system. 

```sh
pip install molecule
```
The installation can be verified by running `molecule --version`. If an error is displayed, consider adding the local directory to path by executing the command below: 

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Molecule vagrant driver is used to build and test the playbooks. Hence, the vagrant driver should be installed on the machine running the molecule using the commands below:

```sh
sudo apt-get install libvirt-dev
vagrant plugin install vagrant-libvirt
pip install -U molecule-plugins[vagrant]
```
#### Useful molecule commands
```sh
molecule create
molecule converge
molecule verify
molecule test
molecule check
```
