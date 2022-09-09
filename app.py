import requests
import json

header = {'X-API-Key': 'GTW7MbCwHEa1z398lj3l71Rj1pw9wjjT7VC4RZ3m'}
end_point = 'https://opendata.resas-portal.go.jp'
get_code = '/api/v1/cities'
req = requests.get(end_point + get_code, headers=header)
data = json.loads(req.content)
city = {item['cityName']: item['cityCode'] for item in data['result']}
flag = {cflag['cityName']: cflag['bigCityFlag'] for cflag in data['result']}

print("ResponseCode", req.status_code)
#print(data)

while True:
    item = input('市区町村の CityCode と特別区・行政区フラグを知ることができます\n(0:一般の市区町村、1:政令指定都市の区、2:政令指定都市の市、3:東京都23区)\n※ 名古屋市のように区域が必要な場合は最後まで入力してください\n　ex)名古屋市→ 名古屋市北区\n市区町村を入力してください: ')
    print(item, "CityCode:"+ city[item], "CityFlag:"+ flag[item])
    if (res := input('他の市区町村を見ますか y/n ') != 'y'):
        break
