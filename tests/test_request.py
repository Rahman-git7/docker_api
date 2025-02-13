import pytest
import requests
from unittest.mock import patch
from request import APIMonitor

def test_check_status_online():
    """API online test."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        monitor = APIMonitor()
        status = monitor.check_status()
        assert status == "online"

def test_check_status_offline():
    """API offline test."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        monitor = APIMonitor()
        status = monitor.check_status()
        assert "offline" in status

def test_check_status_connection_error():
    """Error connection test."""
    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")
        monitor = APIMonitor()
        status = monitor.check_status()
        assert "connection_error" in status