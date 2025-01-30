import requests
import configparser
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
    try:
        config = configparser.ConfigParser() # create a new instance of ConfigParser to read the config file
        config.read("config.ini")
        return config["DEFAULT"]["url"]
    except (configparser.Error, KeyError) as e:
        print(f"Error reading config file: {e}")
        exit(1)

def setup_logging():
    logging.basicConfig(
        filename= "api_monitor.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_status(status):
    logging.info(f"Api status: {status}") # save the api status to the log file

def alert_error(status):
    logging.error(f"Api status: {status}") # save the api status to the log file



if __name__ == "__main__":
    setup_logging() # configure the logging module
    api_url = load_config() # load the api url from the config file
    status = check_api_status(api_url)
    log_status(status)
    if "offline" in status or "error" in status:
        alert_error(status)
    print(f"Api status: {status}")

