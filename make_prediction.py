import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'MSSubClass': 120,
    'LotFrontage': 80,
    'LotArea': 1500,
    'OverallQual': 7,
    'YearBuilt': 2005,
    'GrLivArea': 2000
}

print(f"Sending POST request to {url} with data: {data}")
response = requests.post(url, json=data)
print(response.status_code)  # Check the status code
print(response.json())  # Check the response
