mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "David", the output would be:
#0 D
#1 a
#2 v
#3 i
#4 d
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.
counter = 0

#Add your code here!
for i in mystery_string:
    print(counter, mystery_string[counter])
    counter += 1
