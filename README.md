<h1  align="center">NORAD-ID</h1>

### Introduction
When I was introduced to the world of API's, this was the first program where i learned to work with it.

Also this is just for my own memory of it.

##

### How does it work?

Code starts here with `While True:` loop for endless running.

`aircrafts` is list of norad-id's. You can extend it if you want.

`user_retard` variable is used for determining if user typed right norad-id format.

`vst` is variable for storing the norad-id user wants to use.

```py
aircrafts = {
	"ISS": "25544",
	"HST": "20580"
	}
	
while True:
	user_retard = True
	print("Type NORAD-ID from these:")
	print("")
	for letadla  in  aircrafts:
		print(letadla + ": " + aircrafts[letadla])	
	print("")
	print("For quit type: q!")
	print("")

	vst = input()
```

##

First if determines if in `vst` variable is stored "q!". If it's true, program will close ifself.

For loop is used for checking if in `vst` value is stored anything from the `aircrafts` list of NORAD-ID's and it will change `user_retard` variable to "False".

Last if check's if `user_retard` value is still "True". If it's true, it will pring "Bad input" and continues to the end of while loop. 	

```py
#exit sequence
if vst == "q!":
	exit(1)

for letadla in aircrafts:
	if vst == aircrafts[letadla]:
	user_retard = False
	break

if user_retard:
	print("Bad input")
	continue
```

##

When is determined that input is valuable and everything is checked, we create new variable called `response` where we store the API's link and after that it will convert itself into json.

```py
import  requests

...
...

response = requests.get("https://api.n2yo.com/rest/v1/satellite/tle/"  +  vst + "?apiKey=" + "NKGSFK-R68X7Z-6FLUFA-4XW3")
response = response.json()
print("")
for informace in response["info"]:
	print(informace + ": " + str(response["info"][informace]))
print("")
print("Again?")
if input() == "yes":
	continue
else:
	exit()
```

###

For loop is used to find informations about the satellite and print them out. json we get looks like this. for loop finds info list and print it out

```json
{'info': 
	{'satid': 25544, 
	'satname': 'SPACE STATION', 
	'transactionscount': 1
	}, 
	'tle': '1 25544U 98067A   24061.30012289  .00013763  00000-0  25294-3 0  9993\r\n2 25544  51.6417 130.0584 0005875 311.6600  83.8246 15.49506288441827'
}
```

##

With all these steps, your program should look like this:
```py
import requests


aircrafts = {
	"ISS": "25544",
	"HST": "20580"
	}
	
while True:
	user_retard = True
	print("Type NORAD-ID from these:")
	print("")
	for letadla  in  aircrafts:
		print(letadla + ": " + aircrafts[letadla])	
	print("")
	print("For quit type: q!")
	print("")

	vst = input()

	if vst == "q!":
		exit(1)

	for letadla in aircrafts:
		if vst == aircrafts[letadla]:
		user_retard = False
		break

	if user_retard:
		print("Bad input")
		continue

	response = requests.get("https://api.n2yo.com/rest/v1/satellite/tle/"  +  	vst + "?apiKey=" + "NKGSFK-R68X7Z-6FLUFA-4XW3")
	response = response.json()
	print("")
	for informace in response["info"]:
		print(informace + ": " + str(response["info"][informace]))
	print("")
	print("Again?")
	if input() == "yes":
		continue
	else:
		exit()
```

##

<p align="center">Only python was used</p>
<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
</div>


