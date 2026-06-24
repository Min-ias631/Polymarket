import requests
import json
import datetime
from order_book import order_book
from event import Event

from GLOBAL_VARIABLES import GAMMA, CLOB

SERIES_IDS = {'lol': None, 'val': None}

def get_gamma_data(path, **params):
    response = requests.get(f'{GAMMA}{path}', params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def get_series_id():
    global SERIES_IDS
    if None in SERIES_IDS.values():
        response = get_gamma_data('/sports')
        for sport in response:
            if sport['sport'] in SERIES_IDS:
                SERIES_IDS[sport['sport']] = sport['series']

def get_events_by_tag(game, page = 100, starting_date = None):
    page = min(100, page)
    get_series_id()  # Ensure series IDs are up to date
    output = []
    offset = 0
    now_iso = datetime.datetime.now(datetime.timezone.utc).replace(
        microsecond=0).isoformat().replace("+00:00", "Z")
    if starting_date is not None:
        starting_date = datetime.datetime.fromisoformat(starting_date.replace("Z", "+00:00")).replace(
            microsecond=0).isoformat() + 'Z'
    while True:
        if starting_date is None:
            response = get_gamma_data(
                "/events",
                series_id=SERIES_IDS[game],
                limit=page,
                offset=offset,
                end_date_min = now_iso
            )
        else:
            response = get_gamma_data(
                "/events",
                series_id=SERIES_IDS[game],
                limit=page,
                offset=offset,
                end_date_min=starting_date,
                end_date_max=now_iso
            )
        output += response
        if len(response) < page:
            break
        offset += page
    return output

if __name__ == "__main__":
    events = get_events_by_tag('lol')
    event = Event(events[0])
    event.markets[0].print_all_info()