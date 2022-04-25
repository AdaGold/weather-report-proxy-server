
from flask import Blueprint

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)
location_key = os.environ.get("LOCATION_KEY")
weather_key = os.environ.get("WEATHER_KEY")


@proxy_bp.route("/location", methods=["GET"])
def get_lat_lon():
    return "Lat, Lon!"


@proxy_bp.route("/weather", methods=["GET"])
def get_weather():
    return "Weather!"
