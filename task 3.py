# Initialize empty list to store words
word_list = []

# Get words from the user until "stop" is entered
while True:
    word = input('Enter a word to input.  "stop" to end: ')
    if word.lower() == "stop":
        break
    word_list.append(word)

# Set up vowel count
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Loop through words and count vowels
for word in word_list:
    for char in word:
        lower_char = char.lower()
        if lower_char == "a":
            a_count +=1
        if lower_char == "e":
            e_count +=1
        if lower_char == "i":
            i_count +=1
        if lower_char == "o":
            o_count +=1
        if lower_char == "u":
            u_count +=1


# Output results
print(f"Instances of a/A: {a_count}")
print(f"Instances of e/E: {e_count}")
print(f"Instances of i/I: {i_count}")
print(f"Instances of o/O: {o_count}")
print(f"Instances of u/U: {u_count}")