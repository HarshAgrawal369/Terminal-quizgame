questions = {
    "What is the capital of France?": "paris",
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Greece?": "athens",
}

answers = {
    "What is the capital of France?": ["paris", "berlin", "rome", "madrid"],
    "What is the capital of Germany?": ["lisbon", "berlin", "athens", "rome"],
    "What is the capital of Italy?": ["madrid", "paris", "rome", "berlin"],
    "What is the capital of Spain?": ["athens", "madrid", "lisbon", "paris"],
    "What is the capital of Portugal?": ["rome", "berlin", "madrid", "lisbon"],
    "What is the capital of Greece?": ["paris", "athens", "berlin", "madrid"]
}

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(f"\nQuestion {question_num}: {key}")
        options = answers[key]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        guess_index = input("\nEnter the option number: ")
        if guess_index.isdigit():
            guess_index = int(guess_index) - 1
            if 0 <= guess_index < len(options):
                guess = options[guess_index]
            else:
                guess = ""
        else:
            guess = ""
        
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    
    display_score(correct_guesses, guesses)
    play_again()

def check_answer(answer, guess):
    if guess == answer:
        print(f"Correct! The answer was {answer}.\n")
        return 1
    else:
        print(f"Incorrect. The answer was {answer}.\n")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Results")
    print("-------------------------")
    print(f"Questions answered correctly: {correct_guesses}")
    print(f"Questions answered incorrectly: {len(guesses) - correct_guesses}")
    print(f"Total questions: {len(guesses)}")
    print(f"Accuracy: {correct_guesses / len(guesses) * 100:.2f}%")
    print("Your answers: ", guesses)

def play_again():
    response = input("Would you like to play again? (yes/no): ").lower()
    if response == "yes":
        new_game()
    elif response == "no":
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    new_game()
