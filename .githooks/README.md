# Using Git hooks

This project utilizes Git Hooks to automate certain tasks and maintain code quality. Here's a brief explanation of each Hook used:

## Commit Message Hook
This Hook is triggered before each commit creation. Its purpose is to ensure that commit messages adhere to a certain convention. By having consistent and informative commit messages, it aids in understanding the changes made to the code, whether for yourself or other team members.

## Pre-Commit Hook
The Pre-Commit Hook runs just before finalizing a commit. Its role is to automatically check the code that will be added to the repository. This may include running automated tests, checking code syntax, or other quality criteria. If the Pre-Commit Hook detects issues, it can prevent the commit from being made, allowing you to fix errors before they are integrated into the repository.


# Activate the git hook
From the root directory execute these commands 
-  `cd .githooks`
- `git config core.hooksPath .githooks`

# Activate the yamllint
When a commit is made, yamllint is used to strictly check the playbooks for compliance with the ruleset in the ```.yamllint``` file. Hence, yamllint must be installed on the local machine of the developer before making a commit. Use the following command to install yamllint on your machine.

```sh
apt install yamllint
```
After the installation, ensure that the ```.yamllint``` file is located in the janus project root directory. To manually test your playbooks against the yamllint, the command below can be executed in the project root or children folder of the project directory. 

```sh
yamllint .  #test all playbooks in the project
yamllint directory/to/test
yamllint your_playbook.yml
```
>Note: Yamllint command should not be executed in the parent folder of the project or any other preceding directories. See  [this](https://yamllint.readthedocs.io/en/stable/configuration.html)

## Structure of branch name

The structure of your branch name is :
```
<Course>-<Last_name>-<task>
```

where :
 - `Course` is why you are working on the project
 - `Last_name`is your last name
 - `task`is the task you are working on

 example : internship-bruyere-FILLREADME

## Structure of commit messages

The commit messages are structured as follows :
  
```
[<type of change>] <message>
```

where `<type of change>` can be one of the following :
- `UPDATE` : when the commit is an update of an existing feature;
- `ADD` : when the commit is the addition of a new feature;
- `FIX` : when the commit is a fix of an existing feature;
- `DELETE` : when the commit is the removal of an existing feature;
- `DOC` : when the commit is a documentation update;