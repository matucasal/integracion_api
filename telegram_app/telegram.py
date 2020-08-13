import os, requests, json


BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

url = 'https://api.telegram.org/bot' + BOT_TOKEN

#getMe
response = requests.request('GET', url + '/getMe')
data = json.loads(response.text)


if data ['ok']:
        print(data['result'])

print('*' * 50)

#getUpdates
response = requests.request('GET', url + '/getUpdate')
data = json.loads(response.text)


if data['ok']:
        for m in data['result']:
                print(m)
                print('*' * 50)
else:
    print('fallo')
