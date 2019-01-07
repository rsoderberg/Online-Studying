beats_per_measure = 4
measures = 5

#Using the original values of the variables
#above, this will initially print the following numbers (but each
#on their own line): 1 2 3 4 2 2 3 4 3 2 3 4 4 2 3 4 5 2 3 4
counter = 1
for x in range(measures):
    for y in range(beats_per_measure):
        if y == 0:
            print(counter)
            counter += 1
        else:
            print(y + 1)