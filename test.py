from aifc import Aifc_read
from mailcap import findmatch
import requests
import json
from funkce import api_request


aircrafts = {
    "ISS": "25544",
    "HST": "20580"
    }

while True:
    user_retard = True
    print("Zadej NORAD ID z následujících:")
    print("")
    for letadla in aircrafts:
        print(letadla + ": " + aircrafts[letadla])
    print("")
    print("Pro odchod napiš q!")
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
        print("Jsi kokot!")
        continue

    response = api_request(vst)
    response = response.json()
    print("")
    for informace in response["info"]:
        print(informace + ": " + str(response["info"][informace]))
    print("")
    print("chceš se vrátit?")
    if input() == "ano":
        continue
    else:
        exit()

## konec true loopu 25544 20580


#{
# "info": {
#  "satid": 25544,
#  "satname": "SPACE STATION",
#  "transactionscount": 25
# },
# "tle": "1 25544U 98067A   22290.50488293  .00013999  00000-0  25167-3 0  9999\r\n2 25544  51.6427  90.5895 0003447 313.4987 150.1352 15.50128511364151"
#}