from python:3.8-alpine

# Add scripts to the running container
ENV PATH="/scripts:${PATH}"

# Copy requirements.txt to the Docker image
COPY ./requirements.txt /requirements.txt

