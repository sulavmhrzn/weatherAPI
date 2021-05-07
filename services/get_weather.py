import httpx

API_KEY: str = None


async def get_weather(city: str, country: str, units: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={country}&appid={API_KEY}&units={units}"
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={country},{city}&appid={API_KEY}&units={units}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            json_data = response.json()
            data = {
                "main": json_data["weather"][0]["main"],
                "description": json_data["weather"][0]["description"],
                "temp": json_data["main"]["temp"],
                "feels_like": json_data["main"]["feels_like"],
                "temp_min": json_data["main"]["temp_min"],
                "temp_max": json_data["main"]["temp_max"],
                "country": json_data["sys"]["country"],
                "name": json_data["name"],
            }
            return data
        return response.json()
