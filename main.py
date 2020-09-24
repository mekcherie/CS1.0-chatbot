
# this is a new python file
from random import choice


# Create a function called get_bot_response(). 
# It should have 1 parameter called user_response
def get_therapy_bot_response(user_response):


  
  bot_response_depressed = ["how can I help yoou?", "go take a walk at the park", "I want to see you happy!come home"]
  bot_response_excited = ["yes whats the news", "yes positive energy only"]
  bot_response_lazy= ["get up go to the gym","whatever it is, don't give up!"]
# It should return a string with the chat bot’s response. 
  if user_response == "depressed":
    return choice(bot_response_depressed)
  elif user_response == "excited":
    return choice(bot_response_excited)
  elif user_response == "lazy":
    return choice(bot_response_lazy)
  else:
    return "I hope your day gets better"


print("Greetings to Therapy Bot")
print("Please enter how you are feeling this evening?")


user_response = ""

while True:
  user_response = input("How are you feeling today?: ")
  

  if user_response == 'done':
    break

  
  bot_response = get_therapy_bot_response(user_response)
  print(bot_response)



