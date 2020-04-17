import requests

def client():
    data = {
        "username": "teste1234", 
        "email": "email@teste1234.com",
        "password1": "qwerty1234#",
        "password2": "qwerty1234#"
        }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                              data=data)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()