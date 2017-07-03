# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Fill in the blanks quiz from Python documentation
'''

'''This program features three different levels: easy, medium, and hard, all
drawn from the official Python documentation. For each level, the player will
be presented with a short paragraph containing several "hidden" words. The user
will have three tries to guess the correct word to replace the hidden word.
I have plans to amend the program to allow the user to chose how many guesses
they will have before the game boots them out.'''

easy_sample = "__1__ is an __2__, interactive, object-oriented __3__ language.\
It incorporates modules, exceptions, __4__ typing, very high level dynamic data\
types, and classes. __1__ combines remarkable power with very clear syntax."
easy_key = {1: 'python', 2: 'interpreted', 3: 'programming', 4: 'dynamic'}

med_sample = "Many other __1__ of Python make it a good first language. Like\
Java, Python has a large standard __2__ so that students can be assigned\
programming projects very early in the course that do something. Assignments\
aren’t restricted to the standard four-function calculator and check balancing\
programs. By using the standard __2__, students can gain the satisfaction of\
working on realistic applications as they learn the __3__ of programming. Using\
the standard __2__ also teaches students about code reuse. Third-party __4__\
such as PyGame are also helpful in __5__ the students’ reach."
med_key = {1: 'aspects', 2: 'library', 3: 'fundamentals', 4: 'modules', 5: 'extending'}

hard_sample = "A __1__ can be based on one or more other __1__es, called its\
base __1__(es). It then __2__s the __3__ and __4__s of its base __1__es. This\
allows an __5__ model to be successively refined by __2__ance. You might have a\
generic Mailbox __1__ that provides basic __6__ __4__s for a mailbox, and\
sub__1__es such as MboxMailbox, MaildirMailbox, OutlookMailbox that handle\
various specific mailbox formats."
hard_key = {1: 'class', 2: 'inherit', 3: 'attributes', 4: 'methods', 5: 'object', 6: 'accessor'}

def switch(str, dict):
    '''
    switch takes in two arguments, a string and a dictionary, and returns a
    string with the dictionary keys appearing in the string replaced with
    the associated values. We will use a dictionary to hold the strings to
    be replaced (i.e. __1__) and the user generated responses.
    '''
    for i, j in dict.items():
        str = str.replace(i, j)
    return str

def ending(boolean):
    '''
    This function takes a boolean arguement, and returns the appropriate
    message based on whether the user got all the answers right or not
    '''
    if boolean:
        print "\nCongrats! You did a great job!\n"
    else:
        print "\nSorry. You lose.\n"

def initialize_question(s, num_blanks):
    '''
    This function takes two arguments, a string and a number of blanks. It
    returns a number list, as well as the user-generated number of guesses
    allowed before failure. It also prints out the original sentence for the
    user to study before making their guesses.
    '''
    nums = [i + 1 for i in range(num_blanks)]
    guesses = int(raw_input("\nHow many guesses would you like to have? ")) - 1
    answers = {}

    print "\nHere is the initial sentence.\n\n" + s

    return nums, guesses, answers

def get_answers(s, num_blanks, answer_key):
    '''
    Takes in three arguements: a string, an integer
    to represent the number of fill-in-the-blanks there are, and
    an answer key (dictionary). It returns the appropriate message depending
    on whether the user got all the questions right or not.
    '''
    num_list, guess_count, answer_dict = initialize_question(s, num_blanks)

    i = 0
    while i < num_blanks:
        rep_string = "__" + str(num_list[i]) + "__"
        guesses_left, correct = True, True

        while guesses_left:
            user_guess = raw_input("\nWhat is your guess for " + rep_string + "? ")

            if user_guess.lower() == answer_key[i + 1]:
                answer_dict[rep_string] = user_guess
                print "\nCorrect!\n\n" + switch(s, answer_dict)
                guesses_left, i = False, i + 1

            else:
                if guess_count > 0:
                    print "Nope. %d more..." % (guess_count)
                    guess_count -= 1

                else:
                    guesses_left, correct, i = False, False, num_blanks

    return ending(correct)

def play_game_helper():
    '''
    Allow the user to select their level
    '''
    sample_bank = {'easy': easy_sample, 'medium': med_sample, 'hard': hard_sample}
    key_bank = {'easy': easy_key, 'medium': med_key, 'hard': hard_key}

    level = raw_input("\nWhat level would you like to play? Easy, Medium, or Hard? ").lower()

    if level in ('easy', 'medium', 'hard'):
        return get_answers(sample_bank[level], len(key_bank[level]), key_bank[level])
    else:
        print "\nSorry, that's not a level. Try again.\n"

def play_game():
    '''
    This function takes no arguments, but allows the user to play the game
    multiple times if they wish. Calls the play_game_helper function.
    '''
    repeat = True
    play_count = 0
    while repeat:
        play = ""
        if play_count == 0:
            play = raw_input("\nDo you want to play? Yes or No: ").lower()
        else:
            play = raw_input("Do you want to play again? Yes or No: ").lower()
        if play == 'y' or play == 'yes':
            play_count += 1
            play_game_helper()
        else:
            print "\nOk, Maybe later...take it easy!\n"
            repeat = False

play_game()
