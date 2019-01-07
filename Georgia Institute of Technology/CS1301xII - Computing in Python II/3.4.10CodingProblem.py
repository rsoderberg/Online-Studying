# In this problem, you should write three functions:
# word_count, letter_count, and average_word_length.
#
# word_count should take as input a string. It should return
# the number of words in the string. You may assume that the
# number of words in the string will be one more than the
# number of spaces in the string.
#
# letter_count should take as input a string. It should return
# the number of letters in the string. You may assume that
# the string is only letters and spaces: no punctuation or
# numbers.
#
# average_word_length should take as input a string. It should
# return the average length of the words in the string. You
# can find the average length by dividing the number of letters
# by the number of words.
#
# Your implementation for average_word_length *must* call
# word_count and letter_count.

def word_count(a_string):
    word_counter = 1

    for words in a_string:
        if words == " ":
            word_counter += 1

    return word_counter


def letter_count(a_string):
    letter_counter = 0

    for letters in a_string:
        if letters != " ":
            letter_counter += 1

    return letter_counter


def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)

a_string = "Up with the white and gold"

print(average_word_length(a_string))

