import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"node_address":"http://127.0.0.1:8000"}'

response = requests.post('http://127.0.0.1:8003/register_with', headers=headers, data=data)
