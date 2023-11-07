# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python in unbuffered mode and disable pycache
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory within the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install Python packages from requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container at /app
COPY . /app/

# Expose a port for your Django application (adjust as needed)
EXPOSE 8005

# Start the Django application (adjust the command as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
