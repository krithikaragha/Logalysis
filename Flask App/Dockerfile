# Pull up the python image 
FROM python:3.7.6

# Add everything in current directory to the image 
ADD . /logalysis-docker

# Set the working directory
WORKDIR /logalysis-docker

# Install all dependencies and packages in requirements.txt
RUN pip install -r requirements.txt
