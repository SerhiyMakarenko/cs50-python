# Ask user for their name, remove whitespaces and capitilize name
name = input("Hellow, what's your name? ").strip().title()

# Separate fisrt and last name
first, last = name.split(" ")

# Say hello to user and print his name
print(f"hello, {first}")