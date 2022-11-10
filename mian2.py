import requests

web ='https://jsonplaceholder.typicode.com/posts/7'
print(requests.get(web).json())

response = requests.patch(web,data={
    "id": 7,
    'userId':13,
    'title':'CRIST',

})

print(response.json())