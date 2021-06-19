import requests
response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=411060&date=19-06-2021")
print(response)
print(response.json())