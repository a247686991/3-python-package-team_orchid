import random;
import textwrap
from pathlib import Path
from .bubble import make_bubble



ascii_art = r"""
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%##(##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#%%%%%%%%%#######%@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@%%#%%&%%%###%%####(#%&&&%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@%&&&&&#((///((((////**////(#&&&&&&%@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@&&&&&&%#(////***************////(#@@&&&@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@&&&@&#(///***************,*****///(&@&&&@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&&#(///********,,,,,,,,,,,****///(&&&&&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&%(////*****,*,*,,,,,,,,,,,,****//#&&@&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&&&&&%(////*******,,,,,,,,,,********//(&&&&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&@&&&%////**********,,,,,,,,,,******//(%&&&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&@@&&%(///*******,,,,,,,,,,,,,,******//#&@&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&&@@&%(///(#(####(/****,**//(%%%%##(///(&&&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&(//%###%##%%###(/***/(((%&&&&%###((&@&//@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@(((#&&(//(#%#(*##,/(/(/***///(**#*/(((///&%#((/@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@/(//&&(//***//*////////****/*****/******/#(**/*@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@/(/(%&(//***/*******//**,,*/*******,,**//##(*/@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@/(#(&(///*********///*,,,,*//*********//%%(*#@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@///&%(//********/////****///*******///(&%//&@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@(/&&##((///**//((#&##%####(//***//(###&#/&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@(&&&&%#(/(%%###%%%##%##%%%((##(((##%&&&@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@&&&&%##%&%&&%###%##((###%%%%#%%%%%&&&@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@&&&&&&%&%%#//(////////////%&&&#&&&&@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@(%&@&&&&%#((((###%##((((((%&&&&@&%@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@,#%/#&&&&&&&&%##%%#%%%##(#%&&%&&@&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@..(&//(&&&&&&&&&%%%%#%%(%%&&@&&@%(@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@....,///(%&&&&@&&&&%%%%%&&&&@@@&(/..@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@.......////((#%&&&&&&@&&&@&@&&@%(//*,../@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@............//(((((((##&&@@@@@&&#/////#,,......(@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@%..........    ...*///////(((((((//////*//&(.......... *@@@@@@@@@@@@
        @@@@@@@@@%.                 ..,..//**///////////****//%/*. ............ .&@@@@@@
        """


def avg(*grades):

    average = sum(grades)/ len(grades)
    message = f"Your average grade is {average:.2f}"

    bubble = make_bubble(message)
    print(f"{bubble}\n{ascii_art}")

    return average

def random_quote(n=1):
    profLines = ["everything is due at class time", "ask Bloombot", "Quizzes: 25%", "Exercises & Projects: 75%", "Discord is our main source of communitcation"]
    selected_quotes = [random.choice(profLines) for _ in range(n)]

    bubble_text = "\n".join(selected_quotes)
    
    bubble = make_bubble(bubble_text)
    print(f"{bubble}\n{ascii_art}")
    
    return selected_quotes

def coding_wisdom(language="Python"):
    wisdom_dict = {
        "Python": [
            "Remember: readability counts!",
            "Use list comprehensions wisely",
            "Virtual environments are your friend",
            "PEP 8 is the style guide to follow",
            "Test your code with pytest"
        ],
        "JavaScript": [
            "Async/await makes life easier",
            "Always use const and let, never var",
            "Arrow functions are your friend",
            "npm install is just the beginning",
            "Console.log is for debugging only"
        ],
        "Java": [
            "Object-oriented design matters",
            "Exceptions should be exceptional",
            "Use interfaces wisely",
            "The JVM is powerful but watch memory",
            "Unit tests save production bugs"
        ],
        "C++": [
            "Manage your memory carefully",
            "RAII is your best friend",
            "Smart pointers over raw pointers",
            "The STL is incredibly powerful",
            "Compile warnings are errors in disguise"
        ],
        "default": [
            "Write clean, readable code",
            "Test early, test often",
            "Documentation is never optional",
            "Version control is essential",
            "Code reviews make better developers"
        ]
    }
    
    wisdom_list = wisdom_dict.get(language, wisdom_dict["default"])
    message = random.choice(wisdom_list)
    full_message = f"{language} wisdom: {message}"
    
    bubble = make_bubble(full_message)
    print(f"{bubble}\n{ascii_art}")
    
    return message