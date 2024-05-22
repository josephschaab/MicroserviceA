import requests

BASE = "http://127.0.0.1:5000/"

# Receive data
data = [{"name": "image0", "image_url": "abc"}, {"name": "image1", "image_url": "def"}, {"name": "image2", "image_url": "ghi"}]

for i in range(len(data)):
    response = requests.post(BASE + "image/" + str(i), data[i])
    print(response.json())

input()

# Delete data
response = requests.delete(BASE + "image/0")
print(response)

input()

# Request data
response = requests.get(BASE + "image/2")
print(response.json())
