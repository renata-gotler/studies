FROM python:3.10.0

## System Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Remove unused files to make the image smaller
RUN apt-get autoremove -yqq --purge \
    && apt-get clean

# Python Packages
COPY requirements.txt /requirements.txt

# Install Pip Requirements
RUN pip install -r requirements.txt

# Install cv2 dependencies
RUN apt-get update && apt-get install libgl1

## Create User Directory
RUN mkdir -p /home/user

ENV PYTHONPATH "${PYTHONPATH}:/home/user"

WORKDIR /home/user
