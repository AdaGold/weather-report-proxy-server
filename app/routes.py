
from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import requests

load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

location_key = os.environ.get("LOCATION_KEY")
weather_key = os.environ.get("WEATHER_KEY")

