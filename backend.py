import requests

API_KEY = "3cb20440456110257a2a9d8889b838c4"
def get_date(place, forecast=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    print(get_date(place="Tokyo"))