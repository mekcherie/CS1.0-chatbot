
# this is a new python file

# Create a function called get_bot_response(). This function must: 

# It should have 1 parameter called user_response, which is a string with the users input.
    
    def get_therapy_bot_response(user_response):

#   It should use at least 2 lists to store at least 3 unique responses to different user inputs.

  bot_response_lonely = ["sorry, you had to go through that, how can I help!", "Keep smiling!life will get better ", "I love to see you happy! what can I do?"]
  bot_response_tired = ["Go to the park", "meditate", "ouch, go drink a coffee"]
  bot_response_depressed = ["Go to the gym", "call your friends", "aww, you want to talk about it?"]

# Use conditionals to decide which of the response lists to select from.
# Use choice() to randomly select one of the three responses. 

  if user_response == "lonely":
      return choice(bot_response_lonely)
  elif user_response == "tired":
    return choice(bot_response_tired)
    if user_response == "depressed":
      return choice(bot_response_depressed)




