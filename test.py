import joblib
import pandas as pd

# Load the saved model
model = joblib.load('house_price_model.pkl')

# Sample input for prediction
data = {
    'MSSubClass': [120],
    'LotFrontage': [80],
    'LotArea': [1500],
    'OverallQual': [7],
    'YearBuilt': [2005],
    'GrLivArea': [2000]
}

df = pd.DataFrame(data)

# Make predictions
predicted_price = model.predict(df)
print(f"Predicted House Price: ${predicted_price[0]:,.2f}")
