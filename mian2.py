import requests

web ='https://jsonplaceholder.typicode.com/posts/1'
print(requests.get(web).json())

response = requests.put(web,data={
    "id": 7,
    'userId':13,
    'title':'CRIST',
    'body':'sewey',

})

print(response.json())