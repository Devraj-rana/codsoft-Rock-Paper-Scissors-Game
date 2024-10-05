import random
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return 'You win!'
        else:
            return 'Computer wins!'
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            return 'You win!'
        else:
            return 'Computer wins!'
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return 'You win!'
        else:
            return 'Computer wins!'
    else:
        return "Invalid choice!"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0
    
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        rounds += 1
        print(f"Score after {rounds} round(s): You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game Over!")
            print(f"Final Score: You {user_score} - Computer {computer_score}")
            break
play_game()
