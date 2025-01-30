import requests
import configparser

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

def load_config():
    try:
        config = configparser.ConfigParser() # create a new instance of ConfigParser to read the config file
        config.read("config.ini")
        return config["DEFAULT"]["url"]
    except (configparser.Error, KeyError) as e:
        print(f"Error reading config file: {e}")
        exit(1)

api_url = load_config()
status = check_api_status(api_url)
print(f"Api status: {status}")

