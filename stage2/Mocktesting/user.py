import requests

def get_user_name(user_id):
    response = requests.get(
        f"https://example.com/users/{user_id}"
    )

    data = response.json()

    return data["name"]