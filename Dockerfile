# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port (default is 5000)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]  # Change app.py to your main Flask file name
