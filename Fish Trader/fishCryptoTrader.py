import requests
import json
import random
import numpy as np
import time
import pygame

#fetch crypto information
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?sort=cmc_rank'
api = input('Enter API Key: ')
headers = {'X-CMC_PRO_API_KEY' : api}
response = requests.get(url, headers=headers)
response_dict = json.loads(response.text)

#pick two random cryptos
def getCrypto():
    x = random.sample(range(0, 50), 2)
    choice_1 = response_dict["data"][x[0]]["symbol"]
    choice_2 = response_dict["data"][x[1]]["symbol"]

    return (choice_1, choice_2)

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

crypto = getCrypto()
#Simulation Starts
print("Choices: ", crypto[0], crypto[1])

timeSpan = input("Duration: ")
timeSpan = float(timeSpan)

input("Press any key to start fish")

#Creating Environment
pygame.init()
screen = pygame.display.set_mode([tankLength, tankWidth])
bg = pygame.image.load("aqua_bg.jpeg")
goldfish = pygame.image.load('goldfish.png')
goldfish = pygame.transform.scale(goldfish, (75, 75))
pygame.display.set_caption('CRYPTO FISH TRADER')
font = pygame.font.Font('freesansbold.ttf', 32)

#Start the fish
start = time.time()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    cryptoColor_1 = (0, 0, 0)
    cryptoColor_2 = (0, 0, 0)

    if end - start >= timeSpan:
        if counterLeft > counterRight:
            cryptoColor_1 = (0, 255, 0)
        else:
            cryptoColor_2 = (0, 255, 0)
        

    #draw and update fish
    screen.blit(bg, (0, -250))
    screen.blit(goldfish, (fishCurrPosX - (75/2), fishCurrPosZ - (75/2)))

    #set up text
    cryptoDisp_1 = font.render(crypto[0] + ': ' + str(counterLeft), True, cryptoColor_1)
    cryptoDisp_2 = font.render(crypto[1] + ': ' + str(counterRight), True, cryptoColor_2)
    screen.blit(cryptoDisp_1, ((tankLength / 2) / 4, 10))
    screen.blit(cryptoDisp_2, ((tankLength / 2) + (tankLength / 2) / 2, 10))

    if end - start >= timeSpan:
        pygame.display.flip()
        pygame.time.delay(5000)
        counterLeft = 0
        counterRight = 0
        start = time.time()
        crypto = getCrypto()

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
        goldfish = pygame.transform.flip(goldfish, True, False)
    if dir == 3:
        fishCurrPosZ -= 7
    if dir == 4:
        fishCurrPosX += 7
        goldfish = pygame.transform.flip(goldfish, True, False)
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
    pygame.display.flip()

    end = time.time()


if(counterLeft > counterRight):
    print("Winner: ", crypto[0])
else:
    print("Winner: ", crypto[1])

pygame.quit()

