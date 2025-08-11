## Gitlab Runner

### The gitlab runner allow users to run job in the CI/CD pipeline. It continously executes, making it available 24/7 to take on job from the pipeline. To start the virtualbox runner, the hashicorp vagrant package must be installed on the user's machine using the command below:

```sh
apt install vagrant
```
### It is important to replace the `registration_key` variable befor running the script. The registration key can be retrieved from the repository by navigating to `Setting -> CI/CI -> Runners` and clicking the toggle button close to `New project runner` button