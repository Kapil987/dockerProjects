# Docker Real Time
![alt text](https://cdn.dribbble.com/users/1008970/screenshots/6140230/blog_post_docker.gif)

## Description

Docker is a software platform that allows you to build, test, and deploy applications quickly

## Getting Started

Docker works by providing a standard way to run your code. Docker is an operating system for containers. Similar to how a virtual machine virtualizes (removes the need to directly manage) server hardware, containers virtualize the operating system of a server. Docker is installed on each server and provides simple commands you can use to build, start, or stop containers.

### Dependencies

* An IDE (VScode preferred)
* Linux OS

### Installing

* Follow instruction from https://docs.docker.com/engine/install
```
yum install docker
```

### Get Familiar with Dockerfile

- Name of file should be with name **Dockerfile**, “D” should be capital letters, Docker components in the file should be capital letters only
- **FROM**: Which base image I want. This command must be on top of the docker file
- **RUN**: lets you execute commands while creating Docker image, it will create a layered image
- **LABEL**: Author/Owner/Description, MAINTAINER is deprecated
- **COPY**: Copy files from local system (docker VM), we need to provide source, destination. Used for copying from local file system, not from internet
    * COPY /source/file/path  /destination/path
- **ADD**: like copy, download files from internet, also extract file at docker image side
    * ADD sourceFileUrl  /destination/path
    * ADD /source/file/path  /destination/path
    * ADD source.file.tar.gz /temp
- **EXPOSE**: to expose ports, such as port 8080 for tomcat and port 80 for Nginx etc.
- **WORKDIR**: To set working directory, so that once the container is created you are directly landed to this dir
- **CMD**: execute commands but after container creation, and inside container
- **ENTRYPOINT**: Like CMD but has higher priority over CMD, first commands will be executed by ENTRYPOINT only
- **ENV**: Environment variable
- **ARG**: Argument 
- **HEALTHCHECK** : check the health of any resource to determine whether that resource is operating normally


### Executing program

* How to run the program
```
docker run -td --name Container_Name Image_Name:optional_tag
```

## Help

```
docker --help
```

## Authors

Contributors names and contact info

[@KAPIL0123](https://twitter.com/KAPIL0123)

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.
* [Begining with Docker](https://medium.com/@kmdkhadeer/docker-get-started-9aa7ee662cea)
* [Using SSH keys inside docker container](https://stackoverflow.com/questions/18136389/using-ssh-keys-inside-docker-container)
* [Docker multi-stage builds](https://towardsdatascience.com/using-multi-stage-builds-to-make-your-docker-image-almost-10x-smaller-239068cb6fb0)
## License

Free Software, Hell Yeah!
