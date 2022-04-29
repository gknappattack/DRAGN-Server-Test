import json
import requests

class Client:
    def __init__(self, ip="localhost", port="8088", path="/"):
        self.ip = ip
        self.port = port
        self.path = path

    def set_ip(self, ip):
        self.ip = ip
    
    def set_port(self, port):
        self.port = port
    
    def set_path(self, path):
        self.path = path
    
    def communicate_with_server(self, message="This is a test message"):
        # Assemble url for request
        url = "http://" + self.ip + ":" + self.port + self.path
        
        # Create json object for request
        json_message = {}
        json_message["text"] = message

        # Send request
        client_request = json.dumps(json_message)

        # Receive response
        server_response = json.loads(requests.post(url, client_request).text)

        return server_response['text']

class Console:
    def __init__(self):
        self.chatbot_index_mapping = {
            0:"ECHO",
            1:"TREVOR",
            2:"KEVIN"
        }

        self.chatbot_path_mapping = {
            0:"/chatbot/echo",
            1:"/chatbot/trevor",
            2:"/chatbot/kevin"
        }

        self.ip = "192.168.86.65"
        self.port = "8088"

    def print_all_chatbots(self):
        print("\nPrinting all available chatbots!!")

        for key in  self.chatbot_index_mapping.keys():
            print(f"Index: {key} == Chatbot: {self.chatbot_index_mapping.get(key)}")

        print("")


    def receive_input(self):
        print("Welcome to DRAGNTown Chatbot Test Interface\n")

        while True:
            user_in = input("Select a chatbot to interface with: ")

            # Check to print all chatbots
            if user_in == "--help" or user_in == "-h":
                self.print_all_chatbots()
            else: # Process input like normal
                try:
                    int_input = int(user_in)
                    #print("User input: ", user_in)

                    if 0 > int_input or int_input >= len(self.chatbot_index_mapping):
                        raise LookupError("Invalid input. Number outside of chatbot indices range. \nView chatbot indices using -h or \"--help\"\n")
                    
                    # Get path to chatbot
                    else:
                        chatbot_path = self.chatbot_path_mapping.get(int_input)
                        #print("Chatbot Path: ", chatbot_path)
                        try:
                            client = Client(self.ip, self.port, chatbot_path)
                            # Get user input for message to send.
                            user_message = input(f"\nType a message to send to {self.chatbot_index_mapping.get(int_input)}: ")

                            # Send message through client
                            server_response = client.communicate_with_server(message=user_message)

                            print(f"\n{self.chatbot_index_mapping.get(int_input)} says: " + server_response + "\n")

                        # Catch exceptions for communication failures.
                        except requests.exceptions.ConnectionError as e:
                            print(e)


                except ValueError:
                    print("Invalid input. User input must be an integer value. \nView chatbot indices using -h or \"--help\"\n")
                except LookupError as e:
                    print(e)

if __name__ == "__main__":
    console = Console()
    console.receive_input()