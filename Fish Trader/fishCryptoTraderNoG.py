import requests
import json
import random
import numpy as np
import time

#fetch crypto information
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?sort=cmc_rank'
api = input('Enter API Key: ')
headers = {'X-CMC_PRO_API_KEY' : api}
response = requests.get(url, headers=headers)
response_dict = json.loads(response.text)

#pick two random cryptos
x = random.sample(range(0, 50), 2)

choice_1 = response_dict["data"][x[0]]["symbol"]
choice_2 = response_dict["data"][x[1]]["symbol"]

#set up tank information
tankLength = 1250
tankWidth = tankLength / 2
tankHeight = tankLength / 2

fishCurrPosX = tankLength / 2
fishCurrPosY = tankWidth / 2
fishCurrPosZ = tankHeight / 2

fishLength = 50
fishWidth = 25

end = 0.0

counterLeft = 0
counterRight = 0

running = True

#Simulation Starts
print("Choices: ", choice_1, choice_2)

timeSpan = input("Duration: ")
timeSpan = float(timeSpan)

input("Press any key to start fish")

#Start the fish
start = time.time()
while end - start <= timeSpan:

    if end - start < timeSpan:
        if(fishCurrPosX < tankLength / 2):
            counterLeft += 1
        else:
            counterRight += 1

    #randomize direction
    dir = random.randint(0, 5) + 1
    if dir == 1:
        fishCurrPosZ += 7
    if dir == 2:
        fishCurrPosX -= 7
    if dir == 3:
        fishCurrPosZ -= 7
    if dir == 4:
        fishCurrPosX += 7
    if dir == 5:
        fishCurrPosY += 7
    if dir == 6:
        fishCurrPosY -= 7

    #check borders
    if fishCurrPosX <= 0:
        fishCurrPosX = 0
    if fishCurrPosX >= tankLength:
        fishCurrPosX = tankLength
    if fishCurrPosY <= 0:
        fishCurrPosY = 0
    if fishCurrPosY >= tankWidth:
        fishCurrPosY = tankWidth
    if fishCurrPosZ <= 0:
        fishCurrPosZ = 0
    if fishCurrPosZ >= tankHeight:
        fishCurrPosZ = tankHeight

    #print fishes location
    print(fishCurrPosX, fishCurrPosY, fishCurrPosZ)

    end = time.time()


if(counterLeft > counterRight):
    print("Winner: ", choice_1)
else:
    print("Winner: ", choice_2)
