# Logalysis - Design Doc

In this coding exercise, I have designed a simple API whose main task involves receiving user input in the form of a log file and performing some processing on the backend to serve up a JSON response back to the user as output.

### PART I - Designing a Flask API to process log files

Since the task involved is a simple one where the user uploads a log file to be processed and receives a JSON response, I have decided to expose a single URL endpoint which will serve as both where the user submits a request and receives a response.

The URL endpoint is - ```http://127.0.0.1:5000/fileinput```

Once the user uploads a log file of appropriate format, a Python function ```process_log_input()``` is then triggered by the route decorator to perform the necessary processing. 

The file and its contents are first saved at a designated Uploads folder location after which a file read operation is performed. After processing all the lines of the file, we create a JSON output and send it back to the user via ```jsonify()``` through the Flask API.

To run the application, the user has to first navigate to the root folder ```Flask App``` that contains the python script ```app.py```. Then, the following command is executed:

```flask run```

This fires up a web server at localhost ```127.0.0.1```, ```port 5000``` and route ```/fileinput``` serves up a HTML template that contains form input for the user to upload the log file.

### PART II - Writing a Dockerfile to dockerize the flask application.

In order to run the flask application on a Docker container, we first need to write a Dockerfile and a corresponding docker compose YAML file on the macOS platform with Docker Desktop daemon running in the background.

The Dockerfile, which is used to create a Docker image that contains Python and web framework Flask as a dependency, has the following steps and commands in it:

* First, we pull up a pre-built official Python image from Dockerhub

* Next, we add everything in the current (root) folder to a directory in the image.

* Then, we set the working directory inside the image

* Finally, we run the following command to install any dependencies and libraries required to run the flask application

```pip install -r requirements.txt```

Here, ```requirements.txt``` contains Flask with its current version.

The ```docker-compose.yml``` file will be used to run a Docker container using the docker image created previously. The contents of the docker compose file include the following elements:

* ```version``` tag is used to define the docker compose file format
* ```services``` tag is used to define the services required for our application, in this case - ```app```
* ```build``` command builds the Docker image using the Dockerfile created earlier
* ```ports``` tag is used to define both host and container ports
* ```volumes``` tag is used to mount a folder from the host machine to the container.

To start and run the entire Flask application on the container, we execute the following command:

```docker compose up```

The Flask application running inside the container can again be accessed at ```127.0.0.1``` and ```port 5000```
