import pygame
from grid import Grid
import ai

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic-tac-toe")

grid = Grid()

player = "X"

def intro():
  intro = True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    surface.fill((200, 200, 200))
    pygame.font.init()
    font = pygame.font.SysFont(None, 100)
    img = font.render('Tic-Tac-Toe', False, (200, 0, 200))
    surface.blit(img, (125, 225))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 350 > mouse[0] > 250 and 400 > mouse[1] > 350:
      pygame.draw.rect(surface, (0, 255, 0), (250, 350, 100, 50))
      if click[0] == 1:
        game_loop()
    pygame.draw.rect(surface, (0, 200, 0), (250, 350, 100, 50))
    pygame.font.init()
    myfont = pygame.font.SysFont(None, 40)
    textsurface = myfont.render('Play', False, (200, 200, 200))
    surface.blit(textsurface, (270, 365))
    pygame.display.update()

def game_loop():
  running = True
  while running:
    surface.fill((0,0,0))

    grid.draw(surface)
    pygame.display.update()

    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0] == 1:
          x = pygame.mouse.get_pos()[0] // 200
          y = pygame.mouse.get_pos()[1] // 200
          grid.play(x, y, player)
          if ai.terminal(grid.matrix):
            grid.draw(surface)
          else:
            act = ai.minimax(grid.matrix)
            grid.matrix = ai.result(grid.matrix, act)
intro()
game_loop()