# 🏠 House Price Prediction API

This project is a simple Flask-based web API that predicts the price of a house using a trained machine learning model. The model takes in a few key features about a house (e.g., square footage, lot size, quality, etc.) and returns the predicted price.

---

## 🚀 Features

- RESTful API using Flask
- Accepts JSON input for prediction
- Returns predicted house price in formatted currency
- Includes a basic HTML form for manual input
- Uses a pre-trained `LinearRegression` model

---

## 🧠 Model Features Used

The model predicts house prices using the following features:

- `MSSubClass`: The type of dwelling
- `LotFrontage`: Linear feet of street connected to property
- `LotArea`: Lot size in square feet
- `OverallQual`: Overall material and finish quality
- `YearBuilt`: Original construction date
- `GrLivArea`: Above grade (ground) living area square feet

---

## 🛠️ Requirements

- Python 3.x
- Flask
- pandas
- scikit-learn
- joblib
- numpy

Install dependencies:
```bash
pip install flask pandas scikit-learn joblib numpy
house_price_prediction_project/
│
├── app.py                  # Flask API app
├── house_price_model.pkl   # Trained ML model
├── make_prediction.py      # Python script to test API
├── templates/
│   └── index.html          # Web form for manual input
└── README.md               # This file
python app.py
By default, the app runs at http://127.0.0.1:5000

Visit the browser:
Go to http://127.0.0.1:5000 and input house details using the HTML form.