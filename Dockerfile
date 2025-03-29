FROM python:3.10-slim as builder

WORKDIR /app

# Copy just the requirements and setup files first to leverage Docker cache
COPY pyproject.toml setup.py ./
COPY src/llamacalc/__init__.py ./src/llamacalc/

# Install build dependencies and the package in development mode
RUN pip install --no-cache-dir build wheel
RUN pip wheel --no-deps --wheel-dir /app/wheels .

# Start a fresh stage for the runtime
FROM python:3.10-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy wheels from the builder stage
COPY --from=builder /app/wheels /app/wheels

# Install the package
RUN pip install --no-cache-dir /app/wheels/*

# Create a non-root user to run the app
RUN useradd -m llamauser
USER llamauser

# Create cache directory
RUN mkdir -p /home/llamauser/.llamacalc

# Set up a volume for persistent cache
VOLUME /home/llamauser/.llamacalc

# Set up entrypoint
ENTRYPOINT ["llamacalc"]

# Default to help/usage information if no arguments provided
CMD ["--help"]