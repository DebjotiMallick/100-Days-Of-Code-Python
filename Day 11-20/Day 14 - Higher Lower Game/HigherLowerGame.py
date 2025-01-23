import random
from game_data import data
import art


def compare(a_followers, b_followers):
    if a_followers > b_followers:
        return 'A'
    else:
        return 'B'


correct = True
score = 0
while correct:
    print(art.logo)
    A = random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

    print(art.vs)
    B = random.choice([ele for ele in data if ele != A])
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    more_followers = compare(A['follower_count'], B['follower_count'])
    if choice == more_followers:
        score += 1
        print(f"You're right. Your current score: {score}.")
    else:
        print(f"You're wrong. Your final score is {score}.")
        correct = False
