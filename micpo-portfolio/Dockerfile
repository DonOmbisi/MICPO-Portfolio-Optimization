FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    python3 \
    python3-pip \
    python3-venv \
    libeigen3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /micpo-portfolio

# Copy Python requirements
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . ./

# Build C++ solver using CMake
WORKDIR /micpo-portfolio/cpp
RUN mkdir -p build && cd build && cmake .. && make

# Add C++ binary to PATH
ENV PATH="/micpo-portfolio/cpp/build:${PATH}"

# Back to root
WORKDIR /micpo-portfolio

# Default command
CMD ["python3", "main.py"]
