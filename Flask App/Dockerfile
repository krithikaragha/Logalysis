# Pull up a pre-built Python image from Docker Hub
FROM python:3.9.1

# Add everything in current folder to a directory in the image
ADD . /logalysis-docker

# Set the working directory 
WORKDIR /logalysis-docker

# Install any dependencies for the application
RUN pip install -r requirements.txt

# Expose the port for the Flask application to run
EXPOSE 5001

