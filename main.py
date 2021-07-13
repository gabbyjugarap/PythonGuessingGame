import random
number=random.randrange(0,100)
guessCheck="wrong"
print("Let's play a game!")
print("\n")
while guessCheck=="wrong":
  response=int(input("Guess a number from 1 to 99! \n"))
  try:
    val=int(response)
  except ValueError:
      print("Not a valid number please choose between 1 and 99!")
      continue
  val=int(response)
  if val<number:
    print("Too Low!")
  elif val>number:
    print("Too High!")
  else:
    print("You guessed it!")
    guessCheck="correct"
print("Thank you for playing!")
