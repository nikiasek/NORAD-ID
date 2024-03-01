import requests


aircrafts = {
    "ISS": "25544",
    "HST": "20580"
    }

while True:
    user_retard = True
    print("Type NORAD-ID from these:")
    print("")
    for letadla in aircrafts:
        print(letadla + ": " + aircrafts[letadla])
    print("")
    print("For quit type: q!")
    print("")

    vst = input()
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

    response = requests.get("https://api.n2yo.com/rest/v1/satellite/tle/" + vst + "?apiKey=" + "NKGSFK-R68X7Z-6FLUFA-4XW3")
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