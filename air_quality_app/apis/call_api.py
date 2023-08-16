from django.conf import settings
import requests

class AirQuality:

    @classmethod
    def get_quality_data(cls, city=None):
        if city is None:
            url = f"http://api.waqi.info/feed/here/?token={settings.AQI_TOKEN}"
        else:
            url = f"http://api.waqi.info/feed/{city}/?token={settings.AQI_TOKEN}"
        headers = {
            "Content-Type": "application/json",
        }
        """Get air quality data."""
        response = requests.request("GET", url, headers=headers)
        if "status" in response.json().keys():
            if response.json().get("status") == "ok":
                data = response.json()
            else:
                url = f"http://api.waqi.info/feed/here/?token={settings.AQI_TOKEN}"
                headers = {
                    "Content-Type": "application/json",
                }
                """Get air quality data."""
                response = requests.request("GET", url, headers=headers)
                if "status" in response.json().keys():
                    if response.json().get("status") == "ok":
                        data = response.json()
                    else:
                        data = {
                            "status": "error",
                            "data": {
                                "aqi": 0,
                                "idx": 0,
                                "city": {"name":city}
                            },
                            "message": "location not found"
                        }
                else:
                    data = {
                    "status": "error",
                    "data": {
                        "aqi": 0,
                        "idx": 0,
                        "city": {"name":city}
                    },

                    "message": "location not found"
                }
        else:
            data = {
                "status": "error",
                "data": {
                    "aqi": 0,
                    "idx": 0,
                    "city": {"name":city}
                },
                "message": "location not found"
            }
        return data

    
    @classmethod
    def get_city(cls, ip_addr):
        """Handle HTTP GET request."""
        url = f"https://ipinfo.io/{ip_addr}?token={settings.IPINFO_TOKEN}"
        headers = {
            "Content-Type": "application/json",
        }
        """Get air quality data."""
        response = requests.request("GET", url, headers=headers)
        return response.json().get("region")