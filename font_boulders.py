#!/usr/bin/python3
# a test for converting french to american grades for bouldering and sport climbiing
import random
from os import system, name
import time
from art import *

bouldering = dict()
bouldering["VB"] = "3"
bouldering["V0-"] = "4-"
bouldering["V0"] = "4"
bouldering["V0+"] = "4+"
bouldering["V1"] = "5A"
bouldering["V2"] = "5B/5C"
bouldering["V3"] = "6A/6A+"
bouldering["V4"] = "6B/6B+"
bouldering["V5"] = "6C/6C+"
bouldering["V6"] = "7A"
bouldering["V7"] = "7A+"
bouldering["V8"] = "7B/7B+"
bouldering["V9"] = "7B+/7C"
bouldering["V10"] = "7C+"
bouldering["V11"] = "8A"
bouldering["V12"] = "8A+"
bouldering["V13"] = "8B"
bouldering["V14"] = "8B+"
bouldering["V15"] = "8C"
bouldering["V16"] = "8C+"
bouldering["V17"] = "9A"


art_font = "clr8x10"
art_font = "crawford"
art_font = "doom"
art_font = "epic"

def shuffle_dict(d):
    nd = dict()
    keys=list(d.keys()) # List of keys
    random.shuffle(keys)
    for key in keys:
        nd[key] = d[key]
    return nd


def shuffle_keys(d):
    keys=list(d.keys()) # List of keys
    random.shuffle(keys)
    return keys

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#print out the score and errors from the quiz
def print_results(quiz, errors):
    print("Score " + str(len(quiz)-len(errors)) + "/" + str(len(quiz)))
    print("Made the following errors")
    for error in errors:
        print(error, errors[error])


def quiz(set):
    errors = dict()
    keys = shuffle_keys(bouldering)
    for key in keys:
        #print (key, bouldering[key])
        fg = input(key + " to font: ")
        if fg != bouldering[key]:
            print("error Correct Answer " + key + "==" + bouldering[key])
            errors[key] = bouldering[key]
            clear()
    return errors

def get_scrambled_list(correct_answer, dictionary, size):
    scrambled = dict()
    scrambled[correct_answer] = dictionary[correct_answer]
    while len(scrambled) < size:
        value = random.choice(list(dictionary.items()))
        scrambled[value[0]] = dictionary[value[0]]
    return shuffle_dict(scrambled)

def print_choices(question,choices):
    i=1
    output=""

    tprint(question, font=art_font)
    for choice in choices:
        output += choices[choice] + "          "
        i=i+1
    tprint(output, font=art_font)


def get_valid_selection(question,choices):
    print_choices(question, choices)
    prompt_string = "please make a selection in the range 1 - " + str(len(choices))
    int_selection = 0 
    while int_selection ==0:
        selection = input("Choice: ")
        try:
            int_selection = int(selection)
            if int_selection <=0 or int_selection > len(choices):
                print("error out of range slection")
                print(prompt_string)
                int_selection = 0

        except:
                print("error invalid choice")
                print(prompt_string)
                int_selection = 0
    return int_selection

def selection_to_key(selection, choices):
    i=1
    for choice in choices:
        if i == selection:
            return choice
        i=i+1
    print("Something went wronng in converting selection to key")
    return ""
        


def multiple_choice_quiz(quiz):
    errors = dict()
    keys = shuffle_keys(quiz)
    for key in keys:
        choices = get_scrambled_list(key, quiz, 4)
        selection = get_valid_selection(key, choices)
        print(selection)
        key_selection = selection_to_key(selection,choices)
        if key == key_selection:
            tprint("CORRECT", art_font)
        else:
            tprint("INCORRECT", art_font)
        errors[key] = quiz[key]
        time.sleep(0.25)
        clear()
    return errors



clear()

#errors = quiz(bouldering)
errors = multiple_choice_quiz(bouldering)
print_results(bouldering, errors)


