"""Iowa Environmental Mesonet (IEM) -- an API hosted by Iowa State.

Flow:  Python program -> IEM API -> JSON response -> extract data -> display

The important difference from weather_app.py: Open-Meteo gives you a *forecast*
produced by a computer model. IEM gives you *observations* -- what physical
instruments at Iowa airports actually recorded. That is why the two disagree.
"""
import requests
from datetime import date, timedelta

BASE_URL = "https://mesonet.agron.iastate.edu/api/1"
NETWORK = "IA_ASOS"  # airport weather stations across Iowa

COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

# METAR sky-cover abbreviations
SKY_COVER = {
    "CLR": "clear",
    "SKC": "clear",
    "FEW": "a few clouds",
    "SCT": "scattered clouds",
    "BKN": "broken clouds",
    "OVC": "overcast",
    "VV": "vertical visibility obscured",
}

def to_compass(degrees):
    """Turn a wind bearing in degrees into a compass point like 'SE'."""
    if degrees is None:
        return "unknown"
    return COMPASS[round(degrees / 22.5) % 16]

def knots_to_mph(knots):
    return None if knots is None else knots * 1.15078

def f_to_c(fahrenheit):
    return None if fahrenheit is None else (fahrenheit - 32) * 5 / 9

def fetch(endpoint: str, **params):
    """Call an IEM endpoint and hand back the rows.

    IEM answers with a 'table' shaped payload: {"schema": {...}, "data": [...]}.
    The schema lists ~70 possible columns; 'data' holds one dict per row. Most
    columns are null for any given station, so always use .get() on these rows.
    """
    response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=30)
    response.raise_for_status()  # raise an error if the request failed
    return response.json()["data"]

def current_conditions(station: str = "AMW"):
    """Latest observation for one station. AMW is the Ames municipal airport."""
    # One call returns every station in the network, so filter down to ours.
    rows = fetch("currents.json", network=NETWORK)
    for row in rows:
        if row["station"] == station:
            return row
    raise ValueError(f"Station {station!r} not found in network {NETWORK}")

def all_current():
    """Latest observation for every station in the network."""
    return fetch("currents.json", network=NETWORK)

def day_history(station: str = "AMW", day: str = None):
    """Every observation a station reported on one date (usually hourly)."""
    if day is None:
        day = str(date.today() - timedelta(days=1))
    return fetch("obhistory.json", network=NETWORK, station=station, date=day)

def describe_sky(row) -> str:
    """Build a readable sky description from the METAR cloud layers."""
    layers = []
    for i in (1, 2, 3, 4):
        cover = row.get(f"skyc{i}")
        level = row.get(f"skyl{i}")
        if not cover:
            continue
        text = SKY_COVER.get(cover, cover)
        layers.append(f"{text} at {level:.0f} ft" if level else text)
    return ", ".join(layers) if layers else "not reported"

if __name__ == "__main__":
    # --- 1. Current conditions at one station -------------------------------
    now = current_conditions("AMW")
    temp_f = now.get("tmpf")
    print(f"\n{now['name']} ({now['station']}), {now['county']} County, {now['state']}")
    print(f"Observed at: {now['local_valid']} local  /  {now['utc_valid']}")
    print(f"Temperature: {temp_f} F / {f_to_c(temp_f):.1f} C   "
          f"(feels like {now.get('feel')} F)")
    print(f"Dew point:   {now.get('dwpf')} F")
    print(f"Humidity:    {now.get('relh'):.0f}%")
    print(f"Wind:        {knots_to_mph(now.get('sknt')):.0f} mph from the "
          f"{to_compass(now.get('drct'))}")
    print(f"Visibility:  {now.get('vsby')} miles")
    print(f"Sky:         {describe_sky(now)}")
    print(f"Pressure:    {now.get('mslp')} mb")

    # The raw METAR the station actually transmitted -- the real source format.
    print(f"\nRaw METAR: {now.get('raw')}")

    # --- 2. Use the whole network, not just one station ---------------------
    # currents.json already returned every Iowa station, so this costs no
    # extra request -- a good habit to point out to students.
    rows = [r for r in all_current() if r.get("tmpf") is not None]
    warmest = max(rows, key=lambda r: r["tmpf"])
    coldest = min(rows, key=lambda r: r["tmpf"])
    print(f"\nAcross {len(rows)} reporting Iowa stations right now:")
    print(f"  Warmest: {warmest['name']} at {warmest['tmpf']} F")
    print(f"  Coldest: {coldest['name']} at {coldest['tmpf']} F")
    print(f"  Spread:  {warmest['tmpf'] - coldest['tmpf']:.1f} F")

    # --- 3. A full day of observations at one station -----------------------
    yesterday = str(date.today() - timedelta(days=1))
    history = day_history("AMW", yesterday)
    temps = [(r["local_valid"], r["tmpf"]) for r in history
             if r.get("tmpf") is not None]
    print(f"\nAmes temperature trace for {yesterday} "
          f"({len(temps)} observations):")
    # Scale the bars to the day's own range, otherwise every bar starts at 0 F
    # and they all look identical.
    lo = min(v for _, v in temps)
    hi = max(v for _, v in temps)
    span = max(hi - lo, 1)  # guard against a flat day (divide by zero)
    for stamp, value in temps[::8]:  # every 8th reading, to keep it short
        bar = "#" * int((value - lo) / span * 40)
        print(f"  {stamp[11:16]}  {value:5.1f} F  {bar}")
    print(f"  (bars scaled to {lo:.0f}-{hi:.0f} F)")
