import requests

url = "http://127.0.0.1:5000/api/time"
data = {"sleep": 8, "study": 3, "fun": 2, "sport": 1}

response = requests.post(url, json=data)
print(response.json())