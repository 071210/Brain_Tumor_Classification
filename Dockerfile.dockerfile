FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install requirements
RUN pip install -r requirements.txt

# Expose port
EXPOSE 10000

# Run Flask
CMD ["python", "app.py"]
