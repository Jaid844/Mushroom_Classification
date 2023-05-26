FROM render/base:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables, if needed
# ENV VARIABLE_NAME=value

# Expose the port on which your application listens
EXPOSE 8000

# Start the application
CMD [ "python", "app.py" ]