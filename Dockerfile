# Get the base image
FROM python:3.8-slim

# Create user
RUN useradd -ms /bin/bash user
USER user

# Set the working directory
WORKDIR /DangerousPickle

# Create flag
RUN touch /tmp/flag.txt
RUN echo "RubenDidNothingWrong" > /tmp/flag.txt
RUN chmod 075 /tmp/flag.txt

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 5000
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]