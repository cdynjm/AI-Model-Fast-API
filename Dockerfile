# Use Python 3.7 base image
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Copy your code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN python train.py

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]