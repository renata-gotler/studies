# Data Science Test

This project aims to perform tasks that are usual for a data scientist, such as normalize json, explore data and classifiy images.

## Setup information

To run this project, follow the steps below.

### Start the project's container

To start the main container of the project, you can use the Docker CLI.

#### Docker CLI

You must first build the image of the project:

```bash
$ sudo docker build --tag=data-science-test:1.0 .
```

Then, you can create and start the container with the following commands:

```bash
$ sudo docker create -t -i --name data-science-test \
    -p 8000:8000 -v $PWD:/home/user \
    data-science-test:1.0

$ sudo docker start data-science-test
$ sudo docker exec -it data-science-test bash
$ jupyter lab --ip 0.0.0.0 --port 8000 --allow-root
```
