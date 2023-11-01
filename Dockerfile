# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install the FLAC utility
RUN apt-get update && apt-get install -y flac

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg


# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000
