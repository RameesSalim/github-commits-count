import requests
import json

user = "rameessalim"

i=0
response = requests.get("https://api.github.com/users/"+str(user)+"/repos")
repo = json.loads(response.content)
print(response.status_code)
for repos in repo:
	print(repos['name'])
	i+=1
print("number of repos = "+str(i))
	




		
