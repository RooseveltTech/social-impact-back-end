import requests

class AirQuality:

    @classmethod
    def get_quality_data(cls, city=None):
        if city is None:
            url = "http://api.waqi.info/feed/here/?token=fb6107dda11d7fe319f54e9a2924f0f551e5dbfc"
        else:
            url = f"http://api.waqi.info/feed/{city}/?token=fb6107dda11d7fe319f54e9a2924f0f551e5dbfc"
        headers = {
            "Content-Type": "application/json",
        }
        """Get air quality data."""
        response = requests.request("GET", url, headers=headers)
        if "status"in response.json().keys():
            if response.json().get("status") == "ok":
                data = response.json()
            else:
                data = {
                    "status": "error",
                    "message": "location not found"
                }
        else:
            data = {
                "status": "error",
                "message": "location not found"
            }
        return data

    
    @classmethod
    def get_city(cls, ip_addr):
        """Handle HTTP GET request."""
        url = f"https://ipinfo.io/{ip_addr}?token=27ef33152cacc4"
        headers = {
            "Content-Type": "application/json",
        }
        """Get air quality data."""
        response = requests.request("GET", url, headers=headers)
        return response.json().get("region")