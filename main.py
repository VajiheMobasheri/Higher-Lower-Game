from famouspeople import famous_people_list
import random


#Define a function to randomly select two celebrities from the list.
def random_name(famous_people):
    """Return two random celebrities"""
    random_person_a = random.choice(famous_people)
    random_person_b = random.choice(famous_people)
    return random_person_a, random_person_b


#Define a function to calculate the user's score.
def calculate_score(random_person_a, random_person_b, guess):
    """Return True if guess is right and False if not."""
    if (guess == "A" and random_person_a['number of followers on Instagram'] > random_person_b[
        'number of followers on Instagram']) or (
            guess == "B" and random_person_a['number of followers on Instagram'] > random_person_b[
        'number of followers on Instagram']):
        return True
    else:
        return False


def game():
    score = 0
    while True:
        random_person_a, random_person_b = random_name(famous_people_list)
        #Display information about the two celebrities to the user.
        print(f"Compare A : {random_person_a['famous person name']}, {random_person_a['where they are from']}")
        print(f"Compare B : {random_person_b['famous person name']}, {random_person_b['where they are from']}")
        #Ask for the user's guess.
        guess = input("Who has more followers? A or B?")
        #Check the user's guess.
        if calculate_score(random_person_a, random_person_b, guess):
            score += 1
            print(f"That's right! your score is : {score}")
        else:
            print(f"You lose! your score is : {score}")
            break


game()
