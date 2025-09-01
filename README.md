Iris KNN Classifier with Flask, Docker, and Kubernetes

Overview
This project implements a K-Nearest Neighbors (KNN) classifier for the Iris dataset, achieving 1.0 accuracy on a 70/30 train-test split. The model is served via a Flask web application with an HTML interface, allowing users to input Iris features (sepal length, sepal width, petal length, petal width) and receive predictions. The app is containerized using Docker and deployed locally to a Kubernetes cluster using Minikube. The project was developed in PowerShell on Windows 11 as part of ANA 680 Module 4 Assignment 6.
Features

KNN Model: Trained on the Iris dataset (70% training, 30% testing) with k=3, achieving 1.0 accuracy.
Flask App: A web interface (index.html) for inputting features and displaying predictions.
Docker: Containerized app with Python 3.12, Flask, and dependencies.
Kubernetes: Deployed locally using Minikube with a LoadBalancer service.

HTML Interface: Allows typing numerical inputs (1–2 decimal places) with range validation for Iris dataset features:

  Sepal Length: 4.3–7.9 cm
  
  Sepal Width: 2.0–4.4 cm
  
  Petal Length: 1.0–6.9 cm
  
  Petal Width: 0.1–2.5 cm

Directory Structure

Assignment 6/

├── app/

│   ├── model/

│   │   └── iris_knn_model.pkl

│   ├── templates/

│   │   └── index.html

│   ├── app.py

│   ├── Dockerfile

│   └── requirements.txt

├── deployment.yaml

├── service.yaml

├── data

│   └── iris.data 

└── train_model.py

train_model.py: Trains and saves the KNN model.

app.py: Flask app serving the HTML interface.

index.html: Web interface for predictions.

Dockerfile: Builds the Docker image.

requirements.txt: Lists dependencies.

deployment.yaml & service.yaml: Kubernetes manifests.

Prerequisites

Python 3.12: For training and running the Flask app.

Docker Desktop: For containerization.

Minikube: For local Kubernetes deployment (v1.36.0 used).

kubectl: Kubernetes CLI.

PowerShell: For running commands on Windows 11.

Train the Model

Ensure iris.data is in the project root (download from UCI Iris Dataset).

python train_model.py

*Output: Accuracy: 1.0*

This generates app/model/iris_knn_model.pkl.

Install Dependencies

  cd app
  
  pip install -r requirements.txt

Test Locally

  python app.py

Open http://localhost:5000 in a browser, enter values (e.g., 5.1, 3.5, 1.4, 0.2), and verify the prediction (e.g., “Iris-setosa”).

Docker Instructions

Build the Docker Image

  cd D:\Masters Of Data Science\ANA 680\Module 4\Assignment 6\app
  
  docker build -t iris-knn-app:latest .

Run the Container

  docker run -p 5000:5000 iris-knn-app:latest

Access http://localhost:5000 to use the HTML interface.

Verify Container Contents

  docker run -it iris-knn-app:latest /bin/bash
  
  ls -R

Expected:

  .: app.py  model  requirements.txt  templates

  ./model: iris_knn_model.pkl

  ./templates: index.html

Kubernetes Deployment with Minikube

Start Minikube

  minikube start --driver=docker

Build Image for Minikube

  & minikube docker-env | Invoke-Expression
  
  docker build -t iris-knn-app:latest .

Apply Kubernetes Manifests

  cd D:\Masters Of Data Science\ANA 680\Module 4\Assignment 6\app
  
  kubectl apply -f deployment.yaml
  
  kubectl apply -f service.yaml

Verify Deployment

  kubectl get pods
  
  kubectl get services

Get the URL

  minikube service iris-knn-service --url
  
  http://127.0.0.1:56645

Open the URL in a browser to access the HTML interface.

Usage

Navigate to http://localhost:5000 (Docker) or the Minikube URL (Kubernetes).

Enter Iris features (e.g., Sepal Length: 5.1, Sepal Width: 3.5, Petal Length: 1.4, Petal Width: 0.2).

Submit to see the prediction (e.g., “Prediction: Iris-setosa”).

The interface validates inputs to ensure they are numbers with 1–2 decimal places within the specified ranges.

Evidence of Completion

Model Training: train_model.py output showing 1.0 accuracy.

Docker: Successful build and browser screenshot at http://localhost:5000.

Kubernetes: Minikube start output, kubectl get pods/services, and browser screenshot at the Minikube URL.

Code: All files are included in this repository.

Acknowledgments

Randall C. Crawford

Built for ANA 680 Module 4 Assignment 6.

Uses the UCI Iris dataset.

Developed in PowerShell on Windows 11 with Docker Desktop, Minikube v1.36.0, and Kubernetes v1.33.1.
