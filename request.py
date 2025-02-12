import requests
import os
import logging

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
    api_url = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts") # load the api url from the environment variable
    return api_url

def setup_logging():
    log_dir = "/app/logs" # define the log directory
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=os.path.join(log_dir, "api_monitoring.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_status(status):
    logging.info(f"Api status: {status}") # save the api status to the log file

def alert_error(status):
    logging.error(f"ALERT : API is offline or in error {status}") # save the api status to the log file



if __name__ == "__main__":
    setup_logging() # configure the logging module
    api_url = load_config() # load the api url from the config file
    status = check_api_status(api_url)
    log_status(status)
    if "offline" in status or "error" in status:
        alert_error(status)
        print(f"ALERT: API is offline or in error. Status :{status}")
    else:
        print(f"Api status: {status}")

