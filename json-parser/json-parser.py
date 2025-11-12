import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
    first_10 = todos[:10]  # Slice to get the first 10
    print("First 10 todos:")
    for todo in first_10:
        print(todo)
else:
    print(f"Request failed with status code {response.status_code}")


for todo in first_10:
    print(todo["title"])