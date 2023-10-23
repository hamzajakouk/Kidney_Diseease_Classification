# Use an appropriate base image with Python (e.g., python:3.8-slim-buster)
FROM python:3.8-slim-buster

# Set the working directory within the container
WORKDIR /app

# Copy your Streamlit Python script and any other necessary files
COPY . /app

# Install any required dependencies
RUN pip install -r requirements.txt

# Expose the Streamlit port (8501 is the default)
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "strm.py"]
