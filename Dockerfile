# Start with a Python 3.9 slim image as the base image.
FROM python:3.9-slim

#Set the working directory in the container to /app.
WORKDIR /app

#Set environment variables for Flask
ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

# Copy the current directory (containing the Flask app) into the /app directory in the container.
COPY . /app

#Install the dependencies specified in requirements.txt using pip, without caching.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the container, allowing access to the Flask app.
EXPOSE 8000

#Set the dfault command to run the flask application

CMD ["flask", "run", "--host=0.0.0.0"]

