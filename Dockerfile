# Use a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the gRPC port (replace with your actual port if different)
EXPOSE 50051

# Command to run your gRPC server
CMD ["python", "./grpc/server.py"]