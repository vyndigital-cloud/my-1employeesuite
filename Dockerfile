# Use official Python 3.11.8 slim image
FROM python:3.11.8-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (adjust if your Flask app uses another)
EXPOSE 5000

# Command to run your Flask app
CMD ["python", "app.py"]
