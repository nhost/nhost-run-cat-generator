# Start with a base image containing Python runtime
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add the requirements file to the container
ADD requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application when the container launches
CMD ["python", "cat-generator.py"]

