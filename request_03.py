import requests


url = "https://movie.douban.com/j/chart/top_list"
User_Agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"
}
# 重新封装参数（最底下那个）
param = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
resp = requests.get(url=url, params=param, headers=User_Agent)
print(resp.json())
# 关掉resp
resp.close()