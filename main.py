import random
import pygame, sys
import Gui
import Wordle

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Wordle')
my_font = pygame.font.Font("Merriweather-Regular.ttf", 35)

wordList = []
file = open("Wordbank.txt")

for line in file.readlines():
  wordList.append(line.strip().lower())

rand = random.randint(0, len(wordList)-1)

target = wordList[rand] 
print(target)
guesses = []
hints = []
done = False


n = len(target)
totalWidth = 50*n+10*(n-1)
totalHeight = 50*6+10*5
xStart = 250 - (totalWidth/2)
yStart = 250 - (totalHeight/2)

screen.fill("white")
for i in range(6):
    Gui.drawEmptyRow(target, screen, xStart, 60 * i + yStart)

pygame.display.update()
while True:
  if not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
  
    guess = input("Enter " + str(len(target)) +" letter guess:").strip()
    while len(guess) != len(target):
      guess = input("Invalid length, enter new guess:").strip()
    guess = guess.lower()
    green = Wordle.checkGreens(target, guess)
    #print(green)
    yellow = Wordle.checkYellows(target, guess)
    #print(yellow)
    hint = Wordle.createHint(green, yellow)
    print(hint)
    guesses.append(guess)
    hints.append(hint)
  
    if guess == target:
      
      print("You win!")
      done = True
    
    
 
  
  screen.fill("white")
  for i in range(6):
    if i < len(guesses):
      Gui.drawRow(guesses[i], hints[i], screen, my_font, xStart, 60 * i + yStart)
    else:
      Gui.drawEmptyRow(target, screen, xStart, 60 * i + yStart)
      
  if done:
    text_surf = my_font.render("Guessed in: " + str(len(guesses)), False, "black")
    text_surface = my_font.render("You win!", False, "black")
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, (250-text_rect.width / 2, 0))
    screen.blit(text_surf, (220-text_rect.width / 2, 425))
    
  pygame.display.update()