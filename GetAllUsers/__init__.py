import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    page = req.params.get('page') if req.params.get('page') else ''
    per_page = req.params.get('per_page') if req.params.get('per_page') else ''

    url = 'https://reqres.in/api/users?page=' + page + '&per_page=' + per_page
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
