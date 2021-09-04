# Pull the base image
FROM python:3.9.7-slim-buster

# Create Group and User
RUN groupadd -r rostockerlabs &&  useradd -r rostockerdev -G rostockerlabs

# Set the work directory
WORKDIR /app

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /app

RUN chown -R rostockerdev /app
USER rostockerdev