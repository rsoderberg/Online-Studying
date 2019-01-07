mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]

# Above is a list of strings. Don't worry if this syntax is a
# little unfamiliar, we'll talk you through it and then cover
# it more in chapter 4.3.
# Write some code that will count the number of instances of
# the letter 't' in the list of strings. Count both capital
# 'T' and lower-case 't'. Then, print the number of instances
# of the letter 't'.
# For example, with the list declared above, you would print
# 6: two in the first string, three in the second, one in the
# third.

letter_counter = 0
for string in mystery_list:
    for currentLetter in string:
        if currentLetter == "t" or currentLetter == "T":
            letter_counter += 1
print(letter_counter)
