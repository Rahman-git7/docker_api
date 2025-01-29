import requests

def check_api_status(url): 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "online"
        else:
            return f"offline: {response.status_code}"
    except requests.exceptions.ConnectionError as e:
        return f"offline: {e}"
    except requests.exceptions.RequestException as e:
        return f"error: {e}"

api_url = "https://jsonplaceholder.typicode.com/posts"
status = check_api_status(api_url)
print(f"Api status: {status}")