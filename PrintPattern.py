# this one was super hard worked on it for over 3 hours and eventually had to
# look at video. I kept trying to do this with for loops and whie loops
# I did not think to use range(). I was able to do it with lists and using
# .insert and .remove.

# what guy in video did
def print_pattern(n):
    for star in range(0, n):
        for stars in range(0, star + 1):
            print("*", end=' ')
        print()

    for star in range(n, 0, -1):
        for stars in range(0, star - 1):
            print("*", end=' ')
        print()


print_pattern(4)
