import random

# Create an empty array to store the names
names = []

# Ask the user to input 5 names
for i in range(1, 6):
    name = input(f"Enter name number {i}: ")
    names.append(name)

# Select a random number in the bounds of the 5 element array (zero-based, i.e. 0 - 4)
selected_item = random.randint(0, len(names) - 1)

# Output the random name
print("The name I randomly selected is:", names[selected_item])
