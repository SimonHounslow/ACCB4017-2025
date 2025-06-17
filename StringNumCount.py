user_input = input("Enter a string: ")

letter_count = 0
number_count = 0
whitespace_count = 0
special_count = 0
word_length = len(user_input)
loop_counter = 0

# Loop through each character in the string
while loop_counter<word_length:
    if user_input[loop_counter].isalpha():
    # If the character is a letter
        letter_count += 1
    if user_input[loop_counter].isdigit():
    # If the character is a number
        number_count += 1
    if user_input[loop_counter].isspace():
        whitespace_count += 1
    loop_counter+=1

special_count = len(user_input) - letter_count
special_count -= number_count
special_count -= whitespace_count

# Output the result
print("Number of letters:", letter_count)
print("Number of numbers:", number_count)
print("Number of spaces:", whitespace_count)
print("Number of other characters:", special_count)