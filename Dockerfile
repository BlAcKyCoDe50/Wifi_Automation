# Use the official Python base image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    tcl8.6 \
    tk8.6 \
    unixodbc \
    unixodbc-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

COPY  lpu-bg.png /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
COPY lpu-bg.png /app/

# Entry point to start Xvfb and then run the application
ENTRYPOINT ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & export DISPLAY=:99 && python code-with-D.py"]
