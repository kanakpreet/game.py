#wap and ask the user to get that number and give three guesses.
sec_num = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
  guess = int (input ("Guess:"))
  guess_count += 1
  if guess == sec_num:
    print ("correct")

  else:
    print("sorry , you failed")
