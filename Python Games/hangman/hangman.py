import random
print("Welcome to Hangman!")
print()
print ("There is two game modes: single word or sentance.")
inp = input ("Type '1' for single word or '2' for sentance.")
while not(inp.isdigit() and len(inp)==1 and (inp=="1" or inp =="2")):
  inp = input ("Stop. Please type 1 or 2.")
inp = int(inp)
print()
if inp == 1:
  print("Welcome to word mode.")
  print("Your goal is to guess the word within 6 guesses.")
  n = open("nouns.txt","r")
  strn = n.readlines()
  r1= random.randint(0,len(strn)-1)
  word = strn[r1]
  word = word[0 : len(word)-1]
  #print(word)
  guesses = 6
  gword = ""
  for i in word:
    gword+="*"
  print(gword)
  print()
  gword=""
  letters = []
  tryw = []
  print("Guesses " + str(guesses))
  while guesses>0:
    letter = input("Guess a letter: ")
    print()
    if len(letter)>1:
      print("Guess only one letter.")
      print()
      continue
    if letter.isdigit():
      print("Bro what are you doing? I said put a letter.")
      print()
      continue
    if letter in letters or letter in tryw:
      print("You already guessed that letter!")
      print("Try a diffrent one.")
      print()
      continue
    if letter.isupper():
      letter.lower()
    if word.count(letter) > 0:
      num = word.count(letter)
      print("There are "+ str(num)+" " + letter.capitalize() +"(s).")
      letters.append(letter)
      for i in word:
        if i in letters:
          gword+=i
        else:
          gword+="*"
      print(gword)
      print()
      if gword == word:
        print("You guessed the word!")
        break
      gword=""   
    else:
      tryw.append(letter)
      print("Sorry the word does not have a "+ letter.capitalize())
      guesses-=1
      print("Guesses Left: " + str(guesses))
      print()
  if guesses == 0:
    print("You ran out of guessses.")
    print("The word was " + word)

elif inp == 2:

  print("Welcome to sentance mode.")
  print("Your goal is to guess the scentance within 6 guesses.")
  s = open("sentences.txt","r")
  strs = s.readlines()
  r2= random.randint(0,len(strs)-1)
  sentence = strs[r2]
  sentence = sentence[0 : len(sentence)-2]
  sentence = sentence.lower()
  #print(sentence)
  guesses = 3
  gsen = ""
  for i in sentence:
    if i == " ":
      gsen += " "
    else:
      gsen+="*"
  print(gsen)
  print()
  gsen=""
  letterss = []
  trys = []
  print("Guesses " + str(guesses))
  while guesses>0:
    letter = input("Guess a letter: ")
    print()
    if len(letter)>1:
      print("Guess only one letter.")
      print()
      continue
    if letter.isdigit():
      print("Bro what are you doing? I said put a letter.")
      print()
      continue
    if letter in letterss or letter in trys:
      print("You already guessed that letter!")
      print("Try a diffrent one.")
      print()
      continue

    if sentence.count(letter) > 0:
      num = sentence.count(letter)
      print("There are "+ str(num)+" " + letter.capitalize() +"(s).")
      letterss.append(letter)

      
      for i in sentence:
        if i in letterss:
          gsen+=i
        elif i == " ":
          gsen+=" "
        else:
          gsen+="*"
      print(gsen)
      print()
      if gsen == sentence:
        print("You guessed the sentence!")
        break
      gsen=""   
    else:
      trys.append(letter)
      print("Sorry the sentence does not have a "+ letter.capitalize())
      guesses-=1
      print("Guesses Left: " + str(guesses))
      print()
  if guesses == 0:
    print("You ran out of guessses.")
    print("The sentence was " + sentence)
  
else:
  print("Please type 1 or 2.")
