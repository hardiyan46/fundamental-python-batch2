import requests

url = 'https://detik.com'
try:
    response =  requests.get(url)
    print(f'Berhasil {response}')
except Exception as e:
    print('Ada Error Bro', e)
print('program Berakhir')