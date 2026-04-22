# Simple Quiz Game in Python

def quiz_game():
    score = 0

    print("Welcome to the Quiz Game!\n")

    # Question 1
    print("Q1. What is the capital of India?")
    print("a) Mumbai")
    print("b) Delhi")
    print("c) Kolkata")
    answer = input("Enter your answer (a/b/c): ").lower()

    if answer == 'b':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is Delhi\n")

    # Question 2
    print("Q2. Which language is used for web apps?")
    print("a) Python")
    print("b) Java")
    print("c) Both")
    answer = input("Enter your answer (a/b/c): ").lower()

    if answer == 'c':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is Both\n")

    # Question 3
    print("Q3. What does CPU stand for?")
    print("a) Central Process Unit")
    print("b) Central Processing Unit")
    print("c) Computer Personal Unit")
    answer = input("Enter your answer (a/b/c): ").lower()

    if answer == 'b':
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is Central Processing Unit\n")

    # Final Score
    print("Quiz Completed!")
    print("Your Score:", score, "/ 3")

# Run the game
quiz_game()
