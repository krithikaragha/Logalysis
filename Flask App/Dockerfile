# Pull up the python image 
FROM python:alpine3.7

# Copy the flask app into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install all dependencies and packages in requirements.txt
RUN pip install -r requirements.txt

# Expose the 5001 port
EXPOSE 5001

# Configure the container to run
ENTRYPOINT ["python"]

CMD ["app.py"]
