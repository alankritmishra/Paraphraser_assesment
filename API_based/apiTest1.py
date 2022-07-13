import requests

url = 'https://app.plaraphy.com/api/paraphrase'

payload = 'text= This is a test and I am testing the API'
headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'authorization': 'Bearer 1504|TqwdDX8q1AtziWLZm9AVsH9aGqCYoeppQCNM1Dbm',
    'cache-control': 'no-cache',
}

response = requests.request('POST', url, data=payload, headers=headers)

print(response.text)
