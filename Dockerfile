# Use official Python 3.11.8 image
FROM python:3.11.8-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port (Flask default)
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]

