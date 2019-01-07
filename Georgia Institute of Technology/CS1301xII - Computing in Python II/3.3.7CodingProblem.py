start_character = "A"
end_character = "Z"

#Print all the letters from start_character to end_character,
#each on their own line. Include start_character and
#end_character themselves.
#You may assume that both start_character and end_character
#are uppercase letters (although you might find it fun to
#play around and see what happens if you put other characters
#in instead!).
#Add your code here! With the original values for
#start_character and end_character, this will print the
#letters from A to Z, each on their own line.

for alphabet in range(ord(start_character), ord(end_character) + 1):
    print(chr(alphabet))
