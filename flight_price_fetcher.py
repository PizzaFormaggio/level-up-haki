import os
import requests
import json


def get_access_token():
    client_id = os.getenv('AMADEUS_CLIENT_ID')
    client_secret = os.getenv('AMADEUS_CLIENT_SECRET')
    if not client_id or not client_secret:
        raise EnvironmentError('Please set AMADEUS_CLIENT_ID and AMADEUS_CLIENT_SECRET environment variables.')
    token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    response = requests.post(token_url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

def search_flights(origin, destination, departure_date, return_date=None, adults=1):
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        'originLocationCode': origin,
        'destinationLocationCode': destination,
        'departureDate': departure_date,
        'adults': adults
    }
    if return_date:
        params['returnDate'] = return_date

    url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch flight price data from Amadeus API')
    parser.add_argument('origin', help='Origin IATA code')
    parser.add_argument('destination', help='Destination IATA code')
    parser.add_argument('departure_date', help='Departure date YYYY-MM-DD')
    parser.add_argument('--return_date', help='Return date YYYY-MM-DD')
    parser.add_argument('--adults', type=int, default=1, help='Number of adult passengers')
    args = parser.parse_args()

    data = search_flights(
        args.origin,
        args.destination,
        args.departure_date,
        return_date=args.return_date,
        adults=args.adults
    )
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
