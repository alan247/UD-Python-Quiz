import os

from time import sleep

from pyfiglet import Figlet


# Prepare Figlet (ASCII art library) for later use
figlet = Figlet()

easy = """
Udacity is a for-profit educational organization founded by Sebastian Thrun,
David Stavens, and Mike Sokolsky offering massive open online courses (MOOCs).
According to Thrun, the origin of the name comes from the company's desire to
be "audacious for you, the student". While it originally focused on offering
university-style courses, it now focuses more on vocational courses for
professionals.
"""

medium = """
The first two courses ever launched on Udacity both started on 20 February
2012, entitled "CS 101: Building a Search Engine", taught by David Evans from
the University of Virginia, and "CS 373: Programming a Robotic Car" taught by
Thrun. Both courses use Python.
"""

hard = """
Four more courses began on 16 April 2012, encompassing a range of ability and
subject matter, with teachers including Steve Huffman and Peter Norvig. Five
new courses were announced on 31 May 2012, and marked the first time Udacity
offered courses outside the domain of computer science. Four of these courses
launched at the start of the third "hexamester", on 25 June 2012. One course,
Logic & Discrete Mathematics: Foundations of Computing, was delayed for several
weeks before an email announcement was sent out on 14 August stating that the
course would not be launched, although no further explanation was provided.
"""

text_dictionary = {
    0: easy,
    1: medium,
    2: hard
}

blanks = [
    ["Udacity", "Sebastian", "online", "audacious"],
    ["courses", "Udacity", "February", "Engine", "Robotic", "Python"],
    ["courses", "April", "science", "June", "Mathematics", "Computing"]
]


def choose_difficulty():
    """  Asks the user to select a difficulty level.

    The difficulty levels are represented by a number (0-2). This number will
    be passed as an argument to other functions to reference the selected
    difficulty.

    Returns:
        int:	An integer (0-2) indicating the difficulty level the user chose

    """

    display_message("Welcome!!!")
    difficulty = raw_input(
        "Please select a difficulty level (easy, medium or hard):")

    if difficulty == "easy":
        result = 0
    elif difficulty == "medium":
        result = 1
    elif difficulty == "hard":
        result = 2
    else:
        display_message("Invalid   option")
        choose_difficulty()

    display_message("Here   we   go!!")

    return result


def word_in_list(word, word_list):
    """ Checks if a word exists in a word list

    Loops through all the elements in the lists and checks if the current item
    is a substring of the word that was passed as first argument

    If the check is positive, returns the current item, otherwise returns None

    Args:
        word 		(str):	A word to be checked against the list
        word_list 	(str): 	A list containing words

    Returns:
        The word if the word is in the list. None otherwise.
    """

    for item in word_list:
        if item in word:
            return item
    return None


def create_blanks(difficulty, solved_blanks):
    """ Processes the text and creates blanks acording to the number of
    questions the user has already solved.

    Args:
        difficulty 		(int):	Difficulty level expressed as a single
                                digit (0-2).
        solved_blanks 	(int): 	Number of blanks that the user has
                                already solved correctly

    Returns:
        str:	A string with the processed text containing blanks for the
                words the student hasn't guessed properly yet.

    """

    # Create copy of the original blanks list that we can modify
    level_blanks = list(blanks[difficulty])
    text_split = text_dictionary[difficulty].split()
    index = solved_blanks

    # Not a magic number! We add one to solved_blanks and assign it to the new
    # current_blank variable. This is the new blank the user will try to fill.
    current_blank = solved_blanks + 1

    # Delete solved items from level_blanks
    del level_blanks[:solved_blanks]

    while index < len(text_split):

        replacement = word_in_list(text_split[index], level_blanks)

        if replacement is not None:
            text_split[index] = text_split[index].replace(
                replacement, "______" + str(current_blank) + "______")
            current_blank += 1

            # Avoids repeating words by removing the word from the list
            level_blanks.remove(replacement)

        index += 1

    return " ".join(text_split)


def play(difficulty):
    """ Starts the game and prints the processed text for each level

    Loops until the amount of solved questions equals the number of items in
    the	blanks list for the the selected difficulty.

    In each loop, it shows an updated processed text, asks the user for some
    input and shows a success or error message depending on the answer.

    When all the blanks have been filled, the whole text is shown.

    Args:
        difficulty 	(int):	Difficulty level expressed as a single
                            digit (0-2).
    """

    solved = 0
    blanks_qty = len(blanks[difficulty])

    while solved < blanks_qty:

        print create_blanks(difficulty, solved)
        question = "\n\nWhat word would you use to fill ______" + str(
            solved + 1) + "______ ?  "
        user_answer = raw_input(question).lower()
        right_answer = blanks[difficulty][solved].lower()

        if right_answer == user_answer:
            display_message("That's   right !!")
            solved += 1
        else:
            display_message("Not   quite!!")

    print figlet.renderText("YOU   WON!!")
    print text_dictionary[difficulty]


def display_message(text):
    """ Prints messages in ASCII art and removes them after 750ms. Also clears
    the screen.	It uses the pyfiglet library, based on Figlet and os library.

    Args:
        text 	(str):	The message that will be displayed in ASCII art
    """

    clear_shell()
    print figlet.renderText(text)
    sleep(.75)
    clear_shell()


def clear_shell():
    """ Clears the shell screen with the os library
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    """ Runs the game

    First clears the shell screen and later calls the play() function with
    the outcome	of the choose_difficulty() function as an argument.
    """

    clear_shell()
    play(choose_difficulty())

run()
