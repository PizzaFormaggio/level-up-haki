# Flight Price Fetcher

This repository contains a simple Python script for retrieving flight price data from the Amadeus API. The script demonstrates how to authenticate using client credentials and query flight offers.

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- Amadeus API credentials (`AMADEUS_CLIENT_ID` and `AMADEUS_CLIENT_SECRET` environment variables)

## Usage

Run the script with the origin and destination airport codes and a departure date:

```bash
python flight_price_fetcher.py JFK LHR 2024-12-25
```

Optional arguments:

- `--return_date YYYY-MM-DD` – specify a return date
- `--adults N` – number of adults (default is 1)

The script prints the raw JSON response from the API, which includes pricing information for available flights.
