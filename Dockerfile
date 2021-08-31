# Pull the base image
FROM python:3.9.6

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set the work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/