print("WELCOME TO BASIC ROCK PAPER KNIFE GAME\n"
      "      be ready to lose hehe\n")


Choice = ""

while Choice != "q":
      Choice=input("Choose one of the following:\n "
            "1 = rock\n "
            "2 = paper\n "
            "3 = knife\n "
            "q = quit\n")
      if Choice == "1":
            print("\n\n\n                             Computer played Paper, You lost Choose again\n\n\n")
      elif Choice == "2":
            print("\n\n\n                             Computer played Knife, You lost Choose again\n\n\n")
      elif Choice == "3":
            print("\n\n\n                             Computer Played Rock, You lost Choose again\n\n\n")
      elif Choice == "q":
            print("\n\n\n                             Closing game\n\n\n"
            "\n\n                             Made by Bamb4Boy\n\n")
      else:
            print("                                   wrong input")
            print("                                   Try Again")
      



