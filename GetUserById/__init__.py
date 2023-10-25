import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    if not id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            id = req_body.get('id')

    if id:
        url = 'https://reqres.in/api/users/' + id
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
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass an id in the query string or in the request body for a personalized response.",
             status_code=200
        )
