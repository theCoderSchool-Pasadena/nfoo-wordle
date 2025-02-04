import pygame
def drawRow(word, hint, screen, font, xStart, yStart):
  for i in range(len(word)):
    color = ""
    if hint[i] == "-":
      color = "grey"
    elif hint[i] == "y":
      color = "yellow"
    else: 
      color = "green"
    pygame.draw.rect(screen, color, (xStart + 60 * i, yStart, 50, 50))
    text_surface = font.render(word[i], False, "black")
    text_rect = text_surface.get_rect()
    xText = (xStart + 60 * i)+(25-text_rect.width/2)
    screen.blit(text_surface, (xText, yStart))

def drawEmptyRow(word, screen, xStart, yStart):
  for i in range(len(word)):
    color = "grey"
    pygame.draw.rect(screen, color, (xStart + 60 * i, yStart, 50, 50))