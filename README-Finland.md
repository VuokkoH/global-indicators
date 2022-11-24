# Finland-spesific notes

## Computing environment 

**Computing environment set up for running the analysis in Finland:**

- Launched an Ubuntu 20.04 instance, 3xlarge volume (Size: 80 GB, RAM: 62.5 GB, VCPUs: 8) via [CSC pouta service](https://research.csc.fi/-/cpouta)
- Installed docker following these instructions: https://docs.docker.com/engine/install/ubuntu/ --> install using the repository
- To use docker without sudo; add user 'ubuntu' to user group 'docker': https://docs.docker.com/engine/install/linux-postinstall/ (then log out, log in)
- Verify that docker is installed correctly: 

```$ sudo docker run hello-world```
