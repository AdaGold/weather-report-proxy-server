
from flask import Blueprint, request
import os
from dotenv import load_dotenv
import requests

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

location_key = os.environ.get("LOCATION_KEY")
weather_key = os.environ.get("WEATHER_KEY")

@proxy_bp.get("/location")
def get_lat_lon():
    loc_query = request.args.get("q")
    if not loc_query:
        return {"message": "must provide q parameter (location)"}, 400

    response = requests.get(
        "https://us1.locationiq.com/v1/search.php",
        params={"q": loc_query, "key": location_key, "format": "json"}
    )

    return response.json(), 200

@proxy_bp.get("/weather")
def get_weather():
    lat_query = request.args.get("lat")
    lon_query = request.args.get("lon")
    print(lat_query, lon_query)
    print(weather_key)
    if not lat_query or not lon_query:
        return {"message": "must provide lat and lon parameters"}, 400

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"lat": lat_query, "lon": lon_query, "appid": weather_key}
    )
    return response.json(), 200

