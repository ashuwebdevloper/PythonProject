import random

subject = [
    "Sahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A mumbai Cat",
    "A Group of  Monkeys"
    "MS Dhoni",
    "Rohit Sharma",
    
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "walks",
    "orders",
    "celibrates"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of Samosa"
    "inside parliament",
    "at ganga",
    "during ipl match",
    "at india gate"
]



while True:
    subject = random.choice(subject)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"{subject} {action} {place_or_thing}"
    print(headline)

    user_input = input("\n Do you want another head line ?(yes/no)".strip().split)
    if user_input == "no":
        break

print("Thanks for using a fla enews head line genrator . Have a good day")
