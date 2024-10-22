# Weather Report proxy server

The Weather Report proxy server is to be used with the [Weather Report web app project](https://github.com/adaGold/weather-report)

## Quick Start

1. Clone this repository. **You do not need to fork it first.**
    - `git clone https://github.com/AdaGold/weather-report-proxy-server.git`

1. Create and activate a virtual environment
     ```bash 
       $ python3 -m venv venv
       $ source venv/bin/activate
     ```

2. Install the `requirements.txt`
    ```bash
     (venv) $ pip install -r requirements.txt
    ```
3. Create a `.env` file with your API keys
    ```bash
    # .env

    # LocationIQ API key
    LOCATION_KEY="replace_with_your_api_key"

    # OpenWeather API Key
    WEATHER_KEY="replace_with_your_api_key"
    ```

4. Run the server
    ```bash
     (venv) $ flask run --debug
    ```

## Endpoints

| Route | Query Parameter(s) | Query Parameter(s) Description |
|--|--|--|
|`GET` `/location`| `q` | Free-form query string to search for. For `Weather Report`, this should be the city name. |
|`GET` `/weather` |`lat` & `lon`|Geographical coordinates (latitude, longitude)|


