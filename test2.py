# All of the functions we need come automatically with python but do need to be imported.
import itertools
import time

# This is basically a list of all the different characters that will be tried.
# You will notice many symbols missing as they were slowing down efficiency and very unlikely to appear.
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.")

# This allows the user to decide what password the program will "crack" so they can decide the difficulty
# And also so they are able to see the results a lot more reliably
Password = input("What is your password?\n")

# This sets the start time so that it can be used later on in the program to calculate how long the program took.
start = time.time()

# This tells us how many combinations are used.
counter = 1

# This starts off the number of characters as 1.
CharLength = 1

# This stops the program once it gets to 25 characters (most people would run out of patience WAY before that
# But if you feel the need you can increase the number.
for CharLength in range(25):

    # This finds all of the possible combinations of characters that are of the correct length.
    passwords = (itertools.product(Alphabet, repeat=CharLength))

    # This prints three blank lines.
    print("\n \n")

    # These print information for the user on the progress of the crack.
    print("currently working on passwords with ", CharLength, " chars")
    try:
        print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
    except Exception:
        print(Exception)
    print("It has been ", time.time() - start, " seconds!")
    print("We have tried ", counter, " possible passwords!")

    # This is the way to print the products of generators.
    for i in passwords:

        # This increases the number of combinations tried by one to show that one more has been tried.
        counter += 1

        # As the itertools.products() returns a tuple, it has to be converted into a sting.
        i = str(i)

        # The parts that were added as a result of conversion from tuple have to be removed.
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")

        # This checks if the password created by the user was correct.
        if i == Password:
            # This takes the time at which the program finished.
            end = time.time()

            # This works out the time it took to find the password.
            timetaken = end - start

            # This tells the user how long it took to find the password as well as how many attempts it took.
            print("Found it in ", timetaken, " seconds and ", counter, "attempts")

            # This tells the user how many attempst were made per second.
            print("That is ", counter / timetaken, " attempts per second!")

            # This prints the password to confirm for the user that the program was sucessful.
            print(i)

            # This stops the program from exiting until the user presses enter.
            input("Press enter when you have finished")

            # This exits the program
            exit()
