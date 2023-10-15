import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    url = 'https://reqres.in/api/users?page=1'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.get(url=url, headers=headers)

    return func.HttpResponse(
        response.text,
        status_code=response.status_code,
        mimetype = 'application/json', 
        charset = 'utf-8'
    )
