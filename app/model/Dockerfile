# app/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY model/iris_knn_model.pkl model/iris_knn_model.pkl
COPY templates/ templates/

CMD ["python", "app.py"]





