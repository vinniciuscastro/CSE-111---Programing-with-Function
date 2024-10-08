# Vinnicius Castro
# Feb 8th 2023

def main():
    score = 0
    score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    score += ask_positive_question(
        "2. I feel that I have a number of good qualities.")
    score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question(
        "4. I am able to do things as well as most other people.")
    score += ask_negative_question(
        "5. I feel I do not have much to be proud of.")
    score += ask_positive_question(
        "6. I take a positive attitude toward myself.")
    score += ask_positive_question(
        "7. On the whole, I am satisfied with myself.")
    score += ask_negative_question(
        "8. I wish I could have more respect for myself.")
    score += ask_negative_question(
        "9. I certainly feel useless at times.")
    score += ask_negative_question(
        "10. At times I think I am no good at all.")

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_positive_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score

def ask_negative_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score



if __name__ == "__main__":
    main()