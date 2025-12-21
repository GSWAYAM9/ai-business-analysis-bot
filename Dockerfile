# ===============================
# Base image
# ===============================
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# System dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libffi-dev \
    libssl-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Set working directory
# ===============================
WORKDIR /app

# ===============================
# Backend dependencies
# ===============================
COPY backend/requirements.txt backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# ===============================
# Frontend build
# ===============================
COPY frontend frontend
WORKDIR /app/frontend
RUN npm install
RUN npm run build

# ===============================
# Backend source
# ===============================
WORKDIR /app
COPY backend backend

# ===============================
# Expose port
# ===============================
EXPOSE 8080

# ===============================
# Start BOTH frontend & backend
# ===============================
CMD uvicorn backend.app:app --host 0.0.0.0 --port 8080
