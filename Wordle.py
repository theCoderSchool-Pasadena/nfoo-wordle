import random

def checkGreens(target, guess): 
  hint = ""

  for i in range(len(guess)):
    #print(guess[i], target[i])
    if guess[i] == target[i]:
      hint = hint + "g"
    else:
      hint = hint + "-"
  return hint

def checkYellows(target, guess):
  hint = ""

  for i in range(len(guess)):
    guessLetter = guess[i]
    #print("outer", i)
    match = False

    for j in range(len(target)):
      targetLetter = target[j]
      if guessLetter == targetLetter:
        match = True
    if match:
      hint = hint + 'y'
    else:
      hint = hint + '-'

    #print("HINT", guessLetter, match)

  return hint

def createHint(green, yellow):
  hint = ""

  for i in range(len(green)):
    greenLetter = green[i]
    yellowLetter = yellow[i]
    if greenLetter == "-" and yellowLetter == "-":
      hint = hint + "-"
    elif yellowLetter == "y" and greenLetter == "-":
      hint = hint + "y"
    elif yellowLetter == "y" and greenLetter == "g":
      hint = hint + "g"
    elif greenLetter == "g" and yellowLetter == "-":
      hint = hint + "g"

  return hint

# wordList = []
# file = open("Wordbank.txt")

# for line in file.readlines():
#   wordList.append(line.strip())

# rand = random.randint(0, len(wordList)-1)

# target = wordList[rand] 
# done = False
# while not done: 
#   guess = input("Enter " + str(len(target)) +" letter guess:").strip()
#   while len(guess) != len(target):
#     guess = input("Invalid length, enter new guess:").strip()
#   guess = guess.lower()
#   green = checkGreens(target, guess)
#   #print(green)
#   yellow = checkYellows(target, guess)
#   #print(yellow)
#   hint = createHint(green, yellow)
#   print(hint)

#   if guess == target:
#     print("You win!")
#     done = True