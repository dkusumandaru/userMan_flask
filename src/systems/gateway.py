import requests

class Gateway():

    def auth(destination, content, headers):
        print("success a")
        response = requests.post(destination, json=content, auth = headers)
        result = response.json()

        print(result)
        return result

    def post(destination, content, headers):
        print(content)
        print(headers)
        print("success p")
        response = requests.post(destination, json=content, headers = headers)
        result = response.json()

        print(result)
        return result


    def get():
        pass