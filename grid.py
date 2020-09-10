import pygame
import ai
import time

class Grid:
  def __init__(self):
    self.grid_lines = [((0,200), (600, 200)), #upper horizontal line
                       ((0,400), (600, 400)), #lower horizontal line
                       ((200, 0), (200, 600)), #left vertical line
                       ((400,0), (400, 600))] #right vertical line
    self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  def draw(self, surface):
    for line in self.grid_lines:
      pygame.draw.line(surface, (200,200,200), line[0], line[1], 2)
    for x in range(3):
      for y in range(3):
        if self.matrix[x][y] == "X":
          pygame.draw.line(surface, (200, 200, 200), (x*200, y*200), (x*200 + 200, y*200 + 200), 2)
          pygame.draw.line(surface, (200, 200, 200), (x*200 + 200, y*200), (x*200, y*200 + 200), 2)
        if self.matrix[x][y] == "O":
          pygame.draw.circle(surface, (200, 200, 200), (x*200 + 100, y*200 + 100), 100, 2)
    if ai.terminal(self.matrix):
      #surface.fill((200, 200, 200))
      pygame.font.init()
      font = pygame.font.SysFont(None, 100)
      img = font.render('Game Over', False, (200, 0, 200))
      surface.blit(img, (100, 225))
      if ai.utility(self.matrix) == -1:
        newtext = font.render('AI Wins!', False, (200, 0, 200))
        surface.blit(newtext, (150, 325))
      else:
        newtext = font.render('Tie!', False, (200, 0, 200))
        surface.blit(newtext, (220, 325))

  def play(self, x, y, player):
    self.matrix[x][y] = player
    print(self.matrix)
