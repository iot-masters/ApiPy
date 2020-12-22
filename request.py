import requests

port = "http://127.0.0.1:5000/"

print('Enter the value:')
x = input()
response = requests.get(port+"testing/"+x)
print(response.json())
