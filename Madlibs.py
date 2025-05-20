# Mad libs

# get user input
name=input("Enter a name: ")
place=input("Enter  a place:  ")
animal=input("Enter an animal:")
verb=input("Enter a verb: ")
adjective=input("Enter an adjective: ")

# create a story using f-string 
story=f"""
Once upon a time ,there was a person named {name} who lived in {place}.
One day ,they saw a {adjective} {animal} that could {verb}!
It was  the most amazing thing they had ever seen."""

# Display the story
print("\nHere is your Mad Libs story: ")
print(story)



