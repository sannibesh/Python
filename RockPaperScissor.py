import random

def get_choices():
  player_choice = input("Enter your choice (Rock, Paper, Scissor): ")
  options = ["Rock", "Paper", "Scissor"]
  computer_choice = random.choice(options)
  choices = {"Player": player_choice, "Computer": computer_choice} 
  return choices

def check_win(player, computer) :
  print(f"Player chose: {player}; Computer chose: {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "Rock":
    if computer == "Scissor":
      return "Player wins!"
    else:
      return "Computer wins!"
  elif player == "Paper":
    if computer == "Rock":
      return "Player wins!"
    else:
      return "Computer wins!"
  elif player == "Scissor":
    if computer == "Paper":
      return "Player wins!"
    else:
      return "Computer wins!"
    
choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)