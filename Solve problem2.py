def print_hello(string):
    vowels = 'aeiouAEIOU'

    for char in string:
        if char in vowels:
            print("Hello World")

user_input = input("Enter a string: ")
num_vowels = print_hello(user_input)


