import requests

headers={
    "User-Agent": "ETO OH"
}
response = requests.get("https://httpbin.org/get?a=b",headers=headers,params={'a':'b'})


#if response.status_code == 200:
    #print("ok")

response.raise_for_status()

print(response.text)