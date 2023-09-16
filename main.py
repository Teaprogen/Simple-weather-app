import requests

api = "https://api.weatherapi.com/v1/current.json"
key = 'YOUR_API_KEY_HERE'

if __name__ == "__main__":
    print("Please imput location of your interest")
    name = input()
    response = requests.get(api, params={"key":key,"q": name,})
    if response.status_code == 200:
        response_json = response.json()
        print(f"""
            The wether at {response_json["location"]["name"]} is {response_json['current']['condition']['text']}
            With temperature about {response_json['current']['temp_c']} C ({response_json['current']['temp_f']} F)
            """)
    else:
        print(response.json()['error']['message'])