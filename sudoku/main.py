#!/usr/bin/env python3
import pygame
import requests
import os

RES = (540,800)
WHITE = (255,255,255)
BLACK = (0,0,0)
API = "https://youdosudoku.com/api"
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.Font(r"%s\font.ttf" % os.getcwd(), 20)

def getting_sudoku(API):
    """
    Gets sudoku problem with get request to an api

    :param:
        None
    :return:
        Response with sudoku problem and chosen difficulty
    """

    body = {
    "difficulty": "easy",
    "solution": True,
    "array": False
    }

    headers =  {"Content-Type":"application/json"}

    return requests.post(API, json=body, headers=headers)

post_reponse = getting_sudoku(API)
print(post_reponse.json())
if post_reponse.ok:
    print('ok')
else:
    print('something went wrong')
    quit(1)

def board_cases() -> list:
    """
    Drawing board cases

    :param: 
        None
    :return:
        Nothing
    """
    all_rect = []
    for a in range(0, 9):
            for b in range(0,9):
                rectangle = pygame.draw.rect(screen, WHITE, (60*b, 60*a, 60, 60), 1)
                all_rect.append(rectangle)
    return all_rect

def backtracking():
    """
    Solving sudoku with brute force

    :param:
        None
    :return:
        Nothing
    """
    pass

def placing_numbers(post_reponse, all_rect):
    response = post_reponse.json()
    font = pygame.font.Font(r"%s\font.ttf" % os.getcwd(), 25)
    response['puzzle'] = '037000900509036024082000030103028709000000005006040080065093071090060408704180093'
    #values = [[response['puzzle'][j] for j in range(0, 9)] for i in range(len(response['puzzle']) // 9)]
    values = []
    s = 0
    e = 9
    for i in range(0, 9):
        values.append([])
        for j in range(s, e):
            values[i].append(response['puzzle'][j])
        if not e > len(response['puzzle']):
            e += 9
            s += 9
    for a in range(0, len(all_rect)):
        if response['puzzle'][a] == '0':
            pass
        else:
            img3 = font.render(str(response['puzzle'][a]), True, WHITE)
            screen.blit(img3, (all_rect[a][0] + 25, all_rect[a][1] + 20))



running = True
real_time = 0.00
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False

    screen.fill(BLACK)
    
    all_rect = board_cases()
    real_time += 0.01
    placing_numbers(post_reponse, all_rect)
    img = font.render('Timer:', True, WHITE)
    screen.blit(img, (0, 550))

    img2 = font.render(str(round(real_time, 2)), True, WHITE)
    screen.blit(img2, (65, 552))
    clock.tick(100)
    pygame.display.update()
    
pygame.quit()