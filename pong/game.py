import pygame
import time
from variables import *

pygame.mouse.set_visible(settings["mouse_visibility"])

win_text = pygame.font.Font('font\\pixeltype.ttf', 100)

player_rect = pygame.Rect(26, (info.current_h - 150) // 2, 10, 150)

player_score_text = pygame.font.Font(f'{current_directory}\\font\\pixeltype.ttf', 50)
player_score_text_surface = player_score_text.render(f'{str(settings['player_score'])}', False, 'blue')


player2_rect = pygame.Rect(info.current_w - 35, (info.current_h - 150) // 2, 10, 150)

player2_score_text = pygame.font.Font(f'{current_directory}\\font\\pixeltype.ttf', 50)
player2_score_text_surface = player2_score_text.render(f'{str(settings['player2_score'])}', False, 'red')


top_border_rect = pygame.Rect(0, 0, info.current_w, 15)
bottom_border_rect = pygame.Rect(0, info.current_h - 15, info.current_w, 15)
left_border_rect = pygame.Rect(0, 0, 15, info.current_h)
right_border_rect = pygame.Rect(info.current_w - 15, 0, 15, info.current_h)


ball_x = (info.current_w - 20) // 2
ball_y = (info.current_h - 20) // 2
ball_rect = pygame.Rect(ball_x, ball_y, settings['ball_radius'], settings['ball_radius'])


score_text = pygame.font.Font(f'{current_directory}\\font\\pixeltype.ttf', 50)
score_text_surface = score_text.render('SCORE:', False, 'green')

score_divider_text = pygame.font.Font(f'{current_directory}\\font\\pixeltype.ttf', 50)
score_divider_text_surface = score_text.render('|', False, 'white')

def update(player_score_text_surface, player2_score_text_surface, ball_x_speed):
    screen.fill('black')

    screen.blit(score_text_surface, ((info.current_w - 50) // 2, 30))

    screen.blit(player_score_text_surface, (info.current_w // 2, 65))
    player_score_text_surface = player_score_text.render(f'{str(settings["player_score"])}', False, 'blue')

    screen.blit(score_divider_text_surface, (info.current_w // 2 + 24, 64))

    screen.blit(player2_score_text_surface, (info.current_w // 2 + 50, 65))
    player2_score_text_surface = player2_score_text.render(f'{str(settings["player2_score"])}', False, 'red')

    pygame.draw.rect(screen, 'blue', player_rect)
    pygame.draw.rect(screen, 'red', player2_rect)

    pygame.draw.rect(screen, 'gray', top_border_rect)
    pygame.draw.rect(screen, 'gray', bottom_border_rect)
    pygame.draw.rect(screen, 'gray', left_border_rect)
    pygame.draw.rect(screen, 'gray', right_border_rect)

    ball_rect.center = ((info.current_w - 20) // 2, (info.current_h - 20) // 2)
    pygame.draw.circle(screen, 'white', ball_rect.center, 10)

    ball_x_speed *= -1

    time.sleep(.500)

def print_text_winner():
    win_text_surface_rect = win_text_surface.get_rect()
    win_text_surface_rect.center = ((info.current_w + 325) // 2, (info.current_h - 50) // 2)
    screen.blit(win_text_surface, (win_text_surface_rect.x - 150, win_text_surface_rect.y))
    time.sleep(5)
    settings["player_score"] = 0
    settings["player2_score"] = 0

while settings["running"]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings["running"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            elif event.key == pygame.K_UP:
                settings["player2_up"] = True
            elif event.key == pygame.K_DOWN:
                settings["player2_down"] = True

            elif event.key == pygame.K_w:
                settings["player_up"] = True
            elif event.key == pygame.K_s:
                settings["player_down"] = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                settings["player2_up"] = False
            elif event.key == pygame.K_DOWN:
                settings["player2_down"] = False

            elif event.key == pygame.K_w:
                settings["player_up"] = False
            elif event.key == pygame.K_s:
                settings["player_down"] = False

    if settings["player_up"] and player_rect.top > 15:
        player_rect.y -= settings["speed"]
    if settings["player_down"] and player_rect.bottom < info.current_h - 15:
        player_rect.y += settings["speed"]
    if settings["player2_up"] and player2_rect.top > 15:
        player2_rect.y -= settings["speed"]
    if settings["player2_down"] and player2_rect.bottom < info.current_h - 15:
        player2_rect.y += settings["speed"]

    ball_rect.x += settings["ball_x_speed"]
    ball_rect.y += settings["ball_y_speed"]

    if ball_rect.colliderect(player2_rect) or ball_rect.colliderect(player_rect):
        settings["ball_x_speed"] *= -1

    if ball_rect.colliderect(bottom_border_rect) or ball_rect.colliderect(top_border_rect):
        settings["ball_y_speed"] *= -1

    if ball_rect.colliderect(right_border_rect):
        settings["player_score"] += 1
        update(player_score_text_surface, player2_score_text_surface, settings["ball_x_speed"])
    if ball_rect.colliderect(left_border_rect):
        settings["player2_score"] += 1
        update(player_score_text_surface, player2_score_text_surface, settings["ball_x_speed"])



    screen.fill('black')   
    screen.blit(score_text_surface, ((info.current_w - 50) // 2, 30))

    screen.blit(player_score_text_surface, (info.current_w // 2, 65))
    player_score_text_surface = player_score_text.render(f'{str(settings["player_score"])}', False, 'blue')

    screen.blit(score_divider_text_surface, (info.current_w // 2 + 24, 64))

    screen.blit(player2_score_text_surface, (info.current_w // 2 + 50, 65))
    player2_score_text_surface = player2_score_text.render(f'{str(settings["player2_score"])}', False, 'red')

    pygame.draw.rect(screen, 'blue', player_rect)
    pygame.draw.rect(screen, 'red', player2_rect)

    pygame.draw.rect(screen, 'gray', top_border_rect)
    pygame.draw.rect(screen, 'gray', bottom_border_rect)

    pygame.draw.rect(screen, 'gray', left_border_rect)
    pygame.draw.rect(screen, 'gray', right_border_rect)

    pygame.draw.circle(screen, 'white', ball_rect.center, 10)
    if settings["player_score"] == settings["end_score"]:
        screen.fill('black')
        win_text_surface = win_text.render('BLUE PLAYER WON !', False, 'blue')
        time.sleep(5)
        print_text_winner()
    elif settings["player2_score"] == settings["end_score"]:
        screen.fill('black')
        win_text_surface = win_text.render('RED PLAYER WON !', False, 'red')
        print_text_winner()

    pygame.display.update()
    clock.tick(60)

pygame.quit()