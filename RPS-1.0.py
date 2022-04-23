while True: print(__import__("random").choice(["You win!","You lose!","Draw"] if input("Rock, Paper or Scissors? ").lower()[0] in ["r","p","s"] else ["Incorrect choice!"]))
