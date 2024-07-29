FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    python3-dev \
    libmtdev-dev \
    xclip \
    xsel \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Kivy
RUN pip install kivy

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Expose the port the app runs on (if needed)
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
