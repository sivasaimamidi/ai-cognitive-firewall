# Use lightweight Python 3.11-slim
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (OpenEnv default is 8000, updated to 7860 for HF)
EXPOSE 7860

# Environment variables for production-ready performance
ENV WORKERS=1
ENV PORT=7860
ENV HOST=0.0.0.0

# Start FastAPI server using uvicorn
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860", "--workers", "1"]
