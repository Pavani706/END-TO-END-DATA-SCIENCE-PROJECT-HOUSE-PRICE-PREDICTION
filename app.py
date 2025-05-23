from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            float(request.form['MSSubClass']),
            float(request.form['LotFrontage']),
            float(request.form['LotArea']),
            float(request.form['OverallQual']),
            float(request.form['YearBuilt']),
            float(request.form['GrLivArea'])
        ]

        prediction = model.predict(np.array(features).reshape(1, -1))
        result = f"${prediction[0]:,.2f}"
        return render_template('index.html', prediction=result)
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
