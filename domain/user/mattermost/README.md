# Mattermost

## Getting started

I followed the [official documentation](https://docs.mattermost.com/install/install-docker.html#deploy-mattermost-on-docker-for-production-use) to install Mattermost on docker.

## Configuration Files

### Focalboard 

Focalboard is already integrated in Mattermost. This is now called "Boards" in the top-right menu, next to the 'Start call' button.


# How to launch the project
To properly run the project, the following dependencies must be downloaded and installed on the local machine of the user:

> Note: Repository update (`apt update -y`) may be required before running the commands 

- Virtualbox: The local version of the project runs only on virtualbox.
```sh
apt install virtualbox
```

- Hashicorp vagrant: Required to execute vagrant command on the user machine.
 ```sh
apt install vagrant
```


After the installation of the dependencies, users can deploy the user domain by navigating to the directory ```janus/domain/user``` to execute the following command

```sh
vagrant destroy --force && vagrant box update && vagrant up
```

## To enable CyFun compliance features (asset inventory, vulnerability scan, etc.)

Navigate to the user domain directory:

```sh
cd janus/domain/user
```

## Activate Team Simulation 

Navigate to the user domain directory:

```sh
cd janus/domain/user
```

* On **Linux/macOS**:

```sh
vagrant destroy --force && vagrant box update && MATTERMOST_NPC="true" && Vagrant Up
```


* On **Windows** (PowerShell):

```cmd
MATTERMOST_NPC="true"
vagrant destroy --force
vagrant box update
vagrant up
```

For accessing the Mattermost Team associated with this project, use the following credentials:

- **Username**: [admin]
- **Password**: [AdminPassword123]


