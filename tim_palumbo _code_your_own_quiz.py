#giving values to quiz sets and lists for their answers
EASY_QUIZ = """Programming is a way for a person to communicate with a ___1___.
This then allows the user to create ___2___ that the computer can run.  There are
several ways for a person to program by using ___3___ that the computer
can understand.  A popular one like ___4___ which is an acronym for HyperText
Mark-up Language, is used to create webpages."""

EASY_ANSWERS = ["computer", "programs", "language", "html"]

MEDIUM_QUIZ = """A very popular programming language called ___1___, named after
Monty Python, is widely used.  This language can be used to create programs by
using ___2___ to create commands.  The ___3___ of the language allows for the
user to create various types and sizes of progams.  The language's ___4___ is vast
and allows for complex programming.  Although ___1___ is very sophisticated
it is also more easy to use compared to other programming languages."""

MEDIUM_ANSWERS = ["python", "syntax", "versatility", "library"]

HARD_QUIZ = """When using Python it is imperitive that you distinguish the
difference between values containing a ___1___ or a word and an ___2___ or a
numerical value.  One of the best ways to do this is to use the class "___3___"
for a string or just use "" to determine it.  This becomes useful when creating
___4___ that may contain both words and numbers operating indepedently of each other.
If they are not distinguished from one another the program will crash."""

HARD_ANSWERS = ["string", "integer", "str", "lists"]

#inputs test_choice, outputs string "Great, you have chosen the " + test_choice + " test!" + "\n",
#returns quiz and answers for test choice
def test_selection():
    test_options = ['easy', 'medium', 'hard']
    test_choice = input("Please type in easy, medium or hard for your test difficulty: "
    "\n")
    test_choice = test_choice.lower()
    while test_choice not in test_options:
        test_choice = input("Sorry, invalid input, try again""\n")
    print ("Great, you have chosen the " + test_choice + " test!" + "\n")
    if test_choice == 'easy':
        quiz = EASY_QUIZ
        answers = EASY_ANSWERS
    elif test_choice == 'medium':
        quiz = MEDIUM_QUIZ
        answers = MEDIUM_ANSWERS
    elif test_choice == 'hard':
        quiz = HARD_QUIZ
        answers = HARD_ANSWERS
    else:
        return "\n""Test Failed"
    return quiz, answers

#checks user_input is in answers, returns user_input
def word_in_pos(user_input, answers, w):
    if user_input == answers[w]:
        return user_input

#inputs test_selection, outputs index, inputs user_input, if user_input in answers, prints "\n""Correct, Good Job!""\n"
#replaces blank, advances index, updates quiz, returns quiz.
#else prints "Incorrect! Guess again!", returns quiz
#When index = all_blanks, prints "Test Completed!"


def test_taking():
    quiz, answers = test_selection()
    replaced = []
    blank = ["___1___", "___2___", "___3___", "___4___"]
    index = 0
    index_forward = 1
    all_blanks = 4
    while index < all_blanks:
        current_blank = blank[index]
        print (quiz)
        user_input = input("\n""Your answer: ")
        user_input = user_input.lower()
        if word_in_pos(user_input, answers, index):
            print ("\n""Correct, Good Job!""\n")
            quiz = quiz.replace(current_blank, user_input)
            index += index_forward
        else:
            print ("\n""Incorrect! Guess again!""\n")
    return "Test Completed!"

#inputs if user wants to play again, returns test_taking if "yes"
#prints "Come back again sometime to test your knowledge" if "no"

play_again = "yes"
while play_again == "yes":
    print (test_taking())
    play_again = input("\n""You passed the test! Would you like to try another test? yes or no? ""\n")
    while play_again not in ["yes", "no"]:
        play_again = input("\n""You passed the test! Would you like to try another test? yes or no? ""\n")
    if play_again == "yes":
        print ("\n""Ok let's take another quiz!""\n")
    else:
        print ("\n""Come back again sometime to test your knowledge")
