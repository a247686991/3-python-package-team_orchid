from bloomsays import wisdom

def main():

    # average grade function 
    print("\n1. Calculating the average of grades :")
    wisdom.avg(85, 92, 78, 95)

    # getting a random quote function
    print("\n Getting a random quote from professor :")
    wisdom.random_quote()
    
    print("\n   Getting 2 random quotes from professor :")
    wisdom.random_quote(n=2)

    # getting coding wisdoms
    print("\n Getting some Python coding wisdom:")
    wisdom.coding_wisdom(language="Python")

    print("\n   Getting some JavaScript coding wisdom:")
    wisdom.coding_wisdom(language="JavaScript")

    print("\n   Getting some Java coding wisdom:")
    wisdom.coding_wisdom(language="Java")

    print("\n   Getting some C++ coding wisdom:")
    wisdom.coding_wisdom(language="C++")

    print("\n   Getting some random coding wisdom:")
    wisdom.coding_wisdom()


    # getting funny jokes
    print("\n Here's a funny joke:")
    wisdom.jokes()

    print("\n   Here are 3 random funny jokes:")
    wisdom.jokes(n=3)

    # study tips
    print("\n Getting a study random tip: ")
    wisdom.study_tip()

    print("\n   Getting a study tip for an easy task with 5 hours available:")
    wisdom.study_tip(hours_available=5, difficulty="easy")
    
    print("\n   Getting a study tip for a hard task with 1 hour available:")
    wisdom.study_tip(hours_available=1, difficulty="hard")


if __name__ == "__main__":
    main()