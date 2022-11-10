import requests

headers={
    "User-Agent": "ETO OH"
}
response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a':'b'},
                         json ={'username':"secret"}
                         )


#if response.status_code == 200:
    #print("ok")

response.raise_for_status()

print(response.text)