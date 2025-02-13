import os
import requests
import logging
from typing import Optional

class APIMonitor:
    """Main class for the API monitor"""
    
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    LOG_FILE = "api_monitor.log"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    def __init__(self):
        self._setup_logging()
        self.api_url = self._load_config()
        
    def _load_config(self) -> str:
        """Load the API URL from environment variables"""
        api_url = os.getenv("API_URL")
        if not api_url:
            raise ValueError("API_URL must be set in environment variables")
        return api_url

    def _setup_logging(self) -> None:
        """Configure logging for the monitor"""
        os.makedirs(self.LOG_DIR, exist_ok=True)
        logging.basicConfig(
            filename=os.path.join(self.LOG_DIR, self.LOG_FILE),
            level=logging.INFO,
            format=self.LOG_FORMAT
        )

    def check_status(self) -> str:
        """API status check"""
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return "online"
            return f"offline: {response.status_code}"
            
        except requests.exceptions.ConnectionError as e:
            return f"connection_error: {e}"
            
        except requests.exceptions.RequestException as e:
            return f"request_error: {e}"

    def monitor(self) -> None:
        """Execute the monitoring process"""
        status = self.check_status()
        
        logging.info(f"API status: {status}")
        print(f"API status: {status}")

        if any(error in status for error in ("offline", "error")):
            logging.error(f"ALERT: {status}")
            print(f"ALERT: {status}")

if __name__ == "__main__":
    monitor = APIMonitor()
    monitor.monitor()