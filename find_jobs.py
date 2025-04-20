import requests
import random


def find_jobs():
    apis = [

            {
                'name': 'Remotive',
                'url': 'https://remotive.com/api/remote-jobs',
                'params': {'limit': 10}
            },

            {
                'name': 'Jobicy',
                'url': 'https://jobicy.com/api/v2/remote-jobs',
                'params': {'count': 10}
            },
            {
                'name': 'REMOTEful',
                'url': 'https://remoteful.dev/api/remote_jobs',
                'params': {'limit': 10}
            
            }
    ]


    api = random.choice(apis)
    response = requests.get(api['url'], params=api['params'])
    if response.status_code == 200:
        data = response.json()
        jobs = data.get('jobs', [])
        for job in jobs:
            print(f"Empresa: {job.get('company_name')}")
            print(f"Titulo: {job.get('titulo')}")
            print(f"Localizacao: {job.get('candidate_required_location')}")
            print(f"Link: {job.get('url')}")

    else:
        print(f"Erro ao acessar a API {api['name']}: {response.status_code}")




if __name__ == "__main__":
    find_jobs()
