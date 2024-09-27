from rich import print
from art import logo, vs
def showQuestion(question_1, question_2, score):
    print(logo)
    # print(score)
    if score != 0:
        print(f"[green]You are right![/] Current score: [blue]{score}[/]")
    print(f"Compare A: [green]{question_1['name']}[/], a [blue]{question_1['description']}, from [yellow]{question_1['country']}[/]") 
    print(vs)
    print(f"Against B: [green]{question_2['name']}[/], a [blue]{question_2['description']}[/], from [yellow]{question_2['country']}[/]")
