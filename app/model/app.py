# app/app.py
from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

# Load the model
model_path = os.path.join('model', 'iris_knn_model.pkl')
model = joblib.load(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data
            features = [
                float(request.form['sepal_length']),
                float(request.form['sepal_width']),
                float(request.form['petal_length']),
                float(request.form['petal_width'])
            ]
            features = np.array(features).reshape(1, -1)
            prediction = model.predict(features)[0]
            return render_template('index.html', prediction=prediction, error=None)
        except Exception as e:
            return render_template('index.html', prediction=None, error=str(e))
    return render_template('index.html', prediction=None, error=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)