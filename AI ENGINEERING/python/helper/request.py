import requests

response = requests.get("https://api.github.com/users/dhanushkumar-amk")

print(response.status_code)     # 200
print(response.url)             # full URL
print(response.headers)         # response headers dict
print(response.text)            # raw string body
print(response.json())          # parsed JSON → Python dict
