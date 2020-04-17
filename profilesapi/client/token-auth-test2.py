import requests

def client():
    token = "Token 82ecc77031f98a388b74ee85cd42a0341c3fd4a6"
    headers = {"Authorization": token}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                              headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()