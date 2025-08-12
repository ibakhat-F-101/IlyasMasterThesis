# This git is a copy of the private GIT Janus And it doesn't reflect the final state of Janus, but of my completed personal project.

# Purpose of this work
The aim of this work is to design, implement, and validate a framework that:
1. Deploys a private cloud environment as IaC/CaC for repeatable and secure experimentation.
2. Simulates a realistic enterprise communication ecosystem populated by AI agents acting as human team members (*Green Team*).
3. Enables controlled execution of **social engineering attack scenarios** against these agents to assess susceptibility, defensive mechanisms, and detection workflows.
4. Supports research in improving **human-factor security training** by providing a reproducible, measurable, and ethically safe testbed.

This academic adaptation serves as both:
- A technical contribution in automated, secure cyber range deployment.
- A methodological contribution in evaluating and enhancing social engineering resilience through AI-driven human simulation.

## Project Structure
```
janus/  
└── domain/  
    └── user/                       # Main environment to launch (Vagrant)  
        ├── Vagrantfile  
        ├── mattermost/  
        │   └── mattermost_bot/  
        │       ├── agents.py        # CrewAI agent definitions and LLM wrapper  
        │       ├── behaviors.py     # Role-based behavioral probabilities  
        │       ├── bot.py           # Response personalization logic  
        │       ├── config.py        # Global configuration variables  
        │       ├── levels.py        # Game/Training levels logic  
        │       ├── profiles.json    # User profiles for agents  
        │       ├── roles.json       # Role definitions and backstories  
        │       ├── utils.py         # Utility functions (passwords, profile loading)  
        │       ├── Data/            # Data files used by agents  
        │       └── levels/          # Level content files  
        └── mattermost_bot.yml  
```


# Project lead & copyright Jérôme Dossogne all rights reserved

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

## Activate Team Simulation 

Navigate to the user domain directory:

```sh
cd janus/domain/user
```

* On **Linux/macOS**:

```sh
vagrant destroy --force && vagrant box update && MATTERMOST_NPC="true"
```

* On **Windows** (CMD):

```cmd
set "MATTERMOST_BOT=true" && vagrant destroy --force && vagrant box update && vagrant up
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

