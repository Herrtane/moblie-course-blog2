import requests

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
'username':'admin',
'password':'conan0525',
})

res.raise_for_status()
token = res.json()['token']
print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create
data = {
'title' : 'by code',
'text' : 'by code',
'created_date' : '2023-06-08T17:34:00+09:00',
'published_date' : '2023-06-08T17:34:00+09:00'
}
file = {'image' : open('/Users/lch/Desktop/3156168.png', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())
