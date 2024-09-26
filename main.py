#!/usr/bin/env python3
# logo
# Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
# Logog
# Against B: Vin Diesel, a Actor, from United States.
# Who has more followers? Type 'A' or 'B': l
# if you win, Last score will became A
from rich import print
from replit import clear
from random import randint
from art import logo
from art import vs
from game_data import data

def showQuestion(question_1, question_2, score):
    print(logo)
    # print(score)
    if score != 0:
        print(f"[green]You are right![/] Current score: [blue]{score}[/]")
    print(f"Compare A: [green]{question_1['name']}[/], a [blue]{question_1['description']}, from [yellow]{question_1['country']}[/]") 
    print(vs)
    print(f"Against B: [green]{question_2['name']}[/], a [blue]{question_2['description']}[/], from [yellow]{question_2['country']}[/]")

def getQuestion(data):
    data_len = len(data)
    index = randint(0, data_len - 1)
    return index

def compareAnswer(answer, question_1, question_2):
    if answer == 'a':
        if question_1['follower_count'] > question_2['follower_count']:
            return True
        else:
            return False
    elif answer == 'b':
        if question_2['follower_count'] > question_1['follower_count']:
            return True
        else:
            return False
    else:
        return False


def higherLower(data, last_answer=None, score=0):
    clear()
    initial_data = data
    question_index = getQuestion(initial_data)
    if not last_answer:
        question_1 = initial_data[question_index]
    else:
        question_1 = last_answer
    # remove question_1 from the list
    initial_data.pop(question_index)
    question_index = getQuestion(initial_data)
    question_2 = initial_data[question_index]
    # remove question_2 from the list
    initial_data.pop(question_index)
    showQuestion(question_1, question_2, score)

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = compareAnswer(answer, question_1, question_2)
    if result:
        print("[green]You are right![/]")
        higherLower(initial_data, last_answer=question_1, score=score+1)
    else:
        print("[red]You are wrong![/]")
        print(f"[green]{question_1['name']}[/] has [blue]{question_1['follower_count']}[/](mln) followers")
        print(f"[green]{question_2['name']}[/] has [blue]{question_2['follower_count']}[/](mln) followers")
        print(f"Final score: [blue]{score}[/]")
        return


higherLower(data)
