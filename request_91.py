import requests

url = "https://www.so.com/s?ie=utf-8&src=hao_360so_a1004_b_cube&shb=1&hsid=3b479c5ab4b9a140&q=%E5%91%A8%E6%9D%B0%E4%BC%A6"

dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"
}
resp = requests.get(url, headers=dic)
# 处理一个小小的反扒
print(resp)
print(resp.text)
# 关掉resp
resp.close()