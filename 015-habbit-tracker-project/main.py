import random
import requests
import webbrowser
import datetime
import json


def generate_token():
    text = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_token = ""
    for _ in range(26):
        new_token += random.choice(text)
    return new_token


class Account:
    def __init__(self, username):
        self.API_END_POINT = "https://pixe.la"
        self.username = username.lower()
        self.token = ""
        self.graphs = []

    # 1. Create an account on pixe.la
    def create_new_user(self, not_minor='yes', agree_to_terms_of_services='yes'):
        """
        This Function will Create a user with the given username and RETURN a TOKEN. the Token is necessary for further usages.

        username[REQUIRED] = [required] User name for this service. Validation rule: [a-z][a-z0-9-]{1,32}
        not_minor[optional] = it is true by default, if you change it to false the user won't be created
        agree_to_terms_of_services[optional] = it is true by default, if you change it to no the user won't be created

        Read The Terms of Services HERE: https://github.com/a-know/Pixela/wiki/Terms-of-Service

        """
        create_user_endpoint = f"{self.API_END_POINT}/v1/users"
        generated_token = generate_token()
        request_data = {
            "token": generated_token,
            "username": self.username,
            "agreeTermsOfService": agree_to_terms_of_services,
            "notMinor": not_minor,
        }
        response = requests.post(url=create_user_endpoint, json=request_data).json()
        if response["isSuccess"]:
            self.token = generated_token
        print(response)

    # 2. Create a Graph Definition
    def create_new_graph(self, graph_id, graph_name, graph_unit, graph_type, graph_color="shibafu",
                         timezone="UTC"):
        """
        username[REQUIRED], token[REQUIRED], graph_id[REQUIRED], graph_unit[REQUIRED], graph_type[REQUIRED], graph_color[optional]-green by default, timezone[optional] - UTC by default
        Key	     Type	     Description
        id	     string	 [required] It is an ID for identifying the pixelation graph.
                         Validation rule: ^[a-z][a-z0-9-]{1,16}
        name	 string	 [required] It is the name of the pixelation graph.
        unit	 string	 [required] It is a unit of the quantity recorded in the pixelation graph. Ex. commit, kilogram, calorie.
        type	 string	 [required] It is the type of quantity to be handled in the graph. Only int or float are supported.
        color	 string	 [required] Defines the display color of the pixel in the pixelation graph.
                             shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind.
        timezone string	[optional] Specify the timezone for handling this graph as Asia/Tokyo. If not specified, it is treated as UTC.
        """

        create_graph_url = f"{self.API_END_POINT}/v1/users/{self.username}/graphs"
        headers = {
            "X-USER-TOKEN": self.token,
        }
        request_data = {
            "id": graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": graph_type,
            "color": graph_color,
            "timezone": timezone,
        }
        response = requests.post(url=create_graph_url, json=request_data, headers=headers).json()
        if response["isSuccess"]:
            self.graphs.append(request_data)

    # 3. Get The Graph!!!
    def display_graph(self, graph_id):
        graph_url = f"{self.API_END_POINT}/v1/users/{self.username}/graphs/{graph_id}"
        webbrowser.open(graph_url)

    def __str__(self):
        graphs_names = [item["name"] for item in self.graphs]
        return f"Username: {self.username} \nGraphs_count: {len(self.graphs)} \nGraphs: {graphs_names}"

    # 4. Post Value to a graph
    def post_value_to_graph(self, graph_id, quantity, date=f"{datetime.datetime.now().strftime('%Y%d%m')}"):
        post_to_graph_url = f"{self.API_END_POINT}/v1/users/{self.username}/graphs/{graph_id}"
        request_data = {
            "date": date,
            "quantity": quantity,
        }
        headers = {
            "X-USER-TOKEN": self.token,
        }
        response = requests.post(url=post_to_graph_url, json=request_data, headers=headers).json()
        if response["isSuccess"]:
            print("Value Added to the graph")


new_user = Account("username")

## Saving Information:
new_data = {new_user.username: {"token": new_user.token, "graphs": new_user.graphs}}
data = None
try:
    with open("accounts.json", 'r') as file:
        database = json.load(file)
        database.update(new_data)
        data = database
except FileNotFoundError:
    data = new_data
except AttributeError:
    data = new_data
finally:
    with open("accounts.json", 'w') as new_file:
        json.dump(data, new_file)
