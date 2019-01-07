# In this problem, your goal is to write a function that can
# either count all the vowels in a string or all the consonants
# in a string.
#
# Call this function count_letters. It should have two
# parameters: the string in which to search, and a boolean
# called find_consonants. If find_consonants is True, then the
# function should count consonants. If it's False, then it
# should instead count vowels.
#
# Return the number of vowels or consonants in the string
# depending on the value of find_consonants. Do not count
# any characters that are neither vowels nor consonants (e.g.
# punctuation, spaces, numbers).
#
# You may assume the string will be all lower-case letters

def count_letters(a_string, find_consonants):
    letters = 0
    vowels = "aeiou"

    for let in a_string:
        if find_consonants is False:
            if let in vowels and let != " ":
                letters += 1
        else:
            if let not in vowels and let != " ":
                letters += 1

    return letters

# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))