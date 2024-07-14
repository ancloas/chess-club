# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for Flask
ENV FLASK_APP 'app.py'

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
