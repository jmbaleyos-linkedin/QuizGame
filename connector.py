import requests
class APIClient:
    def __init__(self):
        """Initialize attributes. Assigning the API link as default value."""
        self.url = "https://opentdb.com/api.php?amount=10&difficulty=easy"
        self.data = None
        self._fetch_data()

    def _fetch_data(self):
        """Executing the API link. Checks the response code then extracting the JSON data."""
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Unable to connect to server. Error: {response.status_code}")