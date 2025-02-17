import os
import sys

import pygame
import requests

server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
ll = input("Введите координаты (широта,долгота): ")
x = float(input("Введите маштаб (значение увелечения): "))
if x > 90:
    x = 90
elif x < 0:
    x = 0
spn = f'{x},{x}'
ll_spn = f"ll={ll}&spn={spn}"
map_request = f"{server_address}{ll_spn}&apikey={api_key}"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)



pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_KP9]:
            if x >= 10 and x < 90:
                x += 10
            elif x >= 0 and x < 0.1:
                x += 0.01
                x = round(x, 3)
            elif x >= 0.1 and x <1:
                x += 0.1
                x = round(x, 2)
            elif x >= 1 and x <10:
                x += 1
            elif x >= 90:
                break
            print(x)
        if pygame.key.get_pressed()[pygame.K_KP3]:
            if x > 10:
                x -= 10
            elif x <= 10 and x > 1:
                x -= 1
            elif x <= 1 and x > 0:
                x -= 0.1
                x = round(x, 2)
            elif x <= 0:
                break
            print(x)
    spn = f'{x},{x}'
    ll_spn = f'll={ll}&spn={spn}'
    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    
pygame.quit()
