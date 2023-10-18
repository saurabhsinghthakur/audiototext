# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000