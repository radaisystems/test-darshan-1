

# Python Dockerfile

FROM python:3.11-slim


# Set working directory
WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y \
    
    && rm -rf /var/lib/apt/lists/*


# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .



# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE {{ values.port }}

# Health check

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:{{ values.port }}/health || exit 1


# Start the application
CMD ["python", "app.py"]



