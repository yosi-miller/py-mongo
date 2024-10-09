import requests

from services.logger import log_error, log_info


def get_data_from_api(route_url):
    url = f'https://jsonplaceholder.typicode.com/{route_url}'
    try:
        response = requests.get(url)
        log_info(f'requests api to: {url}. \nstatus code: {response.status_code}')
        return response.json()
    except requests.exceptions.RequestException as e:
        log_error(e)
        print(f'Error: {e}')
        return e