

# Use an official lightweight Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
# Copy just the requirements.txt initially to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . /app

# Remove unnecessary files and clear cache to reduce the image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Use gunicorn as the entrypoint, better suited for production than the basic Flask server
ENTRYPOINT ["gunicorn", "-b", ":5000", "app:app"]
