# learn-docker-with-hack

## Virtual Workshop Recording

[Youtube]() | [Slides]()

## Overview

## Table of Contents

- [What is Docker?](#what-is-docker-?)
- [Prerequisites and Setup](#prerequisites-and-setup)
- [Docker Principles](#docker-principles)
- [Docker Commands](#docker-commands)
- [Tutorial](#tutorial)
- [Additional Material](#additional-material)

## What is Docker?

## Prerequisites and Setup

### Docker Desktop installation: https://www.docker.com/products/docker-desktop

## Docker Principles

- [Images](#images)
- [DockerHub](#dockerhub)
- [Dockerfile](#dockerfile)
- [Containers](#containers)
- [Networking](#networking)
- [Volumes](#volumes)

### Images

### DockerHub

### Dockerfile

### Containers

### Networking

### Volumes:

## Docker Commands

- [docker build](#docker-build)
- [docker network create](#docker-network-create)
- [docker volume create](#docker-volume-create)
- [docker container run](#docker-container-run)

### docker build

```
> docker build -t <image-name>:<version-number> .
```

### docker network create

```
> docker network create <network-name>
```

### docker volume create

```
> docker volume create <volume-name>
```

### docker container run

```
> docker container run --rm --name <container-name> --network <connected-networks> -e <environment-variable>=<value>  -p <publish-port-local>:<publish-port-container> --volume <volume-name>:<container-mount-point> <image-name>:<version-number>
```

## Tutorial

### Overview

In this tutorial, we are going to:

- Do stuff

### Steps

- [Setup](#setup)

### Setup

If you have not already, please follow the instructions [here](#setting-git-up)!

## Additional Material
