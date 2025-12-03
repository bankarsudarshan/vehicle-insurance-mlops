# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . /app

# Install the dependencies
# will run the command within /app
RUN pip install .

# Expose the port FastAPI will run on
EXPOSE 5000

# Command to run the FastAPI app
# the default command to execute when the container starts
CMD ["python3", "app.py"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]