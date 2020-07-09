import requests
a=requests.get("https://api.bilibili.com/x/space/acc/info?mid=15160&jsonp=jsonp")
print(a.status_code)