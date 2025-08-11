# gitlab-ci.yml

this pipeline include :

- [DAST-CI.yml](analyze/.DAST-CI.yml)
- [SAST-CI.yml](analyze/.SAST-CI.yml)
- [packer-ci.yml](packer/.packer-ci.yml)

No pipeline jobs will execute when there are only changes to markdown (.md) files. This is to avoid unnecessary work for the runner(s).

For this pipeline you will need a runner with these tools installed :

- Follow the instructions from gitlab to install the runner [here](https://gitlab.com/jdosec/janus/-/settings/ci_cd) you need to be maintainer
- Packer : [See this](../services/packer/README.md)
- Vagrant
- Python
- Pip install passlib
- (This list need to be completed)

You need to register on vagrant cloud from the runner

`vagrant cloud auth login --token <TOKEN>`

# sonarqube server

You will need a sonarqube server, see [this](analyze/README.md)
