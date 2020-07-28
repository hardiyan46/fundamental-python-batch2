import requests

url = 'https://detik.com'
try:
    response =  requests.get(url)
    print(f'Berhasil {response}')
    print(f'ISI {response.text}')
except Exception as e:
    print('Ada Error Bro', e)
print('program Berakhir')