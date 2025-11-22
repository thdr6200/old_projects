#coding:utf-8

import pygame, time

pygame.init()

resolution = (800, 800)

screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption('Chess Board')
screen_icon = pygame.image.load('images\\chess_icon.png')
pygame.display.set_icon(screen_icon)
clock = pygame.time.Clock()

chess_board = pygame.image.load('images\\chess_board.png').convert()
chess_board = pygame.transform.smoothscale(chess_board, (600, 600))

"------------------------------------------------------------------------------"

black_pawn = pygame.image.load('images\\bp.png').convert_alpha()
black_pawn = pygame.transform.smoothscale(black_pawn, (75, 75))


white_pawn = pygame.image.load('images\\wp.png').convert_alpha()
white_pawn = pygame.transform.smoothscale(white_pawn, (75, 75))


"------------------------------------------------------------------------------"

black_rook = pygame.image.load('images\\br.png').convert_alpha()
black_rook = pygame.transform.smoothscale(black_rook, (75, 75))

white_rook = pygame.image.load('images\\wr.png').convert_alpha()
white_rook = pygame.transform.smoothscale(white_rook, (75, 75))

"------------------------------------------------------------------------------"

black_knight = pygame.image.load('images\\bn.png').convert_alpha()
black_knight = pygame.transform.smoothscale(black_knight, (75, 75))

white_knight = pygame.image.load('images\\wn.png').convert_alpha()
white_knight = pygame.transform.smoothscale(white_knight, (75, 75))

"------------------------------------------------------------------------------"

black_bishop = pygame.image.load('images\\bb.png').convert_alpha()
black_bishop = pygame.transform.smoothscale(black_bishop, (75, 75))

white_bishop = pygame.image.load('images\\wb.png').convert_alpha()
white_bishop = pygame.transform.smoothscale(white_bishop, (75, 75))

"------------------------------------------------------------------------------"

black_queen = pygame.image.load('images\\bq.png').convert_alpha()
black_queen = pygame.transform.smoothscale(black_queen, (75, 75))

white_queen = pygame.image.load('images\\wq.png').convert_alpha()
white_queen = pygame.transform.smoothscale(white_queen, (75, 75))

"------------------------------------------------------------------------------"

black_king = pygame.image.load('images\\bk.png').convert_alpha()
black_king = pygame.transform.smoothscale(black_king, (75, 75))

white_king = pygame.image.load('images\\wk.png').convert_alpha()
white_king = pygame.transform.smoothscale(white_king, (75, 75))

"------------------------------------------------------------------------------"

move_points = pygame.image.load('images\\moves.png').convert_alpha()
move_points = pygame.transform.smoothscale(move_points, (25, 25))

"------------------------------------------------------------------------------"

def pawns_positioning(black_pawn, white_pawn):
    pawn_x = 100
    black_pawn_rects = []
    white_pawn_rects = []
    for i in range(1, 9):

        black_pawn_rect = black_pawn.get_rect(bottomleft=(pawn_x, 250))
        screen.blit(black_pawn, black_pawn_rect)
        black_pawn_rect = pygame.draw.rect(screen, 'black', black_pawn_rect, 1)
        black_pawn_rects.append(black_pawn_rect)

        white_pawn_rect = white_pawn.get_rect(bottomleft=(pawn_x, 625))
        screen.blit(white_pawn, white_pawn_rect)
        white_pawn_rect = pygame.draw.rect(screen, 'white', white_pawn_rect, 1)
        white_pawn_rects.append(white_pawn_rect)

        pawn_x += 75

    return black_pawn_rects, white_pawn_rects

"------------------------------------------------------------------------------"

def rooks_positioning(black_rook, white_rook):
    rook_x = 100
    black_rook_rects = []
    white_rook_rects = []
    for i in range(1, 3):
        black_rook_rect = black_rook.get_rect(bottomleft=(rook_x, 175))
        screen.blit(black_rook, black_rook_rect)
        black_rook_rect = pygame.draw.rect(screen, 'black', black_rook_rect, 1)
        black_rook_rects.append(black_rook_rect)

        white_rook_rect = white_rook.get_rect(bottomleft=(rook_x, 700))
        screen.blit(white_rook, white_rook_rect)
        white_rook_rect = pygame.draw.rect(screen, 'white', white_rook_rect, 1)
        white_rook_rects.append(white_rook_rect)

        rook_x += 525
    return black_rook_rects, white_rook_rects

"------------------------------------------------------------------------------"

def knights_positioning(black_knight, white_knight):
    knight_x = 175
    black_knight_rects = []
    white_knight_rects = []
    for i in range(1, 3):
        black_knight_rect = black_knight.get_rect(bottomleft=(knight_x, 175))
        screen.blit(black_knight, black_knight_rect)
        black_knight_rect = pygame.draw.rect(screen, 'black', black_knight_rect, 1)
        black_knight_rects.append(black_knight_rect)

        white_knight_rect = white_knight.get_rect(bottomleft=(knight_x, 700))
        screen.blit(white_knight, white_knight_rect)
        white_knight_rect = pygame.draw.rect(screen, 'white', white_knight_rect, 1)
        white_knight_rects.append(white_knight_rect)

        knight_x += 375
    
    return white_knight_rects, black_knight_rects

"------------------------------------------------------------------------------"

def bishops_positioning(black_bishop, white_bishop):
    bishop_x = 250
    black_bishop_rects = []
    white_bishop_rects = []
    for i in range(1, 3):
        black_bishop_rect = black_bishop.get_rect(bottomleft=(bishop_x, 175))
        screen.blit(black_bishop, black_bishop_rect)
        black_bishop_rect = pygame.draw.rect(screen, 'black', black_bishop_rect, 1)
        black_bishop_rects.append(black_bishop_rect)

        white_bishop_rect = white_bishop.get_rect(bottomleft=(bishop_x, 700))
        screen.blit(white_bishop, white_bishop_rect)
        white_bishop_rect = pygame.draw.rect(screen, 'white', white_bishop_rect, 1)
        white_bishop_rects.append(white_bishop_rect)

        bishop_x += 225
    return black_bishop_rects, white_bishop_rects

"------------------------------------------------------------------------------"

def queens_positioning(black_queen, white_queen):
    queen_x = 325
    black_queen_rects = []
    white_queen_rects = []
    for i in range(1, 2):
        black_queen_rect = black_queen.get_rect(bottomleft=(queen_x, 175))
        screen.blit(black_queen, black_queen_rect)
        black_queen_rect = pygame.draw.rect(screen, 'black', black_queen_rect, 1)
        black_queen_rects.append(black_queen_rect)

        white_queen_rect = white_queen.get_rect(bottomleft=(queen_x, 700))
        screen.blit(white_queen, white_queen_rect)
        white_queen_rect = pygame.draw.rect(screen, 'white', white_queen_rect, 1)
        white_queen_rects.append(white_queen_rect)

        queen_x += 125
    return black_queen_rects, white_queen_rects
"------------------------------------------------------------------------------"

def kings_positioning(black_king, white_king):
    king_x = 400
    black_king_rects = []
    white_king_rects = []
    for i in range(1, 2):
        black_king_rect = black_king.get_rect(bottomleft=(king_x, 175))
        screen.blit(black_king, black_king_rect)
        black_king_rect = pygame.draw.rect(screen, 'black', black_king_rect, 1)
        black_king_rects.append(black_king_rect)

        white_king_rect = white_king.get_rect(bottomleft=(king_x, 700))
        screen.blit(white_king, white_king_rect)
        white_king_rect = pygame.draw.rect(screen, 'white', white_king_rect, 1)
        white_king_rects.append(white_king_rect)

        king_x += 25
    return black_king_rects, white_king_rects

def see_move_points():
    for black_pawn_rect in black_pawn_rects:
        if black_pawn_rect.collidepoint(cursor.x, cursor.y):
            p1 = screen.blit(move_points, (black_pawn_rect.x + 25, black_pawn_rect.y + 100))
            p2 = screen.blit(move_points, (black_pawn_rect.x + 25, black_pawn_rect.y + 175))

    for white_pawn_rect in white_pawn_rects:
        if white_pawn_rect.collidepoint(cursor.x, cursor.y):
            p1 = screen.blit(move_points, (white_pawn_rect.x + 25, white_pawn_rect.y - 50))
            p2 = screen.blit(move_points, (white_pawn_rect.x + 25, white_pawn_rect.y - 125))

    for black_rook_rect in black_rook_rects:
        if black_rook_rect.collidepoint(cursor.x, cursor.y):
            p1 = screen.blit(move_points, (black_rook_rect.x + 25, black_rook_rect.y - 50))
            p2 = screen.blit(move_points, (black_rook_rect.x + 25, black_rook_rect.y - 125))


    return p1, p2

points = []

running = True
while running:

    cursor_pos = pygame.mouse.get_pos()
    cursor = pygame.draw.line(screen, 'black', cursor_pos, cursor_pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                try:
                    p1, p2 = see_move_points()
                    points.append(p1)
                    points.append(p2)
                except UnboundLocalError:
                    pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill('red')
    screen.blit(chess_board, (100, 100))
    black_pawn_rects, white_pawn_rects = pawns_positioning(black_pawn, white_pawn)
    black_rook_rects, white_rook_rects = rooks_positioning(black_rook, white_rook)
    black_knight_rects, white_knight_rects = knights_positioning(black_knight, white_knight)
    black_bishop_rects, white_bishop_rects = bishops_positioning(black_bishop, white_bishop)
    black_queen_rects, white_queen_rects = queens_positioning(black_queen, white_queen)
    black_king_rects, white_king_rects = kings_positioning(black_king, white_king)

    for p in points:
        if len(points) <= 2:
            screen.blit(move_points, p)
        elif len(points) > 2:
            points = []
            break

    pygame.display.update()
    clock.tick(60)

pygame.quit()