
# 1.1 TODO: Create a function called validate_user_input that will
def validate_user_input():
# - ask the user for a number: 'Please enter a number'
# - try to return the user's input as an integer
    n = 0
# - continue to ask them for a valid number until they input one
    while True:
        try: 
            n = int(input('Please enter a number '))
            break
        except (SyntaxError, ValueError):
# - if the user did not input a number, tell them 'You did not enter a valid number, please try again'
            print('You did not enter a valid number, please try again')
            continue      
    return n
# - once a valid number is received, return that number
# NOTE: What type of error does python throw if you try to turn a non-number string into an integer?
    # Type error
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.


# 1.2 TODO: Once you are done, uncomment the two lines below to ensure that your code works as expected

user_number = validate_user_input()
print(f'The number the user entered is {user_number}.')

# 2.1 TODO: Create a function called print_tenth_item that will
def print_tenth_item(top_ten):
# - take in a list of items as a parameter called `top_ten` 
    while True:
        try:
# - try to print out an f-string stating the 10th item in the list (NOTE: what index is the 10th item in the list?)
            a = (f'{top_ten[9]}')
            break
        except IndexError:
# - if there are not ten items in the list, tell the user that it is not applicable: 'N/A'
            a = "N/A"
    return a
            
# NOTE: What type of error does python throw if you try to index into a list past the number of items in it?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.


# 2.2 TODO: Once you are done, uncomment the two lines below to ensure that your code works as expected

print_tenth_item(['a', 'b', 'c'])  # Should print out that there are not ten items in the list
print_tenth_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Should print out the 10th item in the list
