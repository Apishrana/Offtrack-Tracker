import os
import requests


def usdRate():
    fb = float(os.getenv("USD", 94.53))
    try:
        res = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=3,
        )
        res.raise_for_status()
        data = res.json()
        return data["rates"]["INR"]
    except:
        return fb
