number = 215

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The number above is given in base 10. Let's convert it to
#base 2 and print it in binary. For example, 215 can be written
#in binary as 11010111.
#
#Each digit of that string corresponds to a power of 2. The far
#left digit represents 128, then 64, then 32, then 16, then 8,
#then 4, then 2, and then finally 1 at the far right.
#
#To convert the number to binary, first check to see if it is
#greater than or equal to 128. If it is, your first digit is 1.
#If not, your first digit is 0. If the number was greater than
#128, subtract 128 (because the 128 is captured by the first
#digit of the string).
#
#Then, repeat that process for 64, 32, 16, 8, 4, 2, and 1.
#
#For example:
#
#215 is >= 128: 1
#87 is >= 64: 11
#23 is not >= 32: 110
#23 is >= 16: 1101
#7 is not >= 8: 11010
#7 is >= 4: 110101
#3 is >= 2: 1101011
#1 is >= 1: 11010111
#
#Note that although we use 'if' a lot to describe this problem,
#this can be done entirely with floor division and modulus.
#Remember, if you convert a boolean to an integer, True becomes
#1 and False becomes 0.
#
#Note that we always work with binary in 8-bit chunks: the
#number 7 would be 00000111, not just 111. That's because inside
#the computer, 8 1s and 0s make a byte, which is the smallest
#practical unit of storage (rarely are bits used outside 8-bit
#bytes).
#
#Print the string that results from this conversion.

#Add your code here!
digits = ""
eight_bit = 128
comp = int(number > eight_bit)

while (eight_bit > 0):
    if (number > eight_bit):
        digits += "1"
        number -= eight_bit
        eight_bit //= 2
    else:
        digits += "0"
        eight_bit //= 2


print(digits)

