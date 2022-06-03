import random

print("ROCK, PAPER SCISSORS GAME")
print("R for rock")
print("P for paper")
print("S for scissors")
possible_actions = ['R', 'P', 'S']
player_action = input('Enter a choice (R, P, S): ').upper()
 
# FUNCTION
def action(action, player):
     switcher = {
         'R': player+"(Rock)",
         'P': player+"(Paper)",
         'S': player+"(Scissors)",
     }
     return switcher.get(action,"Invalid action")
     
while True:
     if player_action not in possible_actions:
         print('Your chioce is not a possible action')
         player_action = input('Enter a choice (R, P, S): ').upper()
         continue
     #computer actions
     computer_action = random.choice(possible_actions) 
     #set the action letter to suppose value 
     player_choice = action(player_action, 'Player')
     computer_choice = action(computer_action, 'CPU')
     #print choices
     print(player_choice + " : " + computer_choice)
     if player_action == computer_action:
         print("It's a tie!!!")
         player_action = input('Enter a choice (R, P, S): ').upper()
         continue
     elif player_action =='R':
         if computer_action == 'S':
             print(player_choice + " smashes "+ computer_choice + " you win!!!")
             break
         else:
             print(computer_choice + " covers "+ player_choice + " you lose!!!")
             break
     elif player_action =='P':
         if computer_action == 'R':
             print(player_choice + " covers "+ computer_choice + " you win!!!")
             break
         else:
             print(computer_choice + " cuts "+ player_choice + " you lose!!!")
             break
     elif player_action =='S':
         if computer_action == 'P':
             print(player_choice + " cuts "+ computer_choice + " you win!!!")
             break
         else:
             print(computer_choice + " smashes "+ player_choice + " you lose!!!")
             break