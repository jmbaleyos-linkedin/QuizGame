from connector import APIClient

class GetData:
    def __init__(self):
        """Initialize attributes."""
        self.tries_counter = 0
        self.questions_data = None
        self.api_client = None
        self.request_data()

    def request_data(self):
        """Requests data from the API, retrying up to three times if no data is retrieved,
        and exits the game if the result remains empty."""
        while True:
            self.api_client = APIClient()
            if self.tries_counter == 2:
                print("Cannot reach server. Please try again later. Exiting the game")
                break
            elif self.api_client.data is None:
                self.tries_counter += 1
            else:
                self.questions_data = self.api_client.data
                break