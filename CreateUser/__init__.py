import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('name')
    job = req.params.get('job')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if not job:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            job = req_body.get('job')

    if name and job:
        url = 'https://reqres.in/api/users'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = dict(name=name, job=job)
        response = requests.post(url=url, json=payload, headers=headers)

        return func.HttpResponse(
            response.text,
            status_code=response.status_code,
            mimetype = 'application/json', 
            charset = 'utf-8'
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and job in the query string or in the request body for a personalized response.",
             status_code=200
        )
