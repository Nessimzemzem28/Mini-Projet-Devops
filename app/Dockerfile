FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code and manage.py
COPY app/ ./app
COPY manage.py .

EXPOSE 5000
CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "5000"]

