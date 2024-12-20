# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("Red","Green","Blue","Black","White","Cyan","Lime","Brown","Pink","Yellow","Purple","Orange")

for imposter in people:
    print(people)
    Skeld = int(input("What number is the imposter:"))
    Skeld = Skeld - 1
    print(f"You voted {people[Skeld]}")
    if people[Skeld] == imposter:
        print(f"{people[Skeld]} was the imposter")
    else:
        print(f"{people[Skeld]} was not the imposter")
