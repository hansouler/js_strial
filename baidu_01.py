from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)


print(resp.read().decode("utf-8"))
with open("Mybaidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")

